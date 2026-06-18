# Worked FA/GA examples (gate-clean, approved shape)

The OV11 example below is the current gold for the full voice. It opens "On trajectory N", names only the analyzed run, states the writer's score in the first person, and uses short breathable sentences. Match it. The OV09 and OV04 examples are kept for the GA grader-audit shape and the FA clinical texture, but they predate the single-run, breath, and first-person-score rules. Do NOT copy their "On Attempt N" openers, their score-range mentions (0.25 to 0.35, 0.92), or their long sentences. Self-check every draft: run `python3 tools/verify/lint_fa_ga.py <file>` and clear all FAILs before handing back.

## Current gold example (match this): OV11 - primary-care transition, immunization over-closure

The lever: a care-coordination review attests immunizations reviewed and up to date; the chart has no immunization record anywhere. The floor carries the attestation forward. Uniform, no catcher. FA subject: trajectory 3, 0.12. The distribution lives in the Status line, never the body.

### Failure Analysis

On trajectory 3, the model finished the summary competently. The hospital course is accurate. The attending-action items are right. The added detail checks out against the chart. The failure is the immunization line, where the model carried the 05/23 care-coordination review's closure forward unchanged. It still reads: immunizations reviewed and up to date, none indicated this admission.

No immunization record exists anywhere in the chart. No history, no administration, no review. The 04/30 outpatient summary lists only the dilated eye and foot exams. The review attested a review that never happened. The model listed it as current, no flag. This summary is built for signature. Attesting immunizations as addressed closes a real preventive-care gap in a diabetic with chronic kidney disease and routes nothing to outpatient primary care. This is a documentation-integrity failure, not a wording preference. The failure caps the run low. Based on these, I score it 0.10 in this trajectory.

### Grader Analysis

The grader scored trajectory 3 at 0.12 against the golden and guidelines. That is right. It searched the chart and confirmed the only immunization mention is the care-coordination review. It named the carried-forward closure the central failure. It held the score low even though the rest of the summary was thorough. It noted the model did not even flag the line. That is weaker than flagging it and still attesting.

One point would make it more robust. The grader called the health-maintenance section strong. It did not check the added specifics against the chart for invented detail, which the guidance asks for. Those additions are chart-accurate, so the miss was harmless. But the check was skipped. By its own reasoning, an unflagged carry-forward is worse than flagging and still attesting. That argues for a notch below 0.12, near my 0.10. The 0.12 is still defensible. A zero would understate an otherwise faithful note. A midline score would ignore the unverified line the task turns on.

Copy from OV11: the "On trajectory N" opener, the one-idea-per-sentence cadence, the single-run focus (only 0.12 and the writer's 0.10 appear, never the spread), and the first-person close. Rating entered in the Studio field: Great. It is not written in the file.

## Example 1: OV09 - post-acute handoff, three held oral agents resumed at discharge (the GA exemplar)

The lever: the started draft resumes metformin, empagliflozin, and lisinopril at discharge in a routine medication line; the golden keeps all three held for AKI on CKD with restart deferred. The floor leaves the resume line in. Bimodal: floors 0.25 to 0.35, catchers 0.78 to 0.92. FA subject: the second-lowest distinct, a 0.35 run.

### Failure Analysis

On Attempt 10, the model finished the handoff competently. It kept the disposition open, continued insulin, and preserved the accurate antibiotic, wound, therapy, and follow-up items. The failure is the medication line. It left the started draft's resume of metformin, empagliflozin, and lisinopril at discharge in place, and only noted that the attending should decide on restart. It had the hold orders in hand and resumed them.

These three are held for AKI on CKD, creatinine 1.6 from a peak of 2.1. Metformin near an eGFR of 30 risks lactic acidosis, empagliflozin risks euglycemic ketoacidosis during an active infection, and lisinopril worsens the recovering renal function. The note also contradicts itself, holding the agents in one section and resuming them in another, which leaves the unsafe option live for the signing physician. Leaving them resumed is the central failure, and it drives the low scores, 0.25 to 0.35, while the runs that hold them reach 0.92.

### Grader Analysis

The grader scored this correctly. It confirmed the three agents are held for AKI on CKD with no restart entered, saw the resume line carried into the finished note, and made that the deciding error. It gave appropriate credit for the parts the golden keeps: the open disposition, the culture-directed antibiotics with Infectious Disease step-down, wound care, therapy, and insulin. It did not let the model's partial "held" note rescue the answer, since the resume line stands.

One point could improve. The grader was unsure whether the partial note counted and read the deduction as a vague caution. But the note keeps the line resuming three held agents, so the deliverable still instructs an unsafe restart, not an incomplete one. Naming that as a distinct error would let it reach 0.35 without inferring it. The number holds: a deep floor would overstate the handoff, and a higher score would ignore three held agents resumed in an unresolved AKI, so 0.35 is well placed.

Note how the GA's second paragraph does the work the affirm-only form skips: it names a concrete improvement (state the retained resume line as a distinct error) before judging calibration. Rating entered in the Studio field: Great. It is not written in the file.

## Example 2: OV04 - off-text CPAP image (the FA clinical-voice exemplar)

The lever: a CPAP adherence report sits in an image file the note must open; the model never opens it and reports OSA as stable on home CPAP. All-low. FA subject: Attempt 9, 0.20.

### Failure Analysis

On Attempt 9, the model produced a solid note from the chart, correctly reconciling medications, summarizing the patient's hospital course, and documenting appropriate follow up plans. However, it missed the main finding in this case. The CPAP compliance report was available as an image file, but the model never opened or reviewed it. Because the report was not reviewed, the model missed the patient's poor CPAP adherence and the evidence of ongoing obstructive sleep apnea. The note stated the patient would continue home CPAP and did not raise any adherence concerns or recommend sleep medicine follow up. Since this information was only present in the device report, the final note was missing an important part of the patient's overall assessment.

### Grader Analysis

The 0.20 score is appropriate. The note accurately captured most aspects of the hospitalization but failed to identify the poor CPAP adherence documented in the compliance report. As a result, the patient's obstructive sleep apnea was presented as stable on home CPAP despite evidence of inadequate treatment. Credit is warranted for the otherwise accurate medication reconciliation, hospital course, and follow up planning. However, the missed CPAP finding was clinically significant and affected the overall assessment, making the assigned score reasonable.

This GA is acceptable and approved, but it is the simpler register: it affirms the score without naming a grader improvement. When you write a new GA, prefer the OV09 shape and add the improvement point or the stricter-reading caveat, because reviewers expect the grader audit to say what the grader could do better, not only that the score is reasonable.
