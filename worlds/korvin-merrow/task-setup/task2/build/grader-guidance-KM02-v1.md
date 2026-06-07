# Grader Guidance KM02 v1 - Hospital Discharge Summary (task grader, derived from GG-KM02)

World: Korvin Merrow

Status: CANDIDATE REVIEW. Derived from locked GG-KM02 with two scope corrections (culture and antibiotic), verified against the agent-read world docx. Native structure, no weighting or score-band language.

Mapped prompt: TP-KM02

Mapped expected output: EO-KM02

Mapped golden: Golden-KM02

## Golden Reference

Use Golden-KM02 as the benchmark for a strong discharge-summary synthesis. The golden demonstrates the expected clinical story, but a response should receive credit when it faithfully summarizes the hospitalization with different wording, ordering, or emphasis.

## Clinical Reasoning That Should Be Present

A strong response should summarize the admission as a mixed-physiology hospitalization that began with a reasonable suspected urinary-source infection frame. It should not copy the ED/admission sepsis impression forward as the entire discharge narrative.

The response should include the approximate three-week decline, admission on 05/18/2026, weakness, poor intake, lightheadedness/near-fall, family-noticed confusion, possible urinary symptoms, medication-management mistakes, AKI on CKD, HFrEF/CAD medication complexity, diabetes, PMR/chronic prednisone exposure, and functional decline.

The hospital course should be organized by evolution. HD1-HD2 should reflect acute stabilization, infection-oriented treatment, cautious renal/hemodynamic management, and medication holds or reassessment. HD3-HD4 should reflect the emergence of functional/cognitive concerns, consultant input, and prednisone-source reconstruction. HD5-HD6 should reflect medical improvement with unresolved transition questions.

The summary should preserve consultant chronology and medication uncertainty without creating a final medication reconciliation. It should describe Cardiology and Nephrology as having defensible but different emphases and should describe Endocrinology's steroid-risk concern without proving a single endocrine diagnosis.

Functional and discharge planning evidence should be visible. Credit summaries that integrate nursing, PT, OT, family, and care-management evidence showing improvement without a clean return to baseline.

## Scope And Format Expectations

The answer should read like a discharge-summary clinical narrative, not a problem-list dump or final order set. It may be organized by hospital course, active problems, or major clinical domains if the evolution and unresolved transition issues remain clear.

FI-W22 should be used as discharge-facing planning context, not as the completed summary. The response should preserve unresolved follow-up needs around medication sequencing, renal/potassium/BP monitoring, steroid instruction clarity, functional support, family education, and outpatient follow-up.

## Good Practice That May Receive Credit But Should Not Be Required

- Explicitly separating "initial working diagnosis" from "final hospital-course synthesis."
- Describing medical improvement and transition risk in the same paragraph.
- Listing major active hospital problems in a clinically coherent order.
- Naming why family concern is baseline-informed rather than generic resistance.
- Naming the documented empiric antibiotic regimen (ceftriaxone 1 g IV q24h with oral step-down to cefpodoxime 200 mg PO BID, completion versus continuation to be reconciled at discharge) is a correct world fact and is creditable. It is not required, and a response that keeps the antibiotic general is acceptable. A response that names a different agent, or that narrows by culture, is unsupported.

Do not require a specific discharge-summary template if the answer is clinically faithful and complete enough for the task.

## Known Errors To Penalize

- Copy-forward sepsis-only framing.
- Saying infection was false, steroids explain everything, or adrenal insufficiency is established without support.
- Stating a finalized urine culture result is incorrect because the chart documents none: a named organism, a sensitivity profile, a no-growth or cultures-negative result, or narrowing the antibiotic by culture, is unsupported. Reporting the documented status (urinalysis with pyuria, positive leukocyte esterase, and bacteriuria; urine culture with preliminary growth and speciation and sensitivities pending; never narrowed; blood cultures pending) is correct and creditable.
- Inventing a final steroid diagnosis, post-discharge symptoms, services, visits, readmission, or outcomes.
- Creating a final medication plan or final discharge disposition rather than a summary.
- Omitting consultant chronology.
- Omitting functional, cognitive, family, or discharge-readiness context.
- Treating FI-W22 as the completed discharge summary.
- Exposing internal implementation labels or grading logic.

## Construction Notes For Future Scoring

Future scoring work should evaluate whether the answer reconstructs the hospital course, preserves mixed physiology, integrates key evidence domains, and avoids unsupported closure. This document assigns no points, thresholds, or pass/fail bands.
