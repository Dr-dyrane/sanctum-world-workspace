# Clinical Story Skeleton Interview

Status: interview framework only.

Purpose: facilitate the physician interview needed to lock Korvin Merrow's clinical arc before Identity Package, Governance Package, Clinical Story Skeleton, or World Spec drafting.

This document asks questions. It does not answer them.

## Locked Inputs

Do not revisit these decisions during this interview:

- Patient identity: Korvin Merrow.
- World type: Typical Clinical World.
- Hospitalization length: 6 days.
- World close: Hospital Day 6 at 18:00.
- Task anchors: discharge, +7 day, +30 day.
- Core physiology: mixed physiology world.
- Core interaction: infection + steroid + CKD/HF + polypharmacy.
- Clinical evolution: approximately 3-week decline before presentation.
- Tone: medically improving but operationally dangerous discharge.
- Primary failure target: functional decline, disposition safety, discharge readiness reasoning.
- Complexity target: 12-15 comorbidities and 18-22 medications.

## Interview Rules

- Ask for physician decisions before drafting any clinical narrative.
- Keep adrenal/steroid physiology important but not dominant.
- Do not make the near-fall attributable to one cause.
- Preserve multi-causal deterioration.
- Do not create final labs, vitals, document names, dates, or file inventory.
- Do not write task prompts, golden responses, or grader guidance.

## 1. Baseline State

Goal: establish what "not back to baseline" means later.

Questions:

1. What was Korvin's usual functional baseline 1-2 months before admission?
2. What could he do independently at home: bathing, dressing, toileting, cooking, transportation, medication management?
3. Who lives with him, and what support did they provide before this illness?
4. What was his usual mobility status: no device, cane, walker, stairs, falls history?
5. How cognitively intact was he at baseline, and who would notice subtle changes?
6. How controlled were his chronic diseases before the decline: diabetes, heart failure, CKD, PMR symptoms, neuropathy, sleep apnea?
7. Which baseline facts are clinically important for the discharge-readiness trap, and which would be unnecessary filler?

Reviewer challenge:

- If baseline is too healthy, the decline may feel abrupt or contrived.
- If baseline is too impaired, family concern about not returning to baseline becomes less powerful.

## 2. Prednisone / PMR Timeline

Goal: define the steroid uncertainty without turning the case into an adrenal-insufficiency reveal.

Questions:

1. When was PMR diagnosed relative to this hospitalization: years ago, months ago, or recently?
2. What was the broad prednisone course: chronic stable dose, tapering dose, recently stopped, or intermittently restarted?
3. What taper plan did outpatient rheumatology intend?
4. What does the family believe he was taking at home?
5. What does the medication list imply he was taking?
6. What is the clinically actionable uncertainty: current dose, recent stop date, taper speed, adherence, or copy-forward mismatch?
7. How should steroid physiology influence ED/inpatient thinking without becoming the single explanation?
8. What would be unsafe over-treatment with steroids in this patient?
9. What would be unsafe under-treatment or premature withdrawal?

Reviewer challenge:

- Steroid history must create risk interpretation tension, not a hidden final answer.
- The source-of-truth problem must be reconstructable from future chart evidence.

## 3. Early Decline

Goal: define the approximately 3-week decline before presentation.

Questions:

1. What was the first noticeable change during the 3-week decline?
2. Did weakness, appetite decline, lightheadedness, confusion, or urinary symptoms appear first?
3. How did the family interpret the early symptoms?
4. Did Korvin keep taking his medications normally as intake declined?
5. Did he miss meals, fluids, insulin, diuretics, heart failure medications, or prednisone doses?
6. Was there a slow loss of stamina, more daytime sleepiness, more unsteadiness, or new dependence on family?
7. What features should suggest infection was plausible before arrival?
8. What features should suggest infection was not the only process?

Reviewer challenge:

- The decline should not be a vague "felt weak for weeks."
- It should set up dehydration/AKI, medication vulnerability, steroid uncertainty, and functional decline.

## 4. Escalation Phase

Goal: define the final worsening that pushes the family toward ED care.

Questions:

1. Over the final 2-4 days before admission, what changed?
2. How poor was oral intake: less food, less fluid, nausea, early satiety, malaise?
3. What happened with weakness: difficulty standing, reduced walking distance, chair-bound periods, needed assistance?
4. What urinary symptoms were present: dysuria, frequency, urgency, incontinence, dark urine, foul odor, or only family suspicion?
5. What did confusion look like: slowed responses, disorientation, medication mistakes, unusual behavior, waxing/waning attention?
6. Describe the near-fall/lightheadedness event in concept-level terms. What made it concerning?
7. What multiple contributors could plausibly explain the near-fall?
8. Did family call PCP/rheumatology/cardiology before ED, or go directly to ED?

Reviewer challenge:

- Near-fall should remain multi-factorial: volume depletion, infection physiology, BP meds/diuretics, renal/metabolic issues, deconditioning, possible steroid physiology.
- Do not make it a single-cause clue.

## 5. ED Presentation

