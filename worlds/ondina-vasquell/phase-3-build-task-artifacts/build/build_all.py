#!/usr/bin/env python3
"""One-command DETERMINISTIC rebuild of the entire Ondina world from source.

    python3 worlds/ondina-vasquell/phase-3-build-task-artifacts/build/build_all.py

Rebuilds every docx through the canonical normalized pipeline (epic.py render ->
scrub_all_metadata -> make_deterministic), so a clean checkout plus this command
yields BYTE-IDENTICAL artifacts every time and on any machine (timestamps pinned).
Then regenerates the manifest with live SHAs and runs the verify gate.

Determinism sources removed: zip entry mod-times and core.xml dcterms dates are
pinned to a constant (tools/mode_a_clone.make_deterministic). Pin the toolchain with
requirements.txt (python-docx, Pillow) so the renderer output itself is stable.

NOT rebuilt here: the two writer-produced images (Codex-generated binaries, committed
as-is) and the task prompts/graders text (re-emitted by build_task_packages).
"""
from __future__ import annotations
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = Path(__file__).resolve().parents[4]
PY = sys.executable

STEPS = [
    ("world + supplementary files", HERE / "build_world_files.py"),
    ("task-level files", HERE / "build_task_files.py"),
    ("task-setup goldens", HERE / "build_goldens.py"),
    ("task packages (prompts, graders, run-instructions, prereg, task-file copies)", HERE / "build_task_packages.py"),
    ("World Spec docx", REPO / "tools/build/build-docx-ondina-worldspec.py"),
    ("Brainstorm transcript docx", REPO / "tools/build/build-docx-ondina-brainstorm-claude-transcript.py"),
    ("World Spec transcript docx", REPO / "tools/build/build-docx-ondina-worldspec-claude-transcript.py"),
]


def run(desc, script):
    print(f"== {desc}")
    r = subprocess.run([PY, str(script)], cwd=str(REPO))
    if r.returncode != 0:
        sys.exit(f"FAILED: {desc}")


if __name__ == "__main__":
    for desc, script in STEPS:
        run(desc, script)
    # regenerate the manifest with live SHAs, then gate
    run("verify gate", REPO / "tools/verify/verify_ondina.py")
    print("\nbuild_all complete: deterministic rebuild done and gate green.")
    print("Reproducibility check: run twice and `git status` should show no docx changes.")
