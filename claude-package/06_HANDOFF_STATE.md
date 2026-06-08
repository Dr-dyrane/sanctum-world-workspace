# Handoff State

Purpose: enable a brand-new Claude session to resume accurately without stale assumptions.

## Where We Are

Project Sanctum onboarding is complete for Korvin Merrow. World Spec approval is complete, engineering pipeline run #1 completed, Step 9 generated-file review is closed, Final Files AutoQC passed 78/78 after three revisions, and the world was created as `Healthcare_247_Merrow` on 2026-06-05 at 11:20 AM PDT. Pod assignment is `#vaguspod`; EPM Rose; pod leads Abi O and Larry E. Task 1 final human review is complete / approved. Task 1 advanced through AO rework, hardening, Abi pre-check, revised platform entry, pilot runs, FA/GA, Preference Labeling, and final review. Abi Osagie completed the final review checklist on 2026-06-06 with applicable items marked Yes or N/A. Task 2 clean pilot was too easy; v2 escalation produced a usable discriminator; Abi first review called it "Good task, great failure. No significant errors" and required only a reseed/date fix. KM02 v3 active platform set is prompt `prompt-task2-escalation.txt`, golden `golden-KM02-v5.docx` re-dated to 05/24/2026 with sha256 prefix `2dd3e0ad`, grader `grader-guidelines-task2.txt`, and mounted draft `discharge_summary_draft_incomplete_05242026.docx`. Task AutoQC / Taiga gates passed qcaud_5e, qcaud_4a, and qcaud_ef. V3 spread was 45, 92, 82, 82, 60, 62, 40, 30, 45, 55; all 10 scored, mean 59.3, final FA/GA subject Attempt 8 at 0.30. Preference Labels were submitted with verdict B / B++, all recorded KM02 checks are green, and KM02 is COMPLETE / RFD (Ready for Delivery) after Janette's 6/8 final review. The Step 9 audit trail remains in `worlds/korvin-merrow/file-review/`, especially `file-review-protocol.md`, `time-strategy-and-state.md`, `findings-triage.md`, and `file-review-log.md`. The canonical Task 1 lifecycle record is `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md`; final review record is `worlds/korvin-merrow/task-setup/reviews/task1-final-review-ao-2026-06-06.md`; governing review records live under `worlds/korvin-merrow/task-setup/reviews/`.

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
- Do not access RL Studio, upload additional task prompts/goldens/grader guidelines, run additional agents, run additional QA, create AutoQC responses, create task setup materials, edit submitted Failure Analysis / Grader Analysis or Preference Labeling records, or mutate platform state unless Alexander explicitly authorizes the exact step.

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

Current state: Task 1 final human review complete / approved. Pipeline run #1 output and the Step 9 audit trail are preserved under `worlds/korvin-merrow/file-review/`; final edits, integrity checks, platform lessons, and the upload/holdback split are recorded in `worlds/korvin-merrow/file-review/file-review-log.md`. Task 1 platform provenance, PL backup, final review, and current action sequence are preserved under `worlds/korvin-merrow/task-setup/`, with `task1-lifecycle-log.md` winning over scattered summaries. Batch v2/v3, hardening, pilot, FA/GA, PL, and final review records are preserved as learning evidence and provenance. `docs/reasoning-discipline.md` is the cross-world verification gate for one-way-door decisions and causal platform-behavior claims. Historical locked artifacts remain complete; do not reopen them unless Alexander explicitly authorizes it. Task 2 starts at `worlds/korvin-merrow/task-setup/task2/TASK2-STATE.md`. Clean pilot evidence is under `task2/runs/clean-pilot/`; v2 escalation evidence is under `task2/runs/escalation-v2/`; v3 reseed evidence is under `task2/runs/escalation-v3/`. V3 produced a stronger byte-verified gradient: all 10 scored, mean 59.3, Attempt 8 at 0.30 as the final FA/GA subject after knowingly propagating the draft-only culture result. Preference Labeling evidence is under `task2/preference-labeling/`: A = 0.40 propagation run, B = 0.82 catch run, submitted B / B++ verdict, and hash-matching v3 input copies. The active platform set is `platform/task2/current/prompt-task2-escalation.txt`, `platform/task2/current/golden-KM02-v5.docx` (`2dd3e0ad`), `platform/task2/current/grader-guidelines-task2.txt`, and `platform/task2/current/discharge_summary_draft_incomplete_05242026.docx`. KM02 is COMPLETE / RFD (Ready for Delivery) after Janette's 6/8 final review. Cross-task retrospective: `worlds/korvin-merrow/task-setup/KM-RETROSPECTIVE-tasks1-2.md`. KM03 starts at `worlds/korvin-merrow/task-setup/task3/TASK3-STATE.md`, `worlds/korvin-merrow/task-setup/task3/KM03-state-log.md`, and `worlds/korvin-merrow/task-setup/task3/runs/KM03-taiga-results-58b5f3e3.md`; escalation through v2.1 is difficulty-failed; active v2.2 set passed Task AutoQC and Taiga is held. The v2.1 platform set lives in archive as evidence, not a shipping candidate. KM04 v1 completed Alexander-operated trajectory evidence and failed the difficulty gate: job `55ee209f-c9fa-4a64-8071-70d8917508da`, 10 runs 0.87-0.95, mean 0.912, zero sub-70. Record: `worlds/korvin-merrow/task-setup/task4/runs/KM04-taiga-results-55ee209f.md`. The staged `platform/task4/current/` set is v1 evidence only and should not advance to FA/GA, Preference Labeling, or final review without explicit override or redesign authorization. KM05 has local prebuild review convergence under `worlds/korvin-merrow/task-setup/task5/`; review records are `task5/design/KM05-claude-ai-proposal-6-7.md` and `task5/design/KM05-codex-black-team-6-7.md`; it is review-only, not built, not platform-staged, not uploaded, not AutoQC-run, and not agent-run. Retired KM03 v1 passed Task AutoQC 36/36 (`qcaud_6b`) after DOCX core-metadata scrub; later job `58b5f3e3` confirmed v1 was too easy and is historical only. The finalized live world files were not changed. Task 6 remains held unless Alexander explicitly authorizes bounded parallel prep. Additional RL Studio task mutation, task-material uploads, agent runs, QA runs, AutoQC responses, rubrics, scoring thresholds, pass/fail bands, point allocations, DOCX submission packaging, manifest creation, final submission packages, upload, submission, KM05 build/platform staging, and RL Studio access remain gated on explicit Alexander authorization for the relevant step.

