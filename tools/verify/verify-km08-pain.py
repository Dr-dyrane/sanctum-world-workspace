#!/usr/bin/env python3
"""Pain-axis sweep across ALL 26 world files + fuller gabapentin/sedation context.
Read-only."""
import os, re, zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
FS = str(REPO / "worlds/korvin-merrow/file-review/upload/filesystem")

NS_T = re.compile(r"<w:t[ >].*?</w:t>", re.S)
TAG = re.compile(r"<[^>]+>")

def lines_of(path):
    with zipfile.ZipFile(path) as z:
        raw = z.read("word/document.xml").decode("utf-8", "replace")
    out = []
    for para in raw.split("</w:p>"):
        ts = NS_T.findall(para)
        line = "".join(TAG.sub("", t) for t in ts).strip()
        if line:
            out.append(line)
    return out

PAIN_SCALE = re.compile(r"pain (?:score|scale)|\bnrs\b|0-10|0 to 10|numeric rating|verbal rating|vas\b", re.I)
PAIN_ANY = re.compile(r"\bpain\b", re.I)
GABA = re.compile(r"gabapentin|reassess|clinical question|sedation|fall-risk|fall risk|uptitrat|increase", re.I)

print("### PAIN-SCALE SWEEP (all files) ###")
scale_hits = 0
for f in sorted(os.listdir(FS)):
    if not f.endswith(".docx"):
        continue
    for ln in lines_of(os.path.join(FS, f)):
        if PAIN_SCALE.search(ln):
            scale_hits += 1
            print(f"[{f}] {ln[:160]}")
print(f"-> objective pain-scale lines found: {scale_hits}")

print("\n### ALL 'pain' MENTIONS (context for fairness) ###")
for f in sorted(os.listdir(FS)):
    if not f.endswith(".docx"):
        continue
    for ln in lines_of(os.path.join(FS, f)):
        if PAIN_ANY.search(ln):
            print(f"[{f}] {ln[:170]}")

print("\n### GABAPENTIN / SEDATION / REASSESS CONTEXT ###")
for f in ("medication_administration_record_05232026.docx",
          "initial_medication_reconciliation_note_05182026.docx",
          "hospitalist_discharge_planning_progress_hd5_hd6_05232026.docx"):
    p = os.path.join(FS, f)
    if not os.path.exists(p):
        print(f"!! MISSING {f}"); continue
    for ln in lines_of(p):
        if GABA.search(ln):
            print(f"[{f}] {ln[:180]}")
