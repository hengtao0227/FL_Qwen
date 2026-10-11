"""Validate one input_2 case without importing or reading evaluation_2.

This module is deliberately colocated with the collection runner.  Its fixed
allowlist and validation rules depend only on the public input package.
"""
from __future__ import annotations

import hashlib
import json
import re
import stat
from pathlib import Path

VERSION = "codex-methodfl-classic395-v4-uniform-method-entry"
EVIDENCE = frozenset((
    "TASK.md", "failure_report.txt", "failed_tests.md", "failed_tests.json",
    "candidate_index.tsv", "candidate_index.json", "methods.txt", "fields.json",
))
FILES = EVIDENCE | {"case.json", "prediction_template.json"}
META_KEYS = frozenset((
    "dataset_version", "case_id", "task_type", "evidence_policy",
    "candidate_count", "failed_test_count", "files_sha256", "input_sha256",
    "candidate_order_seed", "candidate_order_algorithm",
))
INDEX_KEYS = frozenset((
    "candidate_id", "signature", "class_name", "src_path", "begin_line",
    "end_line", "bundle_start_line", "bundle_end_line",
))
FIELD_KEYS = frozenset((
    "class_name", "src_path", "signature", "snippet", "begin_line", "end_line", "comment",
))
TEST_KEYS = frozenset((
    "requested_signature", "resolved_signature", "resolution", "src_path",
    "begin_line", "end_line", "comment", "snippet",
))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def fingerprint(hashes):
    return digest(json.dumps(hashes, sort_keys=True, separators=(",", ":")).encode())


def require(condition, message):
    if not condition:
        raise ValueError(message)


def no_links(path):
    """Reject symlinks and Windows reparse points, including parent components."""
    path = Path(path).absolute()
    for part in (path, *path.parents):
        info = part.lstat()
        require(not stat.S_ISLNK(info.st_mode), "Symbolic links are not allowed")
        require(not getattr(info, "st_file_attributes", 0) & 0x400,
                "Reparse points are not allowed")
    return path


def snapshot(case_dir):
    """Load only the ten allowlisted files for one input_2 case."""
    root = no_links(case_dir)
    require(root.is_dir(), "Case directory required")
    entries = list(root.iterdir())
    require({p.name for p in entries} == FILES, "Case file inventory mismatch")
    data = {}
    for path in entries:
        no_links(path)
        require(path.is_file(), "Only regular files allowed")
        data[path.name] = path.read_bytes()
    validate_snapshot(data)
    return data


def validate_snapshot(data):
    require(set(data) == FILES, "Unexpected case files")
    meta = json.loads(data["case.json"])
    require(set(meta) == META_KEYS, "Unexpected metadata schema")
    require(meta["dataset_version"] == VERSION, "Unexpected version")
    require(re.fullmatch(r"(Chart|Closure|Lang|Math|Mockito|Time)_[1-9]\d*", meta["case_id"]),
            "Invalid case ID")
    require(meta["task_type"] == "offline_candidate_restricted_method_fl", "Task mismatch")
    require(meta["evidence_policy"] == "original_source_tests_stack_comments", "Policy mismatch")
    hashes = meta["files_sha256"]
    require(set(hashes) == EVIDENCE, "Evidence allowlist mismatch")
    require(all(digest(data[name]) == value for name, value in hashes.items()),
            "Evidence hash mismatch")
    require(fingerprint(hashes) == meta["input_sha256"], "Input fingerprint mismatch")
    template = json.loads(data["prediction_template.json"])
    require(template == {"case_id": meta["case_id"], "input_sha256": meta["input_sha256"],
                         "ranking": []}, "Nonempty or invalid template")
    index = json.loads(data["candidate_index.json"])
    tests = json.loads(data["failed_tests.json"])
    fields = json.loads(data["fields.json"])
    require(len(index) == meta["candidate_count"], "Candidate count mismatch")
    require(len(tests) == meta["failed_test_count"], "Test count mismatch")
    require(all(set(row) == INDEX_KEYS for row in index), "Candidate schema mismatch")
    require(all(set(row) == TEST_KEYS for row in tests), "Test schema mismatch")
    require(all(set(row) == FIELD_KEYS for row in fields), "Field schema mismatch")
    ids = [row["candidate_id"] for row in index]
    require(ids == [f"M{i:04d}" for i in range(1, len(index) + 1)], "Candidate IDs mismatch")
    columns = ("candidate_id", "signature", "src_path", "begin_line", "end_line",
               "bundle_start_line", "bundle_end_line")
    tsv = ["\t".join(columns)] + ["\t".join(str(row[key]) for key in columns) for row in index]
    require(data["candidate_index.tsv"].decode().splitlines() == tsv, "TSV mismatch")
    lines = data["methods.txt"].decode().splitlines()
    previous = 0
    for row in index:
        first, last = row["bundle_start_line"], row["bundle_end_line"]
        require(previous < first <= last <= len(lines), "Invalid bundle range")
        require(lines[first - 1] == f"===== {row['candidate_id']} =====", "Bundle ID mismatch")
        require(lines[first] == "Signature: " + row["signature"], "Signature mismatch")
        require(lines[first + 1] == "Source: " + row["src_path"], "Source mismatch")
        previous = last
    return meta


def validate_prediction(value, data):
    meta = json.loads(data["case.json"])
    require(isinstance(value, dict) and set(value) == {"case_id", "input_sha256", "ranking"},
            "Prediction schema mismatch")
    require(value["case_id"] == meta["case_id"] and
            value["input_sha256"] == meta["input_sha256"], "Prediction input mismatch")
    ranking = value["ranking"]
    require(isinstance(ranking, list) and 0 <= len(ranking) <= 5,
            "Expect at most 5 candidates")
    allowed = {row["candidate_id"] for row in json.loads(data["candidate_index.json"])}
    seen = set()
    for rank, row in enumerate(ranking, 1):
        require(isinstance(row, dict) and set(row) == {"rank", "candidate_id", "reason"},
                "Ranking entry schema mismatch")
        require(type(row["rank"]) is int and row["rank"] == rank, "Nonsequential rank")
        require(isinstance(row["candidate_id"], str) and row["candidate_id"] in allowed and
                row["candidate_id"] not in seen, "Invalid or duplicate candidate")
        require(isinstance(row["reason"], str) and 1 <= len(row["reason"].strip()) <= 12000,
                "Reason missing or too long")
        seen.add(row["candidate_id"])
    return value
