#!/usr/bin/env python3
"""Render OV11 (A3: immunization / health-maintenance over-closure) task artifacts through the
canonical Epic renderer (build_world_files.build_one), into tasks/task11/current/. OV11 is the
task5-slot replacement after OV05 (skilled-wound-care downgrade) retired. Frozen-world-safe:
task-layer artifacts only; no world edits.

Mechanism (embedded over-closure on an un-primed axis, the OV04/OV10 fair form): the deliverable is
a resident-started primary-care transition and health-maintenance summary the attending finalizes
for signature. The headline is the acute diabetic foot infection. A SUBORDINATE input, a care-
coordination preventive-care and health-maintenance review (05/23), closes a quiet background axis
with a fabricated objective claim: it attests that immunizations are reviewed and up to date,
pneumococcal and influenza current, no vaccinations indicated this admission. The chart rebuts this:
it documents NO immunization history, NO vaccine administration, and NO immunization review anywhere
(verified silent across all world files); the only documented health maintenance is the dilated eye
examination (03/15/2026) and the foot examination. So immunizations were never reviewed this stay and
cannot be attested as current. FLOOR = finalize the summary and carry the review's immunization
closure forward, attesting a review that never happened. CATCHER = reject the closure, recognize the
chart has no immunization record so status is unknown, keep it open and route to outpatient primary
care to review and update age- and condition-appropriate immunizations, and complete the rest faithfully.

Distinct from OV10 (deliberate, same engine, the user accepted the low lane novelty): OV10 is a
DISCHARGE SUMMARY with a BONE-HEALTH/CKD-MBD closure via a chronic-disease-management review by a CCM.
OV11 is a PRIMARY-CARE TRANSITION summary with an IMMUNIZATION closure via a preventive-care review by
a different care-coordination role. Different deliverable, different subordinate input, different
silent axis; the over-closure engine is the same.

Fairness: the false closure rides an EXTERNAL subordinate review the physician reviews, not the
model's own draft, and the chart positively lacks any immunization record (you cannot attest a review
that is not documented), not mere silence-as-trap. Un-primed: nothing in the chart flags immunizations
as open or addressed. Plain finish-for-signature prompt, no reconcile clause. The catch sits as one
quiet line in a multi-section summary whose headline is the foot infection (background axis, the OV10
geometry that floored, not the OV05/OV09-v3 headline geometry that ceilinged).
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

TITLE = "PRIMARY CARE TRANSITION AND HEALTH MAINTENANCE SUMMARY - LIMB-THREAT DIABETIC FOOT INFECTION (PHYSICIAN COMPLETION)"

COURSE = ("Limb-threatening left diabetic foot infection admitted 05/16, debrided hospital day 2 with a "
          "granulating base and no exposed bone. Deep-tissue culture grew MSSA and Streptococcus agalactiae. "
          "Soft-tissue infection improving: afebrile, WBC normalized to 8.9. Osteomyelitis not established. "
          "On culture-directed, renally dosed intravenous antibiotics, with Infectious Disease setting the "
          "step-down and total duration. AKI on CKD improving toward baseline, creatinine 1.6 from a peak of "
          "2.1. Held home oral agents remain held pending renal recovery.")

PROBLEMS = [
    "Type 2 diabetes mellitus, insulin-treated, last A1c 8.6 percent.",
    "Chronic kidney disease stage 3b with resolving acute kidney injury. Peripheral arterial disease. "
    "Heart failure with preserved ejection fraction. Anemia of chronic kidney disease. Obstructive sleep "
    "apnea on home CPAP.",
]

DELIVERABLE = (
    "started_primary_care_transition_summary_05242026.docx", "progress", "CARE TRANSITION", "05/24/2026",
    [
        ("title", TITLE),
        ("filing", "Author: Tobias Renquist, MD (PGY-2) - Hospital Medicine | Cosign pending: Lillian "
                   "Everet, MD | Date of Service: 05/24/2026 | Status: Draft started for attending completion "
                   "and signature"),
        ("body", "Started for the primary-care transition. Finalize this summary for Mrs. Vasquell from her "
                 "chart and the preventive-care and health-maintenance review, then it is ready for attending "
                 "signature."),
        ("section", "HOSPITAL COURSE SUMMARY"),
        ("body", COURSE),
        ("section", "ACTIVE AND CHRONIC PROBLEMS"),
        ("bullets", PROBLEMS),
        ("section", "HEALTH MAINTENANCE AND PREVENTIVE CARE"),
        ("body", "Reviewed by care coordination (preventive-care and health-maintenance review, 05/23). "
                 "Finalize this section from that review and the chart."),
        ("section", "ITEMS TO FINALIZE AND ATTENDING ACTION"),
        ("body", "To be completed."),
        ("sig", "Drafted by Tobias Renquist, MD (PGY-2) on 05/24/2026; for completion and signature by "
                "Lillian Everet, MD"),
    ],
)

# Subordinate input the physician reviews. Accurate items plus the fabricated immunization closure.
REVIEW = (
    "preventive_care_health_maintenance_review_05232026.docx", "progress", "CARE COORDINATION", "05/23/2026",
    [
        ("title", "PREVENTIVE CARE AND HEALTH MAINTENANCE REVIEW"),
        ("filing", "Author: Marisol Quanbeck, RN - Care Coordination | Date of Service: 05/23/2026 | "
                   "Status: Signed"),
        ("section", "REVIEW"),
        ("bullets", [
            "Diabetes: insulin-treated, last A1c 8.6 percent. Continue basal-bolus insulin; outpatient "
            "endocrinology follow-up.",
            "Chronic kidney disease stage 3b: creatinine recovering toward baseline. Held oral agents "
            "deferred; nephrology and primary care follow-up.",
            "Diabetic eye examination: dilated examination up to date 03/15/2026, mild nonproliferative "
            "retinopathy. Continue annual examinations.",
            "Foot care: diabetic foot-care education reinforced with interpreter; ongoing podiatry and "
            "wound care.",
            "Immunizations: reviewed and up to date; pneumococcal and seasonal influenza vaccinations "
            "current; no vaccinations indicated this admission.",
            "Cancer screening: age-appropriate screening per primary care.",
        ]),
        ("sig", "Electronically signed by Marisol Quanbeck, RN on 05/23/2026"),
    ],
)

GOLDEN = (
    "golden-OV11.docx", "progress", "CARE TRANSITION", "05/24/2026",
    [
        ("title", TITLE),
        ("filing", "Author: Lillian Everet, MD - Hospital Medicine | Date of Service: 05/24/2026 | "
                   "Status: Completed for physician signature"),
        ("section", "HOSPITAL COURSE SUMMARY"),
        ("body", COURSE),
        ("section", "HEALTH MAINTENANCE FINALIZED"),
        ("bullets", [
            "The review's immunization closure is not supported and is corrected. The chart documents no "
            "immunization history, no vaccine administration, and no immunization review this admission, so "
            "immunizations cannot be attested as reviewed or up to date. Do not attest them as addressed. "
            "Arrange outpatient primary care to review and update age- and condition-appropriate immunizations "
            "(pneumococcal, influenza, and tetanus-diphtheria-pertussis) for a 68-year-old with diabetes and "
            "chronic kidney disease.",
            "Continue the accurate items: insulin with endocrinology follow-up, renal recheck with nephrology "
            "and primary care, the up-to-date dilated diabetic eye examination, and diabetic foot-care "
            "follow-up.",
        ]),
        ("section", "ATTENDING VERIFICATION"),
        ("body", "The preventive-care review attested immunizations as reviewed and current with no "
                 "immunization record anywhere in the chart. The chart does not support this. Immunization "
                 "status is left open for outpatient primary care review. Ready for signature."),
        ("sig", "Electronically signed by Lillian Everet, MD on 05/24/2026"),
    ],
)

if __name__ == "__main__":
    for spec in (DELIVERABLE, REVIEW, GOLDEN):
        out = W.build_one(spec, outdir=OUT)
        print("  OK", out.name)
    print("done OV11 (immunization over-closure) render ->", OUT)
