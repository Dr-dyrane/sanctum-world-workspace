STATUS 2026-06-18 (v2, redesign after Larry send-back): OV07 = embedded-wrong CLOSURE on the Claims Denial / Appeal Preparation lane, the proven OV08/OV10/OV11 engine. The AI wound photo is removed. The deliverable is an appeal of a skilled nursing facility level-of-care denial. A subordinate transfer-day home health suitability screen wrongly closes the wound as routine and concludes home health is adequate, no skilled need. Floor = the appeal adopts that closure and argues from routine dressings (rebuttable); catcher = it rejects the closure and builds the skilled-need case on the documented undermining, offloading failure, caregiver gap, and intravenous antibiotics. Design rationale: design/OV07-v2-docx-redesign-DESIGN.md; prereg: OV07-pilot-preregistration.md.

## Workflow type
Claims Denial Analysis and Appeal Preparation. Verify the exact string on the LIVE Task Selection Categories sheet at Step 10 before upload.

## Studio task setup
- Prompt: prompt-OV07.txt (plain "finish it from her chart so I can submit it"; no reconcile clause, no image).
- Task files to mount: started_appeal_letter_05242026.docx, home_health_suitability_screen_05242026.docx, transfer_day_nursing_note_05242026.docx, plus the full OV world chart. NO image.
- Golden: golden-OV07-v2.docx. Grader: grader-guidelines-OV07.txt (model grader).
- First-trajectory find /docs gate: exactly one started appeal, one home health suitability screen, and one transfer-day nursing note under /docs/filesystem; NO wound_photo_05242026.jpg task file; no stale golden-OV07-v1; no .apps_data duplicate. The world substrate photo wound_photo_05202026.jpg (05/20, granulating, no finding) stays; it is a world file.
- Run 10 trajectories.

## Build / regen
- python3 worlds/ondina-vasquell/build/build_ov07.py renders the started appeal, the home health suitability screen, the transfer-day wound note, and golden-OV07-v2 into tasks/task7/current/.
- The v1 image, wound-photo-image-spec.md, and golden-OV07-v1 are archived at archive/2026-06-18-v1-image-retired/.

## Pilot read
- Expect bimodal: floors adopt the screen's routine-dressing closure, catchers reject it and build skilled need. Target floor band 0.30 to 0.55 with a catcher above 0.85.
- KNOWN RISK: the appeal genre may prime the model to reject a home-health-adequate framing on its own, which would ceiling. If all-catch, one re-roll with the closure on a quieter axis, then retire per the one-reroll rule. If all-floor, confirm reachability (golden self-score) before banking.

## On re-pilot return
Save the selected run verbatim to tasks/task7/pilot/runs/ FIRST, then redo the FA/GA via the fa-ga-canonical skill from the new run set (second-lowest distinct), to current guidance.
