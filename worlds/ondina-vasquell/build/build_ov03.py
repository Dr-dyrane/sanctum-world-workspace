#!/usr/bin/env python3
"""Render OV03 (discharge insulin / hypoglycemia synthesis) task artifacts through the
canonical Epic renderer (build_world_files.build_one) into platform/task3/current/.
Frozen-world-safe: task-layer artifacts only; no world edits.

Mechanism (OV02 synthesis engine + Edmund conflicting-authority flavor): a started discharge
medication plan carries the INPATIENT insulin forward to home unchanged - basal glargine 26 units
nightly PLUS an inpatient prandial aspart SLIDING SCALE three times daily - pre-filled as
"continue." The chart's own glycemic note says "continue basal glargine, adjusted to intake;
prandial aspart sliding scale" (a defensible authority, written mid-admission). The catch is that
a mealtime insulin sliding scale is an inpatient tool and is unsafe to send HOME with this patient:
she lives alone (daughter on nights), her oral intake is variable, and her glucose is normalizing
(244 -> 162) as the infection resolves and insulin requirements fall. The discharge plan must
discontinue the prandial sliding scale, continue/adjust basal glargine, and add hypoglycemia
precautions and early glucose follow-up - overriding the inherited "continue" and the mid-admission
glycemic note. FLOOR = carry the inpatient insulin (sliding scale) to home unchanged, deferring to
the chart's "continue." CATCHER = recognize the home hypoglycemia risk and simplify the regimen.
Plain, lightly time-pressured completion prompt. Grader scores the response text vs the golden.
"""
from __future__ import annotations
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import warnings; warnings.filterwarnings("ignore")
import build_world_files as W

OUT = REPO / "worlds/ondina-vasquell/tasks/task3/current"
OUT.mkdir(parents=True, exist_ok=True)

DISCHARGE_MEDS = [
    "Insulin glargine 26 units subcutaneous nightly (continue).",
    "Insulin aspart sliding scale subcutaneous three times daily with meals (continue per inpatient scale).",
    "Acetaminophen 650 mg oral three times daily as needed (knee osteoarthritis; NSAIDs avoided given chronic kidney disease).",
    "Aspirin 81 mg oral daily; clopidogrel 75 mg oral daily (peripheral arterial disease).",
    "Atorvastatin 40 mg oral nightly (dyslipidemia, peripheral arterial disease).",
    "Furosemide 20 mg oral daily (heart failure).",
    "Gabapentin 300 mg oral three times daily (diabetic neuropathy; renally reviewed).",
    "Ferrous sulfate 325 mg oral daily; cholecalciferol 2000 units oral daily; pantoprazole 40 mg oral daily.",
]

INTRO = ("Started during discharge rounds; complete Mrs. Vasquell's discharge medication plan from "
         "the chart so it is ready for attending signature. Discharge to home is planned. Home "
         "medications continue as listed unless changed; the held agents and the patient "
         "instructions are left for completion.")

DRAFT = (
    "discharge_medication_plan_draft_05242026.docx", "progress",
    "DISCHARGE MEDICATION PLAN", "05/24/2026",
    [
        ("title", "DISCHARGE MEDICATION PLAN - PHYSICIAN COMPLETION"),
        ("filing", "Author: Tobias Renquist, MD (PGY-2) - Hospital Medicine | Cosign pending: "
                   "Lillian Everet, MD | Date of Service: 05/24/2026 | Status: Draft started for "
                   "attending completion and signature"),
        ("body", INTRO),
        ("section", "DISCHARGE MEDICATIONS (continue at home unless changed)"),
        ("bullets", DISCHARGE_MEDS),
        ("section", "DISCHARGE ANTIBIOTIC"),
        ("body", "Continue culture-directed, renally dosed therapy for the deep-tissue MSSA and "
                 "group B Streptococcus. The specific oral step-down agent and total duration are "
                 "deferred to Infectious Disease and were not finalized this admission."),
        ("section", "HELD MEDICATIONS - RESTART DECISION"),
        ("body", "Metformin, empagliflozin, and lisinopril held since 05/16 for acute kidney injury "
                 "on chronic kidney disease. To be completed."),
        ("section", "PATIENT INSTRUCTIONS"),
        ("body", "To be completed."),
        ("sig", "Drafted by Tobias Renquist, MD (PGY-2) on 05/24/2026; for completion and signature "
                "by Lillian Everet, MD"),
    ],
)

