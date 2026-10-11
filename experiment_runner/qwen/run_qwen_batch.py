#!/usr/bin/env python3
"""Qwen Code batch runner for localization/resource collection only.

The default action only creates/verifies a frozen plan. Model calls require an
explicit --execute or --resume flag. Reference answers and evaluation_2 are
never opened during localization.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import random
import re
import shutil
import signal
import statistics
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _runner_base as base

VERSION = "1.1-qwen-localize-only"
TOKEN_KEYS = ("input_tokens", "uncached_input_tokens", "cached_input_tokens",
              "cache_write_tokens", "output_tokens", "reasoning_output_tokens")
VALID = {"completed", "empty_prediction"}
RETRYABLE = {"rate_limit", "api_error", "network_error", "timeout",
             "process_error", "invalid_prediction"}
RESUME_RETRYABLE = RETRYABLE | {"interrupted", "auth_error", "quota_error", "setup_error"}
STOP_BATCH = {"auth_error", "quota_error", "setup_error", "configuration_error"}


def require(value, message):
    if not value:
        raise ValueError(message)


def read_config(path):
    path = Path(path).resolve()
    cfg = base.load(path)
    allowed = {"mode", "dataset_root", "prompt_file", "cases_file", "cases",
               "expected_case_count", "require_all_manifest_cases", "conditions",
               "repetitions", "timeout_seconds", "max_retries", "retry_backoff_seconds",
               "shuffle_seed", "auth_mode", "cli_mode", "schema_file", "permission_mode",
               "telemetry_disabled", "max_estimated_cost_cny", "max_session_turns",
               "max_tool_calls", "pricing"}
    require(isinstance(cfg, dict) and not set(cfg) - allowed, "Unknown config fields")
    defaults = dict(repetitions=1, timeout_seconds=600, max_retries=2,
                    retry_backoff_seconds=10, shuffle_seed=20261009,
                    max_estimated_cost_cny=None, expected_case_count=None,
                    require_all_manifest_cases=False, cli_mode="bare",
                    permission_mode="plan", telemetry_disabled=True,
                    max_session_turns=20, max_tool_calls=40)
    cfg = {**defaults, **cfg}
    cfg["dataset_root"] = str((path.parent / cfg.get("dataset_root", "..")).resolve())
    cfg["prompt_file"] = str((path.parent / cfg.get("prompt_file", "prompt.txt")).resolve())
    cfg["schema_file"] = str((path.parent / cfg["schema_file"]).resolve())
    require(cfg.get("mode") == "localize_only", "Only mode=localize_only is supported")
    require(cfg.get("auth_mode") == "dashscope_api_key", "Use auth_mode=dashscope_api_key")
    require(cfg["cli_mode"] == "bare", "cli_mode must be bare")
    require(cfg["permission_mode"] == "plan", "permission_mode must be plan")
    require(cfg["telemetry_disabled"] is True, "telemetry_disabled must be true")
    require(Path(cfg["prompt_file"]).is_file() and Path(cfg["schema_file"]).is_file(),
            "Prompt or prediction schema file is missing")
    for key in ("repetitions", "max_retries", "max_session_turns", "max_tool_calls"):
        base.number(cfg[key], key, 1 if key == "repetitions" else 0, integer=True)
    if cfg["shuffle_seed"] is not None:
        base.number(cfg["shuffle_seed"], "shuffle_seed", 0, integer=True)
    base.number(cfg["timeout_seconds"], "timeout_seconds", .1)
    base.number(cfg["retry_backoff_seconds"], "retry_backoff_seconds")
    if cfg["expected_case_count"] is not None:
        base.number(cfg["expected_case_count"], "expected_case_count", 1, integer=True)
    if cfg["max_estimated_cost_cny"] is not None:
        base.number(cfg["max_estimated_cost_cny"], "max_estimated_cost_cny", .000001)

    manifest = base.load(Path(cfg["dataset_root"]) / "input_2/manifest.json")
    require(isinstance(manifest, dict) and isinstance(manifest.get("cases"), list),
            "Invalid input_2 manifest")
    ids = [x.get("case_id") for x in manifest["cases"] if isinstance(x, dict)]
    require(len(ids) == len(manifest["cases"]) == len(set(ids)), "Duplicate/invalid manifest cases")
    require(manifest.get("case_count") == len(ids), "Manifest case_count mismatch")
    available = {x["case_id"]: x for x in manifest["cases"]}
    require(not ("cases" in cfg and "cases_file" in cfg), "Use cases OR cases_file")
    if "cases_file" in cfg:
        p = (path.parent / cfg.pop("cases_file")).resolve()
        raw = p.read_bytes()
        cfg["cases"] = raw.decode("utf-8-sig").split()
        cfg["case_selection_source"] = str(p)
        cfg["case_selection_sha256"] = base.sha(raw)
    else:
        cfg.setdefault("cases", ids)
        cfg["case_selection_source"] = "inline_or_manifest_default"
        cfg["case_selection_sha256"] = None
    require(cfg["cases"] and all(isinstance(x, str) and x in available for x in cfg["cases"]),
            "Invalid case list")
    require(len(cfg["cases"]) == len(set(cfg["cases"])), "Duplicate cases")
    if cfg["expected_case_count"] is not None:
        require(len(cfg["cases"]) == cfg["expected_case_count"],
                f"Expected {cfg['expected_case_count']} cases, found {len(cfg['cases'])}")
    if cfg["require_all_manifest_cases"]:
        require(len(cfg["cases"]) == len(ids) and set(cfg["cases"]) == set(ids),
                "Case list must contain every manifest case exactly once")

    conditions = cfg.get("conditions")
    require(isinstance(conditions, list) and len(conditions) == 1,
            "Exactly one Qwen condition is required")
    c = conditions[0]
    require(set(c) == {"id", "provider", "model", "reasoning_effort"},
            "Unexpected condition fields")
    require(c == {"id": "qwen3_8_max_xhigh", "provider": "alibaba-modelstudio",
                  "model": "qwen3.8-max", "reasoning_effort": "xhigh"},
            "The frozen condition is alibaba-modelstudio/qwen3.8-max/xhigh")
    pricing = cfg.get("pricing")
    require(isinstance(pricing, dict) and pricing.get("currency") == "CNY" and
            pricing.get("billing_reconciliation_verified") is False,
            "Pricing must be an unverified CNY estimate snapshot")
    tiers = pricing.get("per_request_token_tiers")
    require(isinstance(tiers, list) and tiers, "Expected at least one pricing tier")
    for tier in tiers:
        require(set(tier) == {"max_input_tokens", "uncached_input", "cached_input", "output"},
                "Invalid pricing tier")
        for key, value in tier.items():
            base.number(value, key, 1 if key == "max_input_tokens" else 0)
    return cfg, available


def build_plan(cfg, available):
    inputs = Path(cfg["dataset_root"]) / "input_2"
    paths = [Path(__file__), HERE / "_runner_base.py", HERE / "input_validation.py",
             Path(cfg["prompt_file"]), Path(cfg["schema_file"]), inputs / "manifest.json"]
    if cfg["case_selection_source"] != "inline_or_manifest_default":
        paths.append(Path(cfg["case_selection_source"]))
    files = {str(p): base.sha(p.read_bytes()) for p in paths}
    jobs = [dict(condition_id=c["id"], repeat_id=r, case_id=case)
            for r in range(1, cfg["repetitions"] + 1)
            for case in cfg["cases"] for c in cfg["conditions"]]
    if cfg["shuffle_seed"] is not None:
        random.Random(cfg["shuffle_seed"]).shuffle(jobs)
    plan = dict(runner_version=VERSION, harness="Qwen Code", config=cfg,
                file_hashes=files, jobs=jobs,
                input_hashes={x: available[x]["input_sha256"] for x in cfg["cases"]},
                execution="serial", evaluation_performed=False, answer_files_accessed=False,
                host_isolation_verified=False, isolation_status="not_verified",
                usage_scope="Qwen Code stream-json result usage and per-turn assistant usage",
                cost_scope="Estimate from observed per-request usage and frozen Model Studio list prices; not an invoice")
    plan["fingerprint"] = base.sha(json.dumps(plan, sort_keys=True, ensure_ascii=False).encode())
    return plan


def resolve_qwen(explicit=None):
    candidates = [explicit, shutil.which("qwen"), shutil.which("qwen.cmd")]
    path = next((Path(x).resolve() for x in candidates if x and Path(x).is_file()), None)
    require(path is not None, "Qwen Code CLI not found; use --qwen PATH")
    return [str(path)]


def command_for(prefix, cfg):
    condition = cfg["conditions"][0]
    return [*prefix, "--model", condition["model"], "--bare",
            "--no-telemetry", "--no-chat-recording",
            "--auth-type", "openai",
            "--approval-mode", cfg["permission_mode"], "--exclude-tools", "edit",
            "--exclude-tools", "run_shell_command", "--exclude-tools", "agent",
            "--exclude-tools", "get_goal", "--exclude-tools", "update_goal",
            "--max-session-turns", str(cfg["max_session_turns"]),
            "--max-wall-time", f"{cfg['timeout_seconds']}s",
            "--max-tool-calls", str(cfg["max_tool_calls"]),
            "--output-format", "stream-json", "--json-schema", "@" + cfg["schema_file"]]


def json_objects(path):
    malformed, values = 0, []
    if Path(path).exists():
        for line in Path(path).read_text(encoding="utf-8-sig", errors="replace").splitlines():
            if not line.strip():
                continue
            try:
                item = json.loads(line)
                if not isinstance(item, dict):
                    raise ValueError()
                values.append(item)
            except (ValueError, TypeError):
                malformed += 1
    return values, malformed


def int_token(value):
    return value if type(value) is int and value >= 0 else None


def estimate_cost(samples, pricing, usage_complete):
    if not usage_complete:
        return None, "usage_incomplete", Counter()
    total, tiers = 0.0, Counter()
    for sample in samples:
        u = sample["usage"]
        tier_index = next((i for i, item in enumerate(pricing["per_request_token_tiers"])
                           if u["input_tokens"] <= item["max_input_tokens"]), None)
        if tier_index is None:
            return None, "request_exceeded_pricing_tiers", tiers
        rates = pricing["per_request_token_tiers"][tier_index]
        total += (u["uncached_input_tokens"] * rates["uncached_input"] +
                  u["cached_input_tokens"] * rates["cached_input"] +
                  u["output_tokens"] * rates["output"]) / 1_000_000
        tiers[str(rates["max_input_tokens"])] += 1
    return round(total, 12), "estimated_from_qwen_per_request_usage", tiers


def classify_error(text):
    value = text.lower()
    if any(x in value for x in ("insufficient balance", "insufficient_balance", "quota exceeded",
                                "billing_error", "overdue-payment", "account is in good standing",
                                "402", "余额不足", "欠费")):
        return "quota_error"
    if any(x in value for x in ("invalid api key", "authentication", "unauthorized", "401", "api key",
                                "no auth type", "auth type is selected")):
        return "auth_error"
    if any(x in value for x in ("rate limit", "too many requests", "429")):
        return "rate_limit"
    if any(x in value for x in ("enotfound", "econnreset", "etimedout", "network", "connection")):
        return "network_error"
    return "api_error"


def normalize_qwen_usage(raw):
    if not isinstance(raw, dict):
        return dict.fromkeys(TOKEN_KEYS)
    inp = int_token(raw.get("input_tokens"))
    cached = int_token(raw.get("cache_read_input_tokens"))
    out = int_token(raw.get("output_tokens"))
    if inp is not None and cached is None:
        cached = 0
    uncached = None if inp is None or cached is None or cached > inp else inp - cached
    return dict(input_tokens=inp, uncached_input_tokens=uncached,
                cached_input_tokens=cached, cache_write_tokens=None,
                output_tokens=out, reasoning_output_tokens=None)


def parse_qwen_events(path, expected, evidence):
    events, malformed = json_objects(path)
    init = next((x for x in events if x.get("type") == "system" and
                 x.get("subtype") in {"init", "session_start"}), None)
    results = [x for x in events if x.get("type") == "result" and
               x.get("parent_tool_use_id") in (None, "")]
    result = results[-1] if results else None
    assistants = [x for x in events if x.get("type") == "assistant" and
                  x.get("parent_tool_use_id") in (None, "")]
    samples = []
    tool_calls = tool_failures = structured_calls = 0
    for event in assistants:
        message = event.get("message") if isinstance(event.get("message"), dict) else {}
        usage = normalize_qwen_usage(message.get("usage"))
        # Qwen Code emits presentation-only assistant fragments with an all-zero
        # usage object.  They are not model requests and must not inflate the
        # request/tier counters used for cost reporting.
        if (usage["input_tokens"] is not None and usage["output_tokens"] is not None and
                (usage["input_tokens"] > 0 or usage["output_tokens"] > 0)):
            samples.append({"usage": usage})
        for block in message.get("content", []) if isinstance(message.get("content"), list) else []:
            if isinstance(block, dict) and block.get("type") == "tool_use":
                if block.get("name") == "structured_output":
                    structured_calls += 1
                else:
                    tool_calls += 1
    for event in events:
        message = event.get("message") if isinstance(event.get("message"), dict) else {}
        for block in message.get("content", []) if isinstance(message.get("content"), list) else []:
            if isinstance(block, dict) and block.get("type") == "tool_result" and block.get("is_error"):
                tool_failures += 1
    usage = normalize_qwen_usage(result.get("usage") if result else None)
    sample_total = {key: sum(item["usage"][key] or 0 for item in samples)
                    for key in ("input_tokens", "uncached_input_tokens", "cached_input_tokens", "output_tokens")}
    usage_complete = bool(result and all(usage[key] is not None for key in
                          ("input_tokens", "uncached_input_tokens", "cached_input_tokens", "output_tokens")) and
                          samples and all(sample_total[key] == usage[key] for key in sample_total))
    forbidden = []
    if init:
        tools = init.get("tools") if isinstance(init.get("tools"), list) else []
        forbidden = [name for name in tools if name not in {"read_file", "structured_output"}]
    mismatches = []
    if init and init.get("model") != expected["model"]:
        mismatches.append(f"model: expected {expected['model']}, observed {init.get('model')}")
    if init and Path(init.get("cwd") or "").resolve() != Path(evidence).resolve():
        mismatches.append("Qwen Code cwd did not equal the copied evidence directory")
    if forbidden:
        mismatches.append("unexpected tools: " + ", ".join(map(str, forbidden)))
    prediction = result.get("structured_result") if result else None
    final_text = result.get("result") if result else None
    error_text = ""
    if result and result.get("is_error"):
        error = result.get("error")
        error_text = error.get("message", "") if isinstance(error, dict) else str(error or "")
    return dict(events=events, malformed_events=malformed, init=init, result=result,
                usage=usage, usage_samples=samples, usage_complete=usage_complete,
                tool_calls=tool_calls, tool_failures=tool_failures,
                structured_output_calls=structured_calls,
                harness_llm_retry_events=None,
                fallback_events=sum(x.get("type") == "system" and x.get("subtype") == "model_fallback"
                                    for x in events),
                observed_model=init.get("model") if init else None,
                observed_provider="alibaba-modelstudio", configured_reasoning_effort=expected["reasoning_effort"],
                observed_reasoning_effort=None,
                session_id=(result or init or {}).get("session_id"), session_cwd=init.get("cwd") if init else None,
                qwen_code_version=init.get("qwen_code_version") if init else None,
                config_mismatch=mismatches, prediction=prediction, final_text=final_text,
                error_text=error_text)


def extract_prediction_with_method(text):
    """Extract one unambiguous prediction object while preserving strict validation.

    Harness models sometimes prepend a short explanation even when the requested
    payload is valid JSON.  Accept an exact JSON value, one fenced JSON object, or
    one embedded object with the prediction's three top-level keys.  Ambiguous or
    malformed output remains invalid.
    """
    require(isinstance(text, str) and text.strip(), "Harness did not emit a final prediction")
    value = text.strip()
    try:
        return json.loads(value), "exact_json"
    except json.JSONDecodeError as original_error:
        candidates = []

        for match in re.finditer(r"```(?:json)?\s*(.*?)\s*```", value, flags=re.I | re.S):
            try:
                item = json.loads(match.group(1))
            except json.JSONDecodeError:
                continue
            if isinstance(item, dict) and set(item) == {"case_id", "input_sha256", "ranking"}:
                candidates.append((item, "json_code_fence"))

        decoder = json.JSONDecoder()
        for offset, char in enumerate(value):
            if char != "{":
                continue
            try:
                item, _ = decoder.raw_decode(value[offset:])
            except json.JSONDecodeError:
                continue
            if isinstance(item, dict) and set(item) == {"case_id", "input_sha256", "ranking"}:
                candidates.append((item, "embedded_json_object"))

        unique = {}
        for item, method in candidates:
            key = json.dumps(item, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
            unique.setdefault(key, (item, method))
        if len(unique) == 1:
            return next(iter(unique.values()))
        if len(unique) > 1:
            raise ValueError("Harness emitted multiple distinct prediction objects")
        raise original_error


def extract_prediction(text):
    return extract_prediction_with_method(text)[0]


def run_attempt(prefix, cfg, condition, job, attempt_dir, available, input_io, prompt, env):
    start = time.perf_counter()
    attempt_dir.mkdir(parents=True)
    metrics_path = attempt_dir / "metrics.json"
    m = dict(**job, status="preparing", started_at=base.now(), ended_at=None,
             wall_seconds=None, process_seconds=0.0, process_started=False, pid=None,
             exit_code=None, error=None, usage=dict.fromkeys(TOKEN_KEYS), usage_complete=False,
             estimated_cost_cny=None, cost_status="not_started", cost_source=cfg["pricing"]["source"],
             cost_unknown=True, prediction_valid=False, prediction_validation_error=None,
             tool_calls=0, tool_failures=0, structured_output_calls=0,
             harness_llm_retry_events=None, fallback_events=0,
             recovered_connection_errors=None, session_id=None,
             final_failure_type=None, final_error_message=None,
             host_isolation_verified=False, isolation_status="not_verified")
    base.atomic_json(metrics_path, m)
    proc = None
    try:
        source = Path(cfg["dataset_root"]) / "input_2/cases" / job["case_id"]
        data = input_io.snapshot(source)
        require({n: base.sha(b) for n, b in data.items()} == available[job["case_id"]]["files_sha256"],
                "Input differs from trusted manifest")
        evidence = attempt_dir / "evidence"
        evidence.mkdir()
        for name, content in data.items():
            (evidence / name).write_bytes(content)
        command = command_for(prefix, cfg)
        base.atomic_json(attempt_dir / "command.json", command)
        m["status"] = "running"
        base.atomic_json(metrics_path, m)
        process_start = time.perf_counter()
        with (attempt_dir / "events.jsonl").open("wb") as stdout, (attempt_dir / "stderr.log").open("wb") as stderr:
            kwargs = dict(creationflags=subprocess.CREATE_NO_WINDOW | subprocess.CREATE_NEW_PROCESS_GROUP) if os.name == "nt" else dict(start_new_session=True)
            proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=stdout, stderr=stderr,
                                    cwd=evidence, env=env, **kwargs)
            m.update(pid=proc.pid, process_started=True)
            base.atomic_json(metrics_path, m)
            try:
                proc.communicate(prompt.encode("utf-8"), timeout=cfg["timeout_seconds"] + 30)
                m["status"] = "finished"
            except subprocess.TimeoutExpired:
                base.kill_tree(proc)
                m.update(status="timeout", error=f"Harness exceeded timeout_seconds={cfg['timeout_seconds']}")
            except KeyboardInterrupt:
                base.kill_tree(proc)
                m.update(status="interrupted", error="Interrupted by operator")
            finally:
                m["process_seconds"] = time.perf_counter() - process_start
                m["exit_code"] = proc.returncode
        projected = parse_qwen_events(attempt_dir / "events.jsonl", condition, evidence)
        m.update({key: projected[key] for key in (
            "session_id", "usage", "usage_complete", "tool_calls", "tool_failures",
            "structured_output_calls", "harness_llm_retry_events", "fallback_events",
            "observed_provider", "observed_model", "configured_reasoning_effort",
            "observed_reasoning_effort", "session_cwd",
            "qwen_code_version")})
        cost, status, tiers = estimate_cost(projected["usage_samples"], cfg["pricing"],
                                            projected["usage_complete"])
        m.update(estimated_cost_cny=cost, cost_status=status, cost_unknown=cost is None,
                 pricing_tier_request_counts=dict(tiers))
        if m["status"] == "finished":
            stderr_text = (attempt_dir / "stderr.log").read_text(encoding="utf-8", errors="replace")
            combined_errors = projected["error_text"] + "\n" + stderr_text
            if m["exit_code"] != 0 or (projected["result"] and projected["result"].get("is_error")):
                m["status"] = classify_error(combined_errors)
                m["error"] = combined_errors[-8000:] or f"Qwen Code exited {m['exit_code']}"
            elif projected["result"] is None or projected["init"] is None:
                m.update(status="configuration_error", error="Qwen Code did not emit init/result events")
            elif projected["config_mismatch"]:
                m.update(status="configuration_error", error="; ".join(projected["config_mismatch"]))
            else:
                try:
                    raw_text = projected["final_text"] or ""
                    (attempt_dir / "prediction.raw.txt").write_text(raw_text, encoding="utf-8")
                    prediction = projected["prediction"]
                    if prediction is None:
                        prediction = extract_prediction(raw_text)
                    base.atomic_json(attempt_dir / "prediction.raw.json", prediction)
                    input_io.validate_prediction(prediction, data)
                    require(input_io.snapshot(evidence) == data, "Evidence changed during run")
                    base.atomic_json(attempt_dir / "prediction.json", prediction)
                    m["prediction_sha256"] = base.sha((attempt_dir / "prediction.json").read_bytes())
                    m["prediction_valid"] = True
                    m["status"] = "completed" if prediction["ranking"] else "empty_prediction"
                except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
                    m.update(status="invalid_prediction", error=str(exc), prediction_validation_error=str(exc))
    except KeyboardInterrupt:
        if proc and proc.poll() is None:
            base.kill_tree(proc)
        m.update(status="interrupted", error="Interrupted by operator", usage_complete=False)
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        if proc and proc.poll() is None:
            base.kill_tree(proc)
        m.update(status="process_error" if m["process_started"] else "setup_error", error=str(exc))
    finally:
        if not m["process_started"]:
            m.update(usage=dict.fromkeys(TOKEN_KEYS), usage_complete=False,
                     estimated_cost_cny=None, cost_status="no_process_started", cost_unknown=True)
        if m["status"] not in VALID:
            m["final_failure_type"] = m["status"]
            m["final_error_message"] = m.get("error")
        m["ended_at"] = base.now()
        m["wall_seconds"] = time.perf_counter() - start
        base.atomic_json(metrics_path, m)
    return m


def job_dir(out, job):
    return Path(out) / "runs" / job["condition_id"] / f"repeat_{job['repeat_id']:02d}" / job["case_id"]


def attempts(directory):
    return [(p, base.load(p / "metrics.json")) for p in sorted(Path(directory).glob("attempt_*"))
            if (p / "metrics.json").exists()]


def recover(out, jobs):
    for job in jobs:
        for path, m in attempts(job_dir(out, job)):
            if m["status"] in {"preparing", "running"}:
                require(not base.pid_alive(m.get("pid")), f"Old Harness child PID {m.get('pid')} may still be alive")
                m.update(status="interrupted", error="Runner stopped before recording completion",
                         ended_at=None, wall_seconds=None, process_seconds=None,
                         usage_complete=False, estimated_cost_cny=None, cost_unknown=True,
                         cost_status="interrupted_unknown_usage", prediction_valid=False,
                         final_failure_type="interrupted",
                         final_error_message="Runner stopped before recording completion")
                base.atomic_json(path / "metrics.json", m)


def read_only_plan_compatible(saved, current):
    """Allow reports/recovery after a runner-only source upgrade, never execution."""
    stable = ("config", "jobs", "input_hashes", "execution", "evaluation_performed",
              "answer_files_accessed", "host_isolation_verified", "isolation_status",
              "usage_scope", "cost_scope")
    if any(saved.get(key) != current.get(key) for key in stable):
        return False
    if set(saved.get("file_hashes", {})) != set(current.get("file_hashes", {})):
        return False
    changed = {path for path in saved["file_hashes"]
               if saved["file_hashes"][path] != current["file_hashes"][path]}
    return changed == {str(Path(__file__).resolve())}


def recover_saved_predictions(out, plan, available):
    """Re-parse saved raw text without changing or invoking the model.

    Original metrics are copied beside the attempt before a recovered status is
    written.  Token, cost, timing, tool, and retry observations are untouched.
    """
    input_io = base.module_from(HERE / "input_validation.py", "fl_input_validation_qwen_recovery")
    recovered, unresolved = [], []
    recovered_at = base.now()
    recovery_root = Path(out) / "local_recovery"
    for job in plan["jobs"]:
        values = attempts(job_dir(out, job))
        if not values:
            unresolved.append({**job, "status": "not_run", "error": "No saved attempt"})
            continue
        path, metrics = values[-1]
        if metrics.get("prediction_valid"):
            continue
        if metrics.get("status") != "invalid_prediction":
            unresolved.append({**job, "status": metrics.get("status"),
                               "error": metrics.get("final_error_message") or metrics.get("error"),
                               "source_attempt": str(path)})
            continue
        raw_path = path / "prediction.raw.txt"
        try:
            raw = raw_path.read_text(encoding="utf-8")
            prediction, method = extract_prediction_with_method(raw)
            data = input_io.snapshot(path / "evidence")
            meta = available[job["case_id"]]
            require({name: base.sha(content) for name, content in data.items()} == meta["files_sha256"],
                    "Saved evidence differs from trusted input manifest")
            input_io.validate_prediction(prediction, data)
            backup = path / "metrics.pre_local_recovery.json"
            if not backup.exists():
                base.atomic_json(backup, metrics)
            base.atomic_json(path / "prediction.raw.json", prediction)
            base.atomic_json(path / "prediction.json", prediction)
            updated = dict(metrics)
            updated.update(status="completed" if prediction["ranking"] else "empty_prediction",
                           prediction_valid=True, prediction_validation_error=None,
                           prediction_sha256=base.sha((path / "prediction.json").read_bytes()),
                           error=None, final_failure_type=None, final_error_message=None,
                           locally_recovered=True, local_recovery_version=VERSION,
                           local_recovery_method=method, locally_recovered_at=recovered_at,
                           pre_recovery_status=metrics.get("status"),
                           pre_recovery_error=metrics.get("final_error_message") or metrics.get("error"),
                           raw_prediction_text_sha256=base.sha(raw.encode("utf-8")))
            base.atomic_json(path / "metrics.json", updated)
            recovered.append({**job, "source_attempt": str(path), "method": method,
                              "raw_prediction_text_sha256": updated["raw_prediction_text_sha256"],
                              "prediction_sha256": updated["prediction_sha256"]})
        except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
            unresolved.append({**job, "status": metrics.get("status"), "error": str(exc),
                               "source_attempt": str(path)})
    recovery_root.mkdir(parents=True, exist_ok=True)
    report = dict(generated_at=recovered_at, mode="local_prediction_recovery",
                  model_calls_made=0, evaluation_performed=False, answer_files_accessed=False,
                  runner_version=VERSION, source_plan_fingerprint=plan.get("fingerprint"),
                  recovered_count=len(recovered), unresolved_count=len(unresolved),
                  recovered=recovered, unresolved=unresolved)
    base.atomic_json(recovery_root / "report.json", report)
    (recovery_root / "unresolved_cases.txt").write_text(
        "".join(item["case_id"] + "\n" for item in unresolved), encoding="utf-8")
    return report


def summarize_job(out, job):
    values = attempts(job_dir(out, job))
    result = dict(**job, status="not_run", attempts=0, retries=0, prediction_valid=False,
                  wall_seconds=None, process_seconds=None, started_at=None, ended_at=None,
                  estimated_cost_cny=None, known_estimated_cost_cny=None, cost_unknown=None,
                  usage_complete=False, tool_calls=0, tool_failures=0,
                  structured_output_calls=0, harness_llm_retry_events=None,
                  fallback_events=0, recovered_connection_attempts=None,
                  final_failure_type=None, final_error_message=None, last_attempt=None,
                  attempt_durations_seconds=[], **dict.fromkeys(TOKEN_KEYS),
                  **{"known_" + k: None for k in TOKEN_KEYS})
    if not values:
        return result
    metrics = [x for _, x in values]
    last_path, last = values[-1]
    walls = [x.get("wall_seconds") for x in metrics]
    waits = [base.load(p).get("elapsed_seconds") for p in job_dir(out, job).glob("retry_wait_*.json")]
    wait_total = base.sum_complete(waits) if waits else 0
    wall = base.sum_complete(walls)
    result.update(status=last["status"], attempts=len(metrics), retries=len(metrics)-1,
                  prediction_valid=bool(last.get("prediction_valid")), started_at=metrics[0]["started_at"],
                  ended_at=last.get("ended_at"), wall_seconds=wall + wait_total if wall is not None else None,
                  process_seconds=base.sum_complete([x.get("process_seconds") for x in metrics]),
                  estimated_cost_cny=base.sum_complete([x.get("estimated_cost_cny") for x in metrics]),
                  known_estimated_cost_cny=base.sum_observed([x.get("estimated_cost_cny") for x in metrics]),
                  cost_unknown=any(x.get("estimated_cost_cny") is None for x in metrics),
                  usage_complete=all(x.get("usage_complete", False) for x in metrics),
                  tool_calls=sum(x.get("tool_calls", 0) for x in metrics),
                  tool_failures=sum(x.get("tool_failures", 0) for x in metrics),
                  structured_output_calls=sum(x.get("structured_output_calls", 0) for x in metrics),
                  harness_llm_retry_events=base.sum_observed([x.get("harness_llm_retry_events") for x in metrics]),
                  fallback_events=sum(x.get("fallback_events", 0) for x in metrics),
                  recovered_connection_attempts=base.sum_observed([
                      int(x["recovered_connection_errors"]) if x.get("recovered_connection_errors") is not None else None
                      for x in metrics]),
                  final_failure_type=last.get("final_failure_type"),
                  final_error_message=last.get("final_error_message"), last_attempt=str(last_path),
                  attempt_durations_seconds=walls)
    for key in TOKEN_KEYS:
        vals = [x.get("usage", {}).get(key) for x in metrics]
        result[key] = base.sum_complete(vals)
        result["known_" + key] = base.sum_observed(vals)
    return result


def aggregate(rows):
    attempted = [x for x in rows if x["attempts"]]
    valid = [x for x in rows if x["prediction_valid"]]
    failed = [x for x in attempted if not x["prediction_valid"]]
    costs = [x["estimated_cost_cny"] for x in attempted]
    report = dict(planned_runs=len(rows), attempted_runs=len(attempted),
                  completed_runs=sum(x["status"] in VALID for x in rows),
                  valid_prediction_runs=len(valid), failed_runs=len(failed),
                  not_run_runs=len(rows)-len(attempted),
                  failed_or_not_run_runs=len(failed)+len(rows)-len(attempted),
                  outer_retries=sum(x["retries"] for x in attempted),
                  harness_llm_retry_events=base.sum_observed([x["harness_llm_retry_events"] for x in attempted]),
                  fallback_events=sum(x["fallback_events"] for x in attempted),
                  recovered_connection_attempts=base.sum_observed([x["recovered_connection_attempts"] for x in attempted]),
                  tool_calls=sum(x["tool_calls"] for x in attempted),
                  tool_failures=sum(x["tool_failures"] for x in attempted),
                  structured_output_calls=sum(x["structured_output_calls"] for x in attempted),
                  usage_complete_runs=sum(x["usage_complete"] for x in attempted),
                  usage_incomplete_runs=sum(not x["usage_complete"] for x in attempted),
                  known_cost_runs=sum(x is not None for x in costs),
                  unknown_cost_runs=sum(x is None for x in costs),
                  known_estimated_cost_cny=base.sum_observed([x["known_estimated_cost_cny"] for x in attempted]),
                  fully_known_estimated_cost_cny=base.sum_complete(costs),
                  total_wall_seconds=base.sum_observed([x["wall_seconds"] for x in attempted]))
    for key in TOKEN_KEYS:
        report["observed_" + key] = base.sum_observed([x["known_" + key] for x in attempted])
    report["observed_total_tokens"] = (report["observed_input_tokens"] + report["observed_output_tokens"]
                                       if report["observed_input_tokens"] is not None and
                                       report["observed_output_tokens"] is not None else None)
    return report


def write_csv(path, rows):
    if not rows:
        return
    fields = list(dict.fromkeys(k for row in rows for k in row))
    with Path(path).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else v
                             for k, v in row.items()})


def export_results(out, plan, available):
    cfg, rows, attempt_rows = plan["config"], [], []
    input_io = base.module_from(HERE / "input_validation.py", "fl_input_validation_qwen_export")
    condition = cfg["conditions"][0]
    for job in plan["jobs"]:
        row = summarize_job(out, job)
        meta = available[job["case_id"]]
        row.update(provider=condition["provider"], model=condition["model"],
                   reasoning_effort=condition["reasoning_effort"], auth_mode=cfg["auth_mode"],
                   input_sha256=meta["input_sha256"], candidate_count=meta.get("candidate_count"),
                   evaluation_performed=False, prediction=None, raw_prediction=None,
                   prediction_path=None, raw_prediction_path=None, events_path=None,
                   stderr_path=None)
        if row["attempts"]:
            p = Path(row["last_attempt"])
            row.update(events_path=str(p / "events.jsonl"), stderr_path=str(p / "stderr.log"),
                       raw_prediction_path=str(p / "prediction.raw.json") if (p / "prediction.raw.json").exists() else None)
            if (p / "prediction.raw.json").exists():
                row["raw_prediction"] = base.load(p / "prediction.raw.json")
        if row["prediction_valid"]:
            p = Path(row["last_attempt"])
            data = input_io.snapshot(p / "evidence")
            require({n: base.sha(b) for n, b in data.items()} == meta["files_sha256"], "Saved evidence changed")
            prediction = base.load(p / "prediction.json")
            input_io.validate_prediction(prediction, data)
            dest = Path(out) / "predictions" / job["condition_id"] / f"repeat_{job['repeat_id']:02d}" / f"{job['case_id']}.json"
            base.atomic_json(dest, prediction)
            row.update(prediction=prediction, prediction_path=str(dest))
        rows.append(row)
        for p, item in attempts(job_dir(out, job)):
            attempt_rows.append({**job, "attempt_id": p.name, "status": item["status"],
                                 "started_at": item["started_at"], "ended_at": item.get("ended_at"),
                                 "wall_seconds": item.get("wall_seconds"), "process_seconds": item.get("process_seconds"),
                                 "exit_code": item.get("exit_code"), **item.get("usage", {}),
                                 "usage_complete": item.get("usage_complete"),
                                 "estimated_cost_cny": item.get("estimated_cost_cny"),
                                 "cost_status": item.get("cost_status"), "cost_source": item.get("cost_source"),
                                 "cost_unknown": item.get("cost_unknown"),
                                 "prediction_valid": item.get("prediction_valid"),
                                 "tool_calls": item.get("tool_calls"), "tool_failures": item.get("tool_failures"),
                                 "structured_output_calls": item.get("structured_output_calls"),
                                 "harness_llm_retry_events": item.get("harness_llm_retry_events"),
                                 "fallback_events": item.get("fallback_events"),
                                 "recovered_connection_errors": item.get("recovered_connection_errors"),
                                 "session_id": item.get("session_id"),
                                 "observed_provider": item.get("observed_provider"),
                                 "observed_model": item.get("observed_model"),
                                 "configured_reasoning_effort": item.get("configured_reasoning_effort"),
                                 "observed_reasoning_effort": item.get("observed_reasoning_effort"),
                                 "final_failure_type": item.get("final_failure_type"),
                                 "final_error_message": item.get("final_error_message"),
                                 "locally_recovered": item.get("locally_recovered", False),
                                 "local_recovery_version": item.get("local_recovery_version"),
                                 "local_recovery_method": item.get("local_recovery_method"),
                                 "locally_recovered_at": item.get("locally_recovered_at"),
                                 "pre_recovery_status": item.get("pre_recovery_status"),
                                 "pre_recovery_error": item.get("pre_recovery_error"),
                                 "raw_prediction_text_sha256": item.get("raw_prediction_text_sha256"),
                                 "artifact_dir": str(p)})
    report = dict(condition_id=condition["id"], provider=condition["provider"], model=condition["model"],
                  reasoning_effort=condition["reasoning_effort"], **aggregate(rows))
    write_csv(Path(out) / "results.csv", rows)
    write_csv(Path(out) / "attempts.csv", attempt_rows)
    write_csv(Path(out) / "summary.csv", [report])
    base.atomic_json(Path(out) / "results.json", rows)
    note = ("No reference answers were loaded. Costs are estimates, not invoice amounts; "
            "null means unknown. Cache and reasoning tokens are not added twice.")
    summary = dict(generated_at=base.now(), mode="localize_only",
                   evaluation_performed=False, answer_files_accessed=False,
                   host_isolation_verified=False, isolation_status="not_verified",
                   pricing=cfg["pricing"], reports=[report], note=note)
    base.atomic_json(Path(out) / "summary.json", summary)
    cost = "null" if report["known_estimated_cost_cny"] is None else f"{report['known_estimated_cost_cny']:.6f}"
    retries = "null" if report["harness_llm_retry_events"] is None else str(report["harness_llm_retry_events"])
    lines = ["# Qwen Code 仅定位与资源统计汇总", "",
             "未读取参考答案，未计算 Top-k、MRR、召回率或准确率。费用为官方价格快照下的估算，并非账单。",
             "读取隔离未验证：Harness 只读模式不等于严格的 OS 级读取隔离。", "",
             "| 条件 | 已完成/计划 | 有效预测 | 失败 | 未运行 | 外层重试 | Harness 内部重试事件 | 工具失败 | 已知估算费用 CNY | 未知费用运行数 |",
             "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
             f"| {condition['id']} | {report['completed_runs']}/{report['planned_runs']} | {report['valid_prediction_runs']} | {report['failed_runs']} | {report['not_run_runs']} | {report['outer_retries']} | {retries} | {report['tool_failures']} | {cost} | {report['unknown_cost_runs']} |"]
    (Path(out) / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return rows


def cost_limit_reached(out, plan):
    limit = plan["config"]["max_estimated_cost_cny"]
    if limit is None:
        return False
    values = [m for job in plan["jobs"] for _, m in attempts(job_dir(out, job))]
    return any(x.get("estimated_cost_cny") is None for x in values) or sum(x["estimated_cost_cny"] for x in values) >= limit


def execute(out, plan, available, prefix, env, resume=False):
    cfg = plan["config"]
    input_io = base.module_from(HERE / "input_validation.py", "fl_input_validation_qwen_run")
    prompt = Path(cfg["prompt_file"]).read_text(encoding="utf-8-sig")
    condition = cfg["conditions"][0]
    recover(out, plan["jobs"])
    reason = "completed"
    for index, job in enumerate(plan["jobs"], 1):
        old = attempts(job_dir(out, job))
        if old:
            status = old[-1][1]["status"]
            if status in VALID or len(old) >= cfg["max_retries"] + 1:
                continue
            if status not in (RESUME_RETRYABLE if resume else RETRYABLE):
                continue
        if cost_limit_reached(out, plan):
            reason = "cost_limit_or_unknown_cost"
            break
        while len(old) <= cfg["max_retries"]:
            if old:
                delay = cfg["retry_backoff_seconds"] * 2 ** (len(old)-1)
                wait = job_dir(out, job) / f"retry_wait_{len(old):02d}.json"
                begun = time.perf_counter()
                base.atomic_json(wait, dict(started_at=base.now(), requested_seconds=delay, elapsed_seconds=None))
                try:
                    time.sleep(delay)
                finally:
                    base.atomic_json(wait, dict(ended_at=base.now(), requested_seconds=delay,
                                                elapsed_seconds=time.perf_counter()-begun))
            attempt_dir = job_dir(out, job) / f"attempt_{len(old)+1:02d}"
            print(f"[{index}/{len(plan['jobs'])}] {job['case_id']} attempt={len(old)+1}", flush=True)
            m = run_attempt(prefix, cfg, condition, job, attempt_dir, available, input_io, prompt, env)
            print(f"  {m['status']} {m['wall_seconds']:.1f}s cost_estimate_cny={m['estimated_cost_cny']}", flush=True)
            old = attempts(job_dir(out, job))
            if m["status"] not in RETRYABLE or len(old) >= cfg["max_retries"] + 1 or cost_limit_reached(out, plan):
                break
        if m["status"] in STOP_BATCH or m["status"] == "interrupted":
            reason = m["status"]
            break
    base.atomic_json(Path(out) / "run_status.json", dict(stopped_at=base.now(), reason=reason))
    return reason


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=HERE / "config.qwen_full395.localize_only.json")
    parser.add_argument("--out", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--execute", action="store_true")
    mode.add_argument("--resume", action="store_true")
    mode.add_argument("--summarize", action="store_true")
    mode.add_argument("--recover-predictions", action="store_true",
                      help="Re-parse saved raw predictions locally; never invokes Harness")
    parser.add_argument("--qwen", help="Path to qwen.cmd or qwen executable")
    parser.add_argument("--qwen-settings", type=Path, default=Path.home() / ".qwen" / "settings.json")
    args = parser.parse_args(argv)
    out = None
    try:
        cfg, available = read_config(args.config)
        out = args.out.resolve()
        root = Path(cfg["dataset_root"])
        require(not out.is_relative_to(root / "input_2") and not out.is_relative_to(root / "evaluation_2"),
                "Output must be outside input_2 and evaluation_2")
        current_plan = build_plan(cfg, available)
        plan = current_plan
        out.mkdir(parents=True, exist_ok=True)
        with base.experiment_lock(out):
            plan_path = out / "plan.json"
            if plan_path.exists():
                saved_plan = base.load(plan_path)
                if saved_plan["fingerprint"] != current_plan["fingerprint"]:
                    require((args.summarize or args.recover_predictions) and
                            read_only_plan_compatible(saved_plan, current_plan),
                            "Plan inputs changed; use a new output directory")
                    plan = saved_plan
                    print("Using the frozen plan for read-only reporting/local recovery; "
                          "runner source changed, so this output cannot be resumed with this runner.", flush=True)
            else:
                require(not args.resume and not args.summarize and not args.recover_predictions,
                        "No plan exists; create it first")
                require(not (out / "runs").exists(), "Existing runs without a plan")
                base.atomic_json(plan_path, plan)
                (out / "prompt.txt").write_text(Path(cfg["prompt_file"]).read_text(encoding="utf-8-sig"), encoding="utf-8")
            if args.summarize:
                export_results(out, plan, available)
                print(f"Reports: {out / 'summary.md'}")
                return 0
            if args.recover_predictions:
                report = recover_saved_predictions(out, plan, available)
                export_results(out, plan, available)
                print(f"Locally recovered: {report['recovered_count']}; unresolved: {report['unresolved_count']}")
                print(f"Recovery report: {out / 'local_recovery' / 'report.json'}")
                print("No model calls made.")
                return 0
            if not (args.execute or args.resume):
                print(f"PLAN ONLY: {len(plan['jobs'])} runs, at most {len(plan['jobs']) * (cfg['max_retries']+1)} attempts.")
                print(f"Plan: {plan_path}\nNo model calls made. Use --execute to start.")
                return 0
            require(args.resume or not (out / "runs").exists(), "Runs exist; use --resume")
            settings = base.load(args.qwen_settings)
            require(settings.get("security", {}).get("auth", {}).get("selectedType") == "openai",
                    "Qwen Code must use the configured Model Studio OpenAI-compatible provider")
            require(bool(settings.get("env", {}).get("DASHSCOPE_API_KEY")),
                    "Qwen settings do not contain a DASHSCOPE_API_KEY; configure Qwen Code first")
            provider_rows = settings.get("modelProviders", {}).get("openai", [])
            selected = next((row for row in provider_rows if row.get("id") == cfg["conditions"][0]["model"]), None)
            require(selected is not None, "Selected Qwen model is absent from modelProviders.openai")
            reasoning = selected.get("capabilities", {}).get("reasoning", {})
            require("xhigh" in reasoning.get("efforts", []) and reasoning.get("defaultEffort") == "xhigh",
                    "qwen3.8-max xhigh reasoning is not the registered default")
            prefix = resolve_qwen(args.qwen)
            env = os.environ.copy()
            env["DASHSCOPE_API_KEY"] = settings["env"]["DASHSCOPE_API_KEY"]
            env["OPENAI_API_KEY"] = settings["env"]["DASHSCOPE_API_KEY"]
            env["OPENAI_BASE_URL"] = selected["baseUrl"]
            version = subprocess.run([*prefix, "--version"], capture_output=True, check=True, timeout=30, env=env)
            runtime = dict(harness_version=version.stdout.decode(errors="replace").strip(), launcher=prefix,
                           harness="Qwen Code", cli_mode=cfg["cli_mode"],
                           provider=cfg["conditions"][0]["provider"],
                           model=cfg["conditions"][0]["model"],
                           reasoning_effort=cfg["conditions"][0]["reasoning_effort"],
                           base_url=selected.get("baseUrl"), auth_mode=cfg["auth_mode"],
                           permission_mode=cfg["permission_mode"], telemetry_disabled=True,
                           chat_recording=False, settings_path=str(args.qwen_settings.resolve()))
            runtime_path = out / "runtime.json"
            if runtime_path.exists():
                require(base.load(runtime_path) == runtime, "Harness runtime changed; use a new output directory")
            else:
                base.atomic_json(runtime_path, runtime)
            print("Read isolation is NOT verified; Qwen plan/bare mode is not an OS read boundary.", flush=True)
            try:
                reason = execute(out, plan, available, prefix, env, args.resume)
            except KeyboardInterrupt:
                reason = "interrupted"
                base.atomic_json(out / "run_status.json", dict(stopped_at=base.now(), reason=reason))
            finally:
                rows = export_results(out, plan, available)
            print(f"Reports: {out / 'summary.md'}")
            return 0 if reason == "completed" and all(x["prediction_valid"] for x in rows) else 2
    except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        if out is not None and (out / "plan.json").exists():
            try:
                base.atomic_json(out / "run_status.json", dict(stopped_at=base.now(), reason="configuration_error", error=str(exc)))
            except OSError:
                pass
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    if os.name != "nt":
        signal.signal(signal.SIGTERM, lambda *_: (_ for _ in ()).throw(KeyboardInterrupt()))
    raise SystemExit(main())
