#!/usr/bin/env python3
"""Build a Qwen Code quality/resource report from official scores and run results."""
from __future__ import annotations

import argparse
import csv
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import statistics

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


PROJECTS = ("Chart", "Closure", "Lang", "Math", "Mockito", "Time")


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def percentile(values, fraction):
    ordered = sorted(values)
    if not ordered:
        return None
    position = (len(ordered) - 1) * fraction
    low, high = math.floor(position), math.ceil(position)
    if low == high:
        return ordered[low]
    return ordered[low] * (high - position) + ordered[high] * (position - low)


def observed_tokens(row):
    inp, out = row.get("known_input_tokens"), row.get("known_output_tokens")
    return None if inp is None and out is None else (inp or 0) + (out or 0)


def project_of(case_id):
    return case_id.split("_", 1)[0]


def fmt_int(value):
    return "null" if value is None else f"{int(value):,}"


def fmt_num(value, digits=2):
    return "null" if value is None else f"{value:,.{digits}f}"


def save_overall_chart(summary, path):
    labels = ["Top-1", "Top-3", "Top-5", "MRR@5"]
    values = [summary["hit_rates"]["top1"], summary["hit_rates"]["top3"],
              summary["hit_rates"]["top5"], summary["mrr_at5"]]
    fig, ax = plt.subplots(figsize=(8.2, 4.7))
    colors = ["#315c9b", "#5b79ad", "#7f95bf", "#b06f3c"]
    bars = ax.bar(labels, np.array(values) * 100, color=colors, width=.62)
    ax.set_ylabel("Score (%)")
    ax.set_ylim(0, 105)
    ax.set_title("Qwen Code method-level localization quality (n=395)")
    ax.grid(axis="y", color="#d9d9d9", linewidth=.7)
    ax.set_axisbelow(True)
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.2,
                f"{value:.2%}", ha="center", va="bottom", fontsize=10)
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def save_project_chart(project_rows, path):
    x = np.arange(len(project_rows))
    width = .19
    fig, ax = plt.subplots(figsize=(11, 5.3))
    series = (("Top-1", "top1", "#315c9b"), ("Top-3", "top3", "#5b79ad"),
              ("Top-5", "top5", "#7f95bf"), ("MRR@5", "mrr_at5", "#b06f3c"))
    for index, (label, key, color) in enumerate(series):
        values = [row[key] * 100 for row in project_rows]
        ax.bar(x + (index - 1.5) * width, values, width, label=label, color=color)
    ax.set_xticks(x, [row["project"] for row in project_rows])
    ax.set_ylabel("Score (%)")
    ax.set_ylim(75, 102)
    ax.set_title("Quality by project (fixed all-case denominator)")
    ax.grid(axis="y", color="#d9d9d9", linewidth=.7)
    ax.set_axisbelow(True)
    ax.legend(ncol=4, frameon=False, loc="upper center")
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def save_rank_chart(rank_counts, path):
    labels = ["Rank 1", "Rank 2", "Rank 3", "Rank 4", "Rank 5",
              "Miss (with ref.)", "No positive ref."]
    values = [rank_counts.get(str(i), 0) for i in range(1, 6)] + [
        rank_counts["miss_with_reference"], rank_counts["no_positive_reference"]]
    fig, ax = plt.subplots(figsize=(10, 4.9))
    colors = ["#315c9b"] * 5 + ["#b06f3c", "#8d8d8d"]
    bars = ax.bar(labels, values, color=colors, width=.68)
    ax.set_ylabel("Cases")
    ax.set_title("First observed reference rank")
    ax.grid(axis="y", color="#d9d9d9", linewidth=.7)
    ax.set_axisbelow(True)
    ax.tick_params(axis="x", rotation=18)
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                str(value), ha="center", va="bottom", fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def save_resource_chart(project_rows, path):
    names = [row["project"] for row in project_rows]
    x = np.arange(len(names))
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.8))
    wall = [row["mean_wall_seconds"] / 60 for row in project_rows]
    tokens = [row["mean_observed_tokens"] / 1000 for row in project_rows]
    for ax, values, title, ylabel, color in (
        (axes[0], wall, "Mean cumulative wall time per case", "Minutes / case", "#315c9b"),
        (axes[1], tokens, "Mean observed tokens per case", "Thousand tokens / case", "#b06f3c")):
        bars = ax.bar(x, values, color=color, width=.65)
        ax.set_xticks(x, names, rotation=18)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.grid(axis="y", color="#d9d9d9", linewidth=.7)
        ax.set_axisbelow(True)
        for bar, value in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.015,
                    f"{value:.1f}", ha="center", va="bottom", fontsize=8)
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scores", type=Path, required=True)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--runtime", type=Path, required=True)
    parser.add_argument("--truth", type=Path, required=True)
    parser.add_argument("--score-script", type=Path, required=True)
    parser.add_argument("--score-core", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    args.out.mkdir(parents=True, exist_ok=True)
    figures = args.out / "figures"
    figures.mkdir(exist_ok=True)

    scores = load(args.scores)
    run_results = load(args.results)
    run_summary = load(args.summary)
    runtime = load(args.runtime)
    truths = load(args.truth)["cases"]
    require = lambda condition, message: condition or (_ for _ in ()).throw(ValueError(message))
    require(len(run_results) == 395 and len(scores["results"]) == 395, "Expected 395 cases")
    require(all(row.get("prediction_valid") for row in run_results), "All predictions must be valid")
    require(scores["summary"]["statuses"] == {"ok": 395}, "All predictions must score cleanly")

    resource_by_case = {row["case_id"]: row for row in run_results}
    score_by_case = {row["case_id"]: row for row in scores["results"]}
    case_rows = []
    rank_counts = {str(i): 0 for i in range(1, 6)}
    rank_counts.update(miss_with_reference=0, no_positive_reference=0)
    for case_id in sorted(resource_by_case, key=lambda value: (project_of(value), int(value.split("_")[1]))):
        resource, score = resource_by_case[case_id], score_by_case[case_id]
        rr = score["reciprocal_rank_at5"]
        first_rank = round(1 / rr) if rr else None
        if first_rank:
            rank_counts[str(first_rank)] += 1
        elif score["reference_status"] == "positive_reference_available":
            rank_counts["miss_with_reference"] += 1
        else:
            rank_counts["no_positive_reference"] += 1
        case_rows.append(dict(
            case_id=case_id, project=project_of(case_id), reference_status=score["reference_status"],
            reference_count=len(score["reference_candidate_ids"]), first_hit_rank_at5=first_rank,
            top1=score["hits"]["top1"], top3=score["hits"]["top3"], top5=score["hits"]["top5"],
            reciprocal_rank_at5=rr, candidate_count=resource["candidate_count"],
            attempts=resource["attempts"], outer_retries=resource["retries"],
            wall_seconds=resource["wall_seconds"], process_seconds=resource["process_seconds"],
            observed_input_tokens=resource.get("known_input_tokens"),
            observed_output_tokens=resource.get("known_output_tokens"),
            observed_total_tokens=observed_tokens(resource), usage_complete=resource["usage_complete"],
            tool_calls=resource["tool_calls"], tool_failures=resource["tool_failures"],
            harness_llm_retry_events=resource["harness_llm_retry_events"],
            known_estimated_cost_cny=resource["known_estimated_cost_cny"],
            cost_unknown=resource["cost_unknown"],
        ))

    project_rows = []
    for project in PROJECTS:
        subset = [row for row in case_rows if row["project"] == project]
        quality = scores["by_project"][project]
        walls = [row["wall_seconds"] for row in subset if row["wall_seconds"] is not None]
        tokens = [row["observed_total_tokens"] for row in subset if row["observed_total_tokens"] is not None]
        project_rows.append(dict(
            project=project, cases=len(subset), positive_reference_cases=sum(
                row["reference_status"] == "positive_reference_available" for row in subset),
            top1_hits=quality["hit_counts"]["top1"], top3_hits=quality["hit_counts"]["top3"],
            top5_hits=quality["hit_counts"]["top5"], top1=quality["hit_rates"]["top1"],
            top3=quality["hit_rates"]["top3"], top5=quality["hit_rates"]["top5"],
            mrr_at5=quality["mrr_at5"], attempts=sum(row["attempts"] for row in subset),
            outer_retries=sum(row["outer_retries"] for row in subset),
            total_wall_seconds=sum(walls), mean_wall_seconds=statistics.mean(walls),
            median_wall_seconds=statistics.median(walls), p95_wall_seconds=percentile(walls, .95),
            observed_total_tokens=sum(tokens), mean_observed_tokens=statistics.mean(tokens),
            tool_calls=sum(row["tool_calls"] for row in subset),
            tool_failures=sum(row["tool_failures"] for row in subset),
            harness_llm_retry_events=(None if any(row["harness_llm_retry_events"] is None for row in subset)
                                      else sum(row["harness_llm_retry_events"] for row in subset)),
            known_estimated_cost_cny=sum(row["known_estimated_cost_cny"] or 0 for row in subset),
            unknown_cost_cases=sum(bool(row["cost_unknown"]) for row in subset),
            usage_incomplete_cases=sum(not row["usage_complete"] for row in subset),
        ))

    start = min(datetime.fromisoformat(row["started_at"]) for row in run_results if row.get("started_at"))
    end = max(datetime.fromisoformat(row["ended_at"]) for row in run_results if row.get("ended_at"))
    walls = [row["wall_seconds"] for row in run_results if row.get("wall_seconds") is not None]
    report = run_summary["reports"][0]
    resources = dict(
        cases=395, attempts=sum(row["attempts"] for row in run_results),
        outer_retries=sum(row["retries"] for row in run_results),
        cumulative_wall_seconds=sum(walls), calendar_span_seconds=(end - start).total_seconds(),
        mean_wall_seconds=statistics.mean(walls), median_wall_seconds=statistics.median(walls),
        p95_wall_seconds=percentile(walls, .95), max_wall_seconds=max(walls),
        process_seconds=sum(row["process_seconds"] for row in run_results if row.get("process_seconds") is not None),
        observed_input_tokens=report["observed_input_tokens"],
        observed_uncached_input_tokens=report["observed_uncached_input_tokens"],
        observed_cached_input_tokens=report["observed_cached_input_tokens"],
        observed_output_tokens=report["observed_output_tokens"],
        observed_reasoning_output_tokens=report["observed_reasoning_output_tokens"],
        observed_total_tokens=report["observed_total_tokens"],
        usage_complete_cases=report["usage_complete_runs"],
        usage_incomplete_cases=report["usage_incomplete_runs"],
        tool_calls=report["tool_calls"], tool_failures=report["tool_failures"],
        harness_llm_retry_events=report["harness_llm_retry_events"],
        recovered_connection_attempts=report["recovered_connection_attempts"],
        known_estimated_cost_cny=report["known_estimated_cost_cny"],
        fully_known_estimated_cost_cny=report["fully_known_estimated_cost_cny"],
        known_cost_cases=report["known_cost_runs"], unknown_cost_cases=report["unknown_cost_runs"],
        earliest_start=start.isoformat(), latest_end=end.isoformat(),
    )

    save_overall_chart(scores["summary"], figures / "overall_quality.png")
    save_project_chart(project_rows, figures / "quality_by_project.png")
    save_rank_chart(rank_counts, figures / "first_hit_rank.png")
    save_resource_chart(project_rows, figures / "resources_by_project.png")

    for filename, rows in (("case_metrics.csv", case_rows), ("project_metrics.csv", project_rows)):
        with (args.out / filename).open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader(); writer.writerows(rows)
    (args.out / "resource_summary.json").write_text(
        json.dumps(resources, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    provenance = dict(
        generated_at=datetime.now().astimezone().isoformat(), evaluation_case_count=395,
        evaluation_performed=True, prediction_results_sha256=digest(args.results),
        run_summary_sha256=digest(args.summary), runtime_sha256=digest(args.runtime),
        harness="Qwen Code", harness_version=runtime.get("harness_version"),
        ground_truth_sha256=digest(args.truth),
        official_scores_sha256=digest(args.scores), score_script_sha256=digest(args.score_script),
        score_core_sha256=digest(args.score_core), scoring_policy=scores["summary"]["scoring_policy"],
    )
    (args.out / "evaluation_provenance.json").write_text(
        json.dumps(provenance, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    summary = scores["summary"]
    positive = summary["positive_reference_subset"]
    md = ["# Qwen Code 方法级故障定位评估报告", "",
          f"评估对象：`Qwen Code {runtime.get('harness_version') or '版本未知'} / alibaba-modelstudio / qwen3.8-max / xhigh` 的最终 395 例预测。", "",
          "## 核心指标", "",
          "| 指标 | 命中数 | 全部 395 例 | 有正例参考的 385 例 |",
          "|---|---:|---:|---:|",
          f"| **Top-1** | **{summary['hit_counts']['top1']}** | **{summary['hit_rates']['top1']:.4%}** | **{positive['hit_rates']['top1']:.4%}** |",
          f"| Top-3 | {summary['hit_counts']['top3']} | {summary['hit_rates']['top3']:.4%} | {positive['hit_rates']['top3']:.4%} |",
          f"| Top-5 | {summary['hit_counts']['top5']} | {summary['hit_rates']['top5']:.4%} | {positive['hit_rates']['top5']:.4%} |",
          f"| **MRR@5** | — | **{summary['mrr_at5']:.6f}** | **{positive['mrr_at5']:.6f}** |", "",
          "主报告采用固定 395 例分母。10 个案例的候选集合中没有正例参考，它们按官方评分策略在 Hit@k 和 MRR@5 中记零；正例子集结果仅用于解释标签覆盖限制。", "",
          "![总体定位指标](figures/overall_quality.png)", "",
          "## 首次命中位置", "",
          "| 首次命中 | 案例数 |", "|---|---:|",
          *[f"| Rank {rank} | {rank_counts[str(rank)]} |" for rank in range(1, 6)],
          f"| Top-5 未命中（有正例） | {rank_counts['miss_with_reference']} |",
          f"| 无正例参考 | {rank_counts['no_positive_reference']} |", "",
          "![首次命中排名分布](figures/first_hit_rank.png)", "",
          "## 分项目质量", "",
          "| 项目 | 案例 | Top-1 | Top-3 | Top-5 | MRR@5 |", "|---|---:|---:|---:|---:|---:|",
          *[f"| {row['project']} | {row['cases']} | {row['top1']:.2%} | {row['top3']:.2%} | {row['top5']:.2%} | {row['mrr_at5']:.4f} |" for row in project_rows], "",
          "![分项目定位指标](figures/quality_by_project.png)", "",
          "## 资源消耗", "",
          "| 项目 | 尝试数 | 累计耗时 | 中位耗时/例 | 已观测 Token | Token/例 | 已知估算费用 CNY | 未知费用例 |", 
          "|---|---:|---:|---:|---:|---:|---:|---:|",
          *[f"| {row['project']} | {row['attempts']} | {row['total_wall_seconds']/3600:.2f} h | {row['median_wall_seconds']:.1f} s | {fmt_int(row['observed_total_tokens'])} | {fmt_int(row['mean_observed_tokens'])} | {row['known_estimated_cost_cny']:.6f} | {row['unknown_cost_cases']} |" for row in project_rows], "",
          "![分项目资源消耗](figures/resources_by_project.png)", "",
          "### 总体资源", "",
          f"- 395 例共 {resources['attempts']} 次尝试，其中外层重试 {resources['outer_retries']} 次。",
          f"- 累计案例耗时 {resources['cumulative_wall_seconds']/3600:.2f} 小时；首例开始到末例结束的日历跨度 {resources['calendar_span_seconds']/3600:.2f} 小时；单例中位数 {resources['median_wall_seconds']:.1f} 秒，P95 {resources['p95_wall_seconds']:.1f} 秒。",
          f"- 已观测输入 Token {fmt_int(resources['observed_input_tokens'])}，输出 Token {fmt_int(resources['observed_output_tokens'])}，合计 {fmt_int(resources['observed_total_tokens'])}，平均每例 {fmt_int(resources['observed_total_tokens']/resources['cases'])}。",
          f"- 缓存命中输入 Token {fmt_int(resources['observed_cached_input_tokens'])}；未缓存输入 Token {fmt_int(resources['observed_uncached_input_tokens'])}。",
          f"- 用量完整 {resources['usage_complete_cases']} 例、不完整 {resources['usage_incomplete_cases']} 例；推理 Token 未被 Qwen Code 单独提供，保留为 `null`。",
          f"- 工具调用 {resources['tool_calls']} 次、工具失败 {resources['tool_failures']} 次；Qwen Code 内部连接重试事件不可观测，保留为 `null`；恢复成功的连接异常尝试同样不可观测。",
          f"- 已知估算费用 {resources['known_estimated_cost_cny']:.9f} CNY；未知费用 {resources['unknown_cost_cases']} 例。费用按冻结价格表和逐请求 Token 估算，不是实际账单。", "",
          "## 口径与限制", "",
          "- Top-k：前 k 个候选中至少一个命中参考方法。MRR@5：首个参考方法在前 5 名中的倒数排名，未命中记零。",
          "- 评估使用 `evaluation_2/score.py` 的固定 395 例口径；所有预测均通过案例 ID、输入哈希、候选合法性和排名格式校验。",
          "- 资源统计包含正式目录中的全部尝试；缓存 Token 与推理 Token 没有重复加入总量。",
          "- 费用来自冻结价格表的估算，不是实际账单。累计案例耗时不是纯日历运行时，停机和额度等待不会全部计入。",
          "- 定位阶段没有读取参考答案；本报告是在预测冻结后独立读取 `evaluation_2` 生成。读取隔离仍为未验证。",
          "- 数据包含公开 Defects4J 案例标识与源码线索，不能排除模型预训练记忆造成的基准污染。", ""]
    (args.out / "evaluation_report.md").write_text("\n".join(md), encoding="utf-8")
    print(json.dumps(dict(top1=summary["hit_rates"]["top1"], top3=summary["hit_rates"]["top3"],
                          top5=summary["hit_rates"]["top5"], mrr_at5=summary["mrr_at5"],
                          valid_predictions=395, observed_total_tokens=resources["observed_total_tokens"],
                          known_estimated_cost_cny=resources["known_estimated_cost_cny"]), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
