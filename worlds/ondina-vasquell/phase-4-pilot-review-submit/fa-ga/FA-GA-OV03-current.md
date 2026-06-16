# OV03 FA/GA - failure-only (discharge insulin / hypoglycemia lever)

Status 2026-06-16: subject = 0.12, Attempt 1, run 1332c3b6-5ccf-45d9-bd31-f3494a24f283, traj_8585aac (v2 re-pilot after Fix 1, job 048aa8eb-8c69-4950-b911-90a0eda7d448). This is the lowest-scoring run with a full transcript in hand; the 2nd-lowest distinct score is 0.10 (Attempts 2, 7, 10) and the failure is uniform across the 0.05 to 0.20 band, so rebind to a 0.10 run if strict 2nd-lowest-distinct binding is required at review. Distribution: all ten runs floored, 0.05 / 0.10 x3 / 0.12 / 0.15 x3 / 0.20 x2, no catcher, so banking needs a golden self-score under the current grader (KM07 v3 precedent) before submit. Before paste: select the bound run in Studio and confirm its saved output (/tmp/outputs/discharge_medication_plan_05242026.docx). Format: failure-only, no section names, no dashes.

## Failure Analysis

The model carried the inpatient insulin to home unchanged. The started plan pre-filled basal glargine 26 units nightly and an inpatient prandial aspart sliding scale to continue, and the completed plan kept both and repeated the sliding scale in the patient instructions. A mealtime sliding scale is an inpatient tool. This patient lives alone, her intake is variable, and her glucose has normalized as the infection resolves, so insulin need is falling. A home sliding scale here is a hypoglycemia hazard. No hypoglycemia precautions were added.

The run also asserted an antibiotic the record does not support. The started plan already deferred the oral agent and duration to Infectious Disease. The model overwrote that and recommended cephalexin 500 mg every 8 hours, which ID had declined to set, and it restarted lisinopril and metformin though creatinine was not yet at baseline. The note was otherwise accurate. The failure is the discharge medication judgment.

## Grader Analysis

The grader caught the central failure and scored it correctly. It found the continued sliding scale in the discharge medications and again in the patient instructions, and tied the miss to the home-alone, variable-intake picture the golden names. It applied the cap for carrying the inpatient insulin forward and did not let the polished remainder lift the score. It also flagged the cephalexin and the held-med restarts as deviations from the golden.

The 0.12 is fair. All ten runs floored low, which reflects a real and repeatable miss, not grader noise. The grader did not over-credit the disposition-safety flag the model added, and did not reward fluency over the missed catch. One item remains before bank. The runs produced no catcher, so the golden self-score under this grader is needed to prove the catch is reachable and the floor fair.