KM03 superseding platform note 6/8: v2.2 redesign has now been built into the active pre-Taiga platform set and Task AutoQC passed 36/36 (`qcaud_fc`). Use `platform/task3/current/prompt-task3-v2.2.txt`, `platform/task3/current/discharge_planning_summary_draft_05242026.docx`, `platform/task3/current/golden-KM03-v2.2.docx`, and `platform/task3/current/grader-guidelines-task3-v2.2.txt` for any current KM03 work. Taiga is intentionally held.

KM05 update 6/7 late plus 6/8 correction: prebuild review is converged / HOLD only. Review records are `worlds/korvin-merrow/task-setup/task5/design/KM05-claude-ai-proposal-6-7.md` and `worlds/korvin-merrow/task-setup/task5/design/KM05-codex-black-team-6-7.md`, but the older moderate-task classification is retired by the 6/8 no-moderate directive in `TASK-RUNBOOK.md`. Any future KM05 path must become a genuine difficulty discriminator with a real clinical failure. No KM05 DOCX build, platform-current staging, RL Studio upload, Task AutoQC, Taiga trajectories, QA, or platform mutation has occurred.

KM03 update 6/8: KM03 escalation through v2.1 is difficulty-failed: job `58b5f3e3` scored 90-97 (mean about 93.6), zero sub-70; the run record notes a lineage caveat because captured transcripts show v1-era filenames/audit prompt/golden-v1, but Alexander records it as v2.1 and the operational conclusion is v2.2 redesign, not FA/GA/PL/final review from the current mechanism. Track the markdown result at `worlds/korvin-merrow/task-setup/task3/runs/KM03-taiga-results-58b5f3e3.md`; transcript tarballs remain ignored/local evidence.

KM03 v2.2 Lenora plan history 6/8: `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-FINAL-PLAN.md` superseded the earlier cold-axis completion/status idea but is now itself superseded as primary by the KM02-bar plan. Preserve as review history only unless Alexander re-selects that mechanism.

KM03 v2.2 reconciliation update 6/8: `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-reconciliation-6-8.md` adopts the Lenora plant as a pilot mechanism and records the no-moderate directive. If the pilot does not produce a real clinical failure, redesign and re-pilot; do not accept or ship KM03 as moderate. Resolve its listed Codex confirmations before any build gate.

KM03 v2.2 KM02-bar plan update 6/8: current primary mechanism source is `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-KM02-BAR-PLAN.md`, with Claude.ai review request at `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-KM02bar-review-request-for-claude-ai.md`. It supersedes the Lenora supervision-fact plan as primary and defines the tuned CPAP/OSA fabricated objective-result mechanism used by the active v2.2 platform set.

