# OV09 FA/GA - failure-only (post-acute handoff / held oral agents resumed at discharge)

Status 2026-06-18: paste-ready draft for job cc337773-c5c6-4a19-9df7-bfebd12fa593. Scored 0.25, 0.35, 0.35, 0.35, 0.78, 0.85, 0.87, 0.90, 0.92 across nine scored runs, one run errored. Mean about 0.62, bimodal, roughly four floors at 0.25 to 0.35 and five catchers at 0.78 to 0.92. FA subject: Attempt 10 (trajectory 10), run a4ac211b-9d1a-4007-b427-9d8ca7f6f0dd, traj_7a967e7, score 0.35 (the second-lowest distinct; lowest distinct is 0.25). Writer score: 0.30 (my own assessment of this run, against the grader's 0.35; a notch lower given the patient-safety stakes of resuming three contraindicated agents in AKI). Grader rating carried to the writer separately, not in this file.

## Failure Analysis

On trajectory 10, the model finished the handoff competently. It kept the disposition open. It continued insulin. It preserved the accurate antibiotic, wound, therapy, and follow-up items. The failure is the medication line. It left the started draft's resume of metformin, empagliflozin, and lisinopril in place. It only noted that the attending should decide on restart. It had the hold orders in hand and resumed them.

These three are held for AKI on CKD, creatinine 1.6 from a peak of 2.1. Metformin near an eGFR of 30 risks lactic acidosis. Empagliflozin risks euglycemic ketoacidosis during an active infection. Lisinopril worsens the recovering renal function. The note also contradicts itself. It holds the agents in one section and resumes them in another. That leaves the unsafe option live for the signing physician. This is the central failure. Based on these, I score it 0.30 in this trajectory.

## Grader Analysis

The grader scored trajectory 10 at 0.35 against the golden and guidelines. That is right. It confirmed the three agents are held for AKI on CKD with no restart entered. It saw the resume line carried into the finished note. It made that the deciding error. It gave appropriate credit for the parts the golden keeps: the open disposition, antibiotics, wound care, therapy, and insulin. It did not let the partial held note rescue the answer, since the resume line stands.

One point could improve. The grader was unsure whether the partial note counted. It read the deduction as a vague caution. But the note keeps the line resuming three held agents. The deliverable still instructs an unsafe restart, not an incomplete one. Naming that as a distinct error would let it reach 0.35 without inferring it. The 0.35 is defensible. A deep floor would overstate the handoff. A higher score would ignore three held agents resumed in an unresolved AKI. Given the stakes, I put it a notch lower at 0.30.
