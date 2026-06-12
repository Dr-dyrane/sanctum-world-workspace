#!/usr/bin/env python3
"""KM08 substrate verification. Extracts docx text INCLUDING table cells and
greps the gabapentin-uptitration substrate from the agent-read filesystem layer.
Read-only. No build, no mutation."""
import os, re, zipfile, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
FS = str(REPO / "worlds/korvin-merrow/file-review/upload/filesystem")

NS_T = re.compile(r"<w:t[ >].*?</w:t>", re.S)
TAG = re.compile(r"<[^>]+>")
PARA = re.compile(r"</w:p>")

def docx_text(path):
    """All text incl. tables. document.xml stores table-cell text as w:t too."""
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8", "replace")
    # mark paragraph boundaries so grep context is line-ish
    xml = PARA.sub("\n", xml)
    chunks = NS_T.findall(xml)
    text = "".join(TAG.sub("", c) for c in chunks)
    # rebuild line breaks from the paragraph markers we inserted
    # (findall above dropped them; re-split on original is simpler:)
    with zipfile.ZipFile(path) as z:
        raw = z.read("word/document.xml").decode("utf-8", "replace")
    lines = []
    for para in raw.split("</w:p>"):
        ts = NS_T.findall(para)
        line = "".join(TAG.sub("", t) for t in ts).strip()
        if line:
            lines.append(line)
    return "\n".join(lines)

KEYWORDS = {
    "gabapentin": r"gabapentin",
    "morse": r"morse",
    "osa/apnea": r"apnea|osa|cpap",
    "ckd/renal": r"ckd|renal|creatinine|egfr|nephro",
    "confusion/AMS": r"confus|delir|altered ment|disorient|orient",
    "fall": r"fall",
    "sedation": r"sedat|drows|somnolen",
    "pain scale": r"pain (?:score|scale)|nrs|0-10|numeric rating",
    "neuropath": r"neuropath",
}

FILES = [
    "medication_administration_record_05232026.docx",
    "initial_medication_reconciliation_note_05182026.docx",
    "physical_therapy_assessment_05202026.docx",
    "occupational_therapy_assessment_05202026.docx",
    "sleep_study_osa_history_summary_05182026.docx",
    "nephrology_consultation_05212026.docx",
    "nursing_observation_flowsheet_summary_05232026.docx",
    "problem_list_history_snapshot_05182026.docx",
    "hospitalist_progress_hd3_05202026.docx",
    "hospitalist_progress_hd4_05212026.docx",
]

def main():
    targets = FILES if len(sys.argv) < 2 else sys.argv[1:]
    for fname in targets:
        path = os.path.join(FS, fname)
        if not os.path.exists(path):
            print(f"!! MISSING: {fname}"); continue
        text = docx_text(path)
        low = text.lower()
        hits = {k: len(re.findall(pat, low)) for k, pat in KEYWORDS.items()}
        present = {k: v for k, v in hits.items() if v}
        print("=" * 70)
        print(f"FILE: {fname}  ({len(text)} chars)")
        print("  hits:", present if present else "(none of the keywords)")
        # print the actual gabapentin lines for inspection
        for kw in ("gabapentin", "morse"):
            for ln in text.splitlines():
                if kw in ln.lower():
                    print(f"  [{kw}] {ln.strip()[:160]}")

if __name__ == "__main__":
    main()
