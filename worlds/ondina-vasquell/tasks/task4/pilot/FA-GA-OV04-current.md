# OV04 FA/GA - failure-only (off-text CPAP-adherence finding, v3)

<!-- Internal provenance (not pasted): subject = 2nd-lowest distinct score, 0.20 = Attempt 9, run bad52e0a-7096-45fb-b4b3-8d544669226b, traj_907e6e9 (job 517aa586-9c65-4ab8-b539-2adc370e64d6). v3 confirming pilot is a clean bimodal: floors 0.15/0.15/0.20/0.20, catchers 0.80/0.80/0.85/0.88/0.90/0.95 (6 of 10), mean ~0.59, fair and hard; the KM08-v7 off-text lever works. Catcher read done: Attempt 10 (0.95, run 73e9bdba) reviewed the CPAP report and found 9 of 30 nights used, residual AHI 31, poor adherence, sleep-medicine follow up. Before paste: select Attempt 9 in Studio and bind the FA/GA box to run bad52e0a. Format: failure-only, no section names, no dashes. -->

## Failure Analysis

On Attempt 9, the model produced a solid note from the chart, correctly reconciling medications, summarizing the patient's hospital course, and documenting appropriate follow up plans. However, it missed the main finding in this case. The CPAP compliance report was available as an image file, but the model never opened or reviewed it. Because the report was not reviewed, the model missed the patient's poor CPAP adherence and the evidence of ongoing obstructive sleep apnea. The note stated the patient would continue home CPAP and did not raise any adherence concerns or recommend sleep medicine follow up. Since this information was only present in the device report, the final note was missing an important part of the patient's overall assessment.

## Grader Analysis

The 0.20 score is appropriate. The note accurately captured most aspects of the hospitalization but failed to identify the poor CPAP adherence documented in the compliance report. As a result, the patient's obstructive sleep apnea was presented as stable on home CPAP despite evidence of inadequate treatment. Credit is warranted for the otherwise accurate medication reconciliation, hospital course, and follow up planning. However, the missed CPAP finding was clinically significant and affected the overall assessment, making the assigned score reasonable.
