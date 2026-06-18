#!/usr/bin/env python3
"""Build task-level files through the same canonical Epic renderer."""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(HERE))

import build_world_files as W
import task_data as TD

OUTDIR = HERE.parents[0] / "task-files"
OUTDIR.mkdir(parents=True, exist_ok=True)


def _to_world_spec(spec):
    fname, base_key, blocks = spec
    note_type = next((p for k, p in blocks if k == "title"), fname)
    filing = next((p for k, p in blocks if k == "filing"), "")
    m = re.search(r"(\d{2})/(\d{2})/(\d{4})", filing)
    if m:
        dos = f"{m.group(1)}/{m.group(2)}/{m.group(3)}"
    else:
        fm = re.search(r"_(\d{2})(\d{2})(\d{4})", fname)
        dos = f"{fm.group(1)}/{fm.group(2)}/{fm.group(3)}" if fm else "01/01/2025"
    return (fname, base_key, note_type, dos, blocks)


if __name__ == "__main__":
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else len(TD.TASK_FILES)
    for fn in TD.TASK_FILES[lo:hi]:
        print("  task   OK", W.build_one(_to_world_spec(fn()), outdir=OUTDIR).name)
    print(f"done slice [{lo}:{hi}]")
