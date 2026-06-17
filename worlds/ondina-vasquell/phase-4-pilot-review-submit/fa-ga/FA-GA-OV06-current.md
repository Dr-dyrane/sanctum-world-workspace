# OV06 FA/GA - failure-only (vascular referral closed against the chart)

Status 2026-06-17 (revised per pod lead Ahmad G, register-cleaned): paste-ready for job 577effae. Scored 0.10, 0.50, 0.10, 0.40, 0.82, 0.82, 0.08, 0.88, 0.10, 0.10. Mean 0.39, bimodal, three high runs (0.82, 0.82, 0.88). FA subject: Attempt 10, run c5758060, traj_245278a, score 0.10 (second-lowest distinct). FA is failure-only with the clinical consequence named; GA explains the cap in clinical terms. No eval-register terms (golden, grader, rubric, catcher, calibration, floor) in the prose. Two paragraphs each, under about 1000 characters, no bullets.

## Failure Analysis

On trajectory 10 the model closed the outpatient vascular surgery referral. It deferred to the 05/23 vascular triage addendum because it was the most recent vascular note, even though the chart still supported follow up. The model accepted the addendum's adequate-perfusion conclusion and folded the referral closure into the finalized coordination plan, treating the vascular question as resolved.

The error is clinically significant. The ankle indices were noncompressible and therefore unreliable, while the reduced toe pressure of 55 and a toe-brachial index of 0.50 still showed impaired perfusion. The signed vascular consult recommended outpatient follow up and the attending note still had it being arranged, so the addendum was the lone outlier. Closing the referral sends a limb-threat diabetic foot to the skilled nursing facility with no vascular service following the circulation and no trigger to reassess it, the path to a nonhealing ulcer and possible limb loss. Closing follow up that the chart evidence kept open is the central failure.

## Grader Analysis

The 0.10 is appropriate. The completed coordination should have kept the referral active and rejected the addendum's closure, but the model accepted the adequate-perfusion conclusion despite the unreliable ankle indices, the reduced toe pressures, and a signed vascular consult recommending reassessment. It completed the wound, antibiotic, primary care, and eye referrals competently.

The competent remainder does not raise the score. A coordination plan that discharges a limb-threat foot with no vascular follow up is unsafe to sign, so the missed referral holds the score down however complete the rest is. A higher score would tell a signing physician the plan is usable when it is not. The 0.10 is appropriate.
