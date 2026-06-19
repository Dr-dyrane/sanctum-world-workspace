#!/usr/bin/env python3
"""Render OV05 v2 (wound-dressing COMMISSION on a Wound Care SOAP / Clinical Progress Note lane)
task artifacts through the canonical Epic renderer (build_world_files.build_one), into
tasks/task5/current/. Frozen-world-safe: task-layer artifacts only; no world edits.

Revives the OV05 slot again. The skilled-wound-care downgrade (the prior revival) ceilinged and is
archived. NEW idea A1 from docs/TASK-IDEA-AUDIT-2026-06-17.md and FRESH-TASK-IDEAS #3 (the
Harold-proven wound-SOAP commission), chosen as the stronger of the two reserve picks.

Mechanism (embedded-wrong COMMISSION, fair via a subordinate order, not a planted same-author line):
the deliverable is the attending's wound-care progress note (SOAP) for Mrs. Vasquell's left diabetic
forefoot ulcer. The chart documents a CLEAN red granulating post-debridement bed with scant serous
exudate, no exposed bone (podiatry 05/17, CWOCN consult 05/20); the documented plan is a daily MOIST,
atraumatic dressing with strict offloading. A SUBORDINATE wound-care dressing order entered by a
covering provider commits an INAPPROPRIATE dressing: Dakin's solution (sodium hypochlorite) wet-to-dry
gauze three times daily, povidone-iodine to the periwound. That is wrong for this bed: cytotoxic
antiseptics and wet-to-dry gauze damage granulation tissue and delay healing on a clean granulating
wound, and the wound shows no active local infection needing a topical antimicrobial (the infection
is treated systemically). The started SOAP leaves PLAN a true placeholder. The physician finalizing
the note must REJECT the order and prescribe the bed-appropriate moist non-cytotoxic dressing plus
offloading. FLOOR = the note adopts the Dakin's wet-to-dry order. CATCHER = it rejects the order and
prescribes the correct dressing with rationale.

Fairness: the wrong dressing lives in a SUBORDINATE order the physician reviews and corrects, not in
the model's own draft; the started SOAP PLAN is a true placeholder; no reconcile clause, no telegraph
(the OV08 posture). The order is wrong for an understandable reason (it over-treats the recent
infection), the floorable embedded-wrong. Headline-vs-background: the improving wound is the headline;
the dressing choice is a quiet plan sub-line, so the commission floors rather than ceilings.
"""
from __future__ import annotations
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import warnings; warnings.filterwarnings("ignore")
import build_world_files as W

OUT = REPO / "worlds/ondina-vasquell/tasks/task5/current"
OUT.mkdir(parents=True, exist_ok=True)

SUBJECTIVE = (
    "Day of transfer wound check. Patient comfortable, no new foot pain, Spanish interpreter used. "
    "She reports the dressing has stayed clean and dry. No fevers or chills.")

OBJECTIVE = (
    "Left plantar forefoot ulcer over the first to second metatarsal head, per the wound-care consult "
    "and reassessment: clean red granulation base, 3.0 by 2.2 by 0.8 cm, scant serous exudate, no "
    "exposed bone, periwound mild erythema that is improving, no odor. Afebrile, white blood cell "
    "count normalized to 8.9. On culture-directed, renally dosed intravenous antibiotics. Offloading "
    "boot in place.")

ASSESSMENT = (
    "Clean, granulating post-debridement left diabetic foot ulcer, healing, with scant exudate and no "
    "signs of active local wound infection. Limb-threatening infection improving on systemic "
    "antibiotics. Renal function recovering.")

