# Korvin Merrow World

KM04 v2 update 6/8: v2 cleared the difficulty gate after job `709be0e8` (mean 0.689, three sub-70, tail 0.15) on the anemia-of-CKD / absent iron-workup propagation axis. Durable records: `task-setup/task4/runs/KM04-v2-taiga-results-709be0e8.md` and `task-setup/task4/runs/KM04-v2-grading-transcripts-709be0e8.md`; local FA/GA draft: `task-setup/task4/fa-ga/FA-GA-current.md`, subject Attempt 5 (0.15), comparator Attempt 6 (0.97). The v2 platform set remains under `task-setup/platform/task4/current/`; v1 evidence is archived at `task-setup/platform/task4/archive/2026-06-08-pre-clean/`. No platform FA/GA submission, PL, final review, locked-canon edit, or live-world edit exists.

KM04 PL prep update 6/8: local draft `task-setup/task4/preference-labeling/KM04-PL-recommended-verdicts-DRAFT.md` exists for three separate post-FA/GA PL comparisons. It is draft-only, not platform-submitted, and no PL AutoQC has been run.

KM05 reset 6/8: start with `task-setup/task5/TASK5-STATE.md` and `task-setup/task5/design/KM05-v2-design-plan-6-8.md`. Older 6/7 convergence files are historical; their moderate-task fallback is retired. Current lead hypothesis is an unsupported post-discharge BMP / stable renal-potassium monitoring claim inside a transition-clinic draft. No KM05 build, platform staging, upload, AutoQC, Taiga, QA, FA/GA, or PL exists.

Current state: World created as `Healthcare_247_Merrow`; Step 9 generated-file review COMPLETE; Task 1 final human review COMPLETE / APPROVED. Task 2 / KM02 is COMPLETE / RFD (Ready for Delivery) after Janette's 6/8 final review: golden `golden-KM02-v5.docx` is re-dated to 05/24/2026 with sha256 prefix `2dd3e0ad`, Task AutoQC / Taiga gates passed qcaud_5e, qcaud_4a, and qcaud_ef, final FA/GA uses Attempt 8 at 0.30 from v3 job `8f393839`, and Preference Labels were submitted with verdict B / B++. Task 3 / KM03 escalation through v2.1 is difficulty-failed after job `58b5f3e3` (90-97, mean about 93.6, zero sub-70), with the transcript-lineage caveat recorded in `task-setup/task3/runs/KM03-taiga-results-58b5f3e3.md`. Task 3 / KM03 v2.2 then cleared the Taiga difficulty gate after job `877aa204`: mean 69.0, four sub-70 runs, six sub-90 runs, tail 0.20; record at `task-setup/task3/runs/KM03-v2.2-taiga-results-877aa204.md`. Task 4 / KM04 v1 failed the 6/8 trajectory difficulty gate after job `55ee209f`: 10 runs scored 0.87-0.95, mean 0.912, zero sub-70; record at `task-setup/task4/runs/KM04-taiga-results-55ee209f.md`. Task 5 / KM05 is review-converged / HOLD under `task-setup/task5/`, but its older moderate-task label is retired by the 6/8 no-moderate directive; it is not built, not platform-staged, not uploaded, not AutoQC-run, and not agent-run. Retired KM03 v1 passed Task AutoQC 36/36 (`qcaud_6b`), then job `58b5f3e3` confirmed v1 was too easy; it is historical only. KM03 grading transcripts are verified clean, a local FA/GA drafting packet exists, and the verified local FA/GA current draft is `task-setup/task3/fa-ga/FA-GA-current.md`; next KM03 platform step is FA/GA entry on Attempt 9 (0.20), if explicitly authorized. No further platform mutation without exact authorization.

KM03 update 6/8: KM03 escalation through v2.1 is difficulty-failed: job `58b5f3e3` scored 90-97 (mean about 93.6), zero sub-70; the run record notes a lineage caveat because captured transcripts show v1-era filenames/audit prompt/golden-v1, but Alexander records it as v2.1 and the operational conclusion is v2.2 redesign, not FA/GA/PL/final review from the current mechanism. See `task-setup/task3/runs/KM03-taiga-results-58b5f3e3.md`.

