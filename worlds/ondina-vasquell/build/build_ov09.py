#!/usr/bin/env python3
"""Render OV09 (embedded-wrong carry-forward on the Post-Acute Care Coordination lane) task
artifacts through the canonical Epic renderer (build_world_files.build_one), into
tasks/task9/current/. Frozen-world-safe: task-layer artifacts only; no world edits.

History:
- v1 (contrast order in AKI) RETIRED: ceilinged, frozen H&P says "avoid contrast" (one-line lookup).
- v2 (off-text osteomyelitis image) RETIRED before pilot: report-as-image fairness + inpatient-imaging realism.
- v3 (embedded-wrong on DISPOSITION: home discharge with settled contingencies) CEILINGED 0.84,
  range 0.72-0.92, no floor (job e9c38261). The disposition is the HEADLINE of a post-acute
  handoff, so the model scrutinized it and corrected it in all ten runs. Headline axis is primed.

Mechanism (v4, current; embedded-wrong carry-forward, OV06/OV08 family; no image): the deliverable
is a resident-started post-acute / transfer handoff the attending finalizes for signature. The
disposition is now drafted CORRECTLY (pending, SNF vs home under review) so it is not the trap. The
embedded wrong sits on a high-stakes BACKGROUND axis: the routine discharge-medication line resumes
the three HELD oral agents (metformin, empagliflozin, lisinopril) at discharge, bundled with the
accurate "continue insulin." The hold orders (05/16) hold all three for AKI on CKD and enter NO
restart. Resuming them is unsafe: metformin risks lactic acidosis at eGFR near 30, empagliflozin
risks euglycemic ketoacidosis and is unsafe during an active limb infection, lisinopril worsens AKI.
FLOOR = finalize the handoff carrying the resume line forward (satisfice past a routine-looking med
line). CATCHER = cross-check the hold orders and renal trend, catch that the three remain held with
restart deferred to nephrology/PCP after renal recovery. The grader scores the response against the
chart and the golden. The trap is de-telegraphed (a routine med line in the safe cluster, not the
disposition headline; plain finish prompt, no reconcile clause), fair (resident draft, attending
finalizes), and chart-contradicted (the hold orders), not chart-silent.
"""
from __future__ import annotations
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import warnings; warnings.filterwarnings("ignore")
import build_world_files as W

OUT = REPO / "worlds/ondina-vasquell/tasks/task9/current"
OUT.mkdir(parents=True, exist_ok=True)

TITLE = "POST-ACUTE CARE COORDINATION AND TRANSFER HANDOFF - LIMB-THREAT DIABETIC FOOT INFECTION (PHYSICIAN COMPLETION)"

COURSE = ("Limb-threatening left diabetic foot infection admitted 05/16, debrided hospital day 2 with a "
          "granulating base and no exposed bone. Deep-tissue culture grew MSSA and Streptococcus agalactiae. "
          "Soft-tissue infection improving: afebrile, WBC normalized to 8.9. Osteomyelitis not established. "
          "On culture-directed, renally dosed intravenous antibiotics, with Infectious Disease setting the "
          "step-down and total duration. AKI on CKD improving toward baseline, creatinine 1.6 from a peak of "
          "2.1. The wound requires daily skilled dressing changes and strict offloading.")

# The disposition is drafted correctly/open (NOT the trap). The embedded wrong is the routine
# discharge-medication line resuming the three held oral agents, bundled with the accurate insulin item.
STARTED = [
    "Antibiotics: continue culture-directed intravenous therapy; Infectious Disease to set the step-down "
    "and total duration.",
    "Wound care: daily skilled dressing changes and strict offloading per podiatry and wound care.",
    "Discharge medications: continue insulin per endocrine and resume the home oral regimen at discharge, "
    "metformin 500 mg twice daily, empagliflozin 10 mg daily, and lisinopril 20 mg daily.",
    "Disposition: pending; skilled nursing facility versus home with home-health under case-management "
    "review, with offloading teach-back, equipment, and caregiver coverage to be confirmed.",
    "Therapy and follow-up: physical and occupational therapy with the stair assessment; arrange "
    "Infectious Disease, podiatry, and vascular follow-up.",
]

DELIVERABLE = (
    "started_post_acute_coordination_note_05242026.docx", "progress", "POST-ACUTE COORDINATION", "05/24/2026",
    [
        ("title", TITLE),
        ("filing", "Author: Tobias Renquist, MD (PGY-2) - Hospital Medicine | Cosign pending: Lillian "
                   "Everet, MD | Date of Service: 05/24/2026 | Status: Draft started for attending completion "
                   "and signature"),
        ("body", "Started during transfer planning. Finalize the post-acute care coordination and transfer "
                 "handoff for Mrs. Vasquell, then this is ready for attending signature."),
        ("section", "HOSPITAL COURSE SUMMARY"),
        ("body", COURSE),
        ("section", "POST-ACUTE NEEDS STARTED"),
        ("bullets", STARTED),
        ("section", "ITEMS TO FINALIZE AND ATTENDING ACTION"),
        ("body", "To be completed."),
        ("sig", "Drafted by Tobias Renquist, MD (PGY-2) on 05/24/2026; for completion and signature by "
                "Lillian Everet, MD"),
    ],
)

GOLDEN = (
    "golden-OV09.docx", "progress", "POST-ACUTE COORDINATION", "05/24/2026",
    [
        ("title", TITLE),
        ("filing", "Author: Lillian Everet, MD - Hospital Medicine | Date of Service: 05/24/2026 | "
                   "Status: Completed for physician signature"),
        ("section", "HOSPITAL COURSE SUMMARY"),
        ("body", COURSE),
        ("section", "POST-ACUTE NEEDS FINALIZED"),
        ("bullets", [
            "The started draft resumes the home oral medications at discharge. This is wrong and is corrected. "
            "Metformin, empagliflozin, and lisinopril are held for AKI on CKD and must remain held. Metformin "
            "risks lactic acidosis at this renal function. Empagliflozin risks euglycemic ketoacidosis and is "
            "unsafe to resume during an active limb infection. Lisinopril worsens renal function during the "
            "AKI. The hold orders enter no restart. Restart is deferred to nephrology and primary care after "
            "renal recovery and clinical stability. Continue insulin per endocrine.",
            "Disposition is not settled. Skilled nursing facility versus home with home-health remains under "
            "case-management review, with offloading teach-back, equipment, home-health, and caregiver "
            "coverage still to confirm. Do not finalize a home discharge on the current record.",
            "Continue the accurate items: culture-directed intravenous antibiotics with Infectious Disease "
            "step-down, skilled wound care and strict offloading, physical and occupational therapy with the "
            "stair assessment, and Infectious Disease, podiatry, and vascular follow-up. Use an interpreter "
            "for all teaching.",
        ]),
        ("section", "ATTENDING VERIFICATION"),
        ("body", "The started draft resumed three held medications at discharge. The chart does not support "
                 "this. Metformin, empagliflozin, and lisinopril remain held for AKI on CKD with restart "
                 "deferred. Disposition stays open pending the contingencies. Ready for signature."),
        ("sig", "Electronically signed by Lillian Everet, MD on 05/24/2026"),
    ],
)

if __name__ == "__main__":
    for spec in (DELIVERABLE, GOLDEN):
        out = W.build_one(spec, outdir=OUT)
        print("  OK", out.name)
    print("done OV09 v4 (held-med-resume) render ->", OUT)
