#!/usr/bin/env python3
"""Build task-level files (E1-T*) into task-files/ - SEPARATE from world files.

Reference artifacts only (external pressure surfaces + same-author drafts). No Epic
patient banner (they are not chart storyboard notes). Same Mode A clone + scrub +
verify_no_synthetic + banned-char gate. NOT prompts/goldens/graders.
"""
from __future__ import annotations
import sys, zipfile, warnings
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
warnings.filterwarnings("ignore")

from docx import Document
from tools.mode_a_clone import scrub_all_metadata, verify_no_synthetic, verify_no_km_identifiers
import epic
import task_data as TD
from build_world_files import BASE, RENDER, _check_clean

OUTDIR = REPO / "worlds/ondina-vasquell/phase-3-build-task-artifacts/task-files"
OUTDIR.mkdir(parents=True, exist_ok=True)


def build_one(spec):
    fname, base_key, blocks = spec
    doc = Document(str(BASE[base_key]))
    epic.clear_body(doc)
    # external/draft surfaces: clear KM header/footer, plain Confidential footer
    epic.clear_and_set_hf(doc, None, None, None, None)
    for kind, payload in blocks:
        RENDER[kind](doc, payload)
    out = OUTDIR / fname
    doc.save(str(out))
    scrub_all_metadata(str(out))
    verify_no_synthetic(str(out))
    verify_no_km_identifiers(str(out))
    _check_clean(out)
    return out


if __name__ == "__main__":
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else len(TD.TASK_FILES)
    for fn in TD.TASK_FILES[lo:hi]:
        out = build_one(fn())
        print("  task   OK", out.name)
    print(f"done slice [{lo}:{hi}]")
