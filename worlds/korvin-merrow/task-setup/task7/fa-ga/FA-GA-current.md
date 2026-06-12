# KM07 FA/GA - v4 current draft

Status 2026-06-12: current draft for v4 job `db57dc63-fd23-448d-9e6c-a3ecbfdb1f61`. Trajectory Quality passed on rescore after an initial severity-calibration false alarm. Taiga QA and Feedback AutoQC pass. Platform is at Failure Analysis and Grader Analysis.

Subject: Attempt 10, run `e1dd1593-adca-4398-b48c-23063dee9bef`, score 0.40, single lowest run.

## Failure Analysis

On trajectory 10, the model produced a nephrology referral letter that was not adequate for the central medication-reconciliation purpose of the task. It correctly framed the AKI on CKD course, preserved the staged restart question for sacubitril/valsartan, spironolactone, furosemide, empagliflozin, and metformin, and did not invent a prednisone dose. It also found the alendronate detail and correctly noted it was not administered in the hospital. The failure is that it then says alendronate continues on its Sunday schedule at home, grouping it with routine outpatient and as-needed medications rather than leaving it open for nephrology review.

The MAR says alendronate was not administered inpatient and should be reconciled at discharge, and the golden asks nephrology to confirm renal trajectory before resumption after AKI on CKD. This turns a required specialist question into routine continuation, which is the central failure pattern. This failure mode appears at 0.40 on this task and is the priority issue to document.

## Grader Analysis

The errors caught in this trajectory landed the run at 0.40, which is appropriate for an otherwise usable referral that misses the central bone-health reconciliation item. In terms of non-negotiable clinical content, the grader recognized that the letter did not keep alendronate open the way the golden does, despite preserving the staged restart framing for the other held cardiorenal and diabetes agents. It also appropriately credited the correct renal course, the one to two week nephrology follow-up, and the absence of unsupported prednisone dosing or held-agent restart.

The main constructive feedback is that the grader should explicitly state that "not administered inpatient" does not rescue the answer once the letter says alendronate continues on its home Sunday schedule. That phrase is a closure, not a neutral medication-list detail, because the record requires nephrology renal-trajectory confirmation before resumption. The 0.40 score is calibrated to a major central miss with otherwise good structure, but that rationale should be explicit for reproducibility.

## Platform paste version

Failure Analysis:

On trajectory 10, the model produced a nephrology referral letter that was not adequate for the central medication-reconciliation purpose of the task. It correctly framed the AKI on CKD course, preserved the staged restart question for sacubitril/valsartan, spironolactone, furosemide, empagliflozin, and metformin, and did not invent a prednisone dose. It also found the alendronate detail and correctly noted it was not administered in the hospital. The failure is that it then says alendronate continues on its Sunday schedule at home, grouping it with routine outpatient and as-needed medications rather than leaving it open for nephrology review.

The MAR says alendronate was not administered inpatient and should be reconciled at discharge, and the golden asks nephrology to confirm renal trajectory before resumption after AKI on CKD. This turns a required specialist question into routine continuation, which is the central failure pattern. This failure mode appears at 0.40 on this task and is the priority issue to document.

Grader Analysis:

The errors caught in this trajectory landed the run at 0.40, which is appropriate for an otherwise usable referral that misses the central bone-health reconciliation item. In terms of non-negotiable clinical content, the grader recognized that the letter did not keep alendronate open the way the golden does, despite preserving the staged restart framing for the other held cardiorenal and diabetes agents. It also appropriately credited the correct renal course, the one to two week nephrology follow-up, and the absence of unsupported prednisone dosing or held-agent restart.

The main constructive feedback is that the grader should explicitly state that "not administered inpatient" does not rescue the answer once the letter says alendronate continues on its home Sunday schedule. That phrase is a closure, not a neutral medication-list detail, because the record requires nephrology renal-trajectory confirmation before resumption. The 0.40 score is calibrated to a major central miss with otherwise good structure, but that rationale should be explicit for reproducibility.