KM03 v2.2 Lenora plan history 6/8: `task-setup/task3/build-phase-drafts/KM03-v2.2-FINAL-PLAN.md` superseded the earlier cold-axis completion/status idea but is now itself superseded as primary by the KM02-bar plan. Preserve as review history only unless Alexander re-selects that mechanism.

KM03 v2.2 reconciliation update 6/8: `task-setup/task3/build-phase-drafts/KM03-v2.2-reconciliation-6-8.md` adopts the Lenora weekday-morning supervision fact plant as a pilot mechanism and records the no-moderate directive. If the pilot does not produce a real clinical failure, redesign and re-pilot; do not accept or ship KM03 as moderate.

KM03 v2.2 KM02-bar plan update 6/8: current primary mechanism source is `task-setup/task3/build-phase-drafts/KM03-v2.2-KM02-BAR-PLAN.md`, with Claude.ai review request at `task-setup/task3/build-phase-drafts/KM03-v2.2-KM02bar-review-request-for-claude-ai.md`. It supersedes the Lenora supervision-fact plan as the primary mechanism and uses a tuned cold fabricated objective result on OSA/CPAP continuity.

KM03 v2.2 platform / Taiga update 6/8: active platform files are `task-setup/platform/task3/current/prompt-task3-v2.2.txt`, `task-setup/platform/task3/current/discharge_planning_summary_draft_05242026.docx`, `task-setup/platform/task3/current/golden-KM03-v2.2.docx`, and `task-setup/platform/task3/current/grader-guidelines-task3-v2.2.txt`. Task AutoQC passed 36/36 (`qcaud_fc`); Taiga job `877aa204` cleared the difficulty gate. Local FA/GA current draft is `task-setup/task3/fa-ga/FA-GA-current.md`; no platform-entered v2.2 FA/GA, PL, final review, additional upload, or AutoQC response exists.

Start here only after reading `project/STATUS.md`.

## Folder Guide

