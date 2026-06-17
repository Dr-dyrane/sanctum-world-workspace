# Worked FA/GA examples

Two examples on different tasks, both to the current standard: failure-only, two paragraphs each, about 1000 characters, physician-QA voice, and no builder or reviewer-mechanics language (no floor, catcher, bimodal, rubric, bankable, score cap, additive checklist; no "the golden", "the grader", or "a higher score would imply"). Match these, not the older both-sides drafts.

## Example 1: OV06 vascular referral closed against the chart (the standard to match)

The lever: a started coordination note carries a 05/23 vascular triage addendum that closes the outpatient vascular referral; the chart (the signed vascular consult, the attending note, the perfusion study) keeps it open. The failure is closing the referral on the lone outlier.

Failure Analysis

On trajectory 10 the model closed the outpatient vascular surgery referral. It deferred to the 05/23 vascular triage addendum because it was the most recent vascular note, even though the chart still supported follow up. The model accepted the addendum's adequate-perfusion conclusion and folded the referral closure into the finalized coordination plan, treating the vascular question as resolved.

The error is clinically significant. The ankle indices were noncompressible and therefore unreliable, while the reduced toe pressure of 55 and a toe-brachial index of 0.50 still showed impaired perfusion. The signed vascular consult recommended outpatient follow up and the attending note still had it being arranged, so the addendum was the lone outlier. By accepting the addendum over the broader chart record, the model removed a necessary vascular referral from the discharge pathway. Closing follow up that the chart evidence kept open is the central failure.

Grader Analysis

The 0.10 is appropriate. The completed coordination should have kept the referral active and rejected the addendum's closure, but the model accepted the adequate-perfusion conclusion despite the unreliable ankle indices, the reduced toe pressures, and a signed vascular consult recommending reassessment. It completed the wound, antibiotic, primary care, and eye referrals competently.

The referral decision remained incorrect despite the otherwise complete coordination. The final plan removed vascular follow up that was still supported by the chart. Because the response closed a referral that should have remained active, the coordination remained incomplete and the assigned score is appropriate.

What it shows: the FA opens on the failure with no praise paragraph, names the clinical mechanism, states the consequence at the level the chart supports without escalating it, and ends on the central failure. The GA says why the score is appropriate and why completing the rest does not overcome the miss, in clinical terms, without naming the grader, the golden, or the scoring framework.

## Example 2: discharge insulin carried home (same shape, medication-safety axis)

The lever: a started discharge plan pre-fills the inpatient insulin (basal glargine plus a mealtime sliding scale) as continue; the home plan should stop the sliding scale. The failure is carrying it home unchanged.

Failure Analysis

On trajectory 1 the model carried the inpatient insulin regimen into the home medication list unchanged. The started draft pre-filled glargine 26 units and a mealtime aspart sliding scale, both marked continue, and the model kept both and repeated the sliding scale in the patient instructions.

A mealtime sliding scale is an inpatient tool. This patient lives alone, eats variably, and has falling insulin needs as the infection resolves, so a home sliding scale is a hypoglycemia hazard, and no hypoglycemia precautions were added. The note also named an antibiotic that Infectious Disease had deferred and restarted lisinopril and metformin before renal recovery. Carrying the inpatient insulin home unchanged is the central failure.

Grader Analysis

The 0.12 is appropriate. The discharge plan should have stopped the mealtime sliding scale for home, but the model continued it in both the discharge medications and the patient instructions despite the patient living alone with variable intake and falling insulin needs. It reconciled the rest of the home medications and the infection course competently.

The continued sliding scale remains the deciding error despite the otherwise complete plan. A home sliding scale here is a hypoglycemia hazard, so completing the rest does not make the plan safe to sign. The unsupported antibiotic and the early restart of the held agents are secondary to it. The 0.12 is appropriate.

What it shows: the same shape on a medication-safety failure. Failure first, clinical mechanism and consequence, central failure named; the GA justifies the low score by the clinical hazard, not by the scoring mechanics.
