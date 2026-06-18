# Worked FA/GA examples (gate-clean, approved shape)

Two examples. The OV09 held-medication one is the example to match for the GA, because its GA does the grader audit in full: what the grader got correct, then what it could improve, then calibration. The OV04 image one is the cleanest FA clinical-voice exemplar; note its GA is the older, simpler clinical register that affirms the score without an explicit improvement move. Prefer the OV09 GA shape: when the grader was genuinely sound, still add the improvement point or a stricter-or-looser-reading caveat rather than only affirming.

## Example 1: OV09 - post-acute handoff, three held oral agents resumed at discharge (the GA exemplar)

The lever: the started draft resumes metformin, empagliflozin, and lisinopril at discharge in a routine medication line; the golden keeps all three held for AKI on CKD with restart deferred. The floor leaves the resume line in. Bimodal: floors 0.25 to 0.35, catchers 0.78 to 0.92. FA subject: the second-lowest distinct, a 0.35 run.

### Failure Analysis

On Attempt 10, the model finished the handoff competently. It kept the disposition open, continued insulin, and preserved the accurate antibiotic, wound, therapy, and follow-up items. The failure is the medication line. It left the started draft's resume of metformin, empagliflozin, and lisinopril at discharge in place, and only noted that the attending should decide on restart. It had the hold orders in hand and resumed them.

These three are held for AKI on CKD, creatinine 1.6 from a peak of 2.1. Metformin near an eGFR of 30 risks lactic acidosis, empagliflozin risks euglycemic ketoacidosis during an active infection, and lisinopril worsens the recovering renal function. The note also contradicts itself, holding the agents in one section and resuming them in another, which leaves the unsafe option live for the signing physician. Leaving them resumed is the central failure, and it drives the low scores, 0.25 to 0.35, while the runs that hold them reach 0.92.

### Grader Analysis

The grader scored this correctly. It confirmed the three agents are held for AKI on CKD with no restart entered, saw the resume line carried into the finished note, and made that the deciding error. It gave appropriate credit for the parts the golden keeps: the open disposition, the culture-directed antibiotics with Infectious Disease step-down, wound care, therapy, and insulin. It did not let the model's partial "held" note rescue the answer, since the resume line stands.

One point could improve. The grader labored over whether the partial note counted and read the deduction as a vague caution. The sharper point is that the note keeps the line resuming three held agents, so the deliverable still instructs an unsafe restart, not an incomplete one. Naming that as a distinct error would let it reach 0.35 without inferring it. The number holds: a deep floor would overstate the handoff, and a higher score would ignore three held agents resumed in an unresolved AKI, so 0.35 is well placed.

Note how the GA's second paragraph does the work the affirm-only form skips: it names a concrete improvement (state the retained resume line as a distinct error) before judging calibration. Rating entered in the Studio field: Great. It is not written in the file.

## Example 2: OV04 - off-text CPAP image (the FA clinical-voice exemplar)

The lever: a CPAP adherence report sits in an image file the note must open; the model never opens it and reports OSA as stable on home CPAP. All-low. FA subject: Attempt 9, 0.20.

### Failure Analysis

On Attempt 9, the model produced a solid note from the chart, correctly reconciling medications, summarizing the patient's hospital course, and documenting appropriate follow up plans. However, it missed the main finding in this case. The CPAP compliance report was available as an image file, but the model never opened or reviewed it. Because the report was not reviewed, the model missed the patient's poor CPAP adherence and the evidence of ongoing obstructive sleep apnea. The note stated the patient would continue home CPAP and did not raise any adherence concerns or recommend sleep medicine follow up. Since this information was only present in the device report, the final note was missing an important part of the patient's overall assessment.

### Grader Analysis

The 0.20 score is appropriate. The note accurately captured most aspects of the hospitalization but failed to identify the poor CPAP adherence documented in the compliance report. As a result, the patient's obstructive sleep apnea was presented as stable on home CPAP despite evidence of inadequate treatment. Credit is warranted for the otherwise accurate medication reconciliation, hospital course, and follow up planning. However, the missed CPAP finding was clinically significant and affected the overall assessment, making the assigned score reasonable.

This GA is acceptable and approved, but it is the simpler register: it affirms the score without naming a grader improvement. When you write a new GA, prefer the OV09 shape and add the improvement point or the stricter-reading caveat, because reviewers expect the grader audit to say what the grader could do better, not only that the score is reasonable.
