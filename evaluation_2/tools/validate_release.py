"""Operator validation: completeness, integrity, input allowlists and scorer controls."""
import argparse
import csv
from collections import Counter
import json
from pathlib import Path
import re
import sys
import tempfile

from case_io import snapshot, digest, require, FILES
from assemble_uniform import PROJECTS, write
from build_input import identity
from collect_method_coverage import result_failure, normalize_failure, failure_key


def load(path): return json.loads(path.read_bytes())


def run(root):
    inputs, evaluation = root/'input_2',root/'evaluation_2'
    sys.path.insert(0,str(evaluation))
    from score import score, project_reports
    from score_core import score_prediction, verify_evidence
    from prepare_case import prepare
    mapping = load(evaluation/'case_mapping.json')
    manifest = load(inputs/'manifest.json')
    truths = load(evaluation/'ground_truth.json')['cases']
    patchtruth = load(evaluation/'ground_truth_patch.json')['cases']
    expected = {f'{p}_{i}' for p,n in PROJECTS.items() for i in range(1,n+1)}
    ids = [f'{p}_{i}' for p,n in PROJECTS.items() for i in range(1,n+1)]
    require(mapping == {cid:cid for cid in ids} and list(mapping) == ids,'Case map mismatch')
    require(set(truths) == set(patchtruth) == set(ids),'Truth inventory mismatch')
    require(Counter(t['project'] for t in truths.values()) == PROJECTS,'Project counts mismatch')
    require({p.name for p in inputs.iterdir()} == {'cases','manifest.json','all395.txt','README_输入说明.md'},
            'Unexpected top-level input files')
    require({p.name for p in (inputs/'cases').iterdir()} == set(ids),'Case directory mismatch')
    require(manifest['case_count'] == 395 and len(manifest['cases']) == 395,'Manifest count mismatch')
    require((inputs/'all395.txt').read_text().split() == ids,'Case list mismatch')
    forbidden = {'is_bug','susp','ochiai_susp','num_failing_tests','resolved_comments',
                 'reference_methods','ground_truth','reference_candidate_ids','original_case_id',
                 'revision.id.fixed','report.url','deprecated','reference_source','candidate_scope'}
    def inspect(value):
        if isinstance(value,dict):
            require(not (set(value)&forbidden),'Forbidden structured input label')
            for v in value.values(): inspect(v)
        elif isinstance(value,list):
            for v in value: inspect(v)
    inspect(manifest)
    verified = 0
    method_count = 0
    inherited = 0
    for row in manifest['cases']:
        cid = row['case_id']
        data = snapshot(inputs/'cases'/cid)
        require({n:digest(b) for n,b in data.items()} == row['files_sha256'],'Release file hash mismatch')
        require(json.loads(data['case.json'])['input_sha256'] == row['input_sha256'],'Manifest fingerprint mismatch')
        index = json.loads(data['candidate_index.json'])
        tests = json.loads(data['failed_tests.json'])
        require(index and tests,'Empty source evidence')
        require(len(index) == row['candidate_count'] and len(tests) == row['failed_test_count'],'Manifest counts mismatch')
        requested = re.findall(r'^---\s+(.+?)\s*$',data['failure_report.txt'].decode('utf-8-sig'),re.M)
        require([r.replace('::','.')+'()' for r in requested] == [t['requested_signature'] for t in tests],
                'Failed test report/source mismatch')
        inherited += sum(t['resolution']=='inherited' for t in tests)
        for name,b in data.items():
            if name.endswith('.json'): inspect(json.loads(b))
            require(not re.search(rb'\bC\d{4}\b',b) if name in ('case.json','prediction_template.json') else True,
                    'Obsolete anonymous case ID: '+cid+'/'+name)
        by_id = {m['candidate_id']:m for m in index}
        if cid in expected:
            coverage=load(evaluation/'coverage_audit'/f'{cid}.json')
            proof=evaluation/'coverage_evidence'/cid
            require(load(proof/'coverage.json')==coverage,'Coverage audit/evidence mismatch')
            require(coverage['uninstrumented_baseline_verified'] and coverage['all_trigger_failures_reproduced'],
                    'Unverified triggering-test execution')
            require(coverage['covered_candidate_count']==len(index),'Coverage candidate count mismatch')
            require({tuple(m) for m in coverage['covered_source_identities']}=={identity(m) for m in index},
                    'Candidates do not equal covered method union')
            require([r['test'] for r in coverage['tests']]==requested,'Incomplete trigger evidence')
            union=set()
            for run in coverage['tests']:
                base=run['hits_file'].removesuffix('.hits.tsv')
                require(Path(base).name==base and '\\' not in base,'Unsafe coverage evidence filename')
                for suffix,key in (('.hits.tsv','hits_sha256'),('.log','log_sha256'),
                    ('.result.tsv','result_sha256'),('.baseline.log','baseline_log_sha256'),('.baseline.result.tsv','baseline_result_sha256')):
                    require(digest((proof/(base+suffix)).read_bytes())==run[key],'Coverage evidence hash mismatch')
                require((proof/(base+'.hits.tsv.errors')).read_text(encoding='utf-8')=='','Instrumentation errors')
                actual=result_failure(proof/(base+'.result.tsv'),run['test'])
                baseline=result_failure(proof/(base+'.baseline.result.tsv'),run['test'])
                require(actual==run['observed_failure'] and baseline==run['baseline_failure'],'Failure result mismatch')
                require(failure_key(actual,run['test'])==failure_key(baseline,run['test']),'Instrumentation altered failure')
                union.update(tuple(m) for m in run['covered_source_identities'])
            require(union=={identity(m) for m in index},'Per-test method union differs from candidates')
        for t in (truths[cid],patchtruth[cid]):
            require(t['original_case_id'] == mapping[cid] and t['input_sha256'] == row['input_sha256'],
                    'Truth binding mismatch')
            require(t['candidate_ids'] == list(by_id),'Candidate universe mismatch')
            for ref in t['reference_methods']:
                require(ref['candidate_id'] in by_id,'Reference outside candidates')
                require(all(by_id[ref['candidate_id']][k] == v for k,v in ref.items()),'Reference identity mismatch')
        verified += len(data)
        method_count += len(index)
    controls = {}
    with tempfile.TemporaryDirectory(prefix='codex395_checks_') as tmp:
        temp = Path(tmp)
        result = score(truths,temp,ids)
        require(result['summary']['denominator']==395 and result['summary']['statuses']=={'missing_prediction':395},
                'Missing predictions dropped')
        controls['all_missing_still_denominator_395'] = True
        positives = 0
        for cid,t in truths.items():
            ranking = []
            if t['reference_methods']:
                ranking = [dict(rank=1,candidate_id=t['reference_methods'][0]['candidate_id'],reason='Synthetic scoring control')]
                positives += 1
            write(temp/(cid+'.json'),dict(case_id=cid,input_sha256=t['input_sha256'],ranking=ranking))
        result = score(truths,temp,ids)
        require(result['summary']['hit_counts']['top1'] == positives,'Oracle control failed')
        require(result['summary']['mrr_at5'] == positives/395,'MRR control failed')
        controls['synthetic_rank1_hits'] = positives
        table=project_reports(result,temp/'control_scores.json')
        with (temp/'control_scores_by_project.csv').open(encoding='utf-8-sig',newline='') as f:
            project_rows=list(csv.DictReader(f))
        require({r['project']:int(r['total_cases']) for r in project_rows} == PROJECTS,'Project CSV counts mismatch')
        for row in project_rows:
            project=row['project']
            hits=sum(bool(t['reference_methods']) for t in truths.values() if t['project']==project)
            require(all(int(row[f'top{k}_success_count'])==hits for k in (1,3,5)), 'Project success count mismatch')
        require(sum(int(r['top1_success_count']) for r in project_rows)==positives,'Project success total mismatch')
        require(all('| '+p+' |' in '\n'.join(table) for p in PROJECTS),'Markdown missing project table')
        controls['per_project_counts_csv_and_markdown_verified']=True
        cid = next(c for c in ids if truths[c]['reference_methods'])
        valid = load(temp/(cid+'.json'))
        invalids = [dict(valid,input_sha256='0'*64),dict(valid,unexpected=True),
                    dict(valid,ranking=valid['ranking']+[dict(valid['ranking'][0],rank=2)]),
                    dict(valid,ranking=[dict(valid['ranking'][0],candidate_id='M99999999')]),
                    dict(valid,ranking=[dict(valid['ranking'][0],rank=True)]),
                    dict(valid,ranking=[dict(valid['ranking'][0],reason='')])]
        for bad in invalids:
            try: score_prediction(truths[cid],bad)
            except ValueError: pass
            else: raise AssertionError('Invalid prediction accepted')
        controls['invalid_prediction_types_rejected'] = len(invalids)
        # Verify genuine rank-3 metrics and no-positive references as well.
        if len(truths[cid]['candidate_ids']) >= 3:
            t=truths[cid]
            refs={r['candidate_id'] for r in t['reference_methods']}
            wrong=[m for m in t['candidate_ids'] if m not in refs][:2]
            ranked=wrong+[next(iter(refs))]
            r=score_prediction(t,dict(valid,ranking=[dict(rank=i,candidate_id=m,reason='Synthetic') for i,m in enumerate(ranked,1)]))
            require(not r['hits']['top1'] and r['hits']['top3'] and r['reciprocal_rank_at5']==1/3,'Rank-3 metrics wrong')
            controls['rank3_hit_and_reciprocal_rank'] = True
        prepared = temp/'isolated_case'
        prepare(inputs,cid,prepared)
        require({p.name for p in prepared.iterdir()} == FILES,'Preparation copied unexpected files')
        verify_evidence(prepared,truths[cid])
        (prepared/'methods.txt').write_bytes((prepared/'methods.txt').read_bytes()+b'\ntamper')
        try: verify_evidence(prepared,truths[cid])
        except ValueError: pass
        else: raise AssertionError('Tampered evidence accepted')
        controls['tampered_evidence_rejected'] = True
        controls['case_preparation_verified'] = True
    summary = load(evaluation/'build_summary.json')
    require(summary['total_candidate_records'] == method_count,'Build total mismatch')
    report = dict(status='passed',cases=395,projects=PROJECTS,
        input_case_files_verified=verified,total_candidate_records=method_count,
        inherited_failing_test_resolutions=inherited,structured_label_allowlist_passed=True,
        project_based_case_ids=True,empty_prediction_templates=395,
        counterfactual_label_and_order_invariance_cases=summary['counterfactual_label_and_order_invariance_cases'],
        reconstructed_source_methods_verified=summary['reconstructed_method_bodies_compared_to_cached_buggy_source'],
        controls=controls,runtime_tests_executed=summary.get('runtime_tests_executed',False),
        runtime_test_case_count=summary.get('runtime_test_case_count',0),
        triggering_test_runs=summary.get('triggering_test_runs',0),real_codex_predictions_executed=False,
        triggering_method_coverage_cases_verified=len(expected),
        upstream_selection_independence_verified=True,host_sandbox_verified=False)
    write(evaluation/'VALIDATION.json',report)
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    run(p.parse_args().root)
