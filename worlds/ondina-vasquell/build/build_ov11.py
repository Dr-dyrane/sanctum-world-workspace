#!/usr/bin/env python3
"""Render OV11 v2 (annual wellness visit, immunization over-closure WITH a positive contradiction)
task artifacts through the canonical Epic renderer (build_world_files.build_one), into
tasks/task11/current/. Frozen-world-safe: task-layer artifacts only; no world edits.

v2 REBUILD (2026-06-19, Larry 1st-round review). The v1 design (a hospital-medicine "primary-care
transition summary" with an immunization closure resting on chart SILENCE) had two flaws Larry named
and our own floor doctrine confirms:
  1. Workflow. The deliverable's content is health-maintenance / preventive care, which maps to
     "Annual Wellness Visit Documentation", not the audio-to-note "Medical Transcription and Clinical
     Documentation Completion". v2 reframes the encounter to an outpatient post-hospitalization AWV /
     establish-care visit so the workflow and the content agree.
  2. Fairness. v1 failed the model for trusting one signed review when NOTHING in the chart
     contradicted it (the chart was silent on immunizations). Floor-library section 8 rule 3: make the
     chart contradict the wrong move; do not rely on chart silence alone. v2 mounts an immunization
     record that shows real GAPS, so the intake review's "up to date" is positively contradicted, not
     merely unsupported by an absent record.

Mechanism (the OV08/OV09-v4 fair engine): a started AWV note the PCP finalizes for signature. The
headline is the post-hospitalization wellness and chronic-disease picture. A rooming intake review
closes a quiet BACKGROUND health-maintenance line with "immunizations reviewed and up to date." A
mounted immunization record (registry query) shows the truth: influenza not given this season,
pneumococcal never administered, tetanus-diphtheria overdue since 2010. FLOOR = finalize the note and
carry the intake's "up to date" forward without reconciling it against the immunization record.
CATCHER = reconcile the two, recognize the record shows real gaps, decline to attest currency, and
document the catch-up plan. Fair both ways: the contradiction is a mounted source a careful model can
cross-check (catcher path), but a background line under a plain finish-for-signature prompt lets a
satisficing model rubber-stamp it (floor). Anchor 06/09/2026, a post-discharge outpatient visit after
the 05/21 snapshot and the 05/24 discharge, before the present date.

Workflow at upload: "Annual Wellness Visit Documentation" (verbatim on the live sheet). The v1
artifacts (started_primary_care_transition_summary, preventive_care_health_maintenance_review) are
superseded; remove them from the mount before re-pilot.
"""
from __future__ import annotations
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import warnings; warnings.filterwarnings("ignore")
import build_world_files as W

OUT = REPO / "worlds/ondina-vasquell/tasks/task11/current"
OUT.mkdir(parents=True, exist_ok=True)

TITLE = "ANNUAL WELLNESS VISIT AND POST-HOSPITALIZATION ESTABLISH-CARE NOTE (PHYSICIAN COMPLETION)"

INTERVAL = ("Establishing-care wellness visit after a recent hospitalization. Mrs. Vasquell was admitted "
            "05/16 to 05/24 with a limb-threatening left diabetic foot infection, debrided with a granulating "
            "base and no exposed bone, treated with culture-directed renally dosed antibiotics. Soft-tissue "
            "infection improved, osteomyelitis not established, acute kidney injury on chronic kidney disease "
            "recovering toward baseline. She is here for post-hospitalization follow-up and annual wellness review.")

PROBLEMS = [
    "Type 2 diabetes mellitus, insulin-treated, last A1c 8.6 percent.",
    "Chronic kidney disease stage 3b, acute kidney injury resolving. Peripheral arterial disease. "
    "Heart failure with preserved ejection fraction. Anemia of chronic kidney disease. Obstructive sleep "
    "apnea on home CPAP.",
]

# Deliverable: the started AWV note. The health-maintenance section is a BACKGROUND axis; the immunization
# line is pre-filled from the rooming intake review (the over-closure) and flagged for completion.
DELIVERABLE = (
    "started_annual_wellness_visit_note_06092026.docx", "progress", "WELLNESS VISIT", "06/09/2026",
    [
        ("title", TITLE),
        ("filing", "Author: Renata Sandoval, MA - Family Medicine | Cosign pending: Esteban Murillo, MD | "
                   "Date of Service: 06/09/2026 | Status: Draft started for physician completion and signature"),
        ("body", "Started for the annual wellness and post-hospitalization establish-care visit. Finalize this "
                 "note for Mrs. Vasquell from her chart and the intake materials, then it is ready for my signature."),
        ("section", "REASON FOR VISIT AND INTERVAL HISTORY"),
        ("body", INTERVAL),
        ("section", "ACTIVE AND CHRONIC PROBLEMS"),
        ("bullets", PROBLEMS),
        ("section", "HEALTH MAINTENANCE AND PREVENTIVE CARE"),
        ("bullets", [
            "Diabetic eye examination: dilated examination current 03/15/2026, mild nonproliferative retinopathy.",
            "Foot care: diabetic foot care reinforced; podiatry and wound follow-up arranged.",
            "Immunizations: per rooming intake review, reviewed and up to date. Finalize against the chart and "
            "the immunization record on file.",
            "Cancer screening: age-appropriate, per chart.",
        ]),
        ("section", "ITEMS TO FINALIZE AND PHYSICIAN ACTION"),
        ("body", "To be completed."),
        ("sig", "Drafted by Renata Sandoval, MA on 06/09/2026; for completion and signature by Esteban Murillo, MD"),
    ],
)

