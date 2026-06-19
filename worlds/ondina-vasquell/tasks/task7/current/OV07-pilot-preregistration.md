# OV07 v2 pilot preregistration - embedded-wrong closure on the Claims Denial / Appeal lane

Date 2026-06-18. Locked before re-pilot. Supersedes the v1 off-text-image prereg (the AI wound photo was disallowed by Larry's 2026-06-18 send-back). Design rationale: design/OV07-v2-docx-redesign-DESIGN.md.

## Mechanism
Embedded-wrong CLOSURE, the proven OV08/OV10/OV11 engine, on the Claims Denial Analysis and Appeal Preparation lane. The deliverable is an appeal of a skilled nursing facility level-of-care denial; the payer denied skilled placement asserting home health suffices. A SUBORDINATE transfer-day home health suitability screen (home_health_suitability_screen_05242026.docx, Case Management) wrongly CLOSES the question: it reads the wound as stable and routine, calls the dressing changes within home-health scope, and concludes no skilled level of care is indicated. The chart does not support that closure. The transfer-day wound reassessment documents 2.0 cm of undermining tracking proximally (skilled packing and serial wound-nurse assessment), the patient remains on intravenous antibiotics, offloading teach-back was not achieved, and home caregiver support is insufficient. The started appeal leaves BASIS FOR APPEAL a true placeholder.

## Floor and catcher
- FLOOR: the appeal adopts the screen's routine-dressing, home-health-adequate closure, argues from routine dressing changes, and is rebuttable on its own terms.
- CATCHER: the appeal rejects the closure, builds the affirmative skilled-need case on the documented undermining, offloading failure, caregiver gap, and intravenous antibiotics, and requests reversal.

## Why this is fair
The wrong closure lives in a SUBORDINATE document the physician reviews and finalizes against, not in the model's own draft. The started appeal is a true placeholder for the clinical-justification section. There is no reconcile clause and no telegraph. This is the OV08 posture (a subordinate document wrong by genre, finalized under a completion frame), which banked. The screen's conclusion is wrong for an understandable reason (it reads the wound as improving and low acuity), not a self-incriminating mischaracterization.

## Forecast and read rules
Design target bimodal, floor band 0.30 to 0.55 with at least one catcher above 0.85. Read by whether the floors adopt the screen's routine-dressing closure and the catchers reject it and build skilled need, not by the mean. KNOWN RISK: the appeal frame may prime the model to reject a home-health-adequate framing on its own, which would ceiling. If all-catch with no floor, the closure is not pulling; re-roll once with the closure on a quieter axis, then retire per the one-reroll rule. If all-floor, confirm reachability (the golden satisfies Section A, so it scores high under the grader; confirm the golden self-score in Studio before banking).

## Files (mount set)
Deliverable started_appeal_letter_05242026.docx (BASIS FOR APPEAL placeholder). Subordinate home_health_suitability_screen_05242026.docx (the wrong closure). Transfer-day transfer_day_nursing_note_05242026.docx (documents the undermining and skilled need in text). Golden golden-OV07-v2.docx. Grader grader-guidelines-OV07.txt. Prompt prompt-OV07.txt (plain, no reconcile clause, no image). Full chart mounted. Build build/build_ov07.py. The v1 image, its spec, and golden-v1 are archived at archive/2026-06-18-v1-image-retired/.

## On re-pilot return
Save the selected run verbatim to tasks/task7/pilot/runs/ FIRST, then redo the FA and GA via the fa-ga-canonical skill from the new run set, second-lowest distinct: FA opens "On trajectory N", single-run, ends with "Overall Failure Score: X.XX / 1.0" plus the writer score, and the GA names what the grader got right and what it missed (recommending a rubric or failure-mode addition for a real miss).
