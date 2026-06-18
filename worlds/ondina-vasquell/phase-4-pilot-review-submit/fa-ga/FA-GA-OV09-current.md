# OV09 FA/GA - failure-only (post-acute handoff / held oral agents resumed at discharge)

Status 2026-06-18: paste-ready draft for job cc337773-c5c6-4a19-9df7-bfebd12fa593. Scored 0.25, 0.35, 0.35, 0.35, 0.78, 0.85, 0.87, 0.90, 0.92 across nine scored runs, one run errored. Mean about 0.62, bimodal, roughly four floors at 0.25 to 0.35 and five catchers at 0.78 to 0.92. FA subject: Attempt 10, run a4ac211b-9d1a-4007-b427-9d8ca7f6f0dd, traj_7a967e7, score 0.35 (the second-lowest distinct; lowest distinct is 0.25). Guidance applied: fa-ga-canonical.md, one trajectory, failure-only FA, grader-audit GA (what the grader got correct, what could improve, calibration), no grader-section names, no bullets, each field about 1000 characters.

## Failure Analysis

On Attempt 10, the model finished the handoff competently. It kept the disposition open, continued insulin, and preserved the accurate antibiotic, wound, therapy, and follow-up items. The failure is the medication line. It left the started draft's resume of metformin, empagliflozin, and lisinopril at discharge in place, and only noted that the attending should decide on restart. It had the hold orders in hand and resumed them.

These three are held for AKI on CKD, creatinine 1.6 from a peak of 2.1. Metformin near an eGFR of 30 risks lactic acidosis, empagliflozin risks euglycemic ketoacidosis during an active infection, and lisinopril worsens the recovering renal function. The note also contradicts itself, holding the agents in one section and resuming them in another, which leaves the unsafe option live for the signing physician. Leaving them resumed is the central failure, and it drives the low scores, 0.25 to 0.35, while the runs that hold them reach 0.92.

## Grader Analysis

The grader scored this correctly. It confirmed the three agents are held for AKI on CKD with no restart entered, saw the resume line carried into the finished note, and made that the deciding error. It gave appropriate credit for the parts the golden keeps: the open disposition, the culture-directed antibiotics with Infectious Disease step-down, wound care, therapy, and insulin. It did not let the model's partial "held" note rescue the answer, since the resume line stands.

One point could improve. The grader labored over whether the partial note counted and read the deduction as a vague caution. The sharper point is that the note keeps the line resuming three held agents, so the deliverable still instructs an unsafe restart, not an incomplete one. Naming that as a distinct error would let it reach 0.35 without inferring it. The number holds: a deep floor would overstate the handoff, and a higher score would ignore three held agents resumed in an unresolved AKI, so 0.35 is well placed.