- `active/`: current authored world-facing working files and placeholders.
- `planning/`: world-specific pass and planning documents.
- `history/`: historical development artifacts that preserve audit trail.
- `remediation/`: reviewer SEND BACK remediation decision briefs and compliance review.
- `reviews/`: external/human/AutoQC review artifacts and reviewer feedback history.
- `submission/`: RL Studio submission artifacts.
- `task-setup/`: Task setup, trajectory, QA, FA/GA, PL, review, runbook, and bounded pre-build study provenance after world creation. Task 1 is approved. Task 2 starts at `task-setup/task2/TASK2-STATE.md`; clean-pilot evidence lives under `task-setup/task2/runs/clean-pilot/`, v2 escalation evidence under `task-setup/task2/runs/escalation-v2/`, v3 evidence under `task-setup/task2/runs/escalation-v3/`, submitted PL evidence under `task-setup/task2/preference-labeling/`, and the active platform set under `task-setup/platform/task2/current/`. Task 3 starts at `task-setup/task3/TASK3-STATE.md`, `task-setup/task3/KM03-state-log.md`, `task-setup/task3/fa-ga/FA-GA-current.md`, `task-setup/task3/runs/KM03-taiga-results-58b5f3e3.md`, and `task-setup/task3/runs/KM03-v2.2-taiga-results-877aa204.md`; `task-setup/platform/task3/current/` contains the active v2.2 set, `task-setup/platform/task3/archive/v2.1-difficulty-failed-after-58b5f3e3/` contains v2.1 evidence, and `task-setup/task3/build-phase-drafts/` contains the v2.2 mechanism source and review history. Task 4 starts at `task-setup/task4/TASK4-STATE.md`; v1 difficulty-failure evidence is at `task-setup/task4/runs/KM04-taiga-results-55ee209f.md`; platform files under `task-setup/platform/task4/current/` are the v2 set used for current evidence; v1 evidence is in `task-setup/platform/task4/archive/2026-06-08-pre-clean/`. Task 5 starts at `task-setup/task5/TASK5-STATE.md`; review-only design, convergence reviews, and prebuild materials live under `task-setup/task5/design/` and `task-setup/task5/build-phase-drafts/`.
- `world-spec-prep/`: World Spec preparation cockpit plus lifecycle subfolders for locked decisions, locked, ratifications, reviews, decision logs, and planning scaffolds.
- `world-spec-construction/`: World Spec construction lifecycle folders for candidate review artifacts, locked construction artifacts, and ratifications.
- `file-inventory/`: file inventory lifecycle area. Locked architecture defines planned file ecosystem, and locked File Inventory v1 defines the planned inventory rows; neither creates synthetic files or chart contents.
- `synthetic-files/`: synthetic file construction lifecycle area. Locked construction plan governs construction order; Batch 1 through Batch 5 files are locked, and the World-Level Synthetic File Layer is complete.
- `task-layer-architecture/`: task-layer architecture lifecycle area. Locked architecture defines future FI-T governance and does not create task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission materials.
- `task-context-files/`: task-level context file lifecycle area. FI-T01 through FI-T07 are locked request-framing files only.
- `supplementary-file-architecture/`: supplementary FI-S architecture lifecycle area. Locked architecture defines future FI-S01 through FI-S04 only and does not construct FI-S files.
- `supplementary-files/`: supplementary FI-S file construction lifecycle area. FI-S01 through FI-S04 are locked supplementary files.
- `task-prompt-architecture/`: task-prompt architecture lifecycle area. Locked Task Prompt Architecture v1 defines future prompt families and packaging rules only; it does not create task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission materials.
- `task-prompts/`: task prompt construction lifecycle area. TP-KM01 through TP-KM06 are locked prompts only; they do not create expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission materials.
- `expected-output-architecture/`: expected-output architecture lifecycle area. Locked Expected Output Architecture v1 defines EO-KM01 through EO-KM06 structure only; it does not create actual expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission materials.
- `expected-outputs/`: expected-output construction lifecycle area. EO-KM01 through EO-KM06 are locked expected outputs under `locked/`; they are not golden responses, grader guidance, rubrics, AutoQC responses, DOCX artifacts, or submission materials.
- `golden-architecture/`: Golden Architecture lifecycle area. Locked artifacts define future golden-response architecture only; they do not create golden responses, grader guidance, rubrics, AutoQC responses, DOCX artifacts, or submission materials.
- `goldens/`: golden construction lifecycle area. Golden-KM01 through Golden-KM06 are locked golden responses; they are not grader guidance, rubrics, AutoQC responses, DOCX artifacts, or submission materials.
- `grader-guidance-architecture/`: grader-guidance architecture lifecycle area. Locked artifacts define future grader guidance structure only; they do not create grader guidance, scoring rubrics, scoring thresholds, AutoQC responses, DOCX artifacts, or submission materials.
- `grader-guidance/`: grader-guidance construction lifecycle area. GG-KM01 through GG-KM06 are locked grader guidance files; they are not scoring rubrics, scoring thresholds, pass/fail bands, point allocations, AutoQC responses, DOCX artifacts, or submission materials.
- `autoqc-architecture/`: AutoQC architecture lifecycle area. Locked artifacts define how future AutoQC will be organized; they do not run AutoQC, create AutoQC responses, create scoring artifacts, create DOCX artifacts, or create submission materials.
- `autoqc/`: AutoQC construction lifecycle area. Locked artifacts organize future AutoQC execution order and routing only; they do not run AutoQC, create platform responses, create AutoQC responses, create scoring artifacts, create DOCX artifacts, or create submission materials.
- `packaging-architecture/`: packaging architecture lifecycle area. Locked artifacts define future DOCX, manifest, transcript, reference/template, reconciliation, and upload sequencing strategy only; they do not create package artifacts or submit anything.
- `packaging/`: packaging construction lifecycle area. Locked artifacts prepare future packaging execution only; they do not populate DOCX, create manifests, create final submission packages, upload, submit, run AutoQC, create AutoQC responses, or create scoring artifacts.
- `submission-preparation/`: submission preparation lifecycle area. Locked artifacts organize final execution decisions and stop points only; they do not populate DOCX, create manifests, create submission packages, run AutoQC, upload, or submit.
- `final-submission-resolution/`: final submission dependency resolution lifecycle area. Locked artifacts resolved upload set, export targets, folder mapping, DOCX blueprint, transcript export requirements, and FI-W/FI-T/FI-S transformation boundaries only; they did not generate DOCX/PDF artifacts, create manifests, package, upload, submit, run AutoQC, or create scoring artifacts.

