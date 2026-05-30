# James Carter Context

Purpose: compressed Claude context for a fresh Project Sanctum session. Use this as operational context only; the full source of truth remains local under `reference/` and `worlds/james-carter/`.

Boundary: Brainstorm is submitted and awaiting Human Review. World Spec drafting is not authorized until Brainstorm Human Review returns GO and Alexander explicitly authorizes drafting.

## Current World Concept

Working title: James Carter World.

Clinical domain: Emergency Medicine / Internal Medicine / acute hospital medicine.

Core idea: a realistic multi-day hospitalization for a medically complex 62-year-old man who presents from home with altered mental status, progressive weakness, poor oral intake, reduced activity, borderline hypotension, AKI on CKD, possible urinary symptoms, and subjective fever.

Initial management as suspected urinary-source sepsis is appropriate. The case becomes difficult because infection improves but the patient does not return cleanly to baseline. The world tests whether an AI can reassess evolving information rather than using the initial sepsis diagnosis as a total explanation.

Design philosophy:

- Do not create a rare disease puzzle.
- Do not make adrenal insufficiency the hidden answer.
- Complexity should come from common hospital medicine: messy documentation, medication changes, consultant tension, functional decline, and discharge safety.
- The AI should demonstrate prioritization, synthesis across documents, uncertainty handling, medication reasoning, source-of-truth reasoning, and safe decision-making when reasonable clinicians disagree.

## Approved Brainstorm Summary

Brainstorm submitted in RL Studio and passed final Brainstorm AutoQC 51/51.

World setup:

- Multi-day ED-to-inpatient hospitalization.
- World closes on Hospital Day 6 at 18:00 during discharge planning.
- Patient is clinically improved but not clearly back to baseline.
- Persistent concerns include weakness, intermittent cognitive concerns, borderline BP, renal recovery, medication changes, steroid timeline uncertainty, and safe discharge planning.

Patient seed:

- 62-year-old male.
- Long-standing type 2 diabetes mellitus.
- Hypertension.
- CKD stage 3.
- HFrEF and CAD history.
- Polypharmacy.
- Polymyalgia rheumatica previously treated with chronic prednisone and recent tapering.
- Lives at home with spouse/family.
- Baseline: independent ADLs, ambulates without major assistance, manages some medications with family support.

## Locked Primary Frictions

1. Nephrology vs Cardiology

- Nephrology prioritizes renal recovery, avoiding recurrent AKI, preventing hypotension, and holding unsafe medications during AKI/hypotension.
- Cardiology prioritizes HFrEF/CAD guideline-directed therapy, avoiding unnecessary withdrawal of protective therapy, preventing HF decompensation, and reducing readmission risk.
- Core tension: immediate renal/hemodynamic safety vs long-term cardiovascular optimization.

2. Family vs Inpatient Medicine

- Family knows baseline function and cognition and worries the patient is weaker, intermittently confused, and unsafe with a changed medication plan.
- Inpatient team sees improved vitals, controlled infection, improving renal function, and acute stabilization.
- Core tension: medically stable on paper vs functionally safe in the real world.

3. Emergency/Inpatient Medicine vs Endocrinology

- ED/inpatient medicine appropriately treated suspected sepsis and wants to avoid unnecessary prolonged steroids once acute infection appears improved.
- Endocrinology recognizes chronic prednisone exposure for PMR, unclear taper history, persistent weakness, borderline hypotension, and overlapping symptoms.
- Core tension: risk of premature steroid withdrawal vs risk of unnecessary steroid continuation.
- Guardrail: this is a risk-interpretation disagreement, not "Endocrinology finds the missed diagnosis."

## Locked World-Level Traps

1. Steroid timeline/source-of-truth trap

- Older rheumatology documentation shows chronic prednisone.
- Later outpatient plan recommended tapering.
- Outpatient med list was not fully updated.
- Admission med rec pulls older information.
- Family is unsure of exact dose.
- Inpatient notes copy forward inconsistent steroid status.
- Correct reasoning reconstructs whether recent steroid exposure creates adrenal suppression risk relevant to management and discharge.

2. HF-AKI medication reconciliation and time-sensitive consultant trap

- ARB/ARNI, diuretic, SGLT2 inhibitor, beta blocker, and other HFrEF/CAD therapies are held or adjusted during AKI/hypotension.
- Early "hold" recommendations may persist visually after renal function and BP evolve.
- Correct reasoning avoids both premature restart and inappropriate long-term omission.

3. Buried functional/cognitive status trap

- Physician notes say clinically improved.
- Nursing, PT, and family documentation carry weakness, intermittent confusion, assistance needs, and medication-management concerns.
- Correct reasoning does not equate improved labs with safe discharge.

4. Sepsis anchoring after partial improvement trap

