"""Score all 395 cases and report project, candidate-scope and reference-source strata."""
import argparse
import csv
import json
from pathlib import Path
from score_core import load, evaluate, aggregate

def score(truths,predictions,cases):
    result=evaluate(truths,predictions,cases)
    for field in ('project','candidate_scope','reference_source','deprecated'):
        values=sorted({str(truths[c][field]) for c in cases})
        result['by_'+field]={value:aggregate([r for r in result['results']
            if str(truths[r['case_id']][field])==value]) for value in values}
    return result

def project_reports(result,out):
    """Write project counts for both spreadsheet import and human reading."""
    rows=[]
    table=['','## 按项目统计定位成功数量','',
        '成功定义：前 k 个候选中至少一个命中参考方法；Top-1、Top-3、Top-5 分别统计。','',
        '| 项目 | 案例数 | Top-1 成功 | Top-3 成功 | Top-5 成功 | Top-1 成功率 | Top-3 成功率 | Top-5 成功率 | MRR@5 |',
        '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for project,stats in result['by_project'].items():
        counts=stats['hit_counts'];rates=stats['hit_rates']
        table.append(f'| {project} | {stats["denominator"]} | {counts["top1"]} | {counts["top3"]} | {counts["top5"]} | '
            f'{rates["top1"]:.4%} | {rates["top3"]:.4%} | {rates["top5"]:.4%} | {stats["mrr_at5"]:.6f} |')
        rows.append(dict(project=project,total_cases=stats['denominator'],
            **{f'top{k}_success_count':counts[f'top{k}'] for k in (1,3,5)},
            **{f'top{k}_success_rate':rates[f'top{k}'] for k in (1,3,5)},mrr_at5=stats['mrr_at5']))
    with out.with_name(out.stem+'_by_project.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)
    return table+['']


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--truth',type=Path,default=Path(__file__).with_name('ground_truth.json'))
    parser.add_argument('--predictions',type=Path,required=True)
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--cases',nargs='+')
    group.add_argument('--cases-file',type=Path)
    parser.add_argument('--out',type=Path,default=Path('scores395.json'))
    args=parser.parse_args()
    truths=load(args.truth)['cases']
    cases=args.cases_file.read_text(encoding='utf-8-sig').split() if args.cases_file else args.cases or list(truths)
    result=score(truths,args.predictions,cases)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    s=result['summary']
    md=['# 方法级故障定位评估','',f'案例分母：{s["denominator"]}。',
        '', '| 指标 | 命中数 | 比例 |','|---|---:|---:|']
    for k in (1,3,5):
        md.append(f'| Hit@{k} | {s["hit_counts"][f"top{k}"]} | {s["hit_rates"][f"top{k}"]:.4%} |')
    md+=['',f'MRR@5：{s["mrr_at5"]:.6f}。','',
         '缺失、无效、空预测仍计入分母；没有正例参考的案例按可观测标签记零，并单列参考状态。',
         'JSON 中按项目、候选集合来源、参考标签来源及弃用状态分组。',
         '395 个案例均使用相同的方法入口覆盖采集与补丁参考映射；按项目结果须随整体结果共同报告。','']
    md+=project_reports(result,args.out)
    args.out.with_suffix('.md').write_text('\n'.join(md),encoding='utf-8')
    print(json.dumps(s,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
