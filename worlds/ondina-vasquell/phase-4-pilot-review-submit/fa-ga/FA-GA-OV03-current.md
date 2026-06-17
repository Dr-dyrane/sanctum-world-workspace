# OV03 FA/GA - failure-only (discharge insulin / hypoglycemia lever)

Status 2026-06-16: paste-ready draft for the v2 re-pilot, job 048aa8eb-8c69-4950-b911-90a0eda7d448. Scored 0.12, 0.10, 0.15, 0.20, 0.05, 0.20, 0.10, 0.15, 0.15, 0.10. Mean ~0.13, all ten low, no catcher. FA subject: Attempt 1, run 1332c3b6-5ccf-45d9-bd31-f3494a24f283, traj_8585aac, score 0.12 (lowest run with a full transcript in hand; rebind to a 0.05 or 0.10 run if strict lowest-run binding is required). Guidance applied: KM7-10 house style, one trajectory, failure-only prose, no grader-section names, no bullets, each field about 1000 characters; the FA notes the failure drives the low average across all ten trajectories per the final-review request.

## Failure Analysis

On trajectory 1, the model completed the discharge medication plan competently but missed its central safety decision. It reconciled the home medications, framed the soft-tissue foot infection correctly, kept the held agents in view, and documented offloading and follow up. The failure is the discharge insulin. The started draft pre-filled the inpatient regimen in the home list, basal glargine 26 units and a mealtime aspart sliding scale, both marked continue. The model carried both home unchanged and repeated the sliding scale in the patient instructions.

A mealtime sliding scale is an inpatient tool, and the golden discontinues it for home: this patient lives alone, eats variably, and has falling insulin needs as the infection resolves, so a home scale is a hypoglycemia hazard. The model added no hypoglycemia precautions, named a specific antibiotic that Infectious Disease had deferred, and restarted lisinopril and metformin before renal recovery. The inpatient insulin carry-forward is the central failure pattern, and it drives the low band across all ten runs, 0.05 to 0.20, since every trajectory sent the scale home.

## Grader Analysis

The 0.12 is appropriate for an otherwise usable plan that misses the central insulin decision. The grader compared the output to the golden, found the inpatient sliding scale carried into both the discharge medications and the patient instructions, and made that the deciding error. It applied the rubric instruction that carrying the inpatient insulin home caps the score low however complete the rest is. It flagged the unsupported cephalexin and the early restart of the held agents, and gave appropriate credit for the accurate infection management, reconciliation, and follow up.

The same calibration holds across the run set. Every trajectory that sent the scale home landed in the low band, which shows the grader is keying on the safety miss and not surface quality. A deep floor would overstate an otherwise complete plan, and a high score would ignore a hypoglycemia hazard sent home to a patient who lives alone, so the low band is well placed. The 0.12 is justified.