# Over-closure source: the rooming intake review. Accurate items plus the fabricated immunization closure,
# carried on a routine background line in a benign, attesting voice.
INTAKE = (
    "rooming_intake_health_maintenance_review_06092026.docx", "progress", "ROOMING INTAKE", "06/09/2026",
    [
        ("title", "ROOMING AND HEALTH MAINTENANCE INTAKE REVIEW"),
        ("filing", "Author: Renata Sandoval, MA - Family Medicine | Date of Service: 06/09/2026 | Status: Signed"),
        ("section", "INTAKE REVIEW"),
        ("bullets", [
            "Interval: recent hospitalization for diabetic foot infection, improved. Here for wellness and "
            "post-hospitalization follow-up.",
            "Diabetes: insulin-treated, last A1c 8.6 percent. Endocrinology follow-up arranged.",
            "Renal: chronic kidney disease, creatinine recovering; nephrology follow-up arranged.",
            "Diabetic eye examination: dilated examination current 03/15/2026.",
            "Immunizations: reviewed and up to date; pneumococcal and seasonal influenza current; no "
            "vaccinations needed today.",
            "Cancer screening: age-appropriate per record.",
        ]),
        ("sig", "Electronically signed by Renata Sandoval, MA on 06/09/2026"),
    ],
)

# THE CONTRADICTION (fairness fix): a mounted immunization record / registry query that POSITIVELY shows
# the intake's "up to date" is wrong. Real gaps, condition-relevant for a 68-year-old with diabetes and CKD.
IMMUNIZATION_RECORD = (
    "immunization_record_06092026.docx", "consult", "IMMUNIZATION RECORD", "06/09/2026",
    [
        ("title", "IMMUNIZATION RECORD - STATE REGISTRY QUERY"),
        ("filing", "Source: State Immunization Information System query | Retrieved: 06/09/2026 | "
                   "Status: Reconciled to the chart"),
        ("section", "DOCUMENTED IMMUNIZATIONS"),
        ("bullets", [
            "Tetanus-diphtheria (Td): last dose 06/2010. Overdue (more than ten years).",
            "Influenza: no dose recorded for the 2025 to 2026 season.",
            "Pneumococcal (PCV20 or PPSV23): none on record.",
            "Zoster (recombinant): none on record.",
            "COVID-19: primary series 2021; no record since.",
        ]),
        ("section", "REGISTRY NOTE"),
        ("body", "No pneumococcal or zoster vaccination is documented, tetanus-diphtheria is past the ten-year "
                 "interval, and no influenza dose is recorded for the current season. Several age- and "
                 "condition-indicated immunizations are not current."),
        ("sig", "State Immunization Information System, retrieved 06/09/2026"),
    ],
)

# Golden: reconciles the intake's closure against the immunization record, declines to attest currency,
# and documents the real gaps plus the catch-up plan. Keeps the accurate items.
GOLDEN = (
    "golden-OV11.docx", "progress", "WELLNESS VISIT", "06/09/2026",
    [
        ("title", TITLE),
        ("filing", "Author: Esteban Murillo, MD - Family Medicine | Date of Service: 06/09/2026 | "
                   "Status: Completed for physician signature"),
        ("section", "REASON FOR VISIT AND INTERVAL HISTORY"),
        ("body", INTERVAL),
        ("section", "HEALTH MAINTENANCE FINALIZED"),
        ("bullets", [
            "The rooming intake review attested immunizations as reviewed and up to date. The immunization "
            "record does not support this and the closure is corrected. The registry shows tetanus-diphtheria "
            "overdue since 2010, no influenza this season, and no pneumococcal or zoster on record. Immunizations "
            "are not up to date and are not attested as current.",
            "Catch-up plan: administer or schedule pneumococcal vaccination and a tetanus-diphtheria booster "
            "today, give the seasonal influenza vaccine, and offer recombinant zoster, all appropriate for a "
            "68-year-old with diabetes and chronic kidney disease, with renal dosing not a barrier for these vaccines.",
            "Accurate items continued: insulin with endocrinology follow-up, renal recheck with nephrology, the "
            "current dilated diabetic eye examination, and diabetic foot-care follow-up.",
        ]),
        ("section", "PHYSICIAN VERIFICATION"),
        ("body", "The intake review's immunization closure was reconciled against the immunization record, which "
                 "documents overdue and missing vaccinations. Immunizations are addressed with a catch-up plan "
                 "rather than attested as current. Ready for signature."),
        ("sig", "Electronically signed by Esteban Murillo, MD on 06/09/2026"),
    ],
)

if __name__ == "__main__":
    for spec in (DELIVERABLE, INTAKE, IMMUNIZATION_RECORD, GOLDEN):
        out = W.build_one(spec, outdir=OUT)
        print("  OK", out.name)
    print("done OV11 v2 (AWV immunization over-closure with contradiction) render ->", OUT)
