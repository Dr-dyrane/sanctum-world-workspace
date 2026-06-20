#!/usr/bin/env python3
"""Render OV12 (off-text-image: new-onset atrial fibrillation on a pre-discharge ECG) task
artifacts through the canonical renderer into tasks/task12/current/. Frozen-world-safe:
task-layer artifacts only; no world edits.

Lane: Consultation Note (fresh 8th lane). Deliverable: a pre-transfer NEPHROLOGY consultation note
the attending completes and signs. Mechanism: the OV04 off-text-image engine on a fresh cardiac-
rhythm axis. The consult's headline is renal (acute kidney injury on chronic kidney disease,
dosing, held-agent restart); the chart is silent on rhythm; a pre-discharge 12-lead ECG (mounted
image, pre_discharge_ecg_05232026.png) shows new atrial fibrillation with a rapid ventricular
response and no prior on file. Floor = the model completes the renal consult from chart prose and
never opens the ECG, missing the new afib. Catcher = it reads the ECG, recognizes new-onset afib,
and recommends rate control + anticoagulation evaluation dosed to renal function + cardiology, and
does not clear transfer without addressing it. The grader scores the text against the golden; it
does not read the image.
"""
from __future__ import annotations
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import warnings; warnings.filterwarnings("ignore")
import build_world_files as W

OUT = REPO / "worlds/ondina-vasquell/tasks/task12/current"
OUT.mkdir(parents=True, exist_ok=True)

REASON = ("Nephrology consulted by Hospital Medicine for pre-transfer assessment of acute kidney "
          "injury on chronic kidney disease stage 3b: confirm renal recovery, advise renal dosing "
          "and nephrotoxin avoidance, and advise on timing for restart of the home agents held "
          "since admission (metformin, empagliflozin, lisinopril) before transfer to skilled nursing.")

HIST = ("Sixty-eight-year-old woman admitted 05/16 with a limb-threatening left diabetic foot "
        "infection, now clinically improved on culture-directed renally dosed intravenous cefepime "
        "after bedside debridement and with strict offloading. Background of type 2 diabetes on "
        "insulin, heart failure with preserved ejection fraction (euvolemic on furosemide), "
        "peripheral arterial disease, anemia of chronic kidney disease, and a sulfa allergy. "
        "Spanish-preferred; care coordinated through a certified interpreter.")

RENAL_DATA = ("Creatinine 1.6 mg/dL, near the documented baseline of 1.5; eGFR 36; potassium 4.1. "
              "Acute kidney injury on chronic kidney disease stage 3b, improving. Metformin, "
              "empagliflozin, and lisinopril held since 05/16 for the acute injury. Nephrotoxins "
              "and iodinated contrast avoided this stay; all agents renally dosed.")

# renal recommendations, shared substance (golden completes them; the draft leaves them to finish)
RENAL_RECS = [
    "Acute kidney injury on chronic kidney disease stage 3b, improving: continue to trend "
    "creatinine and potassium, maintain euvolemia, and keep avoiding nephrotoxins and iodinated "
    "contrast.",
    "Hold metformin and empagliflozin until renal function is stable at baseline off the acute "
    "injury; restart is parameter-gated and reassessed by primary care, not automatic at transfer.",
    "Resume lisinopril only once the creatinine is stable at baseline with an acceptable potassium; "
    "recheck a renal panel one to two weeks after any restart.",
    "Continue renal dosing of all medications at the facility and monitor the anemia of chronic "
    "kidney disease.",
]

# the off-text catch (golden only): new afib on the mounted pre-discharge ECG
AFIB_GOLD = (
    "The pre-discharge 12-lead ECG obtained 05/23 shows new atrial fibrillation with a rapid "
    "ventricular response and no prior ECG on file for comparison; the record documents no prior "
    "arrhythmia, so this is new-onset. It is not reflected in the started draft and must be "
    "surfaced before sign. Recommend rate control with an agent dosed to renal function; evaluate "
    "for anticoagulation given an elevated stroke risk from her age, hypertension, diabetes, and "
    "vascular disease, choosing and dosing the agent for chronic kidney disease stage 3b and "
    "weighing bleeding risk; obtain a cardiology consultation with telemetry; and do not clear the "
    "patient as renally optimized for transfer until the new atrial fibrillation is addressed."
)

