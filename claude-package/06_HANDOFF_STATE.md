# Handoff State

Purpose: enable a brand-new Claude session to resume accurately without stale assumptions.

## Where We Are

Project Sanctum onboarding is complete for Korvin Merrow. World Spec approval is complete, engineering pipeline run #1 completed, Step 9 generated-file review is closed, Final Files AutoQC passed 78/78 after three revisions, and the world was created as `Healthcare_247_Merrow` on 2026-06-05 at 11:20 AM PDT. Pod assignment is `#vaguspod`; EPM Rose; pod leads Abi O and Larry E. Abi first human review returned SEND BACK / rework required. The active stage is Task 1 AO Review Rework / awaiting Abi round-2 review: RLS entry, Task AutoQC rerun, batch v3 Taiga trajectories/QA, and round-2 FA/GA submission are complete; both task files were deleted, prompt/golden/grader guidelines were replaced with v2/v3/v5, Task AutoQC ended at 2/68 justified, v3 scores were 90-97 with lowest run 8 / db617c58 at 0.90, and the Writer Note disclosed the higher/tighter scores. Active next step is Abi round-2 review / hardening ruling. The Step 9 audit trail remains in `worlds/korvin-merrow/file-review/`, especially `file-review-protocol.md`, `time-strategy-and-state.md`, `findings-triage.md`, and `file-review-log.md`. The canonical Task 1 lifecycle record is `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md`; governing review record is `worlds/korvin-merrow/task-setup/reviews/task1-first-human-review-ao-2026-06-05.md`.

Pipeline run #1 / Step 9 closeout state:

- Output ingested at `worlds/korvin-merrow/file-review/pipeline-output/`.
- Generated DOCX files: 33 under `pipeline-output/filesystem/`.
- Metadata files: 134 under `pipeline-output/.meta/`.
- Initial World Files AutoQC: 74/76 pass. The two fails were access/routing failures because the auditor sandbox could not inspect the files, not evidence of content defects.
- Final Files AutoQC: 78/78 pass after revision #3.
- World created: `Healthcare_247_Merrow`, world ID `world_d50c832ac6474a68ba982a77e28a6bbe`, snapshot `snap_0fb032e95b324710b12a7432cf7da6c1`, 26 files synced.
- Active Claude-assisted triage packet: `worlds/korvin-merrow/file-review/findings-triage.md`.
- Candidate revision log: `worlds/korvin-merrow/file-review/file-review-log.md`.
- Revised 33-file working snapshot: `worlds/korvin-merrow/file-review/revision/filesystem/`.
- Final 26-file world-level upload set: `worlds/korvin-merrow/file-review/upload/filesystem/`.
- Seven task-level request files are held out at `worlds/korvin-merrow/file-review/task-files-holdback/` per platform rule; preserve locally for Step 10 task setup.
- Items marked `[A]` needed Alexander physician ruling before edits; rulings and candidate edits are recorded in the file-review log.
- Do not access RL Studio, upload additional task prompts/goldens/grader guidelines, run additional agents, run additional QA, create AutoQC responses, create task setup materials, edit the submitted Failure Analysis / Grader Analysis, start preference labeling, or mutate platform state unless Alexander explicitly authorizes the exact step.

Historical locked layers remain complete: Batch 1 through Batch 5 are locked. World-Level Synthetic File Layer is complete with FI-W01 through FI-W22 locked. FI-T01 through FI-T07 are locked task-context files. FI-S01 through FI-S04 are locked supplementary files. Entire File Ecosystem is complete. Task Prompt Architecture, Task Prompt Construction, Expected Output Architecture, Expected Output Construction, Golden Architecture, Golden Construction, Grader Guidance Architecture, Grader Guidance Construction, AutoQC Architecture, AutoQC Construction, Packaging Architecture, Packaging Construction, Submission Preparation, Execution Preparation, Transcript Resolution, and Final Submission Resolution are complete/locked unless Alexander explicitly reopens a later phase.

Transcript resolution: `docs/claude-transcript-formatted.md` is the authoritative transcript upload artifact. The Claude share URL `https://claude.ai/share/d5129364-5d6c-4a2c-acb3-282f367a0040` is supporting provenance and reviewer-access support. `docs/claude-transcript.md` remains raw historical/provenance evidence only. Treat historical James Carter references and export encoding artifacts as provenance; do not rewrite, package, upload, or submit transcript materials unless Alexander explicitly authorizes that later execution step.