## Active Entry Points

- `00-MASTER-NARRATIVE.md`
- `world-spec-prep/WORLD_SPEC_KICKOFF.md`
- `task-setup/task1-lifecycle-log.md`
- `task-setup/TASK-RUNBOOK.md`
- `task-setup/CHECKPOINT-AUDIT-pre-task2.md`
- `task-setup/task2/TASK2-STATE.md`
- `task-setup/task2/design/`
- `task-setup/task2/build/`
- `task-setup/task2/runs/clean-pilot/`
- `task-setup/task2/runs/escalation-v2/`
- `task-setup/task2/runs/escalation-v3/`
- `task-setup/task2/qa/KM02-taiga-qa-log.md`
- `task-setup/task2/fa-ga/FA-GA-current.md`
- `task-setup/task2/preference-labeling/`
- `task-setup/task2/learnings/KM02-learnings.md`
- `task-setup/task3/TASK3-STATE.md`
- `task-setup/task3/KM03-state-log.md`
- `task-setup/task3/runs/KM03-taiga-results-58b5f3e3.md`
- `task-setup/task3/runs/KM03-v2.2-taiga-results-877aa204.md`
- `task-setup/platform/task3/current/` (active v2.2 set; use v2.2 filenames)
- `task-setup/task3/KM03-3rd-reader-review-and-build-gates.md`
- `task-setup/task3/build-phase-drafts/`
- `task-setup/task3/build-phase-drafts/KM03-v2.2-KM02-BAR-PLAN.md`
- `task-setup/task3/build-phase-drafts/KM03-v2.2-KM02bar-review-request-for-claude-ai.md`
- `task-setup/task3/build-phase-drafts/KM03-v2.2-FINAL-PLAN.md`
- `task-setup/task3/build-phase-drafts/KM03-v2.2-reconciliation-6-8.md`
- `task-setup/task3/build-phase-drafts/KM03-v2.2-strategy-draft.md` (superseded reference)
- `task-setup/task3/build-phase-drafts/KM03-v2.2-review-request-for-claude-ai.md` (superseded reference)
- `task-setup/task3/design/KM03-design-plan-for-review.md`
- `task-setup/task4/TASK4-STATE.md`
- `task-setup/task4/runs/KM04-taiga-results-55ee209f.md`
- `task-setup/task4/runs/KM04-v2-taiga-results-709be0e8.md`
- `task-setup/task4/runs/KM04-v2-grading-transcripts-709be0e8.md`
- `task-setup/task4/fa-ga/FA-GA-current.md`
- `task-setup/task4/preference-labeling/KM04-PL-recommended-verdicts-DRAFT.md`
- `task-setup/platform/task4/current/` (v2 set used for current KM04 evidence)
- `task-setup/task4/build-phase-drafts/KM04-v2-plan.md` (v2 planning/review only)
- `task-setup/task4/build-phase-drafts/KM04-v2-review-request-for-claude-ai.md` (v2 Claude.ai review request only)
- `task-setup/task4/build-phase-drafts/KM04-v2-build-proposal.md` (v2 draft build proposal)
- `task-setup/task4/build-v2/` (raw local v2 build set; do not upload from here)
- `task-setup/platform/task4/archive/2026-06-08-pre-clean/` (v1 evidence and transitional pre-clean files)
- `task-setup/task4/build-phase-drafts/KM04-codex-black-team-review-6-7.md`
- `task-setup/task5/TASK5-STATE.md`
- `task-setup/task5/design/KM05-v2-design-plan-6-8.md`
- `task-setup/task5/design/KM05-design-plan-for-review.md`
- `task-setup/task5/design/KM05-claude-ai-proposal-6-7.md`
- `task-setup/task5/design/KM05-codex-black-team-6-7.md`
- `task-setup/task5/KM05-prebuild-review-and-build-gates.md`
- `task-setup/task5/build-phase-drafts/KM05-review-request-for-claude-ai.md`
- `task-setup/platform/task2/README.md`
- `task-setup/platform/task2/current/`
- `task-setup/reviews/task1-final-review-ao-2026-06-06.md`
- `task-setup/step10-review-packet.md`
- `world-spec-construction/locked/world-spec-v1.md`
- `final-submission-resolution/locked/final-submission-resolution-v1.md`
- `world-spec-construction/ratifications/world-spec-v1-ratification.md`
- `file-inventory/locked/file-inventory-v1.md`
- `file-inventory/ratifications/file-inventory-v1-ratification.md`
- `file-inventory/reviews/fi-t-inventory-task-layer-architecture-reconciliation.md`
- `file-inventory/reviews/supplementary-file-trap5-reconciliation.md`
- `synthetic-files/locked/synthetic-world-file-construction-plan-v1.md`
- `synthetic-files/ratifications/synthetic-world-file-construction-plan-v1-ratification.md`
- `synthetic-files/locked/batch-1/batch-1-validation-review.md`
- `synthetic-files/ratifications/batch-1-ratification.md`
- `synthetic-files/locked/batch-2/batch-2-validation-review.md`
- `synthetic-files/ratifications/batch-2-ratification.md`
- `synthetic-files/locked/batch-3/batch-3-validation-review.md`
- `synthetic-files/ratifications/batch-3-ratification.md`
- `synthetic-files/locked/batch-4/batch-4-validation-review.md`
- `synthetic-files/ratifications/batch-4-ratification.md`
- `synthetic-files/locked/batch-5/batch-5-validation-review.md`
- `synthetic-files/ratifications/batch-5-ratification.md`
- `task-layer-architecture/locked/task-level-context-file-architecture-v1.md`
- `task-layer-architecture/ratifications/task-level-context-file-architecture-v1-ratification.md`
- `task-context-files/locked/task-context-files-validation-review.md`
- `task-context-files/ratifications/task-level-context-file-construction-ratification.md`
- `task-context-files/locked/FI-T01_discharge-medication-reconciliation-request-context.md`
- `task-context-files/locked/FI-T02_discharge-summary-drafting-request-context.md`
- `task-context-files/locked/FI-T03_discharge-readiness-care-coordination-request-context.md`
- `task-context-files/locked/FI-T04_consultant-synthesis-interdisciplinary-care-plan-request-context.md`
- `task-context-files/locked/FI-T05_early-post-discharge-follow-up-assessment-request-context.md`
- `task-context-files/locked/FI-T06_patient-safety-readmission-risk-review-request-context.md`
- `task-context-files/locked/FI-T07_medication-safety-handoff-task-context-addendum.md`
- `supplementary-file-architecture/locked/supplementary-file-architecture-v1.md`
- `supplementary-file-architecture/locked/supplementary-file-architecture-validation-review.md`
- `supplementary-file-architecture/ratifications/supplementary-file-architecture-v1-ratification.md`
- `supplementary-files/locked/supplementary-file-construction-validation-review.md`
- `supplementary-files/ratifications/supplementary-file-construction-ratification.md`
- `task-prompt-architecture/locked/task-prompt-architecture-v1.md`
- `task-prompt-architecture/locked/task-prompt-architecture-validation-review.md`
- `task-prompt-architecture/ratifications/task-prompt-architecture-ratification.md`
- `task-prompts/locked/task-prompt-construction-validation-review.md`
- `task-prompts/ratifications/task-prompt-construction-ratification.md`
- `task-prompts/locked/TP-KM01.md`
- `task-prompts/locked/TP-KM02.md`
- `task-prompts/locked/TP-KM03.md`
- `task-prompts/locked/TP-KM04.md`
- `task-prompts/locked/TP-KM05.md`
- `task-prompts/locked/TP-KM06.md`
- `expected-output-architecture/locked/expected-output-architecture-v1.md`
- `expected-output-architecture/locked/expected-output-architecture-validation-review.md`
- `expected-output-architecture/ratifications/expected-output-architecture-ratification.md`
- `expected-outputs/locked/EO-KM01.md`
- `expected-outputs/locked/EO-KM02.md`
- `expected-outputs/locked/EO-KM03.md`
- `expected-outputs/locked/EO-KM04.md`
- `expected-outputs/locked/EO-KM05.md`
- `expected-outputs/locked/EO-KM06.md`
- `expected-outputs/locked/expected-output-construction-validation-review.md`
- `expected-outputs/ratifications/expected-output-construction-ratification.md`
- `golden-architecture/locked/golden-architecture-v1.md`
- `golden-architecture/locked/golden-architecture-validation-review.md`
- `golden-architecture/locked/golden-architecture-audit-reconciliation.md`
- `golden-architecture/ratifications/golden-architecture-ratification.md`
- `goldens/locked/Golden-KM01.md`
- `goldens/locked/Golden-KM02.md`
- `goldens/locked/Golden-KM03.md`
- `goldens/locked/Golden-KM04.md`
- `goldens/locked/Golden-KM05.md`
- `goldens/locked/Golden-KM06.md`
- `goldens/locked/golden-construction-validation-review.md`
- `goldens/ratifications/golden-construction-ratification.md`
- `grader-guidance-architecture/locked/grader-guidance-architecture-v1.md`
- `grader-guidance-architecture/locked/grader-guidance-architecture-validation-review.md`
- `grader-guidance-architecture/ratifications/grader-guidance-architecture-ratification.md`
- `grader-guidance/locked/GG-KM01.md`
- `grader-guidance/locked/GG-KM02.md`
- `grader-guidance/locked/GG-KM03.md`
- `grader-guidance/locked/GG-KM04.md`
- `grader-guidance/locked/GG-KM05.md`
- `grader-guidance/locked/GG-KM06.md`
- `grader-guidance/locked/grader-guidance-construction-validation-review.md`
- `grader-guidance/ratifications/grader-guidance-construction-ratification.md`
- `autoqc-architecture/locked/autoqc-architecture-v1.md`
- `autoqc-architecture/locked/autoqc-architecture-validation-review.md`
- `autoqc-architecture/ratifications/autoqc-architecture-ratification.md`
- `autoqc/locked/autoqc-construction-v1.md`
- `autoqc/locked/autoqc-construction-validation-review.md`
- `autoqc/ratifications/autoqc-construction-ratification.md`
- `packaging-architecture/locked/packaging-architecture-v1.md`
- `packaging-architecture/locked/packaging-architecture-validation-review.md`
- `packaging-architecture/ratifications/packaging-architecture-ratification.md`
- `packaging/locked/packaging-construction-v1.md`
- `packaging/locked/packaging-construction-validation-review.md`
- `packaging/ratifications/packaging-construction-ratification.md`
- `submission-preparation/locked/submission-preparation-v1.md`
- `submission-preparation/locked/submission-preparation-validation-review.md`
- `submission-preparation/ratifications/submission-preparation-ratification.md`
- `supplementary-files/locked/FI-S01_remote-pci-coronary-stent-provenance-summary.md`
- `supplementary-files/locked/FI-S02_remote-sleep-study-osa-provenance-summary.md`
- `supplementary-files/locked/FI-S03_home-support-equipment-logistics-reference.md`
- `supplementary-files/locked/FI-S04_problem-list-past-history-snapshot.md`
- `file-inventory/locked/file-inventory-architecture-v1.md`
- `file-inventory/ratifications/file-inventory-architecture-ratification.md`
- `world-spec-construction/locked/world-spec-skeleton-v1.md`
- `world-spec-construction/ratifications/world-spec-skeleton-ratification.md`
- `world-spec-prep/locked/clinical-story-timeline-package-v1.md`
- `world-spec-prep/ratifications/clinical-story-timeline-ratification.md`
- `world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`
- `world-spec-prep/locked/task-architecture-package-v1.md`
- `world-spec-prep/ratifications/task-architecture-ratification.md`
- `world-spec-prep/locked/medication-expansion-package-v1.md`
- `world-spec-prep/ratifications/medication-expansion-ratification.md`
- `world-spec-prep/reviews/medication-expansion-decision-addendum.md`
- `world-spec-prep/locked/comorbidity-expansion-package-v1.md`
- `world-spec-prep/ratifications/comorbidity-expansion-ratification.md`
- `world-spec-prep/locked/provider-roster-package-v1.md`
- `world-spec-prep/ratifications/provider-roster-ratification.md`
- `world-spec-prep/locked/surgical-history-package-v1.md`
- `world-spec-prep/ratifications/surgical-history-ratification.md`
- `world-spec-prep/locked/daily-hospital-course-framework-v1.md`
- `world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md`
- `world-spec-prep/locked/baseline-anchor-package-v1.md`
- `world-spec-prep/ratifications/baseline-anchor-ratification.md`
- `world-spec-prep/locked/identity-package-v1.md`
- `world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md`
- `world-spec-prep/decision-logs/physician-decision-log-02.md`
- `world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`
- `active/brainstorm.md`

