# Korvin Merrow World Spec Kickoff

Status: Identity Package v1 locked / ready for Governance Package.

Purpose: mark the transition from approved Brainstorm to World Spec preparation without drafting the World Spec, populating the template, creating a final file inventory, or inventing clinical values.

## 1. Current State

- Brainstorm approved.
- Reviewer GO received from Stacey S.
- RL Studio task ID: `cyau8803`.
- World Spec phase is authorized for kickoff and preparation.
- World Spec drafting has not started.
- Clinical Story Skeleton v1 is locked and ratified.
- Clinical Story Skeleton review completed with GO recommendation.
- Clinical Story Skeleton ratification completed after Claude hostile review minor findings.
- Identity Package v1 is locked.
- Official Claude World Spec session is still pending.
- Post-kickoff physician decision record: `worlds/korvin-merrow/world-spec-prep/physician-decision-log-01.md`.
- Latest skeleton lock record: `worlds/korvin-merrow/world-spec-prep/physician-decision-log-02.md`.
- Clinical Story Skeleton review: `worlds/korvin-merrow/world-spec-prep/clinical-story-skeleton-review.md`.
- Clinical Story Skeleton ratification: `worlds/korvin-merrow/world-spec-prep/clinical-story-skeleton-ratification.md`.
- Identity Package v1: `worlds/korvin-merrow/world-spec-prep/identity-package-v1.md`.
- Identity Package review addendum: `worlds/korvin-merrow/world-spec-prep/identity-package-review-addendum.md`.
- Next allowed substantive action: begin Governance Package only when Alexander explicitly starts that phase.

## Workspace Bloat And Doctrine Audit

Finding: the workspace has accumulated a lot of useful but overlapping planning documents. This is controlled bloat, not a doctrine breach, as long as we now treat this kickoff file as the active cockpit and avoid re-litigating older prep artifacts unless needed.

Current bloat risks:

- `reference/world-spec-guidelines/04`, `08`, `09`, `10`, `11`, `12`, and `13` overlap around World Spec QC, upload, transcript, and Claude workflow.
- `worlds/korvin-merrow/world-spec-prep/*` contains multiple planning maps that overlap by design.
- `frictions.md` and `traps.md` are still thin placeholders; the approved Brainstorm remains the authoritative source for locked frictions/traps until those files are intentionally updated.
- `tmp/docs/korvin-brainstorm-render/` contains generated render artifacts; these are not authored project logic.

Doctrine check:

- No World Spec draft has been created.
- No official World Spec template has been populated.
- No final Section 3 World File Plan or file inventory has been created.
- No synthetic chart files have been created.
- No final task prompts, golden responses, grader guidelines, or failure analysis have been created.
- Clinical decisions remain physician-originated and Brainstorm-locked.
- Claude remains an official drafting assistant, not the clinical source of truth.

Correction going forward:

1. Use this kickoff file for immediate orientation.
2. Use `project/STATUS.md` for live state.
3. Use `project/WORKSPACE_FILE_MAP.md` to prevent duplicate files.
4. Use `post-go-interview-plan.md` for the interview sequence.
5. Use `08_autoqc_master_index.md` for exact AutoQC checks and `09_world_spec_writer_playbook.md` for practical authoring flow.
6. Use `10`, `11`, `12`, and `13` only when preparing upload package, transcript handling, or Claude workflow.

## 2. Approved Foundation

Patient identity: Korvin Merrow.

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

Identity consistency:

- Age 62 is consistent with DOB for a 2026 encounter after 2026-02-18.
- BMI 30.6 is consistent with 97 kg and 178 cm.
- Later calendar skeleton must preserve age-62 consistency unless Alexander explicitly reopens DOB or age.
- Identity Package review addendum carries forward implementation notes only: lisinopril cough should be treated as ACE-inhibitor intolerance; later medication history should explain prior ACE-inhibitor/ARNI transition coherently; baseline function, baseline creatinine, dry weight, and similar baseline anchors should be placed during Patient Profile / Clinical History design.

World Type: Typical Clinical World.

Clinical domain: Emergency Medicine / Internal Medicine / acute hospital medicine, following an ED presentation into inpatient hospitalization and discharge planning.

Approved comorbidity burden:

