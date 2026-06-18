STATUS 2026-06-17 (v3): OV09 = embedded-wrong carry-forward on the Post-Acute Care Coordination lane (fresh 6th lane). OV08 family, no image. The deliverable is a resident-started transfer handoff that pre-fills a discharge-home disposition with the contingencies marked settled: offloading teach-back completed, the daughter available for daily care, equipment and home-health in place. The chart contradicts all three. Floor = finalize the handoff and carry the home disposition forward. Catcher = cross-check the flowsheet, case management, and family notes, catch the unmet contingencies, and correct the disposition to a skilled nursing facility (or home only after the contingencies are met).

Prior versions retired: v1 (contrast order in AKI) ceilinged, the frozen H&P says "avoid contrast" so the catch was a one-line lookup (job 21e12fc3). v2 (off-text osteomyelitis image) retired before pilot: an inpatient foot film is internal imaging read as text, so a report-as-image is borderline on fairness and the actual film needs a generative render. See OV09-DESIGN-grounding.md.

## Workflow type
Post-Acute Care Coordination Documentation (P1 on the 06/10 snapshot). Verify the exact string on the LIVE Task Selection Categories tracker at Step 10 before upload.

## Studio task setup
- Prompt: prompt-OV09.txt (plain "finish it from her chart so it is ready for my signature"; no reconcile clause).
- Task files to mount: started_post_acute_coordination_note_05242026.docx plus the full OV world chart. No image.
- Golden: golden-OV09.docx. Grader: grader-guidelines-OV09.txt (model grader, 539 words).
- First-trajectory find /docs gate: exactly one started note under filesystem, no stale v1 or v2 deliverable, no radiograph image, no .apps_data duplicate.
- Run 10 trajectories.

## The embedded-wrong element and its refutation (decisive chart files)
- "offloading teach-back completed" / "device in place and tolerated" -> nursing_offloading_flowsheet: not consistently maintained, removed by patient at times, teach-back NOT achieved.
- "daughter available for daily dressing changes and daytime supervision" -> family_communication_note: works nights, cannot be there every day, cannot do daytime dressing changes on workdays.
- "equipment and home-health in place" / "home criteria met" -> case_management_note: offloading device pending, home-health not confirmed, caregiver training incomplete, disposition NOT determined.

## Build
- python3 worlds/ondina-vasquell/phase-3-build-task-artifacts/build/build_ov09.py renders the deliverable and golden into platform/task9/current/ through build_one. No render step, no image.

## Pilot read
- Expect bimodal (OV08 parity). Floors finalize discharge home on the draft's settled contingencies; catchers decline home and correct the disposition. Target floor 0.10-0.40 with a catcher above 0.85. Read by whether the floors carry the home disposition forward and the catchers correct it, not by the mean.
- KNOWN RISK: the caregiver and offloading thread is a visible social-work axis, so a thorough model may catch it and ceiling (the OV08 cold-bench profile). The floor depends on the model satisficing past the embedded "settled" claim rather than cross-checking the flowsheet and family notes. Dyrane is testing by trajectory directly (no cold bench).
- Prereg: OV09-pilot-preregistration.md. Design and the v1/v2 retirements: OV09-DESIGN-grounding.md.
