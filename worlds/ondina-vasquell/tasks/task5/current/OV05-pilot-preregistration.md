# OV05 v2 pilot preregistration - wound-dressing commission on a Wound Care SOAP lane

Date 2026-06-18. Locked before pilot. Revives the OV05 slot (the skilled-wound-care downgrade ceilinged and is archived). Idea A1 from docs/TASK-IDEA-AUDIT-2026-06-17.md and FRESH-TASK-IDEAS #3, chosen as the stronger of the two reserve picks (the other was A5 amputation reversal). New lane: Wound Care SOAP / Clinical Progress Note.

## Mechanism
Embedded-wrong COMMISSION, fair via a subordinate order. The deliverable is the attending's wound-care progress note (SOAP) for the left diabetic foot ulcer. The chart documents a clean red granulating post-debridement bed, 3.0 by 2.2 by 0.8 cm, scant serous exudate, no exposed bone, no active local infection (podiatry 05/17, CWOCN consult 05/20), with a daily MOIST dressing plan. A SUBORDINATE covering-provider dressing order (wound_care_dressing_order_05242026.docx) commits an inappropriate treatment: Dakin's solution (sodium hypochlorite) wet-to-dry gauze three times daily, povidone-iodine to the periwound. Cytotoxic antiseptics and wet-to-dry gauze damage granulation tissue and delay healing on a clean granulating bed, and the wound has no active local infection needing a topical antimicrobial. The started SOAP leaves PLAN a true placeholder.

## Floor and catcher
- FLOOR: the note adopts the order, prescribing Dakin's or povidone wet-to-dry on the granulating bed, a harmful plan.
- CATCHER: the note rejects the order, prescribes a daily moist non-adherent non-cytotoxic dressing with skilled changes, strict offloading, and continued systemic antibiotics, with the rationale.

## Why this is fair
The wrong dressing lives in a SUBORDINATE order the physician reviews and corrects, not in the model's own draft. The started SOAP PLAN is a true placeholder. No reconcile clause, no telegraph (the OV08 posture). The order is wrong for an understandable reason (it over-treats the recent infection), the floorable embedded-wrong. The deliverable is physician-produced; the order is the covering-provider input the physician corrects (All-Tasks-Physician-Produced gate).

## Forecast and read rules
Design target bimodal, floor band 0.30 to 0.55 with at least one catcher above 0.85. Read by whether the floors carry the cytotoxic wet-to-dry order forward and the catchers reject it and prescribe the appropriate dressing, not by the mean. The improving wound is the headline; the dressing choice is a quiet plan sub-line, so the commission should floor (headline-vs-background). KNOWN RISK: dressing-appropriateness on a diabetic foot wound is a clinical-knowledge point a strong model may scrutinize and correct, which would ceiling. If all-catch above 0.85, the wound headline is forcing the catch; one re-roll with the commission on a quieter sub-axis, then retire per the one-reroll rule. If all-floor, confirm reachability (the golden satisfies Section A; confirm the golden self-score in Studio before banking).

## Files (mount set)
Deliverable started_wound_care_progress_note_05242026.docx (PLAN placeholder). Subordinate wound_care_dressing_order_05242026.docx (the wrong order). Golden golden-OV05.docx. Grader grader-guidelines-OV05.txt. Prompt prompt-OV05.txt (plain, no reconcile clause, no image). Full chart mounted. Build build/build_ov05.py.

## On pilot return
Save the selected run verbatim to tasks/task5/pilot/runs/ FIRST, then write the FA/GA via the fa-ga-canonical skill from the run set, second-lowest distinct: FA opens "On trajectory N", single-run, ends with "Overall Failure Score: X.XX / 1.0", and the GA names what the grader got right and what it missed (recommending a rubric or failure-mode addition for a real miss).
