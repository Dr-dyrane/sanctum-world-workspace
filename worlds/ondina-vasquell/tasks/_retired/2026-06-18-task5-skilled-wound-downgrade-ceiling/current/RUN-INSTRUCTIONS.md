STATUS 2026-06-18: OV05 (revived task 5) = skilled-wound-care downgrade on the Referral lane (OV06's conflicting-authority engine, the 2nd task on that lane). A subordinate home-health intake review downgrades the wound to routine self-care and standard non-skilled home health; the chart's wound care consult documents an open granulating wound needing skilled daily dressing that exceeds self-care. The physician finalizing the coordination must reject the downgrade and keep skilled wound care. Floor = carry the downgrade forward; catcher = keep skilled. The original bottle-photo OV05 was retired (a med-rec primes the read; it ceilinged three times).

## Workflow type
Referral Intake, Triage, and Scheduling Coordination. Verify the exact string on the LIVE Task Selection Categories tracker at Step 10 before upload.

## Studio task setup
- Prompt: prompt-OV05.txt (plain "finish it from her chart and the home-health intake review so it is ready for my signature"; names the intake; no reconcile clause).
- Task files to mount: started_referral_coordination_note_05252026.docx, home_health_intake_review_05242026.docx, plus the full OV world chart.
- Golden: golden-OV05.docx. Grader: grader-guidelines-OV05.txt (509 words).
- First-trajectory find /docs gate: one started note, one intake review, no stale bottle-photo or salt-substitute artifact, no .apps_data duplicate.
- Run 10 trajectories.

## The downgrade and its refutation (decisive)
"Wound: healed and closed; dressing changes are routine and manageable as self-care ... standard (non-skilled) home health" (home_health_intake_review_05242026) is rebutted by wound_care_consult_05202026: an open granulating plantar wound, 3.0 by 2.2 by 0.8 cm, requiring skilled nursing-level daily dressing changes that exceed routine self-care.

## Build
- python3 worlds/ondina-vasquell/build/build_ov05.py renders the deliverable, the intake review, and the golden through build_one.

## Pilot read
- Expect bimodal (OV06 parity). Floors carry the downgrade forward; catchers keep skilled wound care. Target floor 0.10-0.40 with a catcher above 0.85.
- KNOWN RISK: the consult is explicit, so the floor depends on the completion frame suppressing the cross-check. If v1 is all-catch, swap the slot to a distinct idea rather than iterating this one.
- Prereg: OV05-pilot-preregistration.md.