World Spec v1 is locked. File Inventory Architecture v1 is locked. File Inventory v1 is locked with FI-W20, FI-T, and FI-S03 reconciliations recorded. FI-W01 through FI-W22, FI-T01 through FI-T07, FI-S01 through FI-S04, Task Prompt Architecture v1, TP-KM01 through TP-KM06, Expected Output Architecture v1, EO-KM01 through EO-KM06, Golden Architecture v1, Golden-KM01 through Golden-KM06, Grader Guidance Architecture v1, GG-KM01 through GG-KM06, AutoQC Architecture v1, AutoQC Construction v1, Packaging Architecture v1, Packaging Construction, Submission Preparation, and Execution Preparation v1 are locked. Entire File Ecosystem, Task Prompt Architecture, Task Prompts, Expected Output Architecture, Expected Outputs, Golden Architecture, Goldens, Grader Guidance Architecture, Grader Guidance, AutoQC Architecture, AutoQC, Packaging Architecture, Packaging, Submission Preparation, and Execution Preparation are complete. Grader Guidance Construction is locked at `grader-guidance/locked/` with GG-KM01 through GG-KM06 plus `grader-guidance-construction-validation-review.md`; ratification is recorded at `grader-guidance/ratifications/grader-guidance-construction-ratification.md`. AutoQC Architecture v1 is locked at `autoqc-architecture/locked/` with ratification recorded at `autoqc-architecture/ratifications/autoqc-architecture-ratification.md`. AutoQC Construction is locked at `autoqc/locked/` with `autoqc-construction-v1.md` and `autoqc-construction-validation-review.md`; ratification is recorded at `autoqc/ratifications/autoqc-construction-ratification.md`. Packaging Architecture v1 is locked at `packaging-architecture/locked/` with ratification recorded at `packaging-architecture/ratifications/packaging-architecture-ratification.md`. Packaging Construction is locked at `packaging/locked/` with ratification at `packaging/ratifications/packaging-construction-ratification.md`. Submission Preparation is locked at `submission-preparation/locked/` with ratification at `submission-preparation/ratifications/submission-preparation-ratification.md`. Execution Preparation v1 is locked at `execution-preparation/locked/` with ratification at `execution-preparation/ratifications/execution-preparation-ratification.md`. Transcript Resolution v1 is locked at `transcript-resolution/locked/`. Final Submission Resolution v1 is locked at `final-submission-resolution/locked/` with ratification at `final-submission-resolution/ratifications/final-submission-resolution-ratification.md`. Execution Artifact Generation is authorized for submission-facing artifacts only. Do not run AutoQC, create platform responses, create AutoQC responses, create scoring rubrics, scoring thresholds, pass/fail bands, point allocations, create manifests, create final submission packages, use RL Studio, upload, submit, or create non-authorized reference files until Alexander explicitly authorizes the relevant step.

Task-design guidance: future task prompts and deliverables must be framed from the physician perspective or physician voice, even when supporting sources come from pharmacy, nursing, PT/OT, case management, social work, family, or administrative sources. This is a task-layer rule only; it does not reopen Governance Package v1 or change source-of-truth hierarchy.

Cross-artifact consistency verification is a standing governance rule. Before creating, modifying, ratifying, or locking architecture, inventory, matrix, mapping, workflow/trap/friction/hierarchy table, or governance artifacts, collaborators must check applicable locked canonical sources and document any coverage or hierarchy change before ratification or lock.
