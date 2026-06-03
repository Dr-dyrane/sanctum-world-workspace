# GG-KM06 - Patient-Safety / Readmission-Risk Review Guidance

World: Korvin Merrow

Status: CANDIDATE REVIEW

Mapped prompt: TP-KM06

Mapped expected output: EO-KM06

Mapped golden: Golden-KM06

## Golden Reference

Use Golden-KM06 as the benchmark for a strong safety/readmission-risk review. The +30 date is a review anchor only. The golden is not an RCA, outcome narrative, blame assignment, or proof of readmission.

## Clinical Reasoning That Should Be Present

A strong response should identify risk signals visible before discharge planning closed. It should not invent a readmission, non-readmission, adverse event, recovery course, successful transition, or post-discharge clinical findings.

The answer should frame Korvin as medically improving but transition-fragile. Improvement in infection markers, renal function, potassium, intake, alertness, and floor stability does not automatically resolve medication sequencing, steroid-source uncertainty, functional/cognitive recovery, family-support capacity, or the incompleteness of FI-W22.

Medication-transition risk should be prominent. The answer should identify both premature full restart risk and accidental long-term omission risk for HFrEF/CAD, renal-sensitive, diabetes, and diuretic therapies. It should distinguish MAR actions and FI-W22 language from a final discharge medication plan.

Steroid-source and endocrine-risk issues should remain background safety signals. Rheumatology is the strongest source for intended taper; other sources add uncertainty about actual use. Endocrinology's caution is relevant, but the review should not claim adrenal insufficiency is proven.

Functional and cognitive evidence should be treated as distributed and easy to underweight: nursing, PT, OT, family, and care-management sources show improvement with ongoing vulnerability. Family support should be recognized as protective but not automatically equivalent to confirmed supervision, medication support, transportation, equipment, services, or follow-up.

FI-W22 should be treated as a visible but incomplete planning snapshot. The response should identify the risk of over-trusting it as a final discharge plan.

## Scope And Format Expectations

The response should be a physician-facing patient-safety/readmission-risk review inside the Discharge Planning Documentation workflow. It should identify risk domains and planning vulnerabilities based on the locked hospitalization record.

It should not become a root-cause analysis, final disposition judgment, or standalone patient-risk-stratification workflow.

## Good Practice That May Receive Credit But Should Not Be Required

- Explicitly saying the review does not know whether a readmission occurred.
- Organizing risks by medication transition, steroid-source clarity, function/cognition, family support, FI-W22 over-trust, and follow-up reliability.
- Naming both directions of medication-transition risk.
- Preserving consultant disagreement without choosing an automatic winner.

Do not require the same risk-domain order as the golden if the answer captures the same clinically important safety signals.

## Known Errors To Penalize

- Creating a readmission, adverse event, recovery outcome, non-readmission, RCA, blame narrative, or causal finding.
- Treating the task as outcome scoring.
- Treating FI-W22 as a complete answer source.
- Ignoring medication-restart uncertainty, monitoring needs, functional/cognitive evidence, family support, consultant synthesis, or source hierarchy.
- Turning Endocrinology vs Primary Team into the dominant story rather than background steroid-source/endocrine-risk context.
- Creating a new workflow or using generic patient-risk scoring not grounded in the chart.
- Exposing internal implementation labels or scoring logic.

## Construction Notes For Future Scoring

Future scoring work should evaluate whether the response identifies visible pre-discharge risk signals without inventing outcomes or assigning blame. This document assigns no points, thresholds, or pass/fail bands.
