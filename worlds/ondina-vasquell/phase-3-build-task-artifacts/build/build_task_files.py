#!/usr/bin/env python3
"""Build task-level files (E1-T*) into task-files/ through the ONE canonical Epic renderer.

CANONICAL RULE: every project docx uses the same KM Epic template. KM rendered its
task-level files in the house Epic chrome (masthead, blue bar, patient storyboard,
patient running header) with the issuer named in the title and filing line, exactly
like its world files. So task files delegate to build_world_files.build_one too, with
the issuer identity carried in the title and filing. NOT prompts/goldens/graders.
"""
from __future__ import annotations
import sys, re
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import warnings; warnings.filterwarnings("ignore")

import build_world_files as W
import task_data as TD

OUTDIR = REPO / "worlds/ondina-vasquell/phase-3-build-task-artifacts/task-files"
OUTDIR.mkdir(parents=True, exist_ok=True)


def _to_world_spec(spec):
    """Convert a task spec (fname, base_key, blocks) to the 5-tuple build_one wants,
    deriving the document title and date from the blocks/filename."""
    fname, base_key, blocks = spec
    note_type = next((p for k, p in blocks if k == "title"), fname)
    filing = next((p for k, p in blocks if k == "filing"), "")
    m = re.search(r"(\d{2})/(\d{2})/(\d{4})", filing)
    if m:
        dos = f"{m.group(1)}/{m.group(2)}/{m.group(3)}"
    else:
        fm = re.search(r"_(\d{2})(\d{2})(\d{4})", fname)
        dos = f"{fm.group(1)}/{fm.group(2)}/{fm.group(3)}" if fm else "05/22/2026"
    return (fname, base_key, note_type, dos, blocks)


if __name__ == "__main__":
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else len(TD.TASK_FILES)
    for fn in TD.TASK_FILES[lo:hi]:
        out = W.build_one(_to_world_spec(fn()), outdir=OUTDIR)
        print("  task   OK", out.name)
    print(f"done slice [{lo}:{hi}] (canonical Epic template)")