Goal: define why ED/inpatient sepsis management is reasonable at first contact.

Questions:

1. What specific event made the family seek care that day?
2. What did the ED team see first: altered mental status, borderline hypotension, dehydration, possible UTI, weakness, AKI?
3. What makes suspected urinary-source sepsis a reasonable initial working diagnosis?
4. What early features should push ED/inpatient teams to treat promptly rather than wait for diagnostic certainty?
5. What early features should remain unexplained or only partially explained?
6. What home medication issues should be recognized early?
7. What steroid-history uncertainty should be visible early, if any?

Reviewer challenge:

- Initial sepsis management should be clinically defensible.
- The trap is premature closure after partial improvement, not failure to identify the initial ED problem.

## 6. Hospital Course

Goal: outline the 6-day arc at concept level before dates, labs, or file rows are created.

Questions:

1. What are the major clinical discoveries during hospitalization?
2. What broad interventions occur: antibiotics, fluids, medication holds, renal monitoring, steroid evaluation/management, diabetes adjustments, PT/case management?
3. How does infection concern evolve over the admission?
4. How does renal function evolve conceptually?
5. How does blood pressure/hemodynamic tolerance evolve conceptually?
6. How does functional status evolve conceptually?
7. Which consultants are involved and why: nephrology, cardiology, endocrinology, PT/case management, others?
8. What does each consultant reasonably prioritize?
9. Which recommendations become time-sensitive or outdated as the patient changes?
10. What medication changes occur conceptually without finalizing a discharge med list yet?
11. What problems improve enough to make discharge seem reasonable?
12. What problems persist enough to make discharge risky?

Reviewer challenge:

- This section should create the logic for documents later, not the final document set.
- Avoid final lab values, exact dates, note titles, or file inventory rows.

## 7. Discharge Tension

Goal: define the "medically improved but operationally dangerous" endpoint.

Questions:

1. What objective markers have improved by HD6 18:00?
2. What remains unresolved clinically?
3. What remains unresolved functionally?
4. What medication plan uncertainties remain?
5. What follow-up needs are fragile or easy to miss?
6. What does family see that the inpatient team may under-weight?
7. What does the inpatient team see that makes discharge feel reasonable?
8. What would make home discharge unsafe without additional planning?
9. What would make continued hospitalization or rehab/home health evaluation reasonable?
10. What is the core judgment error an AI agent should be vulnerable to here?

Reviewer challenge:

- Discharge risk should not depend on one buried PT note alone.
- It should require synthesis of medical stabilization, function, medication changes, family concern, and consultant context.

## 8. Multi-Causal Framework Check

Goal: prevent a single-diagnosis skeleton.

Verification questions:

1. Near-fall: list at least four plausible contributors. Which are strongest?
2. Deterioration: what parts are most likely infection-related?
3. Deterioration: what parts are likely dehydration/AKI/poor intake-related?
4. Deterioration: what parts are medication-related?
5. Deterioration: what parts are endocrine/steroid-risk-related?
6. Deterioration: what parts are deconditioning or functional decline?
7. What should remain uncertain even after the hospital course?
8. What would be too neat or too diagnostic-test-like?

Required validation:

- Near-fall is not attributable to a single cause.
- Deterioration remains multi-factorial.
- Steroid physiology is important but not dominant.

## 9. Sanctum World Validation

Goal: confirm the skeleton will support the approved Brainstorm architecture.

### Trap Support

Questions:

1. Does the arc naturally support the steroid timeline/source-of-truth trap?
2. Does it support the HF-AKI medication reconciliation and time-sensitive consultant trap?
3. Does it support the buried functional/cognitive status trap?
4. Does it support sepsis anchoring after partial improvement?
5. Does it support the discharge plan source-hierarchy trap?
6. Are any traps currently unsupported by the story?

### Friction Support

Questions:

1. Does the arc naturally create Nephrology vs Cardiology tension?
2. Does it create Family vs Inpatient Medicine tension?
3. Does it create Emergency/Inpatient Medicine vs Endocrinology tension without making endocrinology the hero?
4. Are any frictions actually information traps rather than people/perspective conflicts?

### Failure Target Support

Questions:

1. Does the story primarily test functional decline, disposition safety, and discharge readiness reasoning?
2. Does the case remain common hospital medicine rather than rare-disease puzzle?
3. Does the story make it plausible that a competent but rushed clinician could be falsely reassured?

### Future Task Architecture Support

Questions:

1. Does the story support discharge medication reconciliation?
2. Does it support discharge summary generation?
3. Does it support transition-of-care/discharge readiness planning?
4. Does it support post-hospital follow-up assessment?
5. Does it support consultant recommendation synthesis?
6. Does it support readmission risk/patient safety review?
7. Does any task concept feel weak, duplicative, or unsupported by the developing arc?

## Readiness Assessment

Ready for Clinical Story Skeleton Interview.

No blockers identified for the interview framework. The next step is to ask Alexander these questions section by section and record physician answers before creating any Clinical Story Skeleton.

