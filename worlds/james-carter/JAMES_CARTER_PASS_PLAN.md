# James Carter World Pass Plan

This is the world-specific build plan for James Carter. It preserves the seed and open decisions without drafting final clinical content.

## Clinical Seed

Role perspective: Emergency Medicine / Internal Medicine physician managing undifferentiated adult patients in acute hospital settings and coordinating care across specialties.

Core scenario seed:

- 62-year-old male
- Diabetes mellitus
- Hypertension
- Chronic kidney disease
- Cardiovascular comorbidity risk
- Medication complexity
- Possible steroid exposure history
- Presents with altered mental status, progressive weakness, poor oral intake, and borderline hypotension
- Initial working diagnosis: sepsis
- Case evolves beyond first impression

Competing clinical concerns:

- Adrenal insufficiency from previous steroid exposure
- Acute kidney injury
- Electrolyte abnormalities
- Medication-related complications
- Possible cardiac involvement
- Discharge safety concerns

Design principle:

- Do not make this a rare disease puzzle.
- Complexity should come from common diseases, messy documentation, competing priorities, and evolving information.

## Questions Remaining

World Setup:

- What is the intended hospital timeline: ED-only, short admission, multi-day stay, or admission plus return visit?
- What is the world snapshot event and approximate endpoint?
- What is James Carter's baseline kidney function and CKD stage?
- What is his diabetes treatment pattern and degree of control?
- What cardiovascular history is confirmed vs risk-only?
- What exactly is known, suspected, or ambiguous about prior steroid exposure?
- What precipitated poor oral intake and weakness?
- Is infection real, suspected-but-not-confirmed, or one part of a broader picture?

Clinical Arc:

- Is adrenal insufficiency ultimately confirmed, treated empirically, or left as a competing concern?
- What electrolyte pattern should drive concern without making the answer too obvious?
- What medication-related complications are plausible and central?
- What cardiac issue matters: chronic protective meds, demand ischemia, arrhythmia, heart failure risk, or another issue?
- What discharge safety concern should create realistic tension?

Workflow Design:

- What 5-8 task categories are most representative of EM/IM hospital work?
- Which tasks are P0 workflows once mapped to the approved tracker?
- What must be answerable from world files alone?
- Which traps are world-level vs task-level?

## Expected Frictions

These are candidate people/perspective conflicts. Alexander must confirm final choices.

1. Emergency/inpatient team vs endocrinology
   - Emergency/inpatient team prioritizes immediate stabilization and sepsis management.
   - Endocrinology questions adrenal crisis/adrenal insufficiency contribution and steroid strategy.

2. Nephrology vs cardiology
   - Nephrology prioritizes AKI recovery and medication safety.
   - Cardiology weighs restarting or continuing long-term cardiovascular protective medications.

3. Family/caregivers vs inpatient team
   - Family/caregivers believe the patient has not returned to baseline.
   - Inpatient team may view discharge criteria as met based on vitals/labs and acute stabilization.

4. Primary team vs documentation inertia
   - Primary team needs current synthesis.
   - Prior notes, med lists, and consultant recommendations may lag behind the evolving clinical picture.

Reviewer risk:

- Friction 4 may read like an information trap rather than a stakeholder conflict unless tied to people, roles, or decision ownership.

## Expected Traps

These are candidate information problems. Alexander must confirm final choices.

- Copy-forward errors in progress notes or medication lists.
- Outdated home medication list carried into admission or discharge.
- Conflicting source-of-truth documents for medications or steroid exposure.
- Buried nursing observations about mental status, intake, orthostasis, weakness, or family concern.
- Lab timing errors, especially if early labs are treated as current.
- Consultant recommendations becoming outdated as renal function, vitals, or endocrine suspicion evolves.
- Discharge medication reconciliation mistakes involving held/restarted antihypertensives, diabetic medications, steroids, or cardiac medications.
- Source hierarchy ambiguity between attending plan, consultant notes, MAR/orders, patient/family report, and outpatient medication history.

Reviewer risks:

- Traps must not be solvable from a single file.
- Traps should require chart synthesis, not diagnosis recognition alone.
- Adrenal insufficiency must not function as a zebra reveal.
- Medication traps must be clinically meaningful but fair.

## Rough Task Categories

These are candidate categories only, not final task prompts.

- Emergency department assessment or handoff documentation
- Inpatient admission H&P
- Daily progress note or hospitalist reassessment
- Discharge medication reconciliation
- Hospital discharge summary
- Consultant synthesis or response to competing recommendations
- Post-discharge follow-up planning or transition-of-care documentation
- Patient safety or quality review if a medication/documentation miss causes harm

Reviewer risks:

- Tasks must map to approved workflow categories.
- At least one should be P0.
- Each task must produce a concrete evaluable output.
- Tasks must be independent and anchored after the world snapshot.
- Task ideas should not become production prompts during onboarding unless phase changes later.

## Must Be Decided Before Brainstorm Upload

- Final timeline shape at concept level.
- Short World Setup paragraph content.
- At least two confirmed frictions with stakeholders and positions.
- A credible set of major traps with type, mechanism, likely source/location, and world-level vs task-level status.
- 5-8 rough task ideas with deliverable categories and which frictions/traps they test.
- Self-containment argument: why a seasoned clinician could solve from intended files alone.
- Why the world is realistic hospital medicine, not a rare disease puzzle.
- Which clinical uncertainties remain intentionally unresolved vs which are simply undecided.

## Must Wait Until World Spec

- Full clinical timeline and exact dates.
- Detailed patient profile table.
- Exact medication list, doses, frequencies, and changes.
- Exact lab values and lab trend dates.
- Exact consultant note content.
- World snapshot date.
- Key milestones table.
- File inventory and filenames.
- Detailed file descriptions.
- Failure design tables.
- Task-level file plan.
- Draft task prompts, which must be human-written by Alexander.
- Expected outputs and grading anchors.
- Data hierarchy note if source conflicts are central.

## Build Sequence For James Carter

1. Pass 1: Interview Alexander for Brainstorm section answers.
2. Pass 2: Draft Brainstorm from Alexander's answers.
3. Pass 3: Audit Brainstorm for reviewer risks.
4. Pass 4: Prepare official Claude Brainstorm pass/check.
5. Pass 5: Final physician review.
6. Pass 6: Upload to RL Studio and clear Brainstorm AutoQC.
7. Pass 7: Address reviewer feedback until Brainstorm GO.
8. Pass 8: Begin World Spec interview only after Brainstorm GO.

