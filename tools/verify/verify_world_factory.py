#!/usr/bin/env python3
"""Generic verification gate for a world-local build factory.

This is the reusable version of the Ondina gate's mechanical checks. It does not
replace clinical review. It catches the repeatable build failures: synthetic tokens,
prior-world identifiers, banned characters, placeholder leakage, and task artifacts
inside the shared world-file bucket.
"""
from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))

from tools.mode_a_clone import verify_no_synthetic, verify_no_km_identifiers

BANNED = "".join(chr(c) for c in (0x2014, 0x2013, 0x2192, 0x2022, 0x00B0, 0x00D7, 0x2079, 0x00B9, 0x2070))
TEXT_SUFFIXES = {".md", ".txt"}
DOCX_DIRS = {"world-files", "supplementary-files", "task-files", "tasks", "submission"}
WORLD_FILE_FORBIDDEN = ("prompt-", "grader-guidelines", "golden-", "RUN-INSTRUCTIONS", "prereg")


def guard_world(path: Path) -> Path:
    path = path.resolve()
    worlds = (REPO / "worlds").resolve()
    if worlds not in path.parents:
        raise SystemExit(f"Path is not under worlds/: {path}")
    if not path.exists():
        raise SystemExit(f"World path not found: {path}")
    return path


def docx_text_parts(path: Path) -> list[tuple[str, str]]:
    parts: list[tuple[str, str]] = []
    with zipfile.ZipFile(str(path)) as z:
        for name in z.namelist():
            if name.startswith("word/") and name.endswith(".xml"):
                parts.append((name, z.read(name).decode("utf-8", errors="ignore")))
    return parts


def check_docx(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        verify_no_synthetic(str(path))
        verify_no_km_identifiers(str(path))
    except Exception as exc:
        errors.append(f"{path}: metadata or prior-world check failed: {exc}")
    try:
        for name, text in docx_text_parts(path):
            bad = sorted({c for c in BANNED if c in text})
            if bad:
                errors.append(f"{path}:{name}: banned characters {bad}")
            if "<<PHYSICIAN:" in text or "<<PHYSICIAN" in text:
                errors.append(f"{path}:{name}: physician placeholder leaked")
    except Exception as exc:
        errors.append(f"{path}: cannot read docx: {exc}")
    return errors


def check_text(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    errors: list[str] = []
    bad = sorted({c for c in BANNED if c in text})
    if bad:
        errors.append(f"{path}: banned characters {bad}")
    return errors


def iter_files(world: Path):
    for d in DOCX_DIRS:
        root = world / d
        if root.exists():
            yield from root.rglob("*")
    for root in (world / "docs", world / "build"):
        if root.exists():
            yield from root.rglob("*")
    if (world / "00-START-HERE.md").exists():
        yield world / "00-START-HERE.md"


def verify(world: Path) -> int:
    errors: list[str] = []
    docx_count = 0
    text_count = 0
    world_files = world / "world-files"
    if world_files.exists():
        for p in world_files.iterdir():
            if any(tok in p.name for tok in WORLD_FILE_FORBIDDEN):
                errors.append(f"{p}: task artifact appears in shared world-files")

    for path in iter_files(world):
        if not path.is_file():
            continue
        if path.suffix == ".docx":
            docx_count += 1
            errors.extend(check_docx(path))
        elif path.suffix in TEXT_SUFFIXES:
            text_count += 1
            errors.extend(check_text(path))

    if errors:
        print("verify_world_factory: FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print(f"verify_world_factory: PASS for {world.relative_to(REPO)} ({docx_count} docx, {text_count} text files)")
    return 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("world", help="World folder under worlds/")
    args = ap.parse_args()
    raise SystemExit(verify(guard_world((REPO / args.world) if not args.world.startswith("/") else Path(args.world))))


if __name__ == "__main__":
    main()
