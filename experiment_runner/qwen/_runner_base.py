#!/usr/bin/env python3
"""Small standard-library support module for the Qwen experiment runner."""
from __future__ import annotations

from contextlib import contextmanager
import csv
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
import subprocess
import time


def now():
    return datetime.now(timezone.utc).isoformat()


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def atomic_json(path, value):
    """Write JSON through an atomic replacement, tolerating short Windows locks."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
                   encoding="utf-8")
    for attempt in range(20):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            if attempt == 19:
                raise
            time.sleep(0.05 * (attempt + 1))


def number(value, name, minimum=0, integer=False):
    expected = (int,) if integer else (int, float)
    if type(value) not in expected or not math.isfinite(value) or value < minimum:
        raise ValueError(f"Invalid {name}")
    return value


def module_from(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@contextmanager
def experiment_lock(out):
    """Prevent two runners from writing the same output directory."""
    lock = (Path(out) / ".runner.lock").open("a+b")
    if lock.tell() == 0:
        lock.write(b"0")
        lock.flush()
    lock.seek(0)
    try:
        if os.name == "nt":
            import msvcrt
            msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        lock.close()
        raise ValueError("Another runner is using this output directory")
    try:
        yield
    finally:
        if os.name == "nt":
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
        lock.close()


def kill_tree(proc):
    """Terminate a subprocess tree created by the runner."""
    if os.name == "nt":
        result = subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                creationflags=subprocess.CREATE_NO_WINDOW, timeout=15)
        if result.returncode and proc.poll() is None:
            proc.kill()
    else:
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    proc.wait(timeout=15)


def pid_alive(pid):
    if not pid:
        return False
    if os.name == "nt":
        result = subprocess.run(["tasklist", "/FI", f"PID eq {int(pid)}", "/FO", "CSV", "/NH"],
                                capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW,
                                timeout=10)
        output = result.stdout.decode(errors="replace")
        return any(len(row) > 1 and row[1] == str(pid) for row in csv.reader(output.splitlines()))
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


def sum_complete(items):
    return sum(items) if items and all(item is not None for item in items) else None


def sum_observed(items):
    values = [item for item in items if item is not None]
    return sum(values) if values else None