The Brainstorm for Korvin Merrow World has been completed, passed AutoQC, uploaded to RL Studio, returned SEND BACK from Human Review, remediated, reuploaded, resubmitted, and approved by Stacey S.

RL Studio:

- Task ID: `cyau8803`
- Status: Brainstorm approved / ready for World Spec transition
- Brainstorm AutoQC: revised run `0 failed / 51 passed`
- Diagnostics reviewed: yes
- Human Review: GO from Stacey S
- Approval source: Slack / Stacey S
- Reviewer message: "great job! I approved your brainstorm. Next steps are to move forward with world spec and file template development."

Current state: Task 1 AO Review Rework / awaiting Abi round-2 review. Pipeline run #1 output and the Step 9 audit trail are preserved under `worlds/korvin-merrow/file-review/`; final edits, integrity checks, platform lessons, and the upload/holdback split are recorded in `worlds/korvin-merrow/file-review/file-review-log.md`. Task 1 platform provenance and current action sequence are preserved under `worlds/korvin-merrow/task-setup/`, with `task1-lifecycle-log.md` winning over scattered summaries. The post-Abi local rework drafts are `prompt-task1-v2.txt`, `golden-response-task1-v3.docx`, and `grader-guidelines-task1-v5.txt`; they have been entered in RLS, Task AutoQC reran to 2/68 justified, batch v3 completed, and round-2 FA/GA plus Writer Note were submitted. Batch v2 trajectory and FA/GA records are preserved as learning evidence but are superseded for current review. `docs/reasoning-discipline.md` is the cross-world verification gate for one-way-door decisions and causal platform-behavior claims. Historical locked artifacts remain complete; do not reopen them unless Alexander explicitly authorizes it. Additional RL Studio task mutation beyond reviewer-response follow-up, task-material uploads, agent runs, QA runs, AutoQC responses, rubrics, scoring thresholds, pass/fail bands, point allocations, DOCX submission packaging, manifest creation, final submission packages, upload, submission, and RL Studio access remain gated on explicit Alexander authorization for the relevant step.

Repository collaboration readiness note: a new Codex or Claude session can reconstruct the repository state from repository files alone. The repository is collaboration-ready because `project/STATUS.md`, `docs/status-dashboard.md`, `project/PHASE_MAP.md`, `project/WORKSPACE_FILE_MAP.md`, `docs/world-pipeline-playbook.md`, `docs/reasoning-discipline.md`, `worlds/korvin-merrow/file-review/`, `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md`, `worlds/korvin-merrow/task-setup/reviews/task1-first-human-review-ao-2026-06-05.md`, and this handoff converge on Task 1 AO Review Rework / awaiting Abi round-2 review. The canonical file map is `project/WORKSPACE_FILE_MAP.md`.

Cross-artifact consistency verification is a standing governance rule. Before creating, modifying, ratifying, or locking architecture, inventory, matrix, mapping, coverage table, workflow table, trap table, friction table, hierarchy table, or governance artifacts, cross-check applicable locked canonical sources and document any expansion, narrowing, redistribution, reprioritization, relabeling, or reclassification before ratification or lock. Do not silently promote historical, planning, superseded, tracker, or provenance metadata into governing architecture.

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
- Durable record: `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-01.md`.

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
- Review artifact: `worlds/korvin-merrow/world-spec-prep/reviews/clinical-story-skeleton-review.md`.
- Lock record: `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md`.
- Ratification artifact: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`.

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
- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/identity-package-v1.md`.
- Age 62 is consistent with DOB for a 2026 encounter after 2026-02-18.
- BMI 30.6 is consistent with 97 kg and 178 cm.
- Review addendum: `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md`.
- Addendum notes are carry-forward implementation notes only: lisinopril cough is ACE-inhibitor intolerance; later medication history should explain prior ACE-inhibitor/ARNI transition coherently; baseline function, baseline creatinine, dry weight, and similar baseline anchors should be placed during Patient Profile / Clinical History design.
- Do not reopen Identity Package v1.

