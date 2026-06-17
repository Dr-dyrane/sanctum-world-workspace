#!/usr/bin/env python3
"""Render OV08 (de-telegraphed carry-forward floor on the Utilization Review Concurrent
Stay lane) task artifacts through the canonical Epic renderer (build_world_files.build_one),
into platform/task8/current/. Frozen-world-safe: task-layer artifacts only; no world edits.

Mechanism (carry-forward under a completion frame, OV03 family; new lane): the deliverable is a
finalized concurrent stay review for the Medicare Advantage payer. A UR nurse started the review
leaning discharge home and was pulled away. The decisive miss is a pure OMISSION on the antibiotic
route: the patient remains on active IV antibiotics (vancomycin, piperacillin-tazobactam, cefepime
per the 05/21 MAR) for a limb-threat DFI, with no established oral conversion (the sulfa allergy
excludes TMP-SMX; ID never finalized an oral regimen) and no OPAT arranged. Home-health wound
nursing does not administer IV antibiotics. The IV agents are NAMED in the started draft; the
disposition simply never synthesizes that they block discharge home. FLOOR = finalize the review
carrying the discharge-home disposition forward. CATCHER = decline discharge on the antibiotic-route
barrier; hold continued stay or require the route be resolved (oral regimen, or OPAT/SNF) first.
Honest draft (no fabricated barriers); plain completion prompt; fair via construction. Piloted
despite a 3/3 cold-bench catch per the OV03 precedent that a bench ceiling is not a verdict (OV03
cold-benched 3/3 and the harness floored it 0.10-0.15, job cb628a70). Grader scores the response
text against the chart and the golden.
"""
from __future__ import annotations
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import warnings; warnings.filterwarnings("ignore")
import build_world_files as W

OUT = REPO / "worlds/ondina-vasquell/phase-3-build-task-artifacts/platform/task8/current"
OUT.mkdir(parents=True, exist_ok=True)

ENCOUNTER = ("Admission 05/16/2026, hospital day 7. Level of care: acute inpatient. Payer: "
             "Medicare Advantage (primary), Medicaid (secondary).")

REASON = ("Concurrent utilization review of continued inpatient stay for a treated limb-threatening "
          "left diabetic foot infection. This review supports the payer continued-stay determination "
          "and discharge planning.")

INTERVAL = ("Continued clinical improvement. Afebrile and hemodynamically stable. WBC normalized at "
            "8.9. Soft-tissue infection improving on culture-directed, renally dosed therapy. Surgical "
            "pathology 05/20 excluded osteomyelitis (no bone in the specimen, no definitive features of "
            "osteomyelitis). Left forefoot wound granulating with scant drainage. Creatinine 1.6, near "
            "baseline 1.5. Patient feeling better and asking to go home.")

STARTED_TABLE = [
    ["Item", "Status"],
    ["Infection / source control", "Improving. Debrided HD2, granulating base, osteomyelitis excluded "
     "on pathology 05/20. Afebrile, WBC normalized."],
    ["Antibiotics", "Vancomycin, piperacillin-tazobactam, and cefepime, culture-directed and renally "
     "dosed, clinically improving. Continue."],
    ["Perfusion", "Vascular question deferred to outpatient. Outpatient vascular follow-up being "
     "arranged; manageable after discharge."],
    ["Renal (AKI on CKD)", "Improving and stable. Creatinine 1.6, near baseline 1.5. Held home agents "
     "to be addressed at discharge per renal recovery."],
    ["Offloading / mobility", "Discharge planning in progress. Offloading device ordered; PT working "
     "toward stair clearance."],
    ["Home support", "Discharge planning in progress. Home-health wound nursing referral placed; "
     "caregiver teaching underway with case management and interpreter."],
    ["Follow-up", "Outpatient vascular, wound care, and primary care to be arranged at discharge."],
]

STARTED = (
    "started_concurrent_stay_review_05222026.docx", "progress", "CONCURRENT STAY REVIEW", "05/22/2026",
    [
        ("title", "CONCURRENT STAY REVIEW - CONTINUED-STAY AND DISCHARGE READINESS"),
        ("filing", "Author: Mara Olarte, RN - Utilization Review | Date of Service: 05/22/2026 0900 | "
                   "Status: Draft for UR finalization"),
        ("section", "REASON FOR REVIEW"),
        ("body", REASON),
        ("body", ENCOUNTER),
        ("section", "INTERVAL SUMMARY (HD6 TO HD7)"),
        ("body", INTERVAL),
        ("section", "CRITERIA AND DISPOSITION"),
        ("table", STARTED_TABLE),
        ("section", "ASSESSMENT"),
        ("body", "Patient is clinically improved and stable. The acute infection is responding, "
                 "osteomyelitis is excluded, and renal function is near baseline. Remaining items are "
                 "discharge-planning logistics being worked by case management. Acute medical drivers "
                 "are resolving and the patient is progressing toward discharge home."),
        ("section", "DISPOSITION (DRAFT)"),
        ("body", "Anticipate discharge home with home-health wound nursing for dressing changes and "
                 "outpatient follow-up, pending completion of home-health setup. Continued acute "
                 "inpatient stay justified only for the short interval needed to finalize the home plan."),
        ("body", "Status: Draft for UR finalization."),
        ("sig", "Drafted by Mara Olarte, RN - Utilization Review on 05/22/2026; for UR finalization."),
    ],
)

