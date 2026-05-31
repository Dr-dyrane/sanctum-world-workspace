# Handoff State

Purpose: enable a brand-new Claude session to resume accurately without stale assumptions.

## Where We Are

Project Sanctum onboarding is in Phase 1 World Building, but only steps 1-6 are in scope.

The Brainstorm for Korvin Merrow World has been completed, passed AutoQC, uploaded to RL Studio, returned SEND BACK from Human Review, remediated, reuploaded, resubmitted, and approved by Stacey S.

RL Studio:

- Task ID: `cyau8803`
- Status: Brainstorm approved / ready for World Spec transition
- Brainstorm AutoQC: revised run `0 failed / 51 passed`
- Diagnostics reviewed: yes
- Human Review: GO from Stacey S
- Approval source: Slack / Stacey S
- Reviewer message: "great job! I approved your brainstorm. Next steps are to move forward with world spec and file template development."

Current state: Identity Package v1 locked / ready for Governance Package. World Spec drafting has not started and remains gated on explicit Alexander authorization.

## Locked Decisions

Locked from approved Brainstorm:

- Acute hospital medicine world, ED to inpatient admission.
- Multi-day hospitalization ending at Hospital Day 6 at 18:00 during discharge planning.
- Patient seed: 62-year-old male with T2DM, HTN, CKD stage 3, HFrEF, CAD, hyperlipidemia, anemia of CKD, osteoporosis/osteopenia from chronic steroid exposure, obstructive sleep apnea, diabetic peripheral neuropathy, polypharmacy, PMR with prior chronic prednisone and recent taper.
- Presentation: AMS, progressive weakness, poor oral intake, reduced activity, borderline hypotension, AKI on CKD, possible urinary-source infection.
- Initial suspected sepsis treatment is appropriate.
- Complexity evolves from overlapping common hospital contributors, not from a single rare diagnosis.

Locked primary frictions:

1. Nephrology vs Cardiology.
2. Family vs Inpatient Medicine.
3. Emergency/Inpatient Medicine vs Endocrinology.

Locked world-level traps:

1. Steroid timeline/source-of-truth trap.
2. HF-AKI medication reconciliation and time-sensitive consultant trap.
3. Buried functional/cognitive status trap.
4. Sepsis anchoring after partial improvement trap.
5. Discharge plan source-hierarchy trap.

Approved rough task concepts:

1. Discharge medication reconciliation / medication safety review.
2. Hospital discharge summary generation.
3. Transition-of-care / discharge readiness plan.
4. Post-hospital follow-up assessment note.
5. Consultant recommendation synthesis / care coordination note.
6. Readmission risk / patient safety review.

Reserve only:

- Future ED reassessment after return visit.

Approved Brainstorm remediation additions:

- World Type: Typical Clinical World.
- Medication list: sacubitril/valsartan 24/26 mg BID; carvedilol 12.5 mg BID; furosemide 40 mg daily; spironolactone 25 mg daily; empagliflozin 10 mg daily; aspirin 81 mg daily; atorvastatin 40 mg nightly; metformin ER 500 mg BID; insulin glargine 18 units nightly; prednisone with inconsistent documented taper/dose; alendronate 70 mg weekly; calcium/vitamin D daily; ferrous sulfate 325 mg every other day; gabapentin 300 mg nightly.
- Active DOCX: `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx`.

Post-kickoff physician-locked decisions:

- Temporal architecture: 6-day hospitalization; HD6 18:00 world close; discharge anchor; +7 day anchor; +30 day anchor.
- Underlying clinical story: mixed physiology world with infection, steroid issues, CKD/HF, and polypharmacy interaction. Not a single-diagnosis world.
- Presentation trigger: progressive weakness, poor oral intake, near-fall/lightheadedness, family-noticed confusion, possible urinary symptoms.
- Clinical evolution: approximately 3-week decline before presentation.
- World tone: medically improving but operationally dangerous discharge.
- Primary failure target: functional decline, disposition safety, discharge readiness reasoning.
- Complexity targets: exceed reviewer minimums; target 12-15 comorbidities and 18-22 medications.
- Durable record: `worlds/korvin-merrow/world-spec-prep/physician-decision-log-01.md`.

Locked Clinical Story Skeleton v1:

- Patient: Korvin Merrow, 62-year-old male, Typical Clinical World.
- Baseline: lives with family; independent but slowed by chronic illness; occasional cane use; mild age-related forgetfulness only; chronic diseases generally stable before current decline.
- PMR/prednisone: several-year PMR history, chronic prednisone exposure, multiple prior flares and taper attempts, recent taper due to controlled symptoms, and reconstructable source-of-truth inconsistencies.
- Pre-hospital decline: approximately 3 weeks of reduced stamina, reduced activity, poor appetite, reduced fluid intake, increasing weakness, increasing family dependence, possible urinary symptoms, progressive unsteadiness, and progressive cognitive slowing.
- Escalation: medication-management mistakes, increased dependence, lightheadedness, near-fall event, and family recognition of meaningful deviation from baseline.
- ED presentation: suspected urinary-source infection, dehydration, AKI risk, altered baseline mental status, functional decline, and reasonable sepsis-oriented management. Infection is a contributor, not the entire explanation.
- Hospital course: HD1 admission/stabilization; HD2 partial improvement and consultant involvement begins; HD3 PT/OT identify functional concerns; HD4 consultant tensions emerge and steroid-history inconsistencies are recognized; HD5 medical improvement continues and disposition questions become dominant; HD6 patient appears medically improved but discharge remains debatable.
- Discharge state: infection, AKI, hemodynamics, mental status, and oral intake improved, while functional reserve, medication restart strategy, steroid interpretation, family concern, and disposition risk remain unresolved.
- Primary failure target: disposition safety, functional decline recognition, and discharge-readiness reasoning.
- Near-fall framework: multi-factorial and not attributable to a single cause.
- Review artifact: `worlds/korvin-merrow/world-spec-prep/clinical-story-skeleton-review.md`.
- Lock record: `worlds/korvin-merrow/world-spec-prep/physician-decision-log-02.md`.
- Ratification artifact: `worlds/korvin-merrow/world-spec-prep/clinical-story-skeleton-ratification.md`.

