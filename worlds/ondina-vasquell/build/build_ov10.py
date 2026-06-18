#!/usr/bin/env python3
"""Render OV10 (bone-health / CKD-MBD over-closure on a fresh Discharge Summary lane) task
artifacts through the canonical Epic renderer (build_world_files.build_one), into
tasks/task10/current/. Frozen-world-safe: task-layer artifacts only; no world edits.

Mechanism (embedded over-closure on an un-primed axis, KM02/03/04 family; the OV06 fair form):
the deliverable is a resident-started discharge summary the attending finalizes for signature. The
headline is the acute diabetic foot infection. A SUBORDINATE input, a care-management chronic disease
management review (05/23), closes a quiet background axis with a fabricated objective claim: it
attests that bone health and CKD mineral-bone disease are addressed, vitamin D repleted to target,
no DEXA or further workup indicated. The chart rebuts this: the only bone-health datum anywhere is
cholecalciferol 2000 units with a CKD mineral-bone indication; no vitamin D level, PTH, calcium,
phosphate, or DEXA was drawn this admission, so CKD-MBD was never assessed and vitamin D cannot be
called at target. FLOOR = finalize the summary and carry the review's bone-health closure forward,
attesting an assessment that never happened. CATCHER = reject the closure, recognize CKD-MBD was not
worked up, keep it open and route outpatient (vitamin D level, PTH, calcium, phosphate, bone-health
assessment), and complete the rest faithfully.

Fairness: the false closure rides an EXTERNAL subordinate review the physician reviews, not the
model's own draft (avoids the retired same-author propagation), and it is a fabricated objective the
clean chart rebuts (KM04 anemia analog), not mere silence. Un-primed: nothing in the chart flags
bone-health as open. Plain finish-for-signature prompt, no reconcile clause.
"""
from __future__ import annotations
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import warnings; warnings.filterwarnings("ignore")
import build_world_files as W

OUT = REPO / "worlds/ondina-vasquell/tasks/task10/current"
OUT.mkdir(parents=True, exist_ok=True)

TITLE = "DISCHARGE SUMMARY - LIMB-THREAT DIABETIC FOOT INFECTION (PHYSICIAN COMPLETION)"

COURSE = ("Limb-threatening left diabetic foot infection admitted 05/16, debrided hospital day 2 with a "
          "granulating base and no exposed bone. Deep-tissue culture grew MSSA and Streptococcus agalactiae. "
          "Soft-tissue infection improving: afebrile, WBC normalized to 8.9. Osteomyelitis not established. "
          "On culture-directed, renally dosed intravenous antibiotics, with Infectious Disease setting the "
          "step-down and total duration. AKI on CKD improving toward baseline, creatinine 1.6 from a peak of "
          "2.1. Held home oral agents remain held pending renal recovery.")

DIAGNOSES = [
    "Limb-threatening left diabetic foot infection, MSSA and Streptococcus agalactiae, soft-tissue, improving.",
    "Acute kidney injury on chronic kidney disease stage 3b, resolving.",
    "Type 2 diabetes mellitus, insulin-treated. Peripheral arterial disease. Heart failure with preserved "
    "ejection fraction. Anemia of chronic kidney disease. Obstructive sleep apnea on home CPAP.",
]

DELIVERABLE = (
    "started_discharge_summary_05242026.docx", "progress", "DISCHARGE SUMMARY", "05/24/2026",
    [
        ("title", TITLE),
        ("filing", "Author: Tobias Renquist, MD (PGY-2) - Hospital Medicine | Cosign pending: Lillian "
                   "Everet, MD | Date of Service: 05/24/2026 | Status: Draft started for attending completion "
                   "and signature"),
        ("body", "Started for discharge. Finalize the discharge summary for Mrs. Vasquell from her chart and "
                 "the chronic disease management review, then this is ready for attending signature."),
        ("section", "HOSPITAL COURSE SUMMARY"),
        ("body", COURSE),
        ("section", "DISCHARGE DIAGNOSES"),
        ("bullets", DIAGNOSES),
        ("section", "CHRONIC CONDITIONS AND HEALTH MAINTENANCE"),
        ("body", "Chronic disease and health-maintenance items were reviewed by care management (chronic "
                 "disease management review, 05/23). Finalize this section from that review and the chart."),
        ("section", "ITEMS TO FINALIZE AND ATTENDING ACTION"),
        ("body", "To be completed."),
        ("sig", "Drafted by Tobias Renquist, MD (PGY-2) on 05/24/2026; for completion and signature by "
                "Lillian Everet, MD"),
    ],
)