- Type 2 diabetes mellitus, long-standing.
- Hypertension.
- CKD stage 3.
- HFrEF.
- CAD history.
- Hyperlipidemia.
- Anemia of CKD.
- Osteoporosis/osteopenia from chronic steroid exposure.
- Obstructive sleep apnea.
- Diabetic peripheral neuropathy.
- Polymyalgia rheumatica with chronic prednisone exposure and recent taper.
- Polypharmacy.

Approved compact medication list:

- sacubitril/valsartan 24/26 mg BID.
- carvedilol 12.5 mg BID.
- furosemide 40 mg daily.
- spironolactone 25 mg daily.
- empagliflozin 10 mg daily.
- aspirin 81 mg daily.
- atorvastatin 40 mg nightly.
- metformin ER 500 mg BID.
- insulin glargine 18 units nightly.
- prednisone with inconsistent documented taper/dose.
- alendronate 70 mg weekly.
- calcium/vitamin D daily.
- ferrous sulfate 325 mg every other day.
- gabapentin 300 mg nightly.

World close: Hospital Day 6 at 18:00 during discharge planning.

Locked temporal architecture:

- 6-day hospitalization.
- HD6 18:00 world close.
- Discharge anchor after world close.
- +7 day post-discharge anchor.
- +30 day post-discharge anchor.

Locked underlying clinical story:

- Mixed physiology world.
- Infection, steroid issues, CKD/HF, and polypharmacy interact.
- Not a single-diagnosis world.

Locked presentation trigger:

- Progressive weakness.
- Poor oral intake.
- Near-fall/lightheadedness.
- Family-noticed confusion.
- Possible urinary symptoms.

Locked clinical evolution:

- Approximately 3-week decline before presentation.

Locked world tone:

- Medically improving.
- Operationally dangerous discharge.

Locked primary failure target:

- Functional decline.
- Disposition safety.
- Discharge readiness reasoning.

Locked complexity targets:

- Exceed reviewer minimums.
- Target 12-15 comorbidities.
- Target 18-22 medications.

Locked Clinical Story Skeleton v1:

- Baseline: lives with family; independent but slowed by chronic illness; occasional cane use; mild age-related forgetfulness only; chronic diseases generally stable before current decline.
- PMR/prednisone: several-year PMR history with chronic prednisone exposure, multiple prior flares and taper attempts, recent taper due to controlled symptoms, and reconstructable source-of-truth inconsistencies.
- Pre-hospital decline: approximately 3 weeks of reduced stamina, reduced activity, poor appetite, reduced fluid intake, increasing weakness, increasing family dependence, possible urinary symptoms, progressive unsteadiness, and progressive cognitive slowing.
- Escalation: medication-management mistakes, increased dependence, lightheadedness, near-fall event, and family recognition of meaningful deviation from baseline.
- ED presentation: suspected urinary-source infection, dehydration, AKI risk, altered baseline mental status, functional decline, and clinically reasonable sepsis-oriented management. Infection is a contributor, not the entire explanation.
- Hospital course: HD1 admission/stabilization; HD2 partial improvement and consultant involvement begins; HD3 PT/OT identify functional concerns; HD4 consultant tensions emerge and steroid-history inconsistencies are recognized; HD5 medical improvement continues and disposition questions become dominant; HD6 patient appears medically improved but discharge remains debatable.
- Discharge state: infection, AKI, hemodynamics, mental status, and intake improve, while functional reserve, medication restart strategy, steroid interpretation, family concern, and disposition risk remain unresolved.
- Near-fall framework: multi-factorial, not attributable to a single cause.

Ratified governance/story-logic guardrails:

- Endocrine friction wording: Endocrinology vs Primary Team.
- Do not use "Endocrinology vs Documentation." Documentation is evidence, not a friction participant.
- Steroid-record discrepancy remains a trap.
- Prednisone Source-of-Truth Hierarchy: rheumatology attending recommendation > verified medication reconciliation > pharmacy / refill history > family report > patient recollection.
- Family vs Primary Team remains balanced: family concern is defensible because he is not back to baseline and functional/safety concerns remain; primary team discharge reasoning is also defensible because infection, AKI, mental status, and oral intake are improving and follow-up is available.
- Near-fall remains intentionally multi-factorial, with no single intended explanation. Potential contributors include poor intake, volume depletion, medication effects, neuropathy, deconditioning, infection physiology, and steroid-related physiology.

Primary frictions:

1. Nephrology vs Cardiology: renal/hemodynamic safety during AKI/hypotension vs HFrEF/CAD long-term protective therapy.
2. Family vs Inpatient Medicine: medical stability on paper vs functional readiness and real-world discharge safety.
3. Endocrinology vs Primary Team: risk of premature steroid withdrawal vs risk of unnecessary steroid continuation.