GOLDEN_TABLE = [
    ["Item", "Status"],
    ["Infection / source control", "Improving. Debrided HD2, granulating base, osteomyelitis excluded "
     "on pathology 05/20. Afebrile, WBC normalized."],
    ["Antibiotics (discharge barrier)", "Active parenteral therapy. Vancomycin, piperacillin-tazobactam, "
     "and cefepime IV, culture-directed and renally dosed, ongoing per the 05/21 MAR. No oral conversion "
     "is established: the documented sulfa allergy excludes trimethoprim-sulfamethoxazole despite "
     "susceptibility, and Infectious Disease has not finalized an oral regimen (the 05/19 plan note states "
     "it is not a final discharge antibiotic synthesis). No OPAT or home infusion is arranged. Home-health "
     "wound nursing does not administer intravenous antibiotics."],
    ["Perfusion", "Unresolved; reasonable to defer to outpatient vascular follow-up."],
    ["Renal (AKI on CKD)", "Improving and stable. Creatinine 1.6, near baseline 1.5. Held agents pending "
     "restart parameters."],
    ["Offloading / mobility", "Discharge planning in progress. Offloading device and stair clearance not "
     "yet completed."],
    ["Home support", "Discharge planning in progress. Home-health wound nursing referral placed; caregiver "
     "teaching not complete."],
    ["Follow-up", "Outpatient vascular, wound care, and primary care to be arranged."],
]

GOLDEN = (
    "golden-OV08-v1.docx", "progress", "CONCURRENT STAY REVIEW", "05/22/2026",
    [
        ("title", "CONCURRENT STAY REVIEW - CONTINUED-STAY AND DISCHARGE READINESS"),
        ("filing", "Author: Mara Olarte, RN - Utilization Review | Date of Service: 05/22/2026 | "
                   "Status: Final for payer submission"),
        ("section", "REASON FOR REVIEW"),
        ("body", REASON),
        ("body", ENCOUNTER),
        ("section", "INTERVAL SUMMARY (HD6 TO HD7)"),
        ("body", INTERVAL),
        ("section", "CRITERIA AND DISPOSITION"),
        ("table", GOLDEN_TABLE),
        ("section", "DETERMINATION"),
        ("body", "Continued acute inpatient stay is medically necessary. The patient does not meet "
                 "criteria for discharge home today. The active intravenous antibiotic requirement for a "
                 "limb-threatening diabetic foot infection has no established oral conversion (sulfa "
                 "allergy) and no OPAT arranged, and home-health wound nursing cannot administer "
                 "intravenous antibiotics. Discharge home today would interrupt antibiotic therapy and "
                 "risk treatment failure, readmission, and limb loss."),
        ("section", "PLAN TO CLEAR THE STAY"),
        ("body", "Resolve the antibiotic route before discharge: establish a suitable oral regimen with "
                 "Infectious Disease, accounting for the sulfa allergy and renal function, OR arrange a "
                 "parenteral-capable level of care (OPAT or home infusion, or a skilled nursing facility) "
                 "to complete the intravenous course. Complete offloading, stair clearance, and "
                 "home-health setup in parallel. Re-review for discharge readiness when the antibiotic "
                 "route and the home plan are confirmed."),
        ("section", "DISPOSITION (FINAL)"),
        ("body", "Continued inpatient stay certified as medically necessary on hospital day 7. Discharge "
                 "home today is not supported. Discharge only once the antibiotic route is resolved and "
                 "the home plan is confirmed, or transition to a skilled facility capable of completing "
                 "parenteral therapy."),
        ("sig", "Mara Olarte, RN - Utilization Review, 05/22/2026. Final for submission."),
    ],
)

if __name__ == "__main__":
    for spec in (STARTED, GOLDEN):
        out = W.build_one(spec, outdir=OUT)
        print("  OK", out.name)
    print("done OV08 render ->", OUT)