Ratified governance/story-logic guardrails:

- Endocrine friction label is Endocrinology vs Primary Team.
- Do not use Endocrinology vs Documentation. Documentation is evidence, not a friction participant.
- Steroid-record discrepancy remains a trap.
- Prednisone Source-of-Truth Hierarchy: rheumatology attending recommendation > verified medication reconciliation > pharmacy / refill history > family report > patient recollection.
- Family vs Primary Team is balanced: family concern is defensible, and primary team discharge reasoning is also defensible.
- Near-fall is intentionally multi-factorial with no single intended explanation.

Locked Identity Package v1:

- Name: Korvin Merrow.
- DOB: 1964-02-18.
- Age: 62.
- MRN: KM-6427819.
- Height: 178 cm (5'10").
- Weight: 97 kg (214 lb).
- BMI: 30.6.
- Allergy: Lisinopril (cough).
- Code Status: Full Code.
- Artifact: `worlds/korvin-merrow/world-spec-prep/identity-package-v1.md`.
- Age 62 is consistent with DOB for a 2026 encounter after 2026-02-18.
- BMI 30.6 is consistent with 97 kg and 178 cm.

## Decisions Remaining

Do not answer these without Alexander.

Identity/compliance:

- Identity Package v1 is locked.
- Later calendar skeleton must preserve DOB/age consistency unless Alexander explicitly reopens DOB or age.

Clinical scenario:

- Exact calendar dates for ED arrival, admission course, world snapshot, and task anchors.
- Key milestone list.
- Source-of-truth hierarchy for conflicting evidence.

Task architecture:

- Consolidation from current rough mappings to 3-5 distinct approved catalog workflows.
- Whether/how to include a healthcare administration deliverable.
- Final task independence, requester, anchor, and one-deliverable discipline.

Traceability/file strategy:

- Evidence provenance workflow.
- Later file modalities.
- Later trap substrate planning.
- No final file inventory yet.

## Verified World Spec Risks

Use these as future World Spec priorities only after Brainstorm GO:

- AutoQC 2.2: patient name must be unmistakably synthetic.
- AutoQC 2.3: MRN must be clearly synthetic.
- AutoQC 2.14: Decision Friction Table required when 2+ conflicts exist.
- AutoQC 2.18 and 2.48: clinical facts and Expected Output facts must trace to narrative or file rows.
- AutoQC 2.41: temporal architecture is a blocker gate.
- AutoQC 2.65: source-of-truth hierarchy required when authority traps are present.
- AutoQC 2.98: workflow names must match approved tracker exactly.
- AutoQC 2.107: final world must use 3-5 distinct catalog workflows.
- AutoQC 2.108: typical clinical/medical director worlds should include clinical and healthcare administration work products where appropriate.

## Next Legal Action

Use `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md`, `worlds/korvin-merrow/world-spec-prep/physician-decision-log-02.md`, `worlds/korvin-merrow/world-spec-prep/clinical-story-skeleton-ratification.md`, and `worlds/korvin-merrow/world-spec-prep/identity-package-v1.md` for orientation.

Wait for Alexander to explicitly start Governance Package.

If Alexander starts Governance Package:

1. Read `project/STATUS.md`, `project/PASS_PLAN.md`, `WORLD_SPEC_KICKOFF.md`, `physician-decision-log-02.md`, `clinical-story-skeleton-ratification.md`, and `identity-package-v1.md`.
2. Use only locked physician decisions, the ratified Clinical Story Skeleton, locked Identity Package, and approved Brainstorm material.
3. Make governance decisions only. Do not populate the official World Spec template until Alexander authorizes drafting.

If Alexander has not started Governance Package:

1. Continue preparation-only activities.
2. Do not revise the locked Clinical Story Skeleton.
3. Do not draft World Spec.
4. Do not create file inventory.

## Hard Boundaries

Do not:

- draft the World Spec before explicit Alexander authorization;
- revise the locked Clinical Story Skeleton without explicit Alexander approval;
- revise Identity Package v1 without explicit Alexander approval;
- start Governance Package before Alexander explicitly starts that phase;
- populate the World Spec template before explicit Alexander authorization;
- create Section 3 file inventory before explicit authorization;
- create milestones before explicit authorization;
- create synthetic chart files;
- invent labs, vitals, medications, doses, dates, provider names, MRN, or patient name;
- write final task prompts;
- write golden responses;
- write grader guidelines;
- do failure analysis;
- change Brainstorm clinical content unless new reviewer feedback arrives and Alexander approves the response plan.

## Current Best Claude Task

If asked to help now, Claude should only support preparation:

- summarize current state;
- audit against AutoQC v6.3;
- prepare or refine Governance Package interview questions;
- critique proposed physician decisions;
- help maintain consistency with the approved Brainstorm.

## Workspace Doctrine Note

The workspace contains overlapping prep and guideline docs. This is intentional but should now be treated as supporting reference material. The active cockpit for the World Spec transition is `WORLD_SPEC_KICKOFF.md`; the live state source is `project/STATUS.md`; exact AutoQC checks live in `reference/world-spec-guidelines/08_autoqc_master_index.md`; practical authoring flow lives in `reference/world-spec-guidelines/09_world_spec_writer_playbook.md`.
