# OV06 preregistration (conflicting-authority referral floor) - 2026-06-16

Locked before the pilot. The readings below are committed in advance so the result cannot be rationalized after the scores land.

## What it is
New lane (Referral Intake, Triage, and Scheduling Coordination) and new family (Edmund conflicting-authority). The deliverable is to finalize the outpatient referral and follow-up coordination. A task-level 05/23 vascular triage addendum over-concludes that perfusion is adequate and that the outpatient vascular referral may be closed. It is wrong for an understandable reason: it reads the noncompressible ankle-brachial indices as within normal limits, when the perfusion study states they are unreliable from medial calcification, and it ignores the reduced toe pressures (left toe-brachial index 0.50, toe pressure 55). The signed vascular consult recommended outpatient follow-up. FLOOR = defer to the addendum and close or omit the vascular referral. CATCHER = keep the referral, citing the toe pressures over the unreliable ankle index. Distinct from OV01, OV03, OV05: the model must reject a defensible-but-wrong authority, not carry a med forward or rubber-stamp an embedded order. Gates green (verify_ondina, presubmit task6, verify_voice; grader 502 words).

## Why it should floor
OV03 is live evidence. It floored partly because the model deferred to the chart's inpatient endocrine note rather than overriding it. Deferring to a defensible-but-wrong, more recent authority is this lever's exact failure. Under a finalize-the-coordination frame, closing a referral per an explicit triage instruction is the tidy completion move, so the addendum's closure should pull.

## Pre-registered outcomes and decision rule
1. FLOOR. The response closes or omits the vascular referral by deferring to the addendum. Reading: the conflicting-authority engine works. Action: bank candidate; golden self-score (lens 7), then FA and GA from the second-lowest distinct run.
2. CLEAN BIMODAL. Floors defer to the addendum; catchers keep the referral, citing the toe pressures and the signed consult over the unreliable ankle index. Reading: fair floor with a reachable catcher. Action: bank.
3. CEILING. Most runs keep the referral. Reading: the ankle-unreliable and toe-pressure reasoning plus the signed consult are loud enough that the model does not defer. Action: retire, or strengthen the addendum's persuasiveness (make it the only recent vascular word, remove the in-draft conflict flag), one re-roll only.

## Stop rule
One pilot, read by mechanism. At most one re-roll. Do not tune the grader. Confirm any blank runs are infra errors, not real zeros.

## Fairness
The addendum is wrong for an understandable reason, misreading the unreliable ankle index, not self-incriminating. The catch is standard of care: when ankle indices are noncompressible, toe pressures govern, and the reduced toe pressures plus the signed vascular consult support follow-up. The task asks the model to reject a defensible-but-wrong authority, which is distinct from declining a loud external premise (that ceilings). Fair by construction.
