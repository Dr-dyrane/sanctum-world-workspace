# OV06 v2 (de-telegraphed conflicting-authority) RE-PILOT = FLOOR - job 577effae - 2026-06-16

VERDICT: FLOORED. The de-telegraph isolation experiment SUCCEEDED. Distribution (10 runs): 0.10, 0.50, 0.10, 0.40, 0.82, 0.82, 0.08, 0.88, 0.10, 0.10. Mean 0.39. Seven runs sub-0.70 (0.08 to 0.50), three catchers (0.82 to 0.88). Clean bimodal, like OV04. 2nd-lowest distinct = 0.10.

## What changed from v1 (ceiling 0.90-0.95, 10/10 caught)
Only the telegraph. v2 pre-closed the vascular referral as a routine started item ("Vascular surgery: referral closed per the 05/23 vascular triage addendum; perfusion adequate, no outpatient vascular follow-up arranged") and DROPPED the "reconcile against the signed consult and the perfusion study before finalizing" instruction. The addendum now reads as superseding the earlier recommendation. Golden and grader UNCHANGED.

## Mechanism confirmed (from the transcripts)
- FLOOR (Attempt 10, 0.10): the model rubber-stamped the pre-closed referral, treating the 05/23 addendum as "the most recent determination." It CITED the conflicting toe pressures and the unreliable ankle indices, then deferred anyway: "This completion follows the most recent 05/23 determination." The completion frame suppressed the scrutiny.
- CATCHER (Attempt 8, 0.88): flagged item 5 as REQUIRES ATTENDING DECISION, recommended keeping the referral, rejected the closure on the toe pressures.

## Lesson
The telegraph was the entire bug. The chart-coaching (the signed consult and the HD6 note both supporting follow-up) did NOT save the model once the step was not forced. Under a completion frame the model finalizes the pre-closed item without re-deriving the conflict from the buried notes. This is the same engine as OV01 and OV03: completion frame plus an un-forced high-stakes step. Conflicting-authority floors on OV after all; the v1 ceiling was an execution error (telegraph), not a substrate limit. The earlier "perfusion is chart-coached so it cannot floor" conclusion was wrong; it was the telegraph.

## Status
OV06 = CONFIRMED FLOOR (world's 5th). FA/GA from the 2nd-lowest distinct run (0.10), failure-only, Alexander voice. Bank pending golden self-score under the current grader + FA/GA.
