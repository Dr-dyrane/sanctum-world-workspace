# OV03 FA/GA - failure-only (discharge insulin / hypoglycemia lever)

Status 2026-06-16: subject = 0.12, Attempt 1, run 1332c3b6-5ccf-45d9-bd31-f3494a24f283, traj_8585aac (v2 re-pilot after Fix 1, job 048aa8eb-8c69-4950-b911-90a0eda7d448). This is the lowest-scoring run with a full transcript in hand; the 2nd-lowest distinct score is 0.10 (Attempts 2, 7, 10) and the failure is uniform across the 0.05 to 0.20 band, so rebind to a 0.10 run if strict 2nd-lowest-distinct binding is required at review. Distribution: all ten runs floored, 0.05 / 0.10 x3 / 0.12 / 0.15 x3 / 0.20 x2, no catcher, so banking needs a golden self-score under the current grader (KM07 v3 precedent) before submit. Before paste: select the bound run in Studio and confirm its saved output (/tmp/outputs/discharge_medication_plan_05242026.docx). Format: failure-only, no section names, no dashes.

## Failure Analysis

On Attempt 1 the model completed the discharge plan competently. It reconciled the home medications, treated the foot infection appropriately, and documented offloading and follow up. The major error was the discharge insulin. The model carried the inpatient regimen forward unchanged, including the mealtime aspart sliding scale, and repeated it in the patient instructions.

A mealtime sliding scale is an inpatient tool. She lives alone, her intake is variable, and her glucose has normalized, so her insulin need is falling. Sent home this way it is a hypoglycemia hazard. No hypoglycemia precautions were given. The model also recommended cephalexin, which Infectious Disease had deferred. It restarted lisinopril and metformin before renal function returned to baseline. The note was otherwise accurate. The errors were in the medication decisions, not the documentation.

## Grader Analysis

The 0.12 score is appropriate. The deciding error was the continued sliding scale, carried into both the discharge medications and the patient instructions. The grader tied it to the home-alone, variable-intake picture and did not let the polished remainder lift the score. It also flagged the unsupported cephalexin and the early restart of the held agents.

Credit is warranted for the otherwise accurate infection management, medication reconciliation, and follow up. However, the medication errors changed the safety of the discharge plan. A hypoglycemia hazard sent home to someone who lives alone is what brings a patient back. The score is justified.
