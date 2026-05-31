# Korvin Merrow World Spec Kickoff

Status: World Spec kickoff / ready for physician interview.

Purpose: mark the transition from approved Brainstorm to World Spec preparation without drafting the World Spec, populating the template, creating a final file inventory, or inventing clinical values.

## 1. Current State

- Brainstorm approved.
- Reviewer GO received from Stacey S.
- RL Studio task ID: `cyau8803`.
- World Spec phase is authorized for kickoff and preparation.
- World Spec drafting has not started.
- Official Claude World Spec session is still pending.
- Next allowed substantive action: physician decision interview using `worlds/korvin-merrow/world-spec-prep/post-go-interview-plan.md`.

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

Primary frictions:

1. Nephrology vs Cardiology: renal/hemodynamic safety during AKI/hypotension vs HFrEF/CAD long-term protective therapy.
2. Family vs Inpatient Medicine: medical stability on paper vs functional readiness and real-world discharge safety.
3. Emergency/Inpatient Medicine vs Endocrinology: risk of premature steroid withdrawal vs risk of unnecessary steroid continuation.

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

- Synthetic MRN.
- DOB/age consistency.
- Height, weight, and BMI.
- Allergies.
- Code status.
- Calendar date skeleton.

Clinical structure:

- Key Milestones.
- Confirmed vs presumed condition split.
- Care team roster.
- Source-of-truth hierarchy.
- Decision Friction Table details.

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

- World Spec drafting unless Alexander explicitly starts the physician interview and later authorizes drafting.
- Final file inventory.
- Task prompts.
- Golden responses.
- Grader guidelines.
- Invented clinical values, dates, lab values, vitals, provider names, MRN, or file names.
- Synthetic file generation.
- RL Studio upload/submission without explicit authorization.

If any requested step appears to cross these boundaries, pause and ask Alexander.