Governance Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md`.
- Clarification artifact: `worlds/korvin-merrow/world-spec-prep/reviews/governance-package-clarification.md`.
- Ratification artifact: `worlds/korvin-merrow/world-spec-prep/ratifications/governance-package-ratification.md`.
- Status: RATIFIED.
- Care team roster: Hospitalist Service; Cardiology; Nephrology; Endocrinology; Physical Therapy; Occupational Therapy; Case Management; Social Work; Patient; Family/Caregiver; Primary Care Physician.
- Authority hierarchy: attending hospitalist > consulting attending specialists > PT/OT functional assessments > Case Management / Social Work > family reports > patient recollection.
- Master clinical source-of-truth hierarchy: attending documentation > verified medication reconciliation > pharmacy history > consultant documentation > primary care documentation > family report > patient recollection.
- Preserve prednisone-specific hierarchy: rheumatology attending recommendation > verified medication reconciliation > pharmacy / refill history > family report > patient recollection.
- Authority Hierarchy and Source-of-Truth Hierarchy are distinct. Authority Hierarchy governs role-based governance, disposition interpretation, functional/discharge evidence, stakeholder input, and decision ownership. Source-of-Truth Hierarchy governs factual conflict resolution.
- Authority hierarchy does not resolve clinical recommendation disagreements. Consultant disagreements require evidence synthesis, timing, trends, patient status, and discharge safety.
- Confirmed conditions: HFrEF, CKD Stage 3, Type 2 Diabetes, CAD, Hypertension, Hyperlipidemia, OSA, Diabetic Neuropathy, PMR, Anemia of CKD, Osteoporosis/Osteopenia.
- Presumed / active questions: current infection source, steroid contribution, adrenal suppression contribution, degree of dehydration, relative medication contribution, discharge readiness.
- Steroid-related osteoporosis/osteopenia reflects cumulative chronic steroid exposure but does not prove current symptoms are primarily caused by adrenal suppression.
- Final friction table: Cardiology vs Nephrology for medication restart timing; Family vs Primary Team for discharge readiness; Endocrinology vs Primary Team for steroid interpretation and risk.
- Administrative deliverable decision: yes.
- Workflow umbrella: Acute Hospital Management. Exact future task workflow lines must still use official tracker names.
- AutoQC 2.107 workflow count and 2.108 administrative deliverable remain deferred task-architecture watch items.

Completed Architecture Layers:

- Brainstorm: APPROVED.
- Temporal Architecture: LOCKED.
- Clinical Story Skeleton: RATIFIED.
- Identity Package: LOCKED.
- Governance Package: RATIFIED.

Physician Architecture Layer Status: COMPLETE.

Key Milestones Calendar Skeleton v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md`.
- Status: LOCKED.
- Approximate decline begins: 04/27/2026.
- Admission / HD1: 05/18/2026.
- World snapshot / world close: 05/23/2026 18:00.
- Discharge anchor: 05/24/2026.
- +7 day anchor: 05/31/2026.
- +30 day anchor: 06/23/2026.
- Locked doctrine: +7 and +30 anchors are measured from discharge anchor 05/24/2026, not from HD6 world close.
- Ratification artifact: `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md`.
- Date framework only; not a final milestone table, task architecture, file inventory, or World Spec draft.

Baseline Anchor Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/baseline-anchor-ratification.md`.
- Status: LOCKED.
- Physician sign-off completed.
- Locked anchors include baseline creatinine, eGFR, hemoglobin, A1c, dry weight approximately 97 kg, mobility, cognition, medication-management ability, and home support.
- Baseline functional status remains part of the approved baseline framework through mobility, cognition, medication-management ability, and home support.
- Baseline blood pressure may be considered as a future candidate anchor during construction only; do not create a numeric value at this stage.
- These are not admission labs, hospital-course trends, final file inventory, task architecture, or World Spec prose.

Clinical Story Timeline Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md`.
- Status: LOCKED.
- Purpose: canonical story-evolution framework from pre-admission decline through HD1-HD6, discharge, +7, and +30 anchors.
- It does not create labs, vitals, medication doses, medication schedules, hospital notes, file inventory, task architecture, World Spec prose, prompts, goldens, grader guidance, templates, reference files, or synthetic documents.
- Carry-forward note: preserve Trap #3 as buried functional/cognitive evidence and Trap #5 as reassuring but incomplete discharge/source-hierarchy artifact during later file construction.

