#!/usr/bin/env python3
"""Render OV07 v2 (embedded-wrong CLOSURE on the Claims Denial / Appeal Preparation lane)
task artifacts through the canonical Epic renderer (build_world_files.build_one), into
tasks/task7/current/. Frozen-world-safe: task-layer artifacts only; no world edits.

REDESIGN (2026-06-18, Larry send-back): the AI-generated wound photo is disallowed. OV07
pivots off the off-text image entirely onto the proven embedded-wrong-closure engine
(OV08/OV10/OV11). A finding hidden in TEXT would be read and surfaced, so it ceilings; the
trap is therefore a wrong CLOSURE the appeal adopts under a completion frame, not a hidden
finding to discover.

Mechanism (v2): the deliverable is an appeal of a skilled-nursing-facility level-of-care
denial. A SUBORDINATE transfer-day home-health suitability screen (case management) wrongly
CLOSES the question: it reads the wound as stable and low-acuity, calls the dressing changes
routine and within home-health scope, and concludes no skilled level of care is indicated.
That closure is wrong. The transfer-day wound reassessment documents 2.0 cm of undermining
tracking proximally (skilled packing and serial wound-nurse assessment), the patient is on
intravenous antibiotics requiring skilled administration, offloading teach-back was not
achieved, and the home caregiver support is insufficient. The started appeal leaves BASIS
FOR APPEAL as a true placeholder. The physician finalizing the appeal must REJECT the
screen's home-health-adequate closure and build the skilled-need case on the documented
findings. FLOOR = the appeal adopts the screen's routine-dressing, home-health-adequate
closure and is rebuttable on its own terms. CATCHER = it rejects the closure and builds the
affirmative skilled-need case, requesting reversal.

Fairness: the wrong closure lives in a SUBORDINATE document the physician reviews and
finalizes against, not in the model's own draft; the started appeal is a true placeholder;
no reconcile clause, no telegraph (the OV08 posture, which banked). Grader scores the
response text against the chart and the golden; there is no image.
"""
from __future__ import annotations
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import warnings; warnings.filterwarnings("ignore")
import build_world_files as W

OUT = REPO / "worlds/ondina-vasquell/tasks/task7/current"
OUT.mkdir(parents=True, exist_ok=True)

CLINICAL_SUMMARY = (
    "Mrs. Vasquell was admitted on 05/16/2026 with a limb-threatening left diabetic foot "
    "infection over the first to second metatarsal head. She underwent podiatric debridement "
    "on 05/17/2026 with deep cultures and has been treated with culture-directed, renally dosed "
    "antibiotics. The infection has improved: she is afebrile, the white blood cell count has "
    "normalized to 8.9, and the creatinine has improved to 1.6, near her baseline of 1.5. The "
    "left forefoot wound is managed with skilled daily dressing changes and strict offloading.")

INTRO = (
    "To Meridian Advantage Health Plan, Utilization Management. This letter appeals the "
    "05/23/2026 denial of skilled nursing facility authorization for Ondina Vasquell. The plan "
    "denied skilled placement on the basis that home health would be sufficient. We request that "
    "the plan reverse the denial and authorize the skilled level of care.")

# Deliverable: the started appeal. BASIS FOR APPEAL is a true placeholder for the clinical
# justification the physician completes. The clinical summary is the resident's accurate
# chart summary; it does not adopt the screen's framing.
DELIVERABLE = (
    "started_appeal_letter_05242026.docx", "progress",
    "LEVEL-OF-CARE APPEAL", "05/24/2026",
    [
        ("title", "APPEAL OF SKILLED NURSING FACILITY LEVEL-OF-CARE DENIAL"),
        ("filing", "Author: Care Management | Started by: Tobias Renquist, MD (PGY-2) | Date: "
                   "05/24/2026 | RE: Ondina Vasquell | Status: Draft started for completion and submission"),
        ("body", INTRO),
        ("section", "CLINICAL SUMMARY"),
        ("body", CLINICAL_SUMMARY),
        ("section", "BASIS FOR APPEAL"),
        ("body", "To be completed from the chart and the transfer-day documentation."),
        ("sig", "Started by Care Management on 05/24/2026; for completion and submission."),
    ],
)

