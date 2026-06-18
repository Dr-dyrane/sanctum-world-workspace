#!/usr/bin/env python3
"""One-command deterministic rebuild for this world factory."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
PY = sys.executable

STEPS = [
    ("world + supplementary files", HERE / "build_world_files.py"),
    ("task-level files", HERE / "build_task_files.py"),
    ("task goldens", HERE / "build_goldens.py"),
    ("task packages", HERE / "build_task_packages.py"),
]


def run(desc, script):
    print(f"== {desc}")
    r = subprocess.run([PY, str(script)], cwd=str(REPO))
    if r.returncode != 0:
        raise SystemExit(f"FAILED: {desc}")


def run_with_args(desc, script, *args):
    print(f"== {desc}")
    r = subprocess.run([PY, str(script), *args], cwd=str(REPO))
    if r.returncode != 0:
        raise SystemExit(f"FAILED: {desc}")


if __name__ == "__main__":
    for desc, script in STEPS:
        run(desc, script)
    run_with_args("generic world factory verification", REPO / "tools/verify/verify_world_factory.py", "worlds/marva-lydell")
    print("build_all complete for worlds/marva-lydell")
