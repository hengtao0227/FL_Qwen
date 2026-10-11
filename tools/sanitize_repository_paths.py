#!/usr/bin/env python3
"""Redact machine-local user-home prefixes in a copied repository.

This is a byte-for-byte replacement of path prefixes only. It intentionally
does not recompute dataset hashes or alter source evidence, labels, or scores.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--home-prefix", required=True,
                        help=r"User-home prefix to redact, for example C:\Users\name")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    home = args.home_prefix.rstrip("\\/")
    patterns = (
        (home.replace("\\", "\\\\").encode(), b"${USER_HOME}"),
        (home.encode(), b"${USER_HOME}"),
        (home.replace("\\", "/").encode(), b"${USER_HOME}"),
    )
    changed = []
    replacements = 0
    for path in sorted(root.rglob("*")):
        if (not path.is_file() or path.name == "SANITIZATION_REPORT.json" or
                path.resolve() == Path(__file__).resolve()):
            continue
        data = path.read_bytes()
        updated = data
        count = 0
        for before, after in patterns:
            occurrences = updated.count(before)
            if occurrences:
                updated = updated.replace(before, after)
                count += occurrences
        if count:
            changed.append({"path": path.relative_to(root).as_posix(),
                            "replacements": count})
            replacements += count
            if args.apply:
                path.write_bytes(updated)
    report = {
        "mode": "applied" if args.apply else "dry_run",
        "scope": "machine-local user-home path prefixes only",
        "replacement": "${USER_HOME}",
        "changed_files": len(changed),
        "replacements": replacements,
        "files": changed,
    }
    if args.apply:
        (root / "SANITIZATION_REPORT.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in report if key != "files"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
