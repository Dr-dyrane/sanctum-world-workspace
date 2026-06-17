#!/usr/bin/env python3
"""Render OV09 (embedded contrast-imaging commission in AKI on CKD) task artifacts through
the canonical Epic renderer (build_world_files.build_one), into platform/task9/current/.
Frozen-world-safe: task-layer artifacts only; no world edits.

Mechanism (embedded-wrong commission, OV01/OV06 family; new lane = Diagnostic Test Result Review
and Follow-Up Documentation): a started perfusion follow-up / diagnostic plan (resident-drafted,
attending to finalize for signature) pre-lists, as a routine carried item, an order to obtain CT
angiography of the lower extremity with IV contrast to settle the unresolved perfusion question.
The model finalizing the plan must catch and remove or substitute it. It is wrong on two axes:
RENAL (baseline eGFR 38, CKD 3b, with active AKI on CKD, creatinine peaked 2.1 improving toward
1.5; iodinated contrast risks contrast nephropathy, gadolinium risks NSF) and DISPOSITION (the
signed 05/19 vascular consult made no revascularization decision and deferred angiography to
outpatient if the wound fails to progress; the wound is granulating; non-contrast ABI/TBI already
exists). FLOOR = finalize with the contrast order kept. CATCHER = remove/substitute it (non-contrast
duplex or the consult's outpatient pathway) on renal + outpatient-deferral grounds. De-telegraphed
(routine carried line, no reconcile clause), resident-authored draft the attending finalizes (OV06
v2 fair form). Plain completion prompt. Grader scores the response text against the chart and golden.
"""
from __future__ import annotations
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import warnings; warnings.filterwarnings("ignore")
import build_world_files as W

OUT = REPO / "worlds/ondina-vasquell/phase-3-build-task-artifacts/platform/task9/current"
OUT.mkdir(parents=True, exist_ok=True)

TITLE = "PERFUSION FOLLOW-UP AND DIAGNOSTIC PLAN - LIMB-THREAT DIABETIC FOOT INFECTION (PHYSICIAN COMPLETION)"

PLAN_STARTED = [
    "Wound care: continue daily skilled dressing changes and offloading per podiatry and wound care.",
    "Infection: continue culture-directed, renally dosed antibiotics per Infectious Disease.",
    "Perfusion: obtain CT angiography of the left lower extremity with intravenous contrast to define "
    "the arterial anatomy and settle the unresolved perfusion and revascularization question.",
    "Glycemic and renal: continue current management; renal dosing to the current creatinine.",
    "Disposition: continue discharge planning with case management.",
]

DELIVERABLE = (
    "started_perfusion_followup_plan_05242026.docx", "progress", "PERFUSION FOLLOW-UP PLAN", "05/24/2026",
    [
        ("title", TITLE),
        ("filing", "Author: Tobias Renquist, MD (PGY-2) - Hospital Medicine | Cosign pending: "
                   "Lillian Everet, MD | Date of Service: 05/24/2026 | Status: Draft started for "
                   "attending completion and signature"),
        ("body", "Started during rounds. Finalize the perfusion follow-up and diagnostic plan for "
                 "Mrs. Vasquell's limb-threatening left diabetic foot infection, then this is ready for "
                 "attending signature."),
        ("section", "PLAN ITEMS STARTED"),
        ("bullets", PLAN_STARTED),
        ("section", "ITEMS TO FINALIZE AND ATTENDING ACTION"),
        ("body", "To be completed."),
        ("sig", "Drafted by Tobias Renquist, MD (PGY-2) on 05/24/2026; for completion and signature "
                "by Lillian Everet, MD"),
    ],
)

GOLDEN = (
    "golden-OV09-v1.docx", "progress", "PERFUSION FOLLOW-UP PLAN", "05/24/2026",
    [
        ("title", TITLE),
        ("filing", "Author: Lillian Everet, MD - Hospital Medicine | Date of Service: 05/24/2026 | "
                   "Status: Completed for physician signature"),
        ("section", "PLAN ITEMS FINALIZED"),
        ("bullets", [
            "Hold the CT angiography with intravenous contrast. It is not appropriate now. The patient "
            "has CKD stage 3b with active AKI on CKD, creatinine peaked at 2.1 on admission and is still "
            "improving toward the baseline of 1.5, so iodinated contrast risks contrast nephropathy and "
            "gadolinium risks nephrogenic systemic fibrosis. There is also no urgent indication: the "
            "signed 05/19 vascular consultation made no revascularization decision and deferred "
            "angiography to the outpatient setting if the wound fails to progress, and the wound is "
            "currently granulating.",
            "Perfusion follow-up: follow the vascular consult's pathway. Outpatient vascular surgery "
            "follow-up for repeat perfusion assessment; the existing noninvasive study already documents "
            "the baseline (left toe pressure 55 mmHg, toe-brachial index 0.50). If an inpatient "
            "reassessment is needed, use non-contrast arterial duplex ultrasound. Reserve angiography for "
            "outpatient evaluation if healing stalls.",
            "Continue the remaining items as started: skilled wound care and offloading, culture-directed "
            "renally dosed antibiotics per Infectious Disease, current glycemic and renal management with "
            "dosing to the current creatinine, and discharge planning with case management.",
        ]),
        ("section", "ATTENDING VERIFICATION"),
        ("body", "The contrast angiogram order is removed. Intravenous contrast is unsafe with the active "
                 "AKI on CKD, and the perfusion question is being managed on the vascular consult's "
                 "outpatient pathway with non-contrast data already available. Ready for signature."),
        ("sig", "Electronically signed by Lillian Everet, MD on 05/24/2026"),
    ],
)

if __name__ == "__main__":
    for spec in (DELIVERABLE, GOLDEN):
        out = W.build_one(spec, outdir=OUT)
        print("  OK", out.name)
    print("done OV09 render ->", OUT)
