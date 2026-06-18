#!/usr/bin/env python3
"""Emit prompt, grader, runbook, and prereg packages after task approval.

This file starts empty by design. Do not generate task packages until prompts,
goldens, graders, workflow names, and prereg forecasts are approved.
"""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKFILES = ROOT / "task-files"
TASKS = {}


def emit():
    if not TASKS:
        raise SystemExit("No approved task packages configured.")
    for task, data in TASKS.items():
        out = ROOT / "tasks" / task / "current"
        out.mkdir(parents=True, exist_ok=True)
        (out / f"prompt-{data['id']}.txt").write_text(data["prompt"].rstrip() + "\n", encoding="utf-8")
        (out / f"grader-guidelines-{data['id']}.txt").write_text(data["grader"].rstrip() + "\n", encoding="utf-8")
        (out / "RUN-INSTRUCTIONS.md").write_text(data["run_instructions"].rstrip() + "\n", encoding="utf-8")
        (out / f"{data['id']}-pilot-preregistration.md").write_text(data["prereg"].rstrip() + "\n", encoding="utf-8")
        for fname in data.get("task_files", []):
            shutil.copyfile(TASKFILES / fname, out / fname)
        print("  package", data["id"])


if __name__ == "__main__":
    emit()
