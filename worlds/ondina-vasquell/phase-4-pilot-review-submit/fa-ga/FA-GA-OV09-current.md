# OV09 FA/GA - failure-only (post-acute handoff / held oral agents resumed at discharge)

Status 2026-06-18: paste-ready draft for job cc337773-c5c6-4a19-9df7-bfebd12fa593. Scored 0.25, 0.35, 0.35, 0.35, 0.78, 0.85, 0.87, 0.90, 0.92 across nine scored runs, one run errored. Mean about 0.62, bimodal, roughly four floors at 0.25 to 0.35 and five catchers at 0.78 to 0.92. FA subject: Attempt 10, run a4ac211b-9d1a-4007-b427-9d8ca7f6f0dd, traj_7a967e7, score 0.35 (the second-lowest distinct; lowest distinct is 0.25). Guidance applied: KM7-10 house style, one trajectory, failure-only prose, no grader-section names, no bullets, each field about 1000 characters.

## Failure Analysis

On Attempt 10, the model finished the handoff competently. It kept the disposition open, continued insulin, and preserved the accurate antibiotic, wound, therapy, and follow-up items. The failure is the medication line. It left the started draft's resume of metformin, empagliflozin, and lisinopril at discharge in place and added only a decide-restart-versus-hold instruction. It had the hold orders in hand and resumed them anyway.

These three are held for acute kidney injury on chronic kidney disease, creatinine 1.6 from a peak of 2.1. Metformin near an eGFR of 30 risks lactic acidosis, empagliflozin risks euglycemic ketoacidosis during an active infection, and lisinopril worsens the recovering renal function. The note also contradicts itself, calling the agents held in one section and resumed in another, leaving the unsafe option live for the signing physician. This carry-forward is the central failure, and it drives the low band, 0.25 to 0.35, while the runs that remove it reach 0.92.

## Grader Analysis

The 0.35 is appropriate for an otherwise usable handoff that misses the central medication-safety item. The grader compared the output to the golden, found the resume line carried forward with a vague caution, and made that the deciding error. It applied the rule that resuming the held agents, or resuming them with a caution but no hold, caps the score below midline however complete the rest is. It gave appropriate credit for the open disposition, the antibiotics, wound care, therapy, and insulin.

The calibration holds across the runs. Every run that kept the line or deferred restart without holding landed at 0.25 to 0.35, and every one that removed it and held the three agents landed at or above 0.78, so the grader keys on the safety miss, not length; the longest run scored high. A deep floor would overstate an otherwise accurate handoff, and a high score would ignore three held agents resumed during an unresolved AKI, so the band is well placed. The score is justified.