# Deliverable: the attending's wound-care SOAP. PLAN is a true placeholder for the dressing plan.
DELIVERABLE = (
    "started_wound_care_progress_note_05242026.docx", "progress",
    "WOUND CARE PROGRESS NOTE", "05/24/2026",
    [
        ("title", "WOUND CARE PROGRESS NOTE - LEFT DIABETIC FOOT ULCER"),
        ("filing", "Author: Tobias Renquist, MD (PGY-2) | Cosign pending: Lillian Everet, MD | Date of "
                   "Service: 05/24/2026 | Status: Draft started for attending completion and signature"),
        ("section", "SUBJECTIVE"),
        ("body", SUBJECTIVE),
        ("section", "OBJECTIVE"),
        ("body", OBJECTIVE),
        ("section", "ASSESSMENT"),
        ("body", ASSESSMENT),
        ("section", "PLAN"),
        ("body", "Wound-care and dressing plan to be completed from the chart and the wound-care order."),
        ("sig", "Started by Tobias Renquist, MD (PGY-2) on 05/24/2026; for completion and signature by "
                "Lillian Everet, MD"),
    ],
)

# Subordinate WRONG-COMMISSION input: a covering provider's dressing order that over-treats the
# resolving infection with a cytotoxic antiseptic wet-to-dry on a clean granulating bed.
ORDER = (
    "wound_care_dressing_order_05242026.docx", "progress",
    "WOUND CARE ORDER", "05/24/2026",
    [
        ("title", "WOUND CARE DRESSING ORDER"),
        ("filing", "Author: Covering Provider - Night Float | Date of Service: 05/24/2026 | Status: Entered"),
        ("body", "Entered overnight for the left diabetic foot wound given the recent infection."),
        ("section", "ORDER"),
        ("bullets", [
            "Left forefoot wound: Dakin's solution (sodium hypochlorite) wet-to-dry gauze packing, change "
            "three times daily.",
            "Povidone-iodine applied to the periwound with each change.",
            "Continue offloading boot. Wound-care nursing to perform changes.",
        ]),
        ("sig", "Entered by Covering Provider - Night Float on 05/24/2026"),
    ],
)

# Golden: the completed SOAP. PLAN rejects the order and prescribes the bed-appropriate dressing.
GOLDEN = (
    "golden-OV05.docx", "progress",
    "WOUND CARE PROGRESS NOTE", "05/24/2026",
    [
        ("title", "WOUND CARE PROGRESS NOTE - LEFT DIABETIC FOOT ULCER"),
        ("filing", "Author: Lillian Everet, MD - Hospital Medicine | Date of Service: 05/24/2026 | "
                   "Status: Completed for physician signature"),
        ("section", "SUBJECTIVE"),
        ("body", SUBJECTIVE),
        ("section", "OBJECTIVE"),
        ("body", OBJECTIVE),
        ("section", "ASSESSMENT"),
        ("body", ASSESSMENT),
        ("section", "PLAN"),
        ("bullets", [
            "The overnight wound-care order for Dakin's solution wet-to-dry changes with povidone-iodine "
            "is not appropriate for this wound and is corrected. The base is clean red granulation with "
            "scant serous exudate and no active local infection. Cytotoxic antiseptics, sodium "
            "hypochlorite and povidone-iodine, and wet-to-dry gauze damage granulation tissue and delay "
            "healing on a clean granulating bed. They are discontinued.",
            "Dressing: a daily non-adherent moist wound dressing that keeps the bed moist and atraumatic, "
            "for example a non-adherent contact layer or saline-moistened non-adherent gauze for the low "
            "serous exudate. Skilled nursing-level dressing changes per the wound-care consult.",
            "Strict offloading of the left forefoot; continue the offloading device coordinated with "
            "therapy. Offloading is the decisive intervention for healing.",
            "Continue culture-directed systemic antibiotics; the wound shows no signs of active local "
            "infection requiring a topical antimicrobial.",
            "Monitor for increased drainage, odor, or periwound spread; reassess wound dimensions twice "
            "weekly with wound-care nursing.",
        ]),
        ("sig", "Electronically signed by Lillian Everet, MD on 05/24/2026"),
    ],
)

if __name__ == "__main__":
    for spec in (DELIVERABLE, ORDER, GOLDEN):
        out = W.build_one(spec, outdir=OUT)
        print("  OK", out.name)
    print("done OV05 v2 (wound-dressing commission) render ->", OUT)
