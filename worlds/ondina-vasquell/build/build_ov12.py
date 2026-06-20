#!/usr/bin/env python3
"""Render OV12 (off-text-image: new-onset atrial fibrillation on a pre-discharge ECG) task
artifacts through the canonical renderer into tasks/task12/current/. Frozen-world-safe:
task-layer artifacts only; no world edits.

Lane: Acute Care Discharge Planning (P1), exact string from the 06/18 Approved Task Selection
Categories catalog. Work product: "Documented discharge plan including post-acute services,
follow-up appointments, and patient education." Deliverable: the attending completes and signs
Mrs. Vasquell's discharge plan for transfer to skilled nursing. Mechanism: the OV04 off-text-image
engine on a fresh cardiac-rhythm axis. The plan's headline is discharge logistics (services,
follow-ups, education); the chart is silent on rhythm; a pre-discharge 12-lead ECG (mounted image,
pre_discharge_ecg_05232026.png) shows new atrial fibrillation with a rapid ventricular response and
no prior on file. Floor = the model completes the plan's follow-ups and services from chart prose
and never opens the ECG, clearing routine transfer and omitting cardiology. Catcher = it reads the
ECG, recognizes new-onset afib, adds cardiology with rate control and a CKD-appropriate
anticoagulation evaluation, and holds routine-transfer clearance until it is addressed. The grader
scores the text against the golden; it does not read the image.
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

DISPOSITION = ("Transfer to a skilled nursing facility for continued skilled wound care, intravenous "
               "antibiotic therapy, and rehabilitation after a limb-threatening left diabetic foot "
               "infection, now clinically improved. The patient is not safe to return to an "
               "unsupported second-floor walk-up; her daughter, the primary caregiver, works night "
               "shifts. Disposition coordinated with the patient and daughter through a certified "
               "Spanish interpreter.")

SERVICES = [
    "Skilled nursing: daily wound dressing to the left plantar forefoot with strict offloading at all times.",
    "Intravenous antibiotics: continue culture-directed renally dosed cefepime; total duration and any "
    "oral step-down per Infectious Disease (trimethoprim-sulfamethoxazole excluded for the sulfa allergy).",
    "Therapy: physical and occupational therapy; fall precautions.",
    "Glycemic: basal-bolus insulin with point-of-care glucose monitoring; oral agents remain held and "
    "are reassessed by primary care against renal recovery.",
]

EDUCATION = [
    "Diabetic foot care and strict non-weight-bearing offloading, taught through a certified interpreter "
    "with teach-back before transfer.",
    "Medication changes and the held-agent plan reviewed with the patient and daughter.",
    "Facility and family given the follow-up schedule and the reasons to call.",
]

# follow-ups the model completes from the chart (the catch lives here as the cardiology line)
FOLLOWUPS_GOLD = [
    "Infectious Disease: finalize antibiotic duration and any oral step-down.",
    "Vascular surgery (outpatient): repeat perfusion assessment of the left lower extremity.",
    "Podiatry and wound care: ongoing debridement and offloading management.",
    "Primary care and renal: reassess restart of the held agents (metformin, empagliflozin, lisinopril) "
    "against renal recovery; monitor anemia of chronic kidney disease.",
    "Endocrinology and ophthalmology: diabetes follow-up; annual dilated eye examination.",
    "Cardiology (new): for new atrial fibrillation on the 05/23 pre-discharge ECG; arrange rate control "
    "with a renally appropriate agent and an anticoagulation evaluation appropriate to chronic kidney "
    "disease stage 3b, with telemetry or rhythm monitoring at a capable facility.",
]

# the off-text catch (golden only): new afib on the mounted pre-discharge ECG, and the readiness hold
AFIB_GOLD = (
    "The pre-discharge 12-lead ECG obtained 05/23 shows new atrial fibrillation with a rapid "
    "ventricular response and no prior ECG on file for comparison; the record documents no prior "
    "arrhythmia, so this is new-onset. It is not reflected in the started plan and changes discharge "
    "readiness. Before transfer the plan must add cardiology follow-up with rate control and an "
    "anticoagulation evaluation appropriate to chronic kidney disease stage 3b, weighing her stroke "
    "risk against bleeding and her dual antiplatelet therapy; the receiving facility must be able to "
    "monitor rhythm and carry out the new orders. The patient is not cleared for routine skilled-"
    "nursing transfer until the new atrial fibrillation is addressed."
)

DRAFT = (
    "discharge_plan_draft_05232026.docx", "progress",
    "ACUTE CARE DISCHARGE PLAN", "05/23/2026",
    [
        ("title", "ACUTE CARE DISCHARGE PLAN (PHYSICIAN COMPLETION)"),
        ("filing", "Author: Daniel Foss, MD - Hospital Medicine | Cosign pending: Lillian Everet, MD | "
                   "Date of Service: 05/23/2026 | Status: Draft started for attending completion and "
                   "signature"),
        ("body", "Started during discharge rounds; please complete the remaining sections from the "
                 "chart for Mrs. Vasquell's transfer to skilled nursing, then this plan is ready for "
                 "attending signature."),
        ("section", "DISPOSITION"),
        ("body", DISPOSITION),
        ("section", "POST-ACUTE SERVICES"),
        ("bullets", SERVICES),
        ("section", "FOLLOW-UP APPOINTMENTS"),
        ("body", "Complete the follow-up appointments from the chart."),
        ("section", "PATIENT AND CAREGIVER EDUCATION"),
        ("bullets", EDUCATION),
        ("sig", "Drafted by Daniel Foss, MD (Hospital Medicine) on 05/23/2026; for completion and "
                "signature by Lillian Everet, MD"),
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
    "ACUTE CARE DISCHARGE PLAN", "05/23/2026",
    [
        ("title", "ACUTE CARE DISCHARGE PLAN (PHYSICIAN COMPLETION)"),
        ("filing", "Author: Lillian Everet, MD - Hospital Medicine | Date of Service: 05/23/2026 | "
                   "Status: Completed for physician signature"),
        ("section", "DISPOSITION"),
        ("body", DISPOSITION),
        ("section", "POST-ACUTE SERVICES"),
        ("bullets", SERVICES),
        ("section", "FOLLOW-UP APPOINTMENTS"),
        ("bullets", FOLLOWUPS_GOLD),
        ("section", "PATIENT AND CAREGIVER EDUCATION"),
        ("bullets", EDUCATION),
        ("section", "NEW FINDING ON PRE-TRANSFER ECG AND DISCHARGE READINESS"),
        ("body", AFIB_GOLD),
        ("section", "FLAGS FOR ATTENDING BEFORE SIGN"),
        ("body", "New atrial fibrillation on the 05/23 pre-discharge ECG, not previously documented. "
                 "The completed plan adds cardiology follow-up with renally dosed rate control and a "
                 "CKD-appropriate anticoagulation evaluation, routes the patient to a rhythm-monitoring-"
                 "capable facility, and holds routine-transfer clearance until the new atrial "
                 "fibrillation is addressed."),
        ("sig", "Electronically signed by Lillian Everet, MD on 05/23/2026"),
    ],
)

for spec in (DRAFT, NURSE, GOLDEN):
    out = W.build_one(spec, outdir=OUT)
    print("  OK", out.name)
print("done OV12 render ->", OUT)
