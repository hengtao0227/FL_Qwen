#!/usr/bin/env python3
"""Verify every file listed in CHECKSUMS.sha256."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    root = args.root.resolve()
    manifest = root / "CHECKSUMS.sha256"
    checked = 0
    failures = []
    for line in manifest.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        expected, relative = line.split("  ", 1)
        path = root / Path(relative)
        if not path.is_file():
            failures.append(f"missing: {relative}")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            failures.append(f"hash mismatch: {relative}")
        checked += 1
    if failures:
        print("\n".join(failures[:50]))
        print(f"FAILED: {len(failures)} problem(s), {checked} existing file(s) checked")
        return 1
    print(f"PASSED: {checked} files match CHECKSUMS.sha256")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
