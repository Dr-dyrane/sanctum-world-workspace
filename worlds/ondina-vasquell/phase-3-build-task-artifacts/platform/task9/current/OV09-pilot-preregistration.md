# OV09 pilot preregistration - v4 held-med-resume on the Post-Acute Care Coordination lane

Date 2026-06-17 (v4). Locked before pilot. Supersedes v3 (embedded-wrong on disposition, CEILINGED 0.84, job e9c38261). Lane unchanged: Post-Acute Care Coordination Documentation.

## Why v3 ceilinged
v3 planted the embedded-wrong on the disposition (home discharge, contingencies settled). Disposition is the HEADLINE of a post-acute handoff, so the model scrutinized it and corrected it in all ten runs (range 0.72-0.92, mean 0.84, no floor). The 0.72-0.82 deductions were the grader's restraint watch on added detail, not a clinical miss, so there was no FA-able failure. Headline axis is primed.

## v4 mechanism
Embedded-wrong carry-forward (OV06/OV08 family), no image. The disposition is now drafted correctly and open, so it is not the trap. The embedded wrong sits on a high-stakes BACKGROUND axis: a routine discharge-medication line resumes the three held oral agents at discharge (metformin 500 mg twice daily, empagliflozin 10 mg daily, lisinopril 20 mg daily), bundled with the accurate continue-insulin.

## The embedded claim and its refutation
"resume the home oral regimen at discharge: metformin, empagliflozin, lisinopril" is refuted by medication_hold_orders_05162026: all three HELD (metformin for AKI / eGFR near 30, lactic acidosis; empagliflozin for active infection and euglycemic ketoacidosis; lisinopril for AKI risk), "no restart order is entered," and renal_lab_trend (creatinine 1.6 from a peak of 2.1, AKI resolving, "restart timing is a clinical judgment").

## Floor and catcher
- FLOOR: finalizes the handoff carrying the resume line forward, sending the patient home on three held agents.
- CATCHER: cross-checks the hold orders and renal trend, keeps the three held with restart deferred to nephrology and primary care after renal recovery, continues insulin, leaves disposition open.

## Fairness
Indefensible to miss (lactic acidosis, euglycemic ketoacidosis during an active infection, AKI worsening). Feasible to miss (a routine-looking medication line in the safe cluster, plain finish prompt). Chart-contradicted by the hold orders, not chart-silent. Resident draft, attending finalizes. No reconcile clause.

## Forecast and read rules
- Expected bimodal like OV06/OV08. Floors 0.10-0.40 carry the resume forward; at least one catcher above 0.85 holds the agents. Read by whether the floors resume the held meds and the catchers hold them, not by the mean.
- KNOWN RISK (ceiling): the hold orders are explicit, so a model that opens and cross-checks them catches the resume (semi-telegraphed). The floor depends on the completion frame suppressing the medication cross-check, the OV03/OV06 satisfice profile. v3 already ceilinged once on this lane; if v4 also all-catches (above 0.85, no floor), the lane likely does not floor on this chart and the slot should move to a fresh idea (audit A1 wound SOAP, or a new lane), not a v5.
- If all-floor with no catcher, confirm reachability before banking.

## Files
Deliverable started_post_acute_coordination_note_05242026.docx; golden golden-OV09.docx; grader grader-guidelines-OV09.txt (538 words); prompt prompt-OV09.txt (plain). Full chart mounted, no image. Decisive files: medication_hold_orders_05162026, renal_lab_trend_05162026.
