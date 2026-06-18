#!/usr/bin/env python3
"""Build goldens through the same canonical Epic renderer.

Golden content is physician-owned. Add approved golden specs to GOLDENS only after
the task is authorized.
"""
from __future__ import annotations

GOLDENS = []

if __name__ == "__main__":
    raise SystemExit("No approved goldens configured. Add physician-approved specs to build_goldens.py.")