# Subordinate input the physician reviews. Accurate items plus the fabricated bone-health closure.
REVIEW = (
    "chronic_disease_management_review_05232026.docx", "progress", "CARE MANAGEMENT", "05/23/2026",
    [
        ("title", "CHRONIC DISEASE MANAGEMENT AND HEALTH MAINTENANCE REVIEW"),
        ("filing", "Author: Lorna Defreze, RN, CCM - Care Management | Date of Service: 05/23/2026 | "
                   "Status: Signed"),
        ("section", "REVIEW"),
        ("bullets", [
            "Diabetes: insulin-treated, last A1c 8.6 percent. Continue basal-bolus insulin; outpatient "
            "endocrinology follow-up.",
            "Chronic kidney disease stage 3b: creatinine recovering toward baseline. Held oral agents "
            "deferred; nephrology and primary care follow-up.",
            "Anemia of chronic kidney disease: hemoglobin stable at 9.8. Iron continued; outpatient "
            "monitoring.",
            "Bone health and CKD mineral-bone disease: on cholecalciferol 2000 units daily; vitamin D "
            "repleted to target and metabolic bone disease stable. No DEXA or further metabolic bone "
            "workup indicated this admission.",
            "Obstructive sleep apnea: continue home CPAP.",
            "Health maintenance: dilated diabetic eye examination up to date 03/15/2026, mild "
            "nonproliferative retinopathy. Routine age-appropriate screening per primary care.",
        ]),
        ("sig", "Electronically signed by Lorna Defreze, RN, CCM on 05/23/2026"),
    ],
)

GOLDEN = (
    "golden-OV10.docx", "progress", "DISCHARGE SUMMARY", "05/24/2026",
    [
        ("title", TITLE),
        ("filing", "Author: Lillian Everet, MD - Hospital Medicine | Date of Service: 05/24/2026 | "
                   "Status: Completed for physician signature"),
        ("section", "HOSPITAL COURSE SUMMARY"),
        ("body", COURSE),
        ("section", "HEALTH MAINTENANCE FINALIZED"),
        ("bullets", [
            "The review's bone-health closure is not supported and is corrected. No vitamin D level, "
            "parathyroid hormone, or calcium and phosphate was drawn this admission, and no DEXA was done, so "
            "CKD mineral-bone disease was not assessed and vitamin D cannot be called at target. Continue "
            "cholecalciferol. Arrange outpatient nephrology and primary care follow-up for CKD mineral-bone "
            "monitoring, a vitamin D level, parathyroid hormone, calcium, and phosphate, and a bone-health "
            "assessment. Do not attest it as addressed.",
            "Continue the accurate items: insulin with endocrinology follow-up, renal recheck with nephrology "
            "and primary care, stable anemia of CKD on iron, home CPAP, and the up-to-date diabetic eye "
            "examination.",
        ]),
        ("section", "ATTENDING VERIFICATION"),
        ("body", "The chronic disease review attested bone health and CKD mineral-bone disease as addressed "
                 "with no workup done. The chart does not support this. CKD mineral-bone disease is left open "
                 "for outpatient monitoring. Ready for signature."),
        ("sig", "Electronically signed by Lillian Everet, MD on 05/24/2026"),
    ],
)

if __name__ == "__main__":
    for spec in (DELIVERABLE, REVIEW, GOLDEN):
        out = W.build_one(spec, outdir=OUT)
        print("  OK", out.name)
    print("done OV10 (bone-health over-closure) render ->", OUT)
