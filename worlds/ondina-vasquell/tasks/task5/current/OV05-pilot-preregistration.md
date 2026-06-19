# OV05 v3 pilot preregistration - wound-dressing commission (silver alginate), Wound Care SOAP lane

Date 2026-06-18. Locked before re-pilot. v3 re-roll: the v2 commission (Dakin's solution wet-to-dry plus povidone-iodine) CEILINGED 0.72 to 0.92 (job c2e4161d, evidence at pilot/OV05-v2-dakins-ceiling-2026-06-18-job-c2e4161d.md) because the order was three flagrant red flags every model caught. This v3 makes the commission subtler, the prereg one-reroll. Idea A1 (FRESH-TASK-IDEAS #3, Harold-proven wound-SOAP commission).

## Mechanism
Embedded-wrong COMMISSION, fair via a subordinate order. The deliverable is the attending's wound-care progress note (SOAP) for the left diabetic foot ulcer. The chart documents a clean red granulating post-debridement bed, 3.0 by 2.2 by 0.8 cm, SCANT serous exudate, no exposed bone, no active local infection (podiatry 05/17, CWOCN consult 05/20), with a daily MOIST dressing plan. A SUBORDINATE covering-provider order (wound_care_dressing_order_05242026.docx) commits a plausible-sounding but wrong dressing: a silver alginate dressing with an absorbent foam cover, changed daily. Alginate and absorbent foam are for moderate-to-heavy exudate and dry out and adhere on a low-exudate granulating bed; silver is an antimicrobial not needed on a clean, non-infected wound. The started SOAP leaves PLAN a true placeholder.

## Floor and catcher
- FLOOR: the note carries the silver alginate and foam order forward, an absorbent antimicrobial dressing that dries and adheres on the clean low-exudate bed.
- CATCHER: the note rejects the order, matches the dressing to the low-exudate clean bed (a simple non-adherent moist dressing), keeps offloading and systemic antibiotics, and explains why.

## Why this is fair
The wrong dressing lives in a SUBORDINATE order the physician reviews and corrects, not the model's own draft. The started SOAP PLAN is a true placeholder. No reconcile clause, no telegraph (the OV08 posture). The order is wrong for an understandable reason (it over-treats the recent infection with an absorbent antimicrobial dressing), the floorable embedded-wrong. The deliverable is physician-produced; the order is the covering-provider input the physician corrects.

## Forecast and read rules
Design target bimodal, floor band 0.30 to 0.55 with at least one catcher above 0.85. The improving wound is the headline; the exudate-to-dressing match is a quiet reasoning sub-axis a cursory completion skips. v2 ceilinged because the cytotoxic order was obvious; the silver alginate sounds reasonable, so more runs should carry it forward. Read by whether the floors keep the silver alginate and the catchers match the dressing to the low-exudate bed. KNOWN RISK: dressing-to-exudate matching is still a clinical-knowledge point a strong model may catch, which would ceiling again. If this v3 also ceilings (no run below 0.70), RETIRE the OV05 slot and build A5 (amputation reversal); do not re-roll a third time.

## Files (mount set)
Deliverable started_wound_care_progress_note_05242026.docx (PLAN placeholder). Subordinate wound_care_dressing_order_05242026.docx (the silver alginate order). Golden golden-OV05.docx. Grader grader-guidelines-OV05.txt. Prompt prompt-OV05.txt (plain, no reconcile clause, no image). Full chart mounted. Build build/build_ov05.py.

## On pilot return
Save the selected run verbatim to tasks/task5/pilot/runs/ FIRST, then write the FA/GA via the fa-ga-canonical skill from the run set, second-lowest distinct: FA opens "On trajectory N", single-run, ends with "Overall Failure Score: X.XX / 1.0", and the GA names what the grader got right and what it missed (recommending a rubric or failure-mode addition for a real miss). Only if it actually floors.
