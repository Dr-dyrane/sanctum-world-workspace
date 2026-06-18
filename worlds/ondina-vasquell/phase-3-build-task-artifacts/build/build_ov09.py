#!/usr/bin/env python3
"""Render OV09 (embedded-wrong carry-forward on the Post-Acute Care Coordination lane) task
artifacts through the canonical Epic renderer (build_world_files.build_one), into
platform/task9/current/. Frozen-world-safe: task-layer artifacts only; no world edits.

History:
- v1 (contrast commission) RETIRED: ceilinged all-catch, the frozen H&P says "avoid contrast" so the
  catch was a one-line lookup (results/OV09-v1-pilot-2026-06-17-job-21e12fc3.md).
- v2 (off-text osteomyelitis image) RETIRED before pilot: an inpatient foot film is internal imaging
  read as text, so a report-as-image is borderline on fairness, and the actual film needs a
  generative render. The off-text-image render method itself is sound and is preserved as the
  reference in build/render_ov09_image.py; OV09 no longer uses it.

Mechanism (embedded-wrong carry-forward, OV08 family; no image): the deliverable is a post-acute
care coordination / transfer handoff started by a resident, to be finalized for attending signature.
The started draft PRE-FILLS a discharge-home disposition with the offloading teach-back, caregiver
coverage, and equipment marked as settled. The chart contradicts all of it:
  - nursing offloading flowsheet 05/21: offloading not consistently maintained, device removed by the
    patient at times, teach-back NOT achieved;
  - case management 05/20: offloading device pending, home-health not yet confirmed, caregiver
    training incomplete, disposition NOT determined;
  - family communication 05/20: the daughter works nights and cannot provide daytime dressing changes
    or daily supervision, cannot be there every day.
FLOOR = finalize the handoff and carry the home disposition forward (satisfice past the embedded
reassurance). CATCHER = cross-check the flowsheet, case management, and family notes, catch the
unmet contingencies, and correct the disposition to a skilled nursing facility, or home only after
offloading teach-back is achieved and the device, home-health, and caregiver schedule are confirmed.
The grader scores the response text against the chart and the golden.
"""
from __future__ import annotations
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import warnings; warnings.filterwarnings("ignore")
import build_world_files as W

OUT = REPO / "worlds/ondina-vasquell/phase-3-build-task-artifacts/platform/task9/current"
OUT.mkdir(parents=True, exist_ok=True)

TITLE = "POST-ACUTE CARE COORDINATION AND TRANSFER HANDOFF - LIMB-THREAT DIABETIC FOOT INFECTION (PHYSICIAN COMPLETION)"

COURSE = ("Limb-threatening left diabetic foot infection admitted 05/16, debrided hospital day 2 with a "
          "granulating base and no exposed bone. Deep-tissue culture grew MSSA and Streptococcus agalactiae. "
          "Soft-tissue infection improving: afebrile, WBC normalized to 8.9. Osteomyelitis not established. "
          "On culture-directed, renally dosed intravenous antibiotics, with Infectious Disease setting the "
          "step-down and total duration. AKI on CKD improving toward baseline. The wound requires daily "
          "skilled dressing changes and strict offloading.")

# The discharge-home disposition and its three contingencies are pre-filled as settled. Each contradicts
# the chart: teach-back not achieved, device pending, the daughter cannot cover daily care.
STARTED = [
    "Antibiotics: continue culture-directed intravenous therapy; Infectious Disease to set the step-down "
    "and total duration.",
    "Wound care: daily skilled dressing changes; offloading device in place and tolerated, offloading "
    "teach-back completed with the patient.",
    "Caregiver support: the daughter is available to provide daily dressing changes and daytime "
    "supervision at home.",
    "Disposition: discharge home with home-health nursing; home-based wound care criteria are met.",
    "Therapy: physical and occupational therapy to complete the stair assessment before discharge.",
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
            "Disposition cannot be finalized as home, and the started draft is wrong on this point. The "
            "record does not support home-based wound care now. Offloading teach-back was not achieved, the "
            "offloading device is still pending, and the daughter works night shifts and cannot provide "
            "daytime dressing changes or daily supervision. Case management left disposition undetermined.",
            "Offloading is not established. The nursing flowsheet documents that offloading was not "
            "consistently maintained and the device was removed by the patient at times, with teach-back "
            "not achieved. A plantar forefoot wound does not heal without consistent offloading. Offloading "
            "must be demonstrated, with interpreter-supported teach-back, before any home plan.",
            "The supported disposition is a skilled nursing facility for daily wound care, offloading "
            "supervision, and continued therapy. Home with home-health is acceptable only after offloading "
            "teach-back is achieved, the device and home-health wound nursing are confirmed, and a "
            "caregiver schedule covers daily dressing changes.",
            "Continue the accurate items: culture-directed intravenous antibiotics with Infectious Disease "
            "step-down, skilled wound care, physical and occupational therapy with the stair assessment, and "
            "renal-dosed management. Use an interpreter for all teaching.",
        ]),
        ("section", "ATTENDING VERIFICATION"),
        ("body", "The started draft marked offloading teach-back, caregiver availability, and disposition as "
                 "settled. The chart does not support this. Disposition is corrected to a skilled nursing "
                 "facility, or home only after the offloading and caregiver contingencies are met. Ready for "
                 "signature."),
        ("sig", "Electronically signed by Lillian Everet, MD on 05/24/2026"),
    ],
)

if __name__ == "__main__":
    for spec in (DELIVERABLE, GOLDEN):
        out = W.build_one(spec, outdir=OUT)
        print("  OK", out.name)
    print("done OV09 embedded-wrong render ->", OUT)
