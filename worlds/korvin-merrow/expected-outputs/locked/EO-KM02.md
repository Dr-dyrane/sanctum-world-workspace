# EO-KM02 - Hospital Discharge Summary

Expected Output ID: EO-KM02

Mapped Prompt: TP-KM02

Mapped Workflow: Hospital Discharge Summary Generation

Primary Task Context: FI-T02

Status: CANDIDATE REVIEW

Boundary: this is an expected-output draft. It is not a golden response, scoring key, grader guideline, grading document, AutoQC response, DOCX discharge summary, or submission artifact.

## Expected Senior-Clinician Output

The discharge summary should tell the story of a medically complex admission that began with a reasonable suspected urinary-source infection frame and evolved into a broader synthesis problem. It should not copy the ED or admission problem list forward as if it fully explains the hospitalization.

The expected narrative should describe Korvin Merrow as a 62-year-old man with HFrEF, CAD with remote PCI/stent, CKD stage 3, type 2 diabetes, PMR with chronic prednisone exposure and recent taper uncertainty, diabetic neuropathy, OSA, anemia of CKD, steroid-related bone disease, obesity, GERD, constipation tendency, and polypharmacy. He presented on 05/18/2026 after approximately 3 weeks of decline with weakness, poor intake, lightheadedness/near-fall, family-noted confusion, possible urinary symptoms, and medication-management mistakes. The summary should acknowledge that sepsis-oriented ED and admission management was clinically appropriate.

The hospital course should be organized by evolution. HD1-HD2 involved acute stabilization, infection-oriented treatment, cautious volume/renal/hemodynamic management, and early medication holds or reassessments. The summary should note that the patient became less acutely ill but remained weak, cognitively slower than baseline, and vulnerable to medication and renal/hemodynamic issues. HD3 should mark the emergence of functional and cognitive concerns as clinically important rather than minor residual symptoms. HD4 should mark availability of rheumatology prednisone provenance, consultant tension, and the need to reconstruct steroid history without converting it into a single hidden diagnosis. HD5-HD6 should describe medical improvement with discharge planning becoming plausible, while medication timing, steroid instructions, family concerns, functional reserve, and transition logistics remained active issues before final discharge decisions.

The summary should handle medications as part of the course, not as a final medication reconciliation. It should mention that renal/hemodynamic-sensitive HFrEF, diabetes, diuretic, mineralocorticoid antagonist, SGLT2 inhibitor, and metformin decisions required reassessment as renal function and clinical status improved. It should preserve that cardiology and nephrology had defensible but different emphases around HFrEF/CAD protection versus renal, potassium, blood pressure, intake, and monitoring safety.

The endocrine/steroid section should say that prednisone history was inconsistent across patient recollection, family report, medication reconciliation, pharmacy history, and rheumatology documentation. Rheumatology documentation clarified intended cautious taper and chronic exposure but did not prove actual pre-admission adherence. Endocrinology viewed steroid risk as clinically relevant but not proven as the sole explanation. The summary should avoid documenting adrenal insufficiency as established unless the chart evidence actually establishes it.

Functional and discharge planning should be visible. Nursing, PT, OT, family communication, and case management/social work sources showed improvement but not a clean return to baseline: ongoing cueing, fatigue, transfer/ambulation limitations, ADL and medication-management vulnerability, family concern, and support/logistics questions. The summary should include the family concern as baseline-grounded and clinically relevant, while also preserving that the primary team had a defensible reason to continue discharge planning because objective medical markers improved.

FI-W22 should be treated as a useful discharge-facing snapshot, not as the discharge summary itself. The expected summary should reconcile FI-W22 with the broader chart and state unresolved follow-up needs around medication sequencing, renal/potassium/BP monitoring, steroid plan clarity, functional support, family education, and outpatient follow-up.

## Expected Shape

A clinically appropriate summary should include:

- reason for admission and initial working diagnosis;
- relevant baseline and comorbidity context;
- hospital course by clinical evolution rather than copied problem list;
- consultant chronology and unresolved recommendation synthesis;
- medication safety and steroid-source caveats;
- functional/cognitive/discharge-readiness context;
- discharge-planning caveats and follow-up needs evident before the transition.

## Prohibited Drift

The output should not create new post-discharge facts, final outcomes, new diagnoses, completed discharge orders, scoring language, or internal implementation labels. It should not state that infection was false, that steroids explain everything, or that FI-W22 alone is the completed discharge summary.
