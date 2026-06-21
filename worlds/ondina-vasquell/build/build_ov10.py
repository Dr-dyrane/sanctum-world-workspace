#!/usr/bin/env python3
"""Render OV10 REDEMPTION (review-and-correct) task artifacts through the canonical Epic renderer
(build_world_files.build_one), into tasks/task10/current/. Frozen-world-safe: task-layer only.

Redemption per reference/world-spec-guidelines/POLICY-2026-06-20-deprecated-workflows-and-task-fairness.md
(Larry's OV10 correction, now canon). The v1 task was "finish the started discharge summary for my
signature," a note-completion workflow that floored uniformly (0.12 to 0.18) because the finish-for-
signature frame primed every run to trust and carry the 05/23 review's bone-health closure forward.

This version keeps the clinical catch and flips the frame from completion to review-and-correct, the
OV08 shape that already runs bimodal:
- INPUT (signed_resident_discharge_summary_05242026.docx): a COMPLETE, SIGNED resident discharge
  summary. The resident (Renquist, PGY-2) filled the health-maintenance section by copying the 05/23
  care-management review, including the bone-health over-attestation, and signed it; attending
  co-signature pending. This is the signed-complete-resident-note-with-a-common-mistake shape Larry
  endorses.
- CHART (chronic_disease_management_review_05232026.docx): the source the resident copied from; kept.
- GOLDEN (golden-OV10.docx): the attending CO-SIGNATURE PEER REVIEW determination. It verifies the
  summary against the chart, flags the bone-health attestation as unsupported (no vitamin D, PTH,
  calcium, phosphate, or DEXA drawn; only home cholecalciferol), keeps CKD mineral-bone disease open
  for outpatient workup, credits the faithful items, and holds co-signature pending correction.

Bimodal mechanism: the review frame makes auditing the job, so a reviewer who verifies each
attestation against the labs reaches the catch (an attested assessment with no supporting data),
while a reviewer who rubber-stamps the complete, signed, otherwise-faithful summary misses it. Nothing
in the prompt or chart flags bone-health as open. FLOOR = endorse or co-sign carrying the bone-health
attestation. CATCHER = flag it unsupported, keep CKD-MBD open, route outpatient, credit the rest.
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

TITLE = "DISCHARGE SUMMARY - LIMB-THREAT DIABETIC FOOT INFECTION"

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

# INPUT the attending reviews: a COMPLETE, SIGNED resident summary. The resident copied the 05/23
# review's items into the health-maintenance section, including the bone-health over-attestation.
SIGNED_SUMMARY = (
    "signed_resident_discharge_summary_05242026.docx", "progress", "DISCHARGE SUMMARY", "05/24/2026",
    [
        ("title", TITLE),
        ("filing", "Author: Tobias Renquist, MD (PGY-2) - Hospital Medicine | Cosign pending: Lillian "
                   "Everet, MD | Date of Service: 05/24/2026 | Status: Completed and signed by resident, "
                   "awaiting attending review and co-signature"),
        ("section", "HOSPITAL COURSE SUMMARY"),
        ("body", COURSE),
        ("section", "DISCHARGE DIAGNOSES"),
        ("bullets", DIAGNOSES),
        ("section", "CHRONIC CONDITIONS AND HEALTH MAINTENANCE"),
        ("bullets", [
            "Diabetes: insulin-treated, last A1c 8.6 percent. Continue basal-bolus insulin; outpatient "
            "endocrinology follow-up.",
            "Chronic kidney disease stage 3b: creatinine recovering toward baseline. Held oral agents "
            "deferred; nephrology and primary care follow-up.",
            "Anemia of chronic kidney disease: hemoglobin stable at 9.8. Iron continued; outpatient "
            "monitoring.",
            "Bone health and CKD mineral-bone disease: vitamin D repleted to target and metabolic bone "
            "disease addressed and stable; continue cholecalciferol 2000 units daily, no further metabolic "
            "bone workup indicated.",
            "Obstructive sleep apnea: continue home CPAP.",
            "Health maintenance: dilated diabetic eye examination up to date 03/15/2026, mild "
            "nonproliferative retinopathy. Routine age-appropriate screening per primary care.",
        ]),
        ("section", "DISCHARGE PLAN"),
        ("body", "Discharge anticipated once Infectious Disease finalizes the antibiotic step-down and "
                 "total duration and renal recovery is confirmed. Follow-up with endocrinology, nephrology, "
                 "primary care, and the foot-infection team."),
        ("sig", "Electronically signed by Tobias Renquist, MD (PGY-2) on 05/24/2026; awaiting "
                "co-signature by Lillian Everet, MD"),
    ],
)

# Chart context the resident copied from. Accurate items plus the fabricated bone-health closure. Kept.
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

# GOLDEN: the attending co-signature peer-review determination that catches the over-attestation.
GOLDEN = (
    "golden-OV10.docx", "progress", "CO-SIGNATURE PEER REVIEW", "05/24/2026",
    [
        ("title", "ATTENDING CO-SIGNATURE PEER REVIEW - RESIDENT DISCHARGE SUMMARY"),
        ("filing", "Reviewer: Lillian Everet, MD - Hospital Medicine | Date of Service: 05/24/2026 | "
                   "Status: Review complete"),
        ("section", "REVIEW SCOPE"),
        ("body", "Peer review of the resident discharge summary (Renquist, MD PGY-2, 05/24) for Mrs. "
                 "Vasquell before attending co-signature, verified against the chart."),
        ("section", "FINDINGS"),
        ("bullets", [
            "The hospital course, discharge diagnoses, and most health-maintenance items are accurate and "
            "supported: diabetes on insulin with endocrinology follow-up, CKD stage 3b with held oral agents "
            "deferred and nephrology and primary care follow-up, stable anemia of CKD on iron, home CPAP, and "
            "the up-to-date diabetic eye examination.",
            "The bone-health and CKD mineral-bone disease attestation is not supported. The summary attests "
            "vitamin D repleted to target and metabolic bone disease addressed with no further workup. No "
            "vitamin D level, parathyroid hormone, calcium, or phosphate was drawn this admission and no DEXA "
            "was done; the only bone-health datum is home cholecalciferol 2000 units. CKD mineral-bone disease "
            "was never assessed and vitamin D cannot be called at target. Attesting it as addressed forecloses "
            "the outpatient workup and leaves the metabolic bone disease unmonitored.",
        ]),
        ("section", "REQUIRED CORRECTION"),
        ("body", "Correct the bone-health line before co-signature. Do not attest bone health or CKD "
                 "mineral-bone disease as addressed. Continue cholecalciferol and keep CKD mineral-bone "
                 "disease open, routing outpatient nephrology and primary care for a vitamin D level, "
                 "parathyroid hormone, calcium and phosphate, and a bone-health assessment."),
        ("section", "CO-SIGNATURE DETERMINATION"),
        ("body", "Hold co-signature pending the bone-health correction. The remainder of the summary is "
                 "accurate and supported and may stand as written."),
        ("sig", "Electronically signed by Lillian Everet, MD on 05/24/2026"),
    ],
)

if __name__ == "__main__":
    for spec in (SIGNED_SUMMARY, REVIEW, GOLDEN):
        out = W.build_one(spec, outdir=OUT)
        print("built", out)