KM03 v2.2 platform update 6/8: active pre-Taiga files are `worlds/korvin-merrow/task-setup/platform/task3/current/prompt-task3-v2.2.txt`, `worlds/korvin-merrow/task-setup/platform/task3/current/discharge_planning_summary_draft_05242026.docx`, `worlds/korvin-merrow/task-setup/platform/task3/current/golden-KM03-v2.2.docx`, and `worlds/korvin-merrow/task-setup/platform/task3/current/grader-guidelines-task3-v2.2.txt`. Task AutoQC passed 36/36 (`qcaud_fc`). Taiga is intentionally held; no v2.2 Taiga, FA/GA, PL, final review, additional upload, or AutoQC response exists.

Repository collaboration readiness note: a new Codex or Claude session can reconstruct the repository state from repository files alone. The repository is collaboration-ready because `project/STATUS.md`, `docs/status-dashboard.md`, `project/PHASE_MAP.md`, `project/WORKSPACE_FILE_MAP.md`, `docs/world-pipeline-playbook.md`, `docs/reasoning-discipline.md`, `worlds/korvin-merrow/file-review/`, `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md`, `worlds/korvin-merrow/task-setup/reviews/`, and this handoff converge on Task 1 final review complete / approved. The canonical file map is `project/WORKSPACE_FILE_MAP.md`.

Doc-spine rule: `project/WORKSPACE_FILE_MAP.md` Navigation Rule is the repository read spine. For task-stage work, use the spine plus the active `TASKN-STATE.md` before drafting. The builder must state a read receipt: files read, active state, forbidden actions, and three no-repeat lessons.

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

Use `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md`, `worlds/korvin-merrow/task-setup/reviews/task1-final-review-ao-2026-06-06.md`, and `docs/world-pipeline-playbook.md` for Task 1 provenance and future task continuation. For Task 2, start with `worlds/korvin-merrow/task-setup/task2/TASK2-STATE.md`, `worlds/korvin-merrow/task-setup/task2/fa-ga/FA-GA-current.md`, `worlds/korvin-merrow/task-setup/task2/preference-labeling/PL-recommended-verdict-DRAFT.md`, `worlds/korvin-merrow/task-setup/task2/qa/KM02-taiga-qa-log.md`, and `worlds/korvin-merrow/task-setup/task2/runs/escalation-v3/`; read `worlds/korvin-merrow/task-setup/task2/runs/clean-pilot/` and `worlds/korvin-merrow/task-setup/task2/runs/escalation-v2/` only as baselines. For Task 3, start with `worlds/korvin-merrow/task-setup/task3/TASK3-STATE.md`, `worlds/korvin-merrow/task-setup/task3/KM03-state-log.md`, `worlds/korvin-merrow/task-setup/task3/runs/KM03-taiga-results-58b5f3e3.md`, `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-KM02-BAR-PLAN.md`, `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-KM02bar-review-request-for-claude-ai.md`, and `worlds/korvin-merrow/task-setup/platform/task3/current/`; active v2.2 filenames are `prompt-task3-v2.2.txt`, `discharge_planning_summary_draft_05242026.docx`, `golden-KM03-v2.2.docx`, and `grader-guidelines-task3-v2.2.txt`, while v2.1 evidence lives under `platform/task3/archive/v2.1-difficulty-failed-after-58b5f3e3/`. Historical design/gate records remain under `task3/design/`, `task3/KM03-3rd-reader-review-and-build-gates.md`, and `task3/build-phase-drafts/`. For Task 4, start with `worlds/korvin-merrow/task-setup/task4/TASK4-STATE.md` and `worlds/korvin-merrow/task-setup/task4/runs/KM04-taiga-results-55ee209f.md`; treat `platform/task4/current/`, `RUN-INSTRUCTIONS.md`, and prior KM04 black-team review files as v1 evidence only after the difficulty failure. For Task 5, start with `worlds/korvin-merrow/task-setup/task5/TASK5-STATE.md`, `worlds/korvin-merrow/task-setup/task5/design/KM05-design-plan-for-review.md`, `worlds/korvin-merrow/task-setup/task5/design/KM05-claude-ai-proposal-6-7.md`, `worlds/korvin-merrow/task-setup/task5/design/KM05-codex-black-team-6-7.md`, `worlds/korvin-merrow/task-setup/task5/KM05-prebuild-review-and-build-gates.md`, and `worlds/korvin-merrow/task-setup/task5/build-phase-drafts/KM05-review-request-for-claude-ai.md`; treat it as review-converged only until Alexander authorizes build/platform staging. Use `worlds/korvin-merrow/file-review/file-review-protocol.md`, `worlds/korvin-merrow/file-review/time-strategy-and-state.md`, `worlds/korvin-merrow/file-review/findings-triage.md`, and `worlds/korvin-merrow/file-review/file-review-log.md` as the closed Step 9 audit trail. The next legal action is whatever Alexander explicitly authorizes for the next task/pipeline step. Do not run agents, run QA, create AutoQC responses, mutate RL Studio, submit preference labels, upload additional Task 3 or Task 4 files, alter KM04 staged files, rerun or redesign KM04, run KM03 v2.2 Taiga, or build/stage KM05 platform files unless Alexander explicitly authorizes the exact step.

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

