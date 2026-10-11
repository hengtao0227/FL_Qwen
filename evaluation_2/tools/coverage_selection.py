"""Fail-closed selection from verified triggering-test method-entry artifacts."""
import json
from pathlib import Path
import re

from build_input import identity
from case_io import digest, require
from collect_method_coverage import expected_tests, map_hits, verify_failure, result_failure, normalize_failure, failure_key

SCOPE='trigger_test_executed_methods_and_constructors'


def select_covered(case_id, raw, runs):
    folder=Path(runs)/case_id
    audit=json.loads((folder/'coverage.json').read_bytes())
    methods=json.loads((raw/'snippet.json').read_bytes())
    report=(raw/'failing_tests').read_text(encoding='utf-8-sig')
    require(audit['case_id']==case_id and audit['candidate_scope']==SCOPE,'Coverage identity/scope mismatch')
    require(audit['runtime_tests_executed'] is True and audit['all_trigger_failures_reproduced'] is True,'Unverified test execution')
    require(audit.get('uninstrumented_baseline_verified') is True,'Missing uninstrumented control')
    require(audit['raw_methods_sha256']==digest((raw/'snippet.json').read_bytes()),'Coverage source hash mismatch')
    require(audit['trigger_report_sha256']==digest((raw/'failing_tests').read_bytes()),'Coverage trigger hash mismatch')
    expected=dict(expected_tests(report))
    require([r['test'] for r in audit['tests']]==list(expected),'Incomplete/duplicated trigger coverage')
    union=set()
    for row in audit['tests']:
        name=row['hits_file']
        require(Path(name).name==name and '\\' not in name,'Unsafe coverage filename')
        hits=folder/name
        log=folder/name.replace('.hits.tsv','.log')
        result=folder/name.replace('.hits.tsv','.result.tsv')
        baseline_log=folder/name.replace('.hits.tsv','.baseline.log')
        baseline_result=folder/name.replace('.hits.tsv','.baseline.result.tsv')
        require(digest(hits.read_bytes())==row['hits_sha256'],'Method-entry evidence changed')
        require(digest(log.read_bytes())==row['log_sha256'],'Test log changed')
        require(digest(result.read_bytes())==row['result_sha256'],'Test result changed')
        require(digest(baseline_log.read_bytes())==row['baseline_log_sha256'],'Baseline log changed')
        require(digest(baseline_result.read_bytes())==row['baseline_result_sha256'],'Baseline result changed')
        require(result_failure(result,row['test'])==row['observed_failure'],'Observed failure mismatch')
        require(result_failure(baseline_result,row['test'])==row['baseline_failure'],'Baseline failure mismatch')
        require(failure_key(row['baseline_failure'],row['test'])==failure_key(row['observed_failure'],row['test']),'Instrumentation changed failure')
        require(Path(str(hits)+'.errors').read_text(encoding='utf-8')=='','Instrumentation errors')
        require(row['expected_failure']==expected[row['test']],'Expected failure mismatch')
        block=next(b for b in re.split(r'^---\s+',report,flags=re.M)[1:] if b.splitlines()[0].strip()==row['test'])
        verify_failure(expected[row['test']],row['observed_failure'],block,log.read_text(encoding='utf-8',errors='replace'))
        verify_failure(expected[row['test']],row['baseline_failure'],block,baseline_log.read_text(encoding='utf-8',errors='replace'))
        mapped,_=map_hits(hits.read_text(encoding='utf-8').splitlines(),methods)
        identities={identity(m) for m in mapped}
        require(identities=={tuple(m) for m in row['covered_source_identities']},'Per-test coverage mapping mismatch')
        union.update(identities)
    require(union=={tuple(m) for m in audit['covered_source_identities']},'Coverage union mismatch')
    selected=[m for m in methods if identity(m) in union]
    require(len(selected)==audit['covered_candidate_count'] and selected,'Covered count mismatch/empty')
    require(len(methods)==audit['original_candidate_count'],'Original candidate count mismatch')
    return selected,audit
