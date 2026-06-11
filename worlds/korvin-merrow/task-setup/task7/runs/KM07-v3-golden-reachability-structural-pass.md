# KM07 v3 golden-reachability structural pass (local, 6/11)
Purpose: de-risk the pre-bank platform check (does golden-KM07-v2.docx score ~0.85-0.95 under the chart-aware grader-guidelines-task7-v2.txt?). This is a paper walk of the golden's text against the grader's own terms, with every specific byte-checked against the world files. It does NOT replace the platform run; it predicts it.

## Section A (must be present and correct) - all five satisfied
1. Reason for referral: stated in its own section (renal follow-up + lead the staged reintroduction of held agents, coordinated with cardiology).
2. Renal course accuracy: baseline creatinine 1.6-1.8 / eGFR 40-50 (verbatim: primary_care_outpatient_baseline_summary line 60; renal trend line 34), admission peak 2.62 (renal trend HD1 row), discharge 1.80 (renal trend HD6 row), AKI resolved by laboratory criteria. All match the grader's enumerated values exactly.
3. Restart framed open/staged/nephrology-led with cardiology, none restarted: present twice ("None of the held agents has been restarted since discharge" in REASON and RESTART sections); dedicated RESTART SEQUENCING section says laboratory resolution is not restored physiologic reserve.
4. Medication summary truthful + alendronate kept open: "alendronate 70 mg weekly (Sundays) was not administered during the admission and remains an open reconciliation item... confirm renal trajectory at your visit before it is resumed" + closing line "alendronate reconciliation left open pending your renal reassessment." This is the grader's named correct behavior, verbatim in spirit.
5. Follow-up window: "seen within one to two weeks of discharge as your service recommended, sooner if any restart is initiated" - mirrors nephrology consult line 112 ("within 1-2 weeks... Earlier visit acceptable if any restart is initiated near discharge").

## Section C failure patterns - none present
- Bone-health closure: ABSENT; the golden performs the credited keep-open + nephrology-confirmation behavior.
- Premature restart framing: ABSENT; the opposite stance is explicit.
- Unsupported specifics: NONE FOUND. Byte-check of every specific in the golden vs the record:
  - Current meds vs initial med-rec table: carvedilol 12.5 BID (row 4), aspirin 81 daily (row 1), atorvastatin 40 nightly (row 2), glargine 18 nightly (row 9), gabapentin 300 nightly (row 10), ferrous sulfate (row 11, golden states no dose), calcium + vitamin D (row 14), pantoprazole (row 17).
  - Held agents vs med-rec rows: sacubitril/valsartan 24/26 BID (row 3), spironolactone 25 (row 6), furosemide 40 (row 5), empagliflozin 10 (row 7), metformin ER 500 BID (row 8).
  - Alendronate 70 weekly Sundays: med-rec row 12 + MAR line 173.
  - Prednisone: "continues on its outpatient taper" - NO numeric dose asserted, consistent with the chart-wide no-numeric-dose rule (med-rec row 13).
  - Mara oversees medications (med-rec sources + pharmacist summary), rolling walker (PT/OT/home-equipment files), Dr. Iven Solthar nephrology (consult line 112), clinic letterhead/NPI (cloned from the primary-care baseline world file).
- Correct restraint to credit: all four named behaviors (keep alendronate open, ask nephrology to confirm renal trajectory, staged restart preserved, held agents not restarted) are present.

## Predicted band and what a miss would mean
Predicted ~0.90 (0.85-0.95). The golden satisfies every Section A requirement, exhibits zero Section C patterns, and contains no specific the record does not support. If the platform check lands materially below 0.85, the cause is almost certainly configuration, not content - first suspect include_input_files not actually set (the golden-only failure mode of pilot cf00b80c penalized true chart specifics), second suspect register/format judgment drift. Neither would indicate a golden defect; both are grader-side.

## Conditions for the platform check
1. include_input_files=true confirmed on the task before the run (expect + justify the Self-Contained AutoQC warning, KM03/KM04 precedent).
2. Grader file byte-identical to platform/task7/current/grader-guidelines-task7-v2.txt (the 6/11 chart-aware version, 663 words).
3. Read the grader transcript, not just the score, and verify it credited the keep-open behavior under Section C "correct restraint."
