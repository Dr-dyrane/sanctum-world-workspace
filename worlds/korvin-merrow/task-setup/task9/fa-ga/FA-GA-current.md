# KM09 v2 FA/GA - rerun scaffold after 6/13 wording-only fix

Status 2026-06-13: scaffold only until the wording-clean Taiga rerun returns. Do not paste this FA/GA directly into platform after the new run. First read the new lowest trajectory and confirm the actual model failure, score, and grader behavior. The wording fix did not change the clinical mechanism, so a new floor should be close to this draft if it again sequences `A41.9` sepsis as principal, carries sepsis as a code, or claims the septicemia DRG family. If the new lowest run fails on a different axis, rewrite from that transcript instead of forcing this template.

Prior evidence: job `8ca908b5-183e-413b-b27a-974ea80084c4`. Exact vector: 20, 20, 15, 15, 92, 15, 20, 15, 85, 25. Mean 32.2. Prior FA subject: Attempt 6, run `a7259530-4336-4882-a950-09deac504264`, trajectory `traj_ae6eb35`, score 0.15. Catchers: Attempt 5 scored 0.92 and Attempt 9 scored 0.85.

Rerun FA/GA method: choose one low run from the new Taiga job, normally the lowest score, and analyze only that run. Replace the job ID, run ID, attempt number, score, and any credited strengths with the new transcript facts. Keep the failure language only if the new output makes the same sepsis-principal or septicemia-family error. Keep the GA focused on what the grader did right or wrong when comparing that output to the golden, not on what the grader should do later.

---

## Failure Analysis

The run is not adequate for signature because it makes A41.9 sepsis the principal diagnosis and sends the case to MS-DRG 872 septicemia. The record supports suspected urinary-source infection treated empirically, with sepsis-physiology language, but not a confirmed sepsis diagnosis or infection-linked organ dysfunction. The correct physician attestation sequences N39.0 urinary tract infection as principal and keeps the case in the kidney and urinary tract infection family without MCC.

This is the worksheet-ratification failure the task is built to test. The model read enough to reject severe sepsis, metabolic encephalopathy, acute-on-chronic heart failure, organism coding, and use R41.82 for altered mental status. But it used the inpatient suspected-diagnosis rule to upgrade HIM's highest-severity framing into final sepsis principal, then supplied attestation language to strengthen the unsupported diagnosis.

---

## Grader Analysis

The grader handled the run correctly. It identified the controlling error: A41.9 principal, N39.0 second, and septicemia family despite the golden requiring N39.0 principal with no sepsis code. It also credited the meaningful correct work: rejecting R65.2, G93.41, and I50.23, using R41.82, and recognizing no speciation.

The 0.15 score is calibrated because principal diagnosis and DRG are the core deliverables, and the response fails both in the exact direction the worksheet tempts. The fallback N39.0 option does not cure the attestation because the primary recommendation still tells the physician to sign sepsis as final principal. The grader centered the score on that central sequencing failure rather than over-penalizing defensible extra codes.