World-level traps:

1. Steroid timeline/source-of-truth trap.
2. HF-AKI medication reconciliation and time-sensitive consultant trap.
3. Buried functional/cognitive status trap.
4. Sepsis anchoring after partial improvement trap.
5. Discharge plan source-hierarchy trap.

Rough task concepts:

1. Discharge medication reconciliation / medication safety review.
2. Hospital discharge summary generation.
3. Transition-of-care / discharge readiness plan.
4. Post-hospital follow-up assessment note.
5. Consultant recommendation synthesis / care coordination note.
6. Readmission risk / patient safety review.

Reserve only:

- Future ED reassessment after return visit.

## 3. Required World Spec Workflow

1. Physician decision interview first.
2. Official Claude World Spec prompt/session.
3. Codex consolidation against physician intent and source rules.
4. Official World Spec template population only after Alexander authorizes drafting.
5. Claude QC with the appropriate World Spec AutoQC prompt/checklist and supplemental materials.
6. RL Studio World Spec AutoQC.
7. Submission package assembly.

Workflow guardrails:

- The official Claude World Spec session should use a fresh Claude Project chat.
- Claude should load the approved Brainstorm, interview section by section, run audit before drafting, and draft only after confirmation.
- Codex should preserve Claude outputs separately from authored/submission work.
- RL Studio/browser activity requires explicit authorization.

## 4. Pending Physician Decisions

Identity and demographics:

- Identity Package v1 is locked.
- Identity Package review addendum is recorded and does not reopen Identity Package v1.
- Calendar date skeleton remains pending and must preserve DOB/age consistency.

Clinical structure:

- Key Milestones.
- Confirmed vs presumed condition split.
- Care team roster.
- Source-of-truth hierarchy. Prednisone hierarchy is already ratified; broader chart hierarchy still pending.
- Decision Friction Table details.
- Clinical Story Skeleton v1 is ratified. Do not reopen unless Alexander explicitly does so.
- Medication expansion from the approved compact list toward the World Spec target of 18-22 medications.
- Final comorbidity list refinement within the World Spec target of 12-15 comorbidities.

Task architecture:

- Workflow consolidation to 3-5 catalog workflows.
- Administrative deliverable decision.
- Task anchors.
- Task independence discipline.

Traceability:

- Traceability workflow.
- Which facts belong in Clinical History vs later chart files.
- How each trap will eventually map to file evidence without creating the final file inventory yet.

## 5. AutoQC Watch Items

- 2.2 synthetic name already addressed.
- 2.3 synthetic MRN pending.
- 2.14 Decision Friction Table.
- 2.22/2.23 milestone superset/no orphan milestones.
- 2.41 temporal architecture.
- 2.42 file-plan table column mismatch / Source + Tool issue.
- 2.48 fact-to-file traceability.
- 2.65 source-of-truth hierarchy.
- 2.101 no Section D/E or higher.
- 2.107 3-5 distinct workflows.
- 2.108 clinical + administrative work product question.
- 2.113 Source/Tool and file origin convention.

## 6. Submission Package Watch Items

- Final World Spec `.docx`.
- Template/reference files.
- Custom-made files if used.
- Writer-produced files if used.
- Claude transcripts if requested by RL Studio/upload flow.
- No zip; upload files individually.

Known unresolved package questions:

- Source text references a "Claude Transcript" in a World Spec upload tutorial title, but local text does not define transcript scope or format.
- Source text contains a tension between older onboarding language saying "spec only" and later May 20 guidance saying new writers curate template/reference files. Confirm from RL Studio/pod guidance before upload.

## 7. Stop Conditions

Stop before:

- Revising the locked Clinical Story Skeleton unless Alexander explicitly reopens it.
- Revising Identity Package v1 unless Alexander explicitly reopens it.
- Governance Package work unless Alexander explicitly starts that phase.
- World Spec drafting unless Alexander explicitly authorizes drafting.
- Milestone creation.
- Final file inventory.
- Task prompts.
- Golden responses.
- Grader guidelines.
- Invented clinical values, dates, lab values, vitals, provider names, MRN, or file names.
- Synthetic file generation.
- RL Studio upload/submission without explicit authorization.

If any requested step appears to cross these boundaries, pause and ask Alexander.
