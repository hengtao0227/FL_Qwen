#!/usr/bin/env python3
"""Verify the publishable repository is complete, Qwen-only, and unstarted."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def nonempty_lines(path):
    return [line.strip() for line in path.read_text(encoding="utf-8-sig").splitlines()
            if line.strip()]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    root = args.root.resolve()
    inputs = nonempty_lines(root / "input_2" / "all395.txt")
    evaluation = nonempty_lines(root / "evaluation_2" / "all395.txt")
    case_dirs = {path.name for path in (root / "input_2" / "cases").iterdir()
                 if path.is_dir()}
    outputs = [path for path in (root / "experiment_runs" / "qwen").rglob("*")
               if path.is_file() and path.name != ".gitkeep"]
    runner_root = root / "experiment_runner"
    forbidden = [path for path in runner_root.iterdir()
                 if path.name.lower() in {"gpt", "deepseek", "compare_qwen_deepseek.py"}]
    validation = json.loads((root / "evaluation_2" / "VALIDATION.json").read_text(
        encoding="utf-8-sig"))
    checks = {
        "input_cases": len(inputs),
        "unique_input_cases": len(set(inputs)),
        "input_case_directories": len(case_dirs),
        "evaluation_cases": len(evaluation),
        "case_sets_equal": set(inputs) == set(evaluation) == case_dirs,
        "model_output_files": len(outputs),
        "forbidden_non_qwen_runner_entries": [str(path.relative_to(root)) for path in forbidden],
        "dataset_validation_status": validation.get("status"),
    }
    ok = (checks["input_cases"] == checks["unique_input_cases"] ==
          checks["input_case_directories"] == checks["evaluation_cases"] == 395 and
          checks["case_sets_equal"] and checks["model_output_files"] == 0 and
          not forbidden and checks["dataset_validation_status"] == "passed")
    result = {"status": "passed" if ok else "failed", **checks}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
