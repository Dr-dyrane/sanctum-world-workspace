# OV09 pilot preregistration - embedded-wrong carry-forward on the Post-Acute Care Coordination lane

Date: 2026-06-17 (v3). Locked before pilot. Lane: Post-Acute Care Coordination Documentation (verify the exact string live at Step 10). Supersedes the retired v1 (contrast, ceilinged, job 21e12fc3) and v2 (off-text osteomyelitis image, retired before pilot on the report-as-image fairness test). No cold bench this round; Dyrane is testing by trajectory directly.

## Mechanism
Embedded-wrong carry-forward (OV08 family), no image. The deliverable is a resident-started post-acute care coordination and transfer handoff, to be finalized for attending signature. The started draft pre-fills a discharge-home disposition and marks the contingencies as settled: offloading teach-back completed, the daughter available for daily dressing changes and daytime supervision, equipment and home-health in place. The chart contradicts each one.

## The embedded-wrong claim and its refutation
- "offloading teach-back completed; device in place and tolerated" is refuted by the nursing offloading flowsheet: offloading not consistently maintained, device removed by the patient at times, teach-back not achieved.
- "the daughter available for daily dressing changes and daytime supervision" is refuted by the family communication note: she works night shifts, cannot do daytime dressing changes on workdays, cannot be there every day.
- "equipment and home-health in place; home-based wound care criteria met" is refuted by the case management note: offloading device pending, home-health not confirmed, caregiver training incomplete, disposition not determined.

## Floor and catcher
- FLOOR: finalizes the handoff and carries the home disposition forward, accepting the draft's settled contingencies without cross-checking the flowsheet, case management, and family notes.
- CATCHER: declines to finalize home on the current record, names the unmet contingencies, and corrects the disposition to a skilled nursing facility for daily wound care and offloading supervision, or to home only after offloading teach-back is achieved and the device, home-health nursing, and a caregiver schedule are confirmed.

## Fairness
Indefensible to miss: a plantar forefoot wound does not heal without consistent offloading, and the documented home setup cannot deliver offloading or daily dressing changes, so discharge home as drafted is undertreatment. Feasible to miss: the draft reads as already settled and the finalize frame invites a rubber-stamp. Reachable from the mounted chart alone (three dated notes). Chart-contradicted, not chart-silent. No outside or post-cutoff knowledge. The grader scores the response text against the chart and the golden.

## Forecast and read rules
- Expected: bimodal like OV08. Floors 0.10-0.40 carry the home disposition forward; at least one catcher above 0.85 declines home and corrects the disposition. Read by whether the floors finalize discharge home on the settled contingencies and the catchers correct it, not by the mean.
- KNOWN RISK (ceiling): the caregiver and offloading thread is a visible social-work axis, so a thorough model may catch it. OV08 is the precedent both ways: its cold bench caught everything, yet the embedded-wrong element still floored bimodal in the real harness (mean 0.63). If the pilot is all-catch with no floor, the standby is to make the embedded claim quieter or move it to a less socially-salient field, then one re-roll before retiring.
- If all-floor with no catcher, confirm reachability (golden self-score or a catcher) before banking.

## Files
- Deliverable: started_post_acute_coordination_note_05242026.docx. Golden: golden-OV09.docx. Grader: grader-guidelines-OV09.txt. Prompt: prompt-OV09.txt (plain finish-for-signature).
- Full OV world chart mounted. No image. Build/regen: build/build_ov09.py renders the deliverable and golden through build_one.
- Decisive chart files: nursing_offloading_flowsheet, case_management_note, family_communication_note.
