"""Summarize the finished release without reading old reference labels."""
import json
from collections import Counter
from pathlib import Path
import statistics

root=Path(__file__).resolve().parents[2]
new=json.loads((root/'input_2/manifest.json').read_bytes())
old=json.loads((root/'input/manifest.json').read_bytes())
old_counts={row['case_id']:row['candidate_count'] for row in old['cases']}
projects={}
for project in ('Chart','Closure','Lang','Math','Mockito','Time'):
    rows=[r for r in new['cases'] if r['case_id'].startswith(project+'_')]
    counts=[r['candidate_count'] for r in rows]
    projects[project]={'case_count':len(rows),'candidate_count':sum(counts),
        'candidate_median':statistics.median(counts),'candidate_min':min(counts),'candidate_max':max(counts),
        'trigger_test_count':sum(r['failed_test_count'] for r in rows)}
changes=[{'case_id':r['case_id'],'old_candidate_count':old_counts[r['case_id']],
          'new_candidate_count':r['candidate_count'],'delta':r['candidate_count']-old_counts[r['case_id']]}
         for r in new['cases']]
summary={'case_count':new['case_count'],'candidate_count':sum(r['candidate_count'] for r in new['cases']),
    'trigger_test_count':sum(r['failed_test_count'] for r in new['cases']),
    'projects':projects,'count_changes_vs_original_input':changes}
groups=json.loads((root/'evaluation/case_groups.json').read_bytes())
comparison=[]
for cid in groups['reconstructed42']:
    keys=('src_path','begin_line','end_line','signature','class_name')
    def identities(folder):
        rows=json.loads((root/folder/'cases'/cid/'candidate_index.json').read_bytes())
        return {tuple(row[k] for k in keys) for row in rows}
    before,after=identities('input'),identities('input_2')
    comparison.append({'case_id':cid,'same_candidate_identities':before==after,
                       'removed':len(before-after),'added':len(after-before)})
summary['original42_candidate_comparison']=comparison
summary['original42_identical_candidate_sets']=sum(r['same_candidate_identities'] for r in comparison)
(root/'evaluation_2/dataset_statistics.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k not in ('count_changes_vs_original_input','original42_candidate_comparison')},ensure_ascii=False,indent=2))