Task Architecture Interview v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`.
- Status: COMPLETE / SUPERSEDED BY LOCKED TASK ARCHITECTURE PACKAGE.
- Purpose: interview-only framework for resolving AutoQC 2.107 workflow-count constraints, AutoQC 2.108 administrative-deliverable requirements, final task distribution, and workflow consolidation strategy.
- Boundary: does not create tasks, task prompts, expected outputs, goldens, grader guidance, file inventory, World Spec sections, reference templates, synthetic files, or new workflows not already implied by approved architecture.

Task Architecture Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md`.
- Status: LOCKED.
- Purpose: formal task-architecture framework defining six task concepts across four workflows before task drafting.
- Physician decisions: target task count 6; target workflow count 4; administrative deliverable Discharge Planning / Care Coordination; TCM folded into transition/discharge workflow; consultant synthesis distinct; readmission-risk reasoning kept inside existing workflow structures; coding, billing, and prior authorization not preferred unless later required.
- Candidate workflows: Discharge Medication Reconciliation; Hospital Discharge Summary Generation; Discharge Planning Documentation; Interdisciplinary Care Plan Development and Documentation.
- AutoQC 2.108 remains a documented reviewer-risk bet, not a blocker. Utilization Review is contingency only if challenged later and should not be added now.
- TCM and readmission-risk reasoning are embedded inside Discharge Planning Documentation rather than standalone workflow categories.
- Medicine Team Lead task-design guidance is future task-layer framing only, not source-of-truth hierarchy and not governance redesign. Source-of-truth hierarchy answers: "When sources disagree, which evidence source is authoritative?" Task-design guidance answers: "Who is the final deliverable written by or for?" Later task prompts, expected outputs, goldens, and grader guidance must frame final deliverables from the physician perspective or physician voice, even when supporting sources are pharmacy, nursing, PT/OT, case management, social work, family, or administrative sources. Do not redesign the world, reopen Governance Package v1, or alter source-of-truth hierarchy because of this guidance.
- Boundary: does not create task prompts, expected outputs, goldens, grader guidance, file inventory, World Spec sections, templates, reference files, or synthetic documents.

Medication Expansion Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/medication-expansion-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/medication-expansion-ratification.md`.
- Decision addendum: `worlds/korvin-merrow/world-spec-prep/reviews/medication-expansion-decision-addendum.md`.
- Status: LOCKED.
- Purpose: candidate baseline medication architecture targeting approximately 18-22 medications.
- Physician decision: insulin lispro removed from baseline medication architecture and reserved as future inpatient-only candidate medication. Baseline medication count is 20.
- Boundary: does not create doses, frequencies, schedules, medication timelines, reconciliation outputs, hospital medication changes, admission medication lists, discharge medication lists, tasks, prompts, expected outputs, goldens, grader guidance, file inventory, World Spec prose, templates, reference files, or synthetic documents.

Comorbidity Expansion Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/comorbidity-expansion-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/comorbidity-expansion-ratification.md`.
- Status: LOCKED.
- Purpose: baseline chronic-condition architecture targeting approximately 12-15 comorbidities.
- Final baseline condition count: 14.
- Preserves all already-approved conditions and retains only secondary additions: class I obesity by locked BMI, chronic gastroesophageal reflux / chronic acid-suppression indication, and chronic constipation tendency.
- Boundary: does not create labs, vitals, medication doses, medication schedules, hospital-course events, provider names, surgical history, tasks, prompts, expected outputs, goldens, grader guidance, file inventory, World Spec prose, templates, reference files, or synthetic documents.