DRAFT = (
    "nephrology_consult_note_draft_05232026.docx", "progress",
    "NEPHROLOGY CONSULTATION NOTE", "05/23/2026",
    [
        ("title", "NEPHROLOGY CONSULTATION NOTE (PHYSICIAN COMPLETION)"),
        ("filing", "Author: Renata Solis, MD - Nephrology Fellow | Cosign pending: David Aronson, MD "
                   "- Nephrology | Requested by: Hospital Medicine | Date of Service: 05/23/2026 | "
                   "Status: Draft started for attending completion and signature"),
        ("body", "Started on rounds; please complete the remaining sections from the chart for "
                 "Mrs. Vasquell's pre-transfer nephrology review, then this note is ready for "
                 "attending signature."),
        ("section", "REASON FOR CONSULTATION"),
        ("body", REASON),
        ("section", "RELEVANT HISTORY"),
        ("body", HIST),
        ("section", "PERTINENT RENAL DATA"),
        ("body", RENAL_DATA),
        ("section", "ASSESSMENT AND RECOMMENDATIONS"),
        ("body", "Complete the renal assessment and recommendations from the chart: renal recovery, "
                 "medication dosing, and the timing of the held agents."),
        ("sig", "Drafted by Renata Solis, MD (Nephrology Fellow) on 05/23/2026; for completion and "
                "signature by David Aronson, MD"),
    ],
)

NURSE = (
    "pre_discharge_nursing_note_05232026.docx", "progress",
    "NURSING NOTE", "05/23/2026",
    [
        ("title", "PRE-TRANSFER NURSING NOTE"),
        ("filing", "Author: Floor Nursing | Date of Service: 05/23/2026 | Status: Routine"),
        ("body", "Routine pre-transfer care. Patient comfortable, ate breakfast, voiced no acute "
                 "distress. Left forefoot dressing intact, offloading boot on. Spanish interpreter "
                 "used for care and teaching."),
        ("body", "Pre-transfer 12-lead ECG obtained this morning per the covering team's order and "
                 "added to the chart. Transfer paperwork in progress."),
        ("sig", "Floor Nursing, 05/23/2026"),
    ],
)

GOLDEN = (
    "golden-OV12-v1.docx", "progress",
    "NEPHROLOGY CONSULTATION NOTE", "05/23/2026",
    [
        ("title", "NEPHROLOGY CONSULTATION NOTE (PHYSICIAN COMPLETION)"),
        ("filing", "Author: David Aronson, MD - Nephrology | Requested by: Hospital Medicine | "
                   "Date of Service: 05/23/2026 | Status: Completed for physician signature"),
        ("section", "REASON FOR CONSULTATION"),
        ("body", REASON),
        ("section", "RELEVANT HISTORY"),
        ("body", HIST),
        ("section", "PERTINENT RENAL DATA"),
        ("body", RENAL_DATA),
        ("section", "ASSESSMENT AND RECOMMENDATIONS"),
        ("bullets", RENAL_RECS),
        ("section", "NEW FINDING ON PRE-TRANSFER ECG"),
        ("body", AFIB_GOLD),
        ("section", "FLAGS FOR ATTENDING BEFORE SIGN"),
        ("body", "New atrial fibrillation on the 05/23 pre-discharge ECG, not previously documented. "
                 "The completed note recommends renally dosed rate control, anticoagulation "
                 "evaluation appropriate to chronic kidney disease stage 3b, a cardiology "
                 "consultation with telemetry, and holds renal-optimization sign-off for transfer "
                 "until the new atrial fibrillation is addressed."),
        ("sig", "Electronically signed by David Aronson, MD on 05/23/2026"),
    ],
)

for spec in (DRAFT, NURSE, GOLDEN):
    out = W.build_one(spec, outdir=OUT)
    print("  OK", out.name)
print("done OV12 render ->", OUT)
