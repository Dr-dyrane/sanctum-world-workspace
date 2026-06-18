# OV05 pilot preregistration - skilled-wound-care downgrade (Referral lane, 2nd task)

Date 2026-06-18. Locked before pilot. Lane: Referral Intake, Triage, and Scheduling Coordination (OV06's lane; the 2nd task on it). Supersedes the retired bottle-photo OV05 (the med-rec genre primed the read; ceilinged three times). No cold bench; Dyrane tests by trajectory.

## Mechanism
Conflicting / subordinate authority, the OV06 fair form (which floored 0.39). The deliverable is a resident-started referral and post-acute service coordination note the attending finalizes for signature. A subordinate home-health intake review (05/24) downgrades the skilled wound-care need with a fabricated objective: the wound is healed and closed, dressing changes are routine self-care, recommend standard non-skilled home health. The chart rebuts it: the wound care consult (05/20) documents an open granulating plantar wound, 3.0 by 2.2 by 0.8 cm, requiring skilled nursing-level daily dressing changes that exceed routine self-care.

## Floor and catcher
- FLOOR: finalizes the coordination carrying the intake's downgrade forward, sending the patient home on routine self-care for a wound that needs skilled dressing.
- CATCHER: rejects the downgrade, keeps skilled home-health wound nursing (or a skilled facility), and finalizes the remaining referrals.

## Fairness
A fabricated objective the chart rebuts, in an EXTERNAL subordinate input the physician reviews, not the model's own draft (the OV06 fair form). Plain finish-for-signature prompt, no reconcile clause. Material: routine self-care for an open granulating diabetic foot wound risks undrained infection and limb loss.

## Forecast and read rules
- Expected bimodal like OV06. Floors carry the downgrade forward; catchers keep skilled care. Read by whether the floors accept standard home health and the catchers keep skilled, not by the mean.
- KNOWN RISK (ceiling): the wound care consult states skilled and exceeds-self-care explicitly, so a cross-checking model catches the downgrade. OV06 is the precedent both ways: it ceilinged when telegraphed and floored when the completion frame suppressed scrutiny on chart-coached content. The floor depends on that completion-frame satisfice. If all-catch with no floor, swap the slot to a distinct idea (wound-care SOAP or amputation), not a v2.
- Differentiation: OV06 = vascular referral closure; OV05 = skilled wound-care downgrade. Different service, same engine, same lane.

## Files
Deliverable started_referral_coordination_note_05252026.docx; subordinate home_health_intake_review_05242026.docx; golden golden-OV05.docx; grader grader-guidelines-OV05.txt (509 words); prompt prompt-OV05.txt. Full chart mounted. Build: build/build_ov05.py. Decisive chart file: wound_care_consult_05202026 (open granulating wound, skilled daily dressing, exceeds self-care).
