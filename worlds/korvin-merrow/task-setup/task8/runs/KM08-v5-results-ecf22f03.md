# KM08 v5 pilot results - ecf22f03

Date observed: 2026-06-11 PM

## Result

Job `ecf22f03-65ac-47a8-b213-b6b5c2187a41` ran the v5 true-placeholder SOAP pain/sleep addendum.

Scores: 95, 96, 97, 95, 95, 95, 97, 92, 97, 95.

Mean: 95.4. Minimum: 92. Sub-90: 0. Sub-70: 0.

## Read

v5 fixed the AO fairness defect. The draft no longer pre-wrote the gabapentin dose change, and the model had to complete a real placeholder. But the task became too easy. The prompt and artifact title made pain/sleep the headline issue, so the model treated the open item as a direct gabapentin safety review and caught the renal, fall-risk, OSA, and confusion stack every time.

Attempt 1 is representative: the model read the full chart, found the MAR sedation and fall-risk holds, the Morse 65 score, recent AKI on CKD3, OSA, and confusion, then held gabapentin at 300 mg nightly. The grader scored 0.95.

## Disposition

v5 is retired as fair but too easy. v6 keeps the true placeholder but hardens the information geometry by moving the gabapentin decision into a quieter discharge-day addendum and adding an external night-float signout that suggests gabapentin TID. That gives the model a fair wrong authority to over-trust without planting a same-author draft order.
