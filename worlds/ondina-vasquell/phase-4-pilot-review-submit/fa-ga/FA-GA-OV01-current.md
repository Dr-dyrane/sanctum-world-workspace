# OV01 FA/GA - clean-mount pilot (DRAFT for Alexander to finalize)

> SUBJECT MUST CHANGE per King P 2026-06-14: FA/GA now uses the 2nd-LOWEST % run, not the lowest. OV01's lowest is 0.40 (attempt 3, used below); the 2nd-lowest is 0.50 (attempt 7, job 741ba52f). RE-DERIVE this FA/GA from the 0.50 run (need its output + grading transcript) before submission. The 0.40-based text below is retained only until the re-derivation. DO-NOT-REPEAT #20.


Status 2026-06-14: paste-ready draft for the clean-mount bankable pilot. Job `741ba52f-bae9-4594-a25c-ef5ae0e8bcdc` scored 68, 72, 40, 70, 72, 72, 50, 65, 78, 93 (mean 68.0; four sub-70). FA subject: the single lowest genuine-failure run, Attempt 3, run `24acdfc4-37e2-4d1c-9aca-38c2a11c13a3`, trajectory `traj_e6faef3`, score 0.40. Recommended grader rating: Great. Format per ABI 2026-06-09: failure-only, single run, no grader-section names, no bullets, no headers, each part under about 1000 characters, physician voice, no dashes.

## Failure Analysis

On Attempt 3 the failure is the enoxaparin decision. The order set carried enoxaparin 40 mg daily into discharge, but the chart supports it only as inpatient venous thromboembolism prophylaxis; the correct reconciliation stops it at discharge because it is not a home medication and it adds bleeding risk on aspirin plus clopidogrel. The model instead called it reasonable now, marked it confirm rather than discontinue, included it in the patient instructions as a daily shot while she is not walking normally, and asked the physician to confirm continuing it.

It also did not record metformin, empagliflozin, and lisinopril as explicit deferred restarts, leaving them as ambiguous confirm verdicts and calling lisinopril the most clearly supported to resume, which drifts toward resuming an agent held for acute kidney injury rather than holding it. The reconciliation was delivered inline only and not saved as the required output deliverable.

## Grader Analysis

The grader scored the run against the golden and the 0.40 placement supports a Great rating. It caught the central defect, that the golden discontinues enoxaparin at discharge while this run left it alive as a possible discharge medication, and it read the held agents as ambiguous rather than the explicit deferred restarts the golden records, including the lisinopril resume drift; its credit for the antibiotic correction, culture hierarchy, insulin, and NSAID avoidance tracks the golden, so the floor is targeted and not blanket.

The wording weakness is that the grader at points says the model continued enoxaparin outright, when the final answer was hedged to confirm rather than sign. That hedge does not cure the error, because the run still called home enoxaparin reasonable, gave injection instructions, and asked to continue it on aspirin and clopidogrel. A deeper floor would overstate it and a higher score would miss the central prophylaxis error, so the placement is right.
