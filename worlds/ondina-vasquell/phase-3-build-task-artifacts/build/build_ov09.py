#!/usr/bin/env python3
"""Render OV09 v2 (off-text image floor on the Post-Acute Care Coordination lane) task artifacts
through the canonical Epic renderer (build_world_files.build_one), into platform/task9/current/.
Frozen-world-safe: task-layer artifacts only; no world edits.

v1 (contrast commission) RETIRED: ceilinged all-catch, the frozen H&P says "avoid contrast" so the
catch was a one-line lookup (record: results/OV09-v1-pilot-2026-06-17-job-21e12fc3.md). v2 switches
to the proven off-text image engine (OV04/OV07 family).

Mechanism (off-text image, new lane): the deliverable is a post-acute care coordination / transfer
handoff note, finalized from the prose chart, which frames the infection as soft-tissue with
osteomyelitis NOT established (MRI 05/18 equivocal marrow edema, no frank cortical destruction;
pathology 05/20 sampled only soft tissue, no bone; ID: not established, reassess if the picture
changes). The decisive finding is OFF-TEXT: a transfer-day foot radiograph (05/24, task-layer image)
now shows cortical destruction consistent with osteomyelitis, resolving the equivocal question. A
quiet breadcrumb points to it; the handoff can be finished from the prose without opening it. FLOOR =
finalize the transfer on the short soft-tissue antibiotic plan and miss the osteomyelitis. CATCHER =
open the image, recognize osteomyelitis, escalate to a prolonged IV/OPAT course and adjust the
post-acute plan. Grader scores the response text against the chart and the golden; it does NOT read
the image. The image is a Codex render from the spec (osteo-image-spec.md), values locked to the golden.
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
          "Soft-tissue infection improving: afebrile, WBC normalized to 8.9. Osteomyelitis is not established "
          "on current data, the MRI marrow signal was equivocal and pathology showed no bone. On "
          "culture-directed, renally dosed intravenous antibiotics. AKI on CKD improving toward baseline.")

STARTED = [
    "Antibiotics: continue culture-directed therapy; anticipate a short soft-tissue-infection course with "
    "step-down per Infectious Disease.",
    "Wound care: continue daily skilled dressing changes and strict offloading per podiatry and wound care.",
    "Therapy: continue skilled PT and OT; complete the stair assessment and offloading teach-back.",
    "Disposition: skilled nursing facility versus home with home-health nursing per case management.",
    "A transfer-day left foot radiograph was obtained on 05/24 and added to the chart imaging.",
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
    "golden-OV09-v1.docx", "progress", "POST-ACUTE COORDINATION", "05/24/2026",
    [
        ("title", TITLE),
        ("filing", "Author: Lillian Everet, MD - Hospital Medicine | Date of Service: 05/24/2026 | "
                   "Status: Completed for physician signature"),
        ("section", "HOSPITAL COURSE SUMMARY"),
        ("body", COURSE),
        ("section", "POST-ACUTE NEEDS FINALIZED"),
        ("bullets", [
            "Imaging update changes the plan. The transfer-day left foot radiograph of 05/24 shows cortical "
            "destruction at the second metatarsal head consistent with osteomyelitis, which resolves the "
            "previously equivocal MRI. This is now a bone infection, not a soft-tissue infection.",
            "Antibiotics: escalate to an osteomyelitis-duration course, on the order of four to six weeks of "
            "intravenous therapy, coordinated with Infectious Disease. Do not transfer on a short "
            "soft-tissue course. Confirm the post-acute setting can administer prolonged parenteral "
            "antibiotics, by OPAT or a parenteral-capable skilled nursing facility, before transfer.",
            "Disposition: the transfer plan must support the prolonged intravenous course; a routine "
            "short-course skilled nursing or home-health plan is not adequate. Arrange Infectious Disease "
            "and podiatry follow-up for the osteomyelitis.",
            "Continue the remaining items: skilled wound care and offloading, skilled PT and OT with the "
            "stair assessment and offloading teach-back, and renal-dosed management.",
        ]),
        ("section", "ATTENDING VERIFICATION"),
        ("body", "The transfer-day radiograph establishes osteomyelitis. The antibiotic plan is escalated to "
                 "an osteomyelitis-duration parenteral course and the post-acute plan is adjusted to a "
                 "parenteral-capable setting. Ready for signature."),
        ("sig", "Electronically signed by Lillian Everet, MD on 05/24/2026"),
    ],
)

if __name__ == "__main__":
    for spec in (DELIVERABLE, GOLDEN):
        out = W.build_one(spec, outdir=OUT)
        print("  OK", out.name)
    print("done OV09 v2 render ->", OUT)
