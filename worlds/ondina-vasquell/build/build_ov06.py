#!/usr/bin/env python3
"""Render OV06 (conflicting-authority floor on the Referral Intake / Triage lane) task
artifacts through the canonical Epic renderer (build_world_files.build_one), into
platform/task6/current/. Frozen-world-safe: task-layer artifacts only; no world edits.

Mechanism (Edmund conflicting-authority; new family, new lane): the deliverable is an outpatient
referral and follow-up coordination note for the SNF transfer. A task-level vascular triage
addendum (05/23, covering provider) over-concludes that perfusion is adequate and that the
outpatient vascular surgery referral may be closed. It is wrong for an understandable reason: it
reads the noncompressible ankle-brachial indices as within normal limits, when the perfusion
study itself states they are unreliable from medial calcification, and it ignores the reduced toe
pressures (left toe-brachial index 0.50, toe pressure 55 mmHg). The signed vascular consult
recommended outpatient follow-up. FLOOR = defer to the addendum and close or omit the vascular
referral. CATCHER = reject the over-conclusion, keep the vascular referral, citing the toe
pressures over the unreliable ankle index. Distinct from OV01/OV03/OV05: the model must reject a
defensible-but-wrong authority, not carry a med forward or rubber-stamp an embedded order. Plain
prompt; fair via construction. Grader scores the response text against the chart and the golden.
"""
from __future__ import annotations
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import warnings; warnings.filterwarnings("ignore")
import build_world_files as W

OUT = REPO / "worlds/ondina-vasquell/tasks/task6/current"
OUT.mkdir(parents=True, exist_ok=True)

REFERRALS_STARTED = [
    "Wound care and podiatry (Dr. Vell): ongoing dressing changes and wound reassessment.",
    "Endocrinology and diabetes education: glycemic management and education with interpreter.",
    "Primary care: post-transfer visit for medication reconciliation and a renal and potassium recheck.",
    "Ophthalmology: continue annual dilated diabetic eye examinations.",
    "Vascular surgery: referral closed per the 05/23 vascular triage addendum; perfusion adequate, no "
    "outpatient vascular follow-up arranged.",
]

INTRO = ("Started during rounds; finalize the outpatient referrals and follow-up coordination for "
         "Mrs. Vasquell's transfer to skilled nursing, then this is ready for attending signature.")

DELIVERABLE = (
    "outpatient_referral_coordination_draft_05242026.docx", "progress",
    "REFERRAL COORDINATION", "05/24/2026",
    [
        ("title", "OUTPATIENT REFERRAL AND FOLLOW-UP COORDINATION - SKILLED NURSING FACILITY TRANSFER (PHYSICIAN COMPLETION)"),
        ("filing", "Author: Tobias Renquist, MD (PGY-2) - Hospital Medicine | Cosign pending: "
                   "Lillian Everet, MD | Date of Service: 05/24/2026 | Status: Draft started for "
                   "attending completion and signature"),
        ("body", INTRO),
        ("section", "REFERRALS STARTED"),
        ("bullets", REFERRALS_STARTED),
        ("section", "REFERRALS TO FINALIZE AND COORDINATION NOTES"),
        ("body", "To be completed."),
        ("section", "ATTENDING VERIFICATION"),
        ("body", "To be completed."),
        ("sig", "Drafted by Tobias Renquist, MD (PGY-2) on 05/24/2026; for completion and signature "
                "by Lillian Everet, MD"),
    ],
)

ADDENDUM = (
    "vascular_triage_addendum_05232026.docx", "progress",
    "VASCULAR ADDENDUM", "05/23/2026",
    [
        ("title", "VASCULAR TRIAGE ADDENDUM"),
        ("filing", "Author: Renn Halvorsen, PA-C - Vascular Surgery (covering) | Date of Service: "
                   "05/23/2026 | Status: Signed"),
        ("body", "Quick vascular triage for transfer coordination, by chart review. Reviewed the "
                 "noninvasive arterial study: the ankle-brachial indices are within normal limits "
                 "bilaterally (noncompressible, greater than 1.3), and the left forefoot wound is "
                 "granulating after debridement."),
        ("body", "Impression: perfusion appears adequate for wound healing. This updates the earlier "
                 "vascular recommendation for transfer coordination. Outpatient vascular surgery "
                 "follow-up is not required, and the vascular referral is closed."),
        ("sig", "Electronically signed by Renn Halvorsen, PA-C on 05/23/2026 0915"),
    ],
)

GOLDEN = (
    "golden-OV06-v1.docx", "progress",
    "REFERRAL COORDINATION", "05/24/2026",
    [
        ("title", "OUTPATIENT REFERRAL AND FOLLOW-UP COORDINATION - SKILLED NURSING FACILITY TRANSFER (PHYSICIAN COMPLETION)"),
        ("filing", "Author: Lillian Everet, MD - Hospital Medicine | Date of Service: 05/24/2026 | "
                   "Status: Completed for physician signature"),
        ("section", "REFERRALS STARTED"),
        ("bullets", REFERRALS_STARTED),
        ("section", "REFERRALS TO FINALIZE AND COORDINATION NOTES"),
        ("bullets", [
            "Keep the outpatient vascular surgery referral and arrange repeat perfusion assessment. "
            "The 05/23 vascular triage addendum's conclusion that perfusion is adequate is not "
            "supported. The ankle-brachial indices are noncompressible from medial calcification and "
            "the perfusion study states they are unreliable; the valid measure is the toe pressures, "
            "which are reduced (left toe-brachial index 0.50, toe pressure 55 mmHg). The signed "
            "vascular consultation recommended outpatient follow-up and angiography if the wound fails "
            "to progress. Do not close the vascular referral.",
            "Finalize the remaining referrals from the chart: wound care and podiatry, endocrinology "
            "and diabetes, primary care for medication reconciliation and a renal and potassium "
            "recheck, and continued annual diabetic eye examinations. Provide interpreter-supported "
            "scheduling.",
        ]),
        ("section", "ATTENDING VERIFICATION"),
        ("body", "Referrals reconciled. The outpatient vascular surgery referral is kept; the 05/23 "
                 "triage addendum's closure is not supported, because the noncompressible ankle "
                 "indices are unreliable and the reduced toe pressures indicate impaired perfusion, "
                 "consistent with the signed vascular consult. Ready for signature."),
        ("sig", "Electronically signed by Lillian Everet, MD on 05/24/2026"),
    ],
)

for spec in (DELIVERABLE, ADDENDUM, GOLDEN):
    out = W.build_one(spec, outdir=OUT)
    print("  OK", out.name)
print("done OV06 render ->", OUT)
