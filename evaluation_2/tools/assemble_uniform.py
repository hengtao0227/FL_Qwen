"""Build the 395-case release. Input rendering is separate from reference labels.

All paths are explicit CLI arguments. Case IDs use project names and bug IDs.
Only this operator-side script reads labels, patches and source provenance.
"""
import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import shutil
import subprocess
import zipfile

from build_input import (build_case, validate_against_source, read, identity,
                         INPUT_README, SOURCE_KEYS)
from case_io import VERSION, encode, digest, require
import label_patch
from coverage_selection import select_covered, SCOPE as COVERAGE_SCOPE
from collect_sources import patch_strip

PROJECTS = {'Chart':26, 'Closure':133, 'Lang':65, 'Math':106, 'Mockito':38, 'Time':27}
MISSING = {'Closure_63','Closure_93','Lang_2','Time_21',*[f'Mockito_{i}' for i in range(1,39)]}


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(encode(value))


def source_text(path):
    data = path.read_bytes()
    try: return data.decode('utf-8-sig')
    except UnicodeDecodeError: return data.decode('latin-1')


def verify_source(rows, root):
    cache = {}
    for row in rows:
        path = row['src_path']
        if path not in cache:
            cache[path] = source_text(root/path).splitlines()
        require(cache[path][row['begin_line']-1:row['end_line']] == row['snippet'].splitlines(),
                'Cached buggy source mismatch: '+path)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--d4j', type=Path, required=True, help='Defects4J root')
    p.add_argument('--cache', type=Path, required=True, help='dataset395_cache')
    p.add_argument('--coverage', type=Path, required=True, help='Verified method-entry run artifacts for all 395 uniformly reconstructed cases')
    p.add_argument('--out', type=Path, default=Path(__file__).resolve().parents[2])
    a = p.parse_args()
    # Verify every coverage artifact before creating or replacing any release file.
    originals = [f'{project}_{i}' for project,n in PROJECTS.items() for i in range(1,n+1)]
    covered={cid:select_covered(cid,a.cache/'raw_extracted'/cid,a.coverage) for cid in originals}
    require(len({audit['agent_sha256'] for _,audit in covered.values()})==1,'Mixed coverage agent builds')
    require(len({audit['recorder_sha256'] for _,audit in covered.values()})==1,'Mixed recorder builds')
    inputs, evaluation = a.out/'input_2', a.out/'evaluation_2'
    inputs.mkdir(parents=True, exist_ok=True)
    evaluation.mkdir(parents=True, exist_ok=True)
    label_patch.D4J = a.d4j/'framework/projects'
    originals = [f'{project}_{i}' for project,n in PROJECTS.items() for i in range(1,n+1)]
    require(len(originals) == 395, 'Wrong case count')
    mapfile = evaluation/'case_mapping.json'
    if mapfile.exists():
        mapping = read(mapfile)
    else:
        mapping = {cid:cid for cid in originals}
        write(mapfile, mapping)
    require(mapping == {cid:cid for cid in originals}, 'Expected project-based case IDs')
    existing = set(x.name for x in (inputs/'cases').iterdir()) if (inputs/'cases').exists() else set()
    require(existing <= set(mapping), 'Unexpected existing input cases; refusing to mix releases')
    metadata = {}
    for project in PROJECTS:
        for name in ('active-bugs.csv','deprecated-bugs.csv'):
            with (label_patch.D4J/project/name).open(encoding='utf-8-sig',newline='') as f:
                for row in csv.DictReader(f): metadata[f'{project}_{row["bug.id"]}'] = row
    require(set(originals) <= set(metadata), 'Missing official metadata')
    truth, patch_truth, manifest, provenance, groups = {}, {}, [], {}, {}
    dedup = {}
    archived = set()
    source_checked = 0
    for number,(cid,original) in enumerate(mapping.items(),1):
        project,bid = original.split('_')
        reconstructed = True
        raw = a.cache/'raw_extracted'/original
        all_methods = read(raw/'snippet.json')
        methods, coverage_audit = covered[cid] if reconstructed else (all_methods,None)
        fields = read(raw/'field_snippet.json')
        tests = read(raw/'test_snippet.json')
        report = (raw/'failing_tests').read_bytes()
        files,meta,index = build_case(cid, methods, fields, tests, report)
        require(index and meta['failed_test_count'] > 0, 'Empty evidence')
        validate_against_source(files, methods, fields)
        # Counterfactual: changing label/ranking metadata and source-list order
        # must not affect a single byte in the input release (all 395 cases).
        tainted = [{**r,'is_bug':'TAINT','susp':'TAINT','num_failing_tests':'TAINT',
                    'name':'TAINT','resolved_comments':'TAINT'} for r in reversed(methods)]
        counterfactual,_,_ = build_case(cid, tainted, list(reversed(fields)), tests, report)
        require(counterfactual == files, 'Label/order dependence in input renderer')
        dest = inputs/'cases'/cid
        dest.mkdir(parents=True,exist_ok=True)
        for name,data in files.items(): (dest/name).write_bytes(data)
        manifest.append(dict(case_id=cid,input_sha256=meta['input_sha256'],
            candidate_count=len(index),failed_test_count=meta['failed_test_count'],
            files_sha256={name:digest(data) for name,data in sorted(files.items())}))
        by_identity = {identity(m):m for m in index}
        dedup[cid] = len(methods)-len(index)
        # Map patches against the FULL source universe first. Filtering must not
        # reassign an uncovered nested method's label to its covered outer method.
        full_index=[dict(candidate_id=f'FULL{i}',**{k:m[k] for k in
            ('src_path','begin_line','end_line','signature','class_name')}) for i,m in enumerate({identity(m):m for m in all_methods}.values())]
        full_refs,patchaudit = label_patch.label_case(original,full_index)
        id_map={m['candidate_id']:by_identity[identity(m)]['candidate_id']
                for m in full_index if identity(m) in by_identity}
        patchrefs=[{**r,'candidate_id':id_map[r['candidate_id']]} for r in full_refs if r['candidate_id'] in id_map]
        mapped=[]
        for change in patchaudit['mapped_changes']:
            new_ids=[id_map[c] for c in change['candidate_ids'] if c in id_map]
            if new_ids: mapped.append({**change,'candidate_ids':new_ids})
            else: patchaudit['unmapped_changes'].append({k:v for k,v in change.items() if k!='candidate_ids'} | {'reason':'method_outside_candidate_scope'})
        patchaudit['mapped_changes']=mapped
        patchaudit.update(case_id=cid,original_case_id=original)
        write(evaluation/'reference_audit'/f'{cid}.json',patchaudit)
        patch = label_patch.D4J/project/'patches'/f'{bid}.src.patch'
        patchdest = evaluation/'patches'/project/patch.name
        patchdest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(patch,patchdest)
        if reconstructed:
            refs = patchrefs
            scope = COVERAGE_SCOPE
            reference_source = 'official_patch_to_static_method'
            srcroot = a.cache/'buggy_sources'/original
            verify_source(methods+fields+json.loads(files['failed_tests.json']),srcroot)
            source_checked += len(methods)
            sourceaudit = read(a.cache/'source_audit'/f'{original}.json')
            extraction = read(a.cache/'source_audit'/f'{original}.extraction.json')
            require(not extraction['production_parse_errors'],'Production parse errors')
            require(digest(patch.read_bytes()) == sourceaudit['patch_sha256'],'Patch changed')
            archive = a.cache/'archives'/f'{project}-{sourceaudit["revision_fixed"]}.zip'
            if archive not in archived:
                require(digest(archive.read_bytes()) == sourceaudit['archive_sha256'],'Archive changed')
                with zipfile.ZipFile(archive) as z: require(z.testzip() is None,'Bad source archive')
                archived.add(archive)
            result = subprocess.run(['git','apply',patch_strip(patch),'--reverse','--check','--no-index',
                                     '--whitespace=nowarn',str(patch.resolve())],
                                    cwd=srcroot,capture_output=True,text=True)
            require(result.returncode == 0,'Buggy patch reverse-check failed: '+result.stderr)
            official_report = (label_patch.D4J/project/'trigger_tests'/bid).read_bytes()
            require(report == official_report,'Reconstructed report differs from official log')
            write(evaluation/'source_audit'/f'{cid}.json',sourceaudit)
            write(evaluation/'source_audit'/f'{cid}.extraction.json',extraction)
            write(evaluation/'coverage_audit'/f'{cid}.json',coverage_audit)
            proof=evaluation/'coverage_evidence'/cid
            proof.mkdir(parents=True,exist_ok=True)
            write(proof/'coverage.json',coverage_audit)
            for test in coverage_audit['tests']:
                base=test['hits_file'].removesuffix('.hits.tsv')
                for suffix in ('.hits.tsv','.hits.tsv.errors','.log','.result.tsv','.baseline.log','.baseline.result.tsv'):
                    shutil.copyfile(a.coverage/cid/(base+suffix),proof/(base+suffix))
        official = metadata[original]
        deprecated = bool(official.get('deprecated.version'))
        record = dict(case_id=cid,original_case_id=original,project=project,
            input_sha256=meta['input_sha256'],candidate_ids=[m['candidate_id'] for m in index],
            candidate_scope=scope,reference_source=reference_source,deprecated=deprecated,
            deprecated_reason=official.get('deprecated.reason'),reference_methods=refs,
            reference_status='positive_reference_available' if refs else 'no_positive_reference_in_candidates')
        truth[cid] = record
        patch_truth[cid] = dict(record,reference_source='official_patch_to_static_method',
            reference_methods=patchrefs,reference_status='positive_reference_available' if patchrefs else 'no_positive_reference_in_candidates')
        for group in (project,'uniform395'):
            groups.setdefault(group,[]).append(cid)
        if deprecated: groups.setdefault('deprecated_in_local_d4j',[]).append(cid)
        if not refs: groups.setdefault('no_positive_reference',[]).append(cid)
        provenance[cid] = dict(original_case_id=original,raw_directory=str(raw),
            raw_sha256={name:digest((raw/name).read_bytes()) for name in
                        ('snippet.json','field_snippet.json','test_snippet.json','failing_tests')},
            official_metadata=official,duplicate_records_removed=dedup[cid],
            report_source='archived Defects4J trigger log; fresh coverage logs retained separately' if reconstructed else 'local raw failing_tests; cached execution, not rerun',
            candidate_scope=scope,upstream_selection_independence_verified=reconstructed,
            full_buggy_source_body_comparison_performed=reconstructed)
        if reconstructed:
            provenance[cid].update(coverage_audit=f'coverage_audit/{cid}.json',
                original_candidate_count=len(all_methods),covered_candidate_count=len(index),
                triggering_tests_rerun=len(coverage_audit['tests']),
                coverage_collection=coverage_audit['collection'])
        if number % 25 == 0 or number == 395: print(f'BUILT {number}/395',flush=True)
    write(inputs/'manifest.json',dict(dataset_version=VERSION,case_count=395,cases=manifest))
    (inputs/'all395.txt').write_text('\n'.join(mapping)+'\n',encoding='utf-8')
    (inputs/'README_输入说明.md').write_text(INPUT_README + UNIFORM_README,encoding='utf-8')
    write(evaluation/'ground_truth.json',dict(dataset_version=VERSION,cases=truth))
    write(evaluation/'ground_truth_patch.json',dict(dataset_version=VERSION,cases=patch_truth,
        policy='Secondary sensitivity analysis: official patch overlap only; unmapped edits are not guessed.'))
    write(evaluation/'source_provenance.json',provenance)
    write(evaluation/'case_groups.json',groups)
    (evaluation/'all395.txt').write_text('\n'.join(mapping)+'\n',encoding='utf-8')
    for group,cases in groups.items():
        (evaluation/(group+'.txt')).write_text('\n'.join(cases)+'\n',encoding='utf-8')
    summary = dict(dataset_version=VERSION,case_count=395,projects=PROJECTS,
        input_files_per_case=10,total_candidate_records=sum(r['candidate_count'] for r in manifest),
        duplicate_records_removed=sum(dedup.values()),candidate_scopes=Counter(t['candidate_scope'] for t in truth.values()),
        positive_reference_cases=sum(bool(t['reference_methods']) for t in truth.values()),
        no_positive_reference_cases=[t['original_case_id'] for t in truth.values() if not t['reference_methods']],
        deprecated_cases=[mapping[c] for c in groups.get('deprecated_in_local_d4j',[])],
        patch_reference_positive_cases=sum(bool(t['reference_methods']) for t in patch_truth.values()),
        reconstructed_method_bodies_compared_to_cached_buggy_source=source_checked,
        source_archives_hash_and_zip_verified=len(archived),
        counterfactual_label_and_order_invariance_cases=395,
        runtime_tests_executed=True,runtime_test_case_count=len(covered),
        coverage_agent_build_count=len({audit['agent_sha256'] for _,audit in covered.values()}),
        baseline_and_instrumented_jvm_runs=2*sum(len(audit['tests']) for _,audit in covered.values()),
        triggering_test_runs=sum(len(audit['tests']) for _,audit in covered.values()),
        reconstructed_candidates_before=sum(audit['original_candidate_count'] for _,audit in covered.values()),
        reconstructed_candidates_after=sum(audit['covered_candidate_count'] for _,audit in covered.values()),
        real_codex_evaluation_executed=False,
        filesystem_isolation_enforced=False,upstream_selection_independence_verified=True)
    write(evaluation/'build_summary.json',summary)
    print(json.dumps(summary,ensure_ascii=False,indent=2),flush=True)


UNIFORM_README='''
本 input_2 的 395 个案例全部重新采集，不继承 AutoFL 的候选集合。
统一流程：官方固定版本 + 官方缺陷补丁 → 全生产源码方法提取 →
逐个触发测试无插桩复现 → ASM 方法入口插桩复现 → 覆盖方法并集。
包含显式声明且被执行的方法和构造器；不包含隐式构造器、类初始化块、
桥接或合成方法，也不因参考答案而增删候选。测试执行包括 setup/teardown。
测试栈采用 Defects4J 存档；此次运行日志、覆盖证据和平台兼容调整另存 evaluation_2。
字段提供生产源码上下文。参考标签由官方补丁统一映射，存于 evaluation_2，
不要向定位 agent 提供 evaluation_2 或源码/运行缓存。最多输出 5 个是预测限制，
与候选数、失败测试数无关。
'''

if __name__ == '__main__': main()
