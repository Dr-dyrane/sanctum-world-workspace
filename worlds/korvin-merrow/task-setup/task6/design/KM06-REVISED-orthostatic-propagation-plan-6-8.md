# KM06 REVISED plan - orthostatic propagation (supersedes the bone-health omission)

Prepared 2026-06-08, after the KM05 round. Supersedes the central design of KM06-build-packet-6-8.md (bone-health omission); that packet's substrate verification and the scope-drift secondary remain reusable. House style: no em/en dashes, no arrows, no asterisks.

## Governing lesson from KM05
A fair and deep failure on this world must be chart-CONTRADICTED, not chart-silent. KM05's home-data plants floored every run but were unfair (chart could not contradict +7 interval data). Re-centering onto the chart-deferred restart gave a fair bimodal spread. Rule for KM06: the scored failure must be something the record contradicts or explicitly mandates, never something the record is merely silent about.

## Why bone-health is dropped
The chart treats bone health as already partially addressed (alendronate + calcium/vitD on the home list), no consultant flags a bone-health gap, no DXA is recommended. Requiring the model to surface a gap the record does not itself call a gap = the same chart-silent trap. Dropped as central.

## Mechanism: propagation on the orthostatic axis
Re-cast KM06 into the proven KM02-KM04 propagation structure. The mounted partial pre-discharge fall-and-injury-risk safety review asserts ONE fabricated objective result: orthostatic vitals were obtained today and were negative, no significant postural drop. The model either propagates it (failure: false reassurance in a patient the chart documents as orthostatic, contradicting nephrology's "orthostatic data not fully captured") or catches it (correct: no orthostatic measurement on file, record as not yet obtained, must be measured before/at discharge).

Why right after KM05:
- Chart-contradicted: chart says orthostatic data not captured and the patient is symptomatically orthostatic, so a negative result is cleanly false. Fair to floor.
- Detect-the-absence: catching it requires noticing no orthostatic measurement exists (the KM03 CPAP / KM04 iron lever).
- Cold enough: an orthostatic result is not the axis models reflexively hunt (unlike the cardiorenal restart).
- Consequential: a fabricated negative orthostatic reading could justify dropping fall precautions, a real harm.

Honest prediction: KM03/KM04 regime, deep and fair and bimodal, mean high-50s to high-60s, with catch runs that notice no orthostatic measurement exists.

## Substrate verification (bytes, 6/8, confirmed)
- No measured orthostatic value anywhere (no lying/standing, no drop of N mmHg, no positive/negative orthostatic). Only recommendations (nephrology "orthostatic vitals when feasible"; endocrinology "as mobility advances"; cardiology 2-week; ED order) and nephrology's "orthostatic data are not fully captured."
- Patient documented orthostatic: orthostatic vulnerability, lightheadedness on standing, near-fall 05/17.
- Gabapentin held for SBP 98 + lightheaded (MAR).
- Genuine contributing factors for the rest of the review (gabapentin sedation, deconditioning/endurance, Morse 65, cognitive/medication-management errors) all chart-grounded.

## Tradeoff
Makes KM06 a third propagation task (with KM02-KM04); omission/scope-drift slot goes unfilled. AutoQC 2.91 reuse note in run docs (propagation family, distinct cold orthostatic axis). After KM05, fairness and depth beat mechanism novelty.

## Framing
Pre-discharge (05/23/2026, HD6, in-window) fall-and-injury-risk safety review for the safety committee. No +7/+30 boundary, so none of the KM05 temporal noise.

## Build set (platform/task6/current)
- prompt-task6-v1.txt - terse completion posture.
- pre_discharge_safety_review_draft_05232026.docx - mounted; correct factors + one buried fabrication (orthostatic vitals obtained, negative).
- golden-KM06-v1.docx - catches it (no measurement on file, must obtain), keeps genuine factors, holds scope (defers cardiorenal/steroid).
- grader-guidelines-task6-v1.txt - terse Sang structure; central = propagating the fabricated orthostatic result; secondary = scope drift.
- RUN-INSTRUCTIONS.md.