If asked to help now, Claude should support Task 1 final-review-complete handoff and the next explicitly authorized task step:

- use `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md` as the canonical Task 1 state source;
- use `worlds/korvin-merrow/task-setup/reviews/task1-final-review-ao-2026-06-06.md` as the final approval record;
- preserve the post-Abi rework, hardening, FA/GA, PL, and final review history as provenance, not the current gate;
- do not draft or mutate platform state without explicit authorization;
- apply `docs/reasoning-discipline.md` before one-way-door decisions or causal platform-behavior claims;
- use `worlds/korvin-merrow/task-setup/task1/FA-GA-final.md`, grading transcript findings, and the v1/v2 trajectory exports as historical learning evidence only once task files are deleted;
- for Tasks 2-6, review/de-hint task prompts against final generated files and the physician-perspective rule;
- for Tasks 2-6, wait until Task 1's post-Abi pattern is stable, then build from the v5 mechanism-agnostic structure rather than v3/golden-only, v4 `/docs`-aware, or the older A/B/C pattern;
- preserve trap fidelity, especially prednisone ambiguity, EW22 incompleteness, buried functional evidence, and consultant-friction balance;
- keep Step 9 file-review provenance in `worlds/korvin-merrow/file-review/`, not in the original onboarding transcript.

## Workspace Doctrine Note

The workspace contains overlapping prep and guideline docs. This is intentional but should now be treated as supporting reference material. The active cockpit for the World Spec transition is `WORLD_SPEC_KICKOFF.md`; the live state source is `project/STATUS.md`; exact AutoQC checks live in `reference/world-spec-guidelines/08_autoqc_master_index.md`; practical authoring flow lives in `reference/world-spec-guidelines/09_world_spec_writer_playbook.md`.


---
CURRENT STATE 6/8: KM02 COMPLETE / RFD (Ready for Delivery) after Janette's 6/8 final review. Both prior human reviews passed (Abi 6/7), all recorded KM02 checks are green, and Preference Labels were submitted with verdict B / B++. Golden sha 2dd3e0ad. KM03 v2.1 platform set is retained as evidence after difficulty failure; job `58b5f3e3` is recorded as the difficulty-failed trajectory run. Active KM03 v2.2 platform set is present in `platform/task3/current/` and passed Task AutoQC 36/36 (`qcaud_fc`): `prompt-task3-v2.2.txt`, `discharge_planning_summary_draft_05242026.docx`, `golden-KM03-v2.2.docx`, and `grader-guidelines-task3-v2.2.txt`. Taiga is intentionally held. Retired v1 passed Task AutoQC 36/36 (`qcaud_6b`) after core metadata scrub; later job `58b5f3e3` confirmed v1 was too easy and is historical only. KM04 v1 failed the 6/8 trajectory difficulty gate (`55ee209f`, mean 0.912, zero sub-70); the v1 staged set is evidence only and golden sign-off is no longer the next gate unless Alexander explicitly overrides or redesigns. KM05 is review-converged only under `task-setup/task5/`, not built or platform-staged.


---
6/7 late: KM03 v2.1 ACTIVE AFTER ALEXANDER UPLOAD. v2.1 current set is platform/task3/current/ (prompt-task3-v2.txt, care_coordination_handoff_draft_05242026.docx, golden-KM03-v2.docx, grader-guidelines-task3-v2.txt, RUN-INSTRUCTIONS.md). v1 preserved unchanged at platform/task3/archive/v1-retired-after-task-writing-reset/ (uploaded, AutoQC qcaud_6b pass, later job 58b5f3e3 returned too easy, retired after task-writing reset; historical only). Mechanism: authoring posture over a de-authorized unsigned care-coordination handoff DRAFT; fair failure = promoting the draft unverified completion into a signed physician addendum. Build authority = KM03-v2.1-LOCKED-build-plan.md. NOT performed by Claude Code: RL Studio upload or Task AutoQC / pre-Taiga QC. CURRENT: Alexander uploaded the v2.1 files and Task AutoQC passed with no non-pass flags (`qcaud_fc`); job `58b5f3e3` is recorded as the difficulty-failed trajectory run.