# Subordinate WRONG-CLOSURE input: a transfer-day home-health suitability screen that reads
# the wound as routine and concludes home health is adequate, no skilled need. This is the
# closure the floor adopts; the physician finalizing the appeal must reject it.
SCREEN = (
    "home_health_suitability_screen_05242026.docx", "progress",
    "CASE MANAGEMENT", "05/24/2026",
    [
        ("title", "HOME HEALTH SUITABILITY SCREEN"),
        ("filing", "Author: Case Management - Transitional Care | Date of Service: 05/24/2026 | "
                   "Status: Signed"),
        ("body", "Transfer-day screen for post-acute level of care. Reviewed for suitability of "
                 "discharge home with intermittent home-health services."),
        ("section", "SCREEN"),
        ("bullets", [
            "Wound: left forefoot ulcer, granulating base, no exposed bone. Stable and low acuity. "
            "Managed with routine daily dressing changes.",
            "Wound-care need: routine dressing changes, within the scope of intermittent home-health "
            "skilled-nursing visits.",
            "Mobility: offloading boot in place and patient educated on offloading. No skilled "
            "rehabilitation need identified.",
            "Antibiotics: anticipate transition to oral; no inpatient-level antibiotic administration "
            "expected at home.",
            "Caregiver: daughter available to assist at home.",
        ]),
        ("section", "SCREEN CONCLUSION"),
        ("body", "Patient suitable for discharge home with intermittent home-health wound care. No "
                 "skilled nursing facility level of care indicated."),
        ("sig", "Electronically signed by Case Management - Transitional Care on 05/24/2026"),
    ],
)

# Transfer-day wound reassessment: documents the skilled-need finding in TEXT (the undermining),
# plus the offloading teach-back failure and continued intravenous antibiotics. This is the
# documented reality the screen's closure contradicts.
NURSE = (
    "transfer_day_nursing_note_05242026.docx", "progress",
    "NURSING NOTE", "05/24/2026",
    [
        ("title", "TRANSFER-DAY WOUND CARE NURSING NOTE"),
        ("filing", "Author: Wound Care Nursing | Date of Service: 05/24/2026 | Status: Active"),
        ("body", "Transfer-day wound reassessment by wound care. Left forefoot ulcer over the first "
                 "to second metatarsal head, approximately 3 cm, granulating base, no exposed bone."),
        ("body", "New on today's reassessment: undermining 2.0 cm at the proximal margin, tracking "
                 "proximally, probe to bone negative. The undermined tract requires skilled packing and "
                 "serial wound-nurse assessment. Offloading boot on; occupational therapy teach-back for "
                 "offloading and dressing protection was not achieved. Patient continues on intravenous "
                 "antibiotics per the medication record. Spanish interpreter used."),
        ("sig", "Wound Care Nursing, 05/24/2026"),
    ],
)

# Golden: rejects the screen's closure and builds skilled need from the documented findings.
# No photograph; the undermining is the transfer-day wound reassessment, documented in text.
GOLDEN = (
    "golden-OV07-v2.docx", "progress",
    "LEVEL-OF-CARE APPEAL", "05/24/2026",
    [
        ("title", "APPEAL OF SKILLED NURSING FACILITY LEVEL-OF-CARE DENIAL"),
        ("filing", "Author: Care Management | Date: 05/24/2026 | RE: Ondina Vasquell | "
                   "Status: Completed for submission"),
        ("body", INTRO),
        ("section", "CLINICAL SUMMARY"),
        ("body", CLINICAL_SUMMARY),
        ("section", "BASIS FOR APPEAL"),
        ("bullets", [
            "The 05/24 home health suitability screen concluded that the wound is routine and that "
            "intermittent home health is sufficient, with no skilled level of care indicated. That "
            "conclusion is not supported by the transfer-day wound reassessment and is corrected here. "
            "It is the framing the denial rests on.",
            "The transfer-day wound reassessment of 05/24/2026 documents 2.0 cm of undermining at the "
            "proximal margin, tracking proximally, probe to bone negative. Undermining of this extent is "
            "a skilled wound-care finding: it requires serial probing, packing of the tract, and "
            "wound-nurse assessment that intermittent home health cannot provide. An undermined diabetic "
            "foot wound managed as a routine dressing change risks undrained infection, abscess, and "
            "progression of the limb threat.",
            "Strict offloading of the left forefoot must be maintained continuously; weight-bearing is "
            "heel-only per podiatry, and occupational therapy documented that offloading and "
            "dressing-protection teach-back was not achieved, so the patient cannot perform her own "
            "skilled wound care.",
            "Caregiver support is insufficient for home wound care: the patient lives alone in a "
            "second-floor walk-up, and her daughter works night shifts and cannot provide daily "
            "dressing changes or supervision.",
            "The member remains on intravenous antibiotics requiring skilled administration and "
            "renal-dose monitoring, with Infectious Disease yet to finalize duration.",
            "These needs require a skilled level of care. The screen's routine-dressing conclusion does "
            "not account for the undermining, the failed offloading teach-back, the caregiver gap, or the "
            "intravenous antibiotic requirement. Intermittent home health cannot provide the skilled "
            "wound packing and assessment, continuous offloading, and intravenous antibiotic management "
            "this wound and patient require. We request that the plan reverse the 05/23 denial and "
            "authorize skilled nursing facility placement.",
        ]),
        ("sig", "Care Management, 05/24/2026. Ready for submission."),
    ],
)

if __name__ == "__main__":
    for spec in (DELIVERABLE, SCREEN, NURSE, GOLDEN):
        out = W.build_one(spec, outdir=OUT)
        print("  OK", out.name)
    print("done OV07 v2 render ->", OUT)