Provider Roster Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/provider-roster-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/provider-roster-ratification.md`.
- Status: LOCKED.
- Purpose: provider/care-team and stakeholder architecture before note authorship, file planning, task drafting, synthetic documents, or World Spec drafting.
- Locked named high-authority roles: Dr. Elian Vossmere, Dr. Maris Caldrane, Dr. Iven Solthar, Dr. Nerea Veylorn, Dr. Talia Quenor, Dr. Soren Halvek, and Mara Merrow.
- Shared Merrow surname is intentional.
- Resident and pharmacy remain role-based.
- No additional provider naming is authorized.
- Boundary: does not create clinical notes, provider-authored documents, file inventory, task prompts, expected outputs, goldens, grader guidance, medication schedules, hospital-course events, labs, vitals, World Spec prose, templates, reference files, or synthetic documents.

Surgical History Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/surgical-history-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md`.
- Status: LOCKED.
- Purpose: pre-world surgical/procedural history architecture before Daily Hospital Course Framework, World Spec construction, file inventory planning, synthetic documents, task prompts, expected outputs, goldens, or grader guidance.
- Confirmed procedural anchors: remote percutaneous coronary intervention with coronary stent placement and remote diagnostic sleep study confirming obstructive sleep apnea.
- Excluded/noise-controlled procedures: ICD/CRT/pacemaker, CABG, dialysis access, major orthopedic fracture repair or joint replacement, limb amputation/major diabetic foot surgery, temporal artery biopsy/rheumatologic diagnostic procedure, and screening colonoscopy for v1 purposes.
- Boundary: does not create operative reports, procedure notes, hospital-course events, labs, vitals, file inventory, tasks, synthetic files, or World Spec prose.