- Early ED/admission documents correctly emphasize UTI/sepsis.
- Later records show infection improvement but persistent weakness, borderline BP, evolving renal/electrolyte issues, medication changes, functional decline, and steroid timeline questions.
- Correct reasoning recognizes sepsis was real/reasonable initially while avoiding premature closure.

5. Discharge plan source-hierarchy trap

- Draft discharge planning can imply straightforward home discharge.
- Important qualifiers live in medication plan, consultant recommendations, PT/nursing notes, and family communication.
- Correct reasoning understands a reassuring discharge artifact is not the whole source of truth.

## Approved Rough Task Concepts

Use these as rough concepts only. Do not write final prompts, golden responses, or grader guidance.

1. Discharge medication reconciliation / medication safety review
   - Current tracker mapping: P0 Discharge Medication Reconciliation.
   - Requester: hospitalist.
   - Anchor: Hospital Day 7, after world close.
   - Competency: medication action reasoning.

2. Hospital discharge summary generation
   - Current tracker mapping: P0 Hospital Discharge Summary Generation.
   - Requester: attending physician.
   - Anchor: Hospital Day 7, after world close.
   - Competency: narrative fidelity and temporal sequence.

3. Transition-of-care / discharge readiness plan
   - Current tracker mapping: P0 Discharge Planning Documentation.
   - Requester: case manager and hospital medicine team.
   - Anchor: Hospital Day 7, after world close.
   - Competency: disposition safety.

4. Post-hospital follow-up assessment note
   - Current tracker mapping: P0 Transitional Care Management Documentation (TCM).
   - Requester: primary care physician.
   - Anchor: 7 days after discharge.
   - Competency: reassessment after transition.

5. Consultant recommendation synthesis / care coordination note
   - Current tracker mapping: P1 Interdisciplinary Care Plan Development and Documentation.
   - Requester: hospital care team.
   - Anchor: Hospital Day 7, after world close.
   - Competency: consultant-priority synthesis.

6. Readmission risk / patient safety review
   - Current tracker mapping: P0 Patient Risk Stratification Assessment.
   - Requester: quality and patient safety team.
   - Anchor: 30 days after discharge.
   - Competency: retrospective safety analysis.

Reserve only:

- Future ED reassessment after return visit. Do not use unless Alexander later chooses it.

## Current Reviewer Risks

These are World Spec preparation risks, not authorization to change Brainstorm:

- World Spec patient name must be unmistakably synthetic under AutoQC v6.3 Check 2.2.
- World Spec task suite must use 3-5 distinct catalog workflows under Check 2.107; current rough mapping has more distinct workflows than allowed.
- Typical clinical/medical director worlds should include both clinical and healthcare administration work products where appropriate under Check 2.108.
- Decision Friction Table is required if the world depends on 2+ specialty conflicts or embedded diagnostic conflicts under Check 2.14.
- Source-of-truth hierarchy must be documented when authority traps are present under Check 2.65.
- Fact-to-file traceability is a hard requirement under Checks 2.18, 2.48, 2.49, and 2.60.
- Temporal architecture is a blocker gate under Check 2.41.
- Prompts must not telegraph traps under Check 2.31.
- Task independence is a blocker under Check 2.40.
- Failure Design tables need at least 5 grounded traps per task under Check 2.34, without inappropriate duplication under Check 2.91.

## Post-GO Decision Queue

Do not resolve these before Brainstorm Human Review GO unless Alexander explicitly authorizes decision-only planning.

1. Choose final synthetic patient name for World Spec.
2. Choose synthetic MRN format.
3. Confirm demographics, DOB, age, sex, allergies, code status, height, weight, BMI, and relevant social facts.
4. Convert Hospital Day timeline to exact MM/DD/YYYY milestone dates.
5. Approve the world snapshot date/time.
6. Approve source-of-truth hierarchy for conflicting chart evidence.
7. Consolidate final task architecture to 3-5 distinct approved workflows.
8. Decide whether and how to include an administrative deliverable consistent with the existing clinical foundation.
9. Confirm each task remains independent and has one deliverable.
10. Approve traceability workflow before Expected Output, Failure Design, or file plan content is drafted.
11. Plan modalities and trap substrates only after task architecture is settled.

## Claude Use Rules

Claude may:

- organize physician-provided decisions;
- critique against AutoQC and reviewer-risk criteria;
- help prepare decision checklists and consistency audits;
- later help with World Spec drafting only after GO and explicit Alexander approval.

Claude must not:

- invent scenario concept, traps, task ideas, diagnoses, labs, dates, medications, doses, patient identity, MRN, provider names, file inventory, final prompts, golden responses, grader guidance, or failure analysis;
- treat World Spec preparation risks as permission to revise Brainstorm;
- imply World Spec drafting is authorized before Brainstorm GO.