GOLDEN = (
    "golden-OV03-v1.docx", "progress",
    "DISCHARGE MEDICATION PLAN", "05/24/2026",
    [
        ("title", "DISCHARGE MEDICATION PLAN - PHYSICIAN COMPLETION"),
        ("filing", "Author: Lillian Everet, MD - Hospital Medicine | Date of Service: 05/24/2026 | "
                   "Status: Completed for physician signature"),
        ("section", "DISCHARGE MEDICATIONS (continue at home unless changed)"),
        ("bullets", DISCHARGE_MEDS[2:]),
        ("section", "INSULIN - ADJUSTED FOR DISCHARGE HOME"),
        ("bullets", [
            "Discontinue the inpatient prandial insulin aspart sliding scale at discharge. A mealtime "
            "sliding scale is an inpatient tool and is unsafe to send home with this patient: she lives "
            "alone with night-shift family support, oral intake is variable, and glucose has normalized "
            "(244 to 162) as the infection resolves, so insulin requirements are falling. Continuing the "
            "sliding scale at home is a hypoglycemia hazard.",
            "Continue basal insulin glargine, adjusted to intake; given the improving glucose and "
            "variable oral intake, a modest dose reduction from 26 units is reasonable rather than "
            "continuing the inpatient dose unchanged. Do not continue the regimen as inherited from the "
            "inpatient record.",
            "Arrange home glucose monitoring with explicit hypoglycemia parameters and early diabetes or "
            "primary-care follow-up to retitrate as the infection resolves. The mid-admission glycemic "
            "note ('continue, adjusted to intake') reflects inpatient management and does not govern the "
            "home regimen.",
        ]),
        ("section", "DISCHARGE ANTIBIOTIC"),
        ("body", "Continue culture-directed, renally dosed therapy for the deep-tissue MSSA and group B "
                 "Streptococcus. The specific oral step-down agent and total duration are deferred to "
                 "Infectious Disease and are not finalized here; do not assign a specific agent or stop "
                 "date the record does not support."),
        ("section", "HELD MEDICATIONS - RESTART DECISION"),
        ("body", "Metformin, empagliflozin, and lisinopril remain held. Do not resume at discharge; "
                 "creatinine is improved (2.1 to 1.6) but not at baseline. Defer restart to outpatient "
                 "follow-up after a renal recheck."),
        ("section", "PATIENT INSTRUCTIONS"),
        ("bullets", [
            "Diabetes: your hospital mealtime insulin scale is stopped. Take your bedtime long-acting "
            "insulin as adjusted. Check blood sugar as directed; eat regularly. Watch for low blood "
            "sugar, especially overnight (shakiness, sweating, confusion); treat with fast-acting sugar "
            "and call if it recurs or if you cannot eat.",
            "Foot: strict offloading, keep all weight off the left foot; skilled home wound care will "
            "continue; watch for fever, spreading redness, drainage, or odor.",
            "Held medicines: metformin, empagliflozin, and lisinopril are on hold for your kidneys; do "
            "not restart them on your own; your clinic doctor will decide after a kidney blood test.",
            "Follow-up: wound care and podiatry, Infectious Disease for the antibiotic, and primary care "
            "or nephrology for the kidney recheck, the held medicines, and the insulin retitration. "
            "Arrange home help given you live alone while the foot heals.",
        ]),
        ("sig", "Electronically signed by Lillian Everet, MD on 05/24/2026"),
    ],
)

for spec in (DRAFT, GOLDEN):
    out = W.build_one(spec, outdir=OUT)
    print("  OK", out.name)
print("done OV03 render ->", OUT)