Daily Hospital Course Framework v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/daily-hospital-course-framework-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md`.
- Status: LOCKED.
- Purpose: major bridge artifact defining architecture-level HD1-HD6 daily evolution before World Spec/file/task construction.
- Captures primary clinical state, what changed, what improved, what remains concerning, active frictions, active traps, relevant provider groups, and disposition readiness for each hospital day.
- Boundary: does not create labs, lab trends, vitals, medication doses, medication schedules, orders, notes, discharge summaries, file inventory, tasks, prompts, expected outputs, goldens, grader guidance, synthetic files, World Spec prose, templates, or reference files.

Preparation Layer:

- Status: COMPLETE.
- Completed artifacts: Brainstorm, Temporal Architecture, Clinical Story Skeleton, Identity Package, Governance Package, Key Milestones Calendar Skeleton, Baseline Anchor Package, Clinical Story Timeline Package, Task Architecture Package, Medication Expansion Package, Comorbidity Expansion Package, Provider Roster Package, Surgical History Package, and Daily Hospital Course Framework.

World Spec Skeleton v1:

- Artifact: `worlds/korvin-merrow/world-spec-construction/locked/world-spec-skeleton-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-skeleton-ratification.md`.
- Status: LOCKED.
- Purpose: structural map for final World Spec section order, source-package mapping, construction boundaries, Studio alignment, AutoQC readiness, and construction order.
- Boundary: does not create final World Spec prose, synthetic files, file inventory rows, clinical notes, labs, vitals, task prompts, expected outputs, goldens, grader guidance, reference files, or templates.

World Spec v1:

- Artifact: `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-v1-ratification.md`.
- Status: LOCKED.
- Purpose: first complete World Spec candidate built from locked architecture only.
- Boundary: does not create file inventory rows, synthetic files, clinical notes, labs, vitals, medication schedules, task prompts, expected outputs, golden responses, grader guidance, AutoQC responses, reference files, templates, DOCX submission artifacts, or RL Studio upload.

Fetched World Spec source examples:

- Alexander added source/reference examples under `reference/word-spec-examples/`.
- This folder is intentionally local-only and gitignored because the example corpus is large and can confuse project-specific source-of-truth boundaries.
- Treat them as source/reference material only, not authored Korvin Merrow content or the Korvin Merrow World File Plan.

## Decisions Remaining

Do not answer these without Alexander.

Identity/compliance:

- Identity Package v1 is locked.
- Identity Package review addendum is recorded and does not reopen identity values.
- Later calendar skeleton must preserve DOB/age consistency unless Alexander explicitly reopens DOB or age.

Clinical scenario:

- Final key milestone list for the eventual World Spec template.
- Source-of-truth hierarchy for conflicting evidence.

Task architecture:

- Task Architecture Package v1 is locked.
- Later task construction must differentiate the three Discharge Planning Documentation concepts by requester, time anchor, reasoning emphasis, and deliverable surface.
- Final task independence, requester, anchor, and one-deliverable discipline remain to be applied during authorized task specification work.

Traceability/file strategy:

- Evidence provenance workflow.
- Later file modalities.
- Later trap substrate planning.
- File Inventory v1 is locked; later work must preserve its rows unless Alexander explicitly reopens it.

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

Use `docs/world-pipeline-playbook.md` section A2 and the locked task prompt/golden/grader-guidance artifacts for Step 10 preparation. Use `worlds/korvin-merrow/file-review/file-review-protocol.md`, `worlds/korvin-merrow/file-review/time-strategy-and-state.md`, `worlds/korvin-merrow/file-review/findings-triage.md`, and `worlds/korvin-merrow/file-review/file-review-log.md` as the closed Step 9 audit trail. The next legal action is Alexander-authorized task setup handling, or further local review/de-hinting if Alexander continues reviewing with Claude. Do not access RL Studio, upload task setup materials, run agents, run QA, create AutoQC responses, or mutate platform state unless Alexander explicitly authorizes the exact step.

Before ending any working session:

1. Leave the working tree clean, or explicitly document uncommitted state.
2. Update current phase and next eligible phase.
3. Preserve locked artifacts unless Alexander explicitly authorized reopening or editing them.
4. Locate and status-label candidate artifacts.
5. Move newly locked artifacts to locked paths and create/reference ratifications.
6. Update continuity surfaces and Claude handoff files.
7. Remove or explicitly mark stale active candidate paths as historical.
8. Avoid unauthorized files.
9. Record carry-forward watch items and future task-layer guidance.
10. Commit completed work unless Alexander explicitly instructs not to commit.
11. Final report must state what changed, what did not change, current status, next eligible phase, and whether the repository is safe for another collaborator.

## Hard Boundaries

Do not:

- draft the World Spec before explicit Alexander authorization;
- revise the locked Clinical Story Skeleton without explicit Alexander approval;
- revise Identity Package v1 without explicit Alexander approval;
- change Governance Package v1 without Alexander approval;
- populate the World Spec template before explicit Alexander authorization;
- create Section 3 file inventory before explicit authorization;
- create milestones before explicit authorization;
- reopen locked expected outputs, revise locked goldens, run AutoQC, create AutoQC responses, create scoring rubrics, create scoring thresholds, create pass/fail bands, create point allocations, create DOCX artifacts, create RL Studio submission artifacts, or create final task outputs before explicit authorization;
- invent labs, vitals, medications, doses, dates, provider names, MRN, or patient name;
- write final task prompts;
- write additional golden responses or revise candidate goldens without explicit authorization;
- write additional grader guidelines beyond locked GG-KM01 through GG-KM06 or reopen/ratify grader guidance;
- do failure analysis;
- change Brainstorm clinical content unless new reviewer feedback arrives and Alexander approves the response plan.

## Current Best Claude Task

If asked to help now, Claude should support Task 1 AO Review Rework:

- use `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md` as the canonical Task 1 state source;
- preserve the post-Abi rework direction: both Task 1 task files are deleted, mechanism-agnostic v5 grader guidance is live, Task AutoQC is 2/68 justified, batch v3 rerun is complete, round-2 FA/GA is submitted, and the next action is Abi round-2 review / hardening ruling;
- support the current Task 1 sequence: prepare for rework but do not mutate platform state without explicit authorization;
- apply `docs/reasoning-discipline.md` before one-way-door decisions or causal platform-behavior claims;
- use `worlds/korvin-merrow/task-setup/task1/FA-GA-final.md`, grading transcript findings, and the v1/v2 trajectory exports as historical learning evidence only once task files are deleted;
- for Tasks 2-6, review/de-hint task prompts against final generated files and the physician-perspective rule;
- for Tasks 2-6, wait until Task 1's post-Abi pattern is stable, then build from the v5 mechanism-agnostic structure rather than v3/golden-only, v4 `/docs`-aware, or the older A/B/C pattern;
- preserve trap fidelity, especially prednisone ambiguity, EW22 incompleteness, buried functional evidence, and consultant-friction balance;
- keep Step 9 file-review provenance in `worlds/korvin-merrow/file-review/`, not in the original onboarding transcript.

## Workspace Doctrine Note

The workspace contains overlapping prep and guideline docs. This is intentional but should now be treated as supporting reference material. The active cockpit for the World Spec transition is `WORLD_SPEC_KICKOFF.md`; the live state source is `project/STATUS.md`; exact AutoQC checks live in `reference/world-spec-guidelines/08_autoqc_master_index.md`; practical authoring flow lives in `reference/world-spec-guidelines/09_world_spec_writer_playbook.md`.
