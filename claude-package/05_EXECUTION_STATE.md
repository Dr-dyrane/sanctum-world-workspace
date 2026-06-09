# Execution State

Purpose: compressed current state for Claude. Use `project/STATUS.md` and `docs/status-dashboard.md` locally for live status.

## Project State

Current phase override 6/8 for KM05: Task 5 is review-only reset / HOLD from `worlds/korvin-merrow/task-setup/task5/design/KM05-v2-design-plan-6-8.md`; older 6/7 review-convergence language below is historical unless Alexander re-selects it.

Current phase: Task 1 final human review complete / approved; Task 2 / KM02 COMPLETE / RFD (Janette 6/8 final review); Task 3 / KM03 post-Sang rerun complete with FA/GA entered on platform and FA/GA AutoQC passed; Task 4 / KM04 post-Sang rerun complete with FA/GA entered on platform and FA/GA AutoQC passed; Task 5 / KM05 review-only reset / HOLD with cold home-health lead review request, before build/platform staging. World Spec approval is complete, onboarding has ended, engineering pipeline run #1 completed, Step 9 generated-file review is closed, Final Files AutoQC passed 78/78 after three revisions, and the world was created as `Healthcare_247_Merrow` on 2026-06-05 at 11:20 AM PDT. Pod assignment is `#vaguspod`; EPM Rose; pod leads Abi O and Larry E. Task 1 advanced through AO rework, hardening, Abi pre-check, revised platform entry, pilot runs, FA/GA, Preference Labeling, and final human review. Abi Osagie completed the final review checklist on 2026-06-06 with applicable items marked Yes or N/A. KM02 v3 active platform set is prompt `prompt-task2-escalation.txt`, golden `golden-KM02-v5.docx` re-dated to 05/24/2026 with sha256 prefix `2dd3e0ad`, grader `grader-guidelines-task2.txt`, and mounted draft `discharge_summary_draft_incomplete_05242026.docx`; Task AutoQC / Taiga gates passed qcaud_5e, qcaud_4a, and qcaud_ef; v3 spread was 45, 92, 82, 82, 60, 62, 40, 30, 45, 55; final FA/GA subject was Attempt 8 at 0.30; Preference Labels were submitted with verdict B / B++; all recorded KM02 checks are green. KM03 escalation through v2.1 is difficulty-failed: job `58b5f3e3` scored 90-97 (mean about 93.6), zero sub-70; the run record notes a lineage caveat because captured transcripts show v1-era filenames/audit prompt/golden-v1. Active KM03 v2.2 platform files are `platform/task3/current/prompt-task3-v2.2.txt`, `platform/task3/current/discharge_planning_summary_draft_05242026.docx`, `platform/task3/current/golden-KM03-v2.2.docx`, and `platform/task3/current/grader-guidelines-task3-v2.2.txt`; Task AutoQC passed 36/36 (`qcaud_fc`), and Taiga job `877aa204` cleared the difficulty gate with mean 69.0, four sub-70 runs, and tail 0.20. KM03 post-Sang rerun job `8e97cdd7` selected Attempt 4 (0.30); Alexander entered FA/GA on platform and FA/GA AutoQC passed. KM04 v1 trajectory evidence is recorded at `worlds/korvin-merrow/task-setup/task4/runs/KM04-taiga-results-55ee209f.md`: job `55ee209f-c9fa-4a64-8071-70d8917508da`, 10 runs 0.87-0.95, mean 0.912, zero sub-70. KM04 v2 cleared the difficulty gate after job `709be0e8` (mean 0.689, three sub-70, tail 0.15); durable records are `worlds/korvin-merrow/task-setup/task4/runs/KM04-v2-taiga-results-709be0e8.md` and `worlds/korvin-merrow/task-setup/task4/runs/KM04-v2-grading-transcripts-709be0e8.md`; post-Sang KM04 rerun job `979dccde` selected Attempt 9 (0.30); Alexander entered FA/GA on platform, FA/GA AutoQC passed, KM04 PL #1-#2 drafts exist locally; no KM04 PL has been submitted and no final review exists yet. KM05 review-only reset starts at `worlds/korvin-merrow/task-setup/task5/TASK5-STATE.md`, `design/KM05-v2-design-plan-6-8.md`, and `build-phase-drafts/KM05-v2-review-request-for-claude-ai.md`; older 6/7 review records are history; it is not built, not platform-staged, not uploaded, not AutoQC-run, and not agent-run. Retired KM03 v1 passed Task AutoQC 36/36 (`qcaud_6b`) after DOCX core-metadata scrub; later job `58b5f3e3` confirmed v1 was too easy and is historical only. Step 9 audit trail remains at `worlds/korvin-merrow/file-review/`; Task 1 canonical lifecycle state is `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md`; final review record is `worlds/korvin-merrow/task-setup/reviews/task1-final-review-ao-2026-06-06.md`. Reasoning discipline lives at `docs/reasoning-discipline.md`.

KM03 superseding platform note 6/8: v2.2 redesign has now been built into the active platform set, Task AutoQC passed 36/36 (`qcaud_fc`), and Taiga job `877aa204` cleared the difficulty gate. Use `platform/task3/current/prompt-task3-v2.2.txt`, `platform/task3/current/discharge_planning_summary_draft_05242026.docx`, `platform/task3/current/golden-KM03-v2.2.docx`, and `platform/task3/current/grader-guidelines-task3-v2.2.txt` for any current KM03 work.

KM05 update 6/8: review-only reset / HOLD. Start with `worlds/korvin-merrow/task-setup/task5/TASK5-STATE.md`, `worlds/korvin-merrow/task-setup/task5/design/KM05-v2-design-plan-6-8.md`, and `worlds/korvin-merrow/task-setup/task5/build-phase-drafts/KM05-v2-review-request-for-claude-ai.md`; older 6/7 convergence files are historical. Current lead hypothesis is a cold home-health-start / completed medication-review / good-adherence interval-observation claim inside a transition-clinic draft; renal-BMP is backup only. The older moderate-task classification is retired by the 6/8 no-moderate directive in `TASK-RUNBOOK.md`. No KM05 DOCX build, platform-current staging, RL Studio upload, Task AutoQC, Taiga trajectories, QA, or platform mutation has occurred.

KM03 update 6/8: KM03 escalation through v2.1 is difficulty-failed: job `58b5f3e3` scored 90-97 (mean about 93.6), zero sub-70; the run record notes a lineage caveat because captured transcripts show v1-era filenames/audit prompt/golden-v1, but Alexander records it as v2.1 and the operational conclusion is v2.2 redesign, not FA/GA/PL/final review from the current mechanism. Track the markdown result at `worlds/korvin-merrow/task-setup/task3/runs/KM03-taiga-results-58b5f3e3.md`; transcript tarballs remain ignored/local evidence.

KM03 v2.2 Lenora plan history 6/8: `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-FINAL-PLAN.md` superseded the earlier cold-axis completion/status idea but is now itself superseded as primary by the KM02-bar plan. Preserve as review history only unless Alexander re-selects that mechanism.

KM03 v2.2 reconciliation update 6/8: `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-reconciliation-6-8.md` adopts the Lenora plant as a pilot mechanism and records the no-moderate directive. If the pilot does not produce a real clinical failure, redesign and re-pilot; do not accept or ship KM03 as moderate. Resolve its listed Codex confirmations before any build gate.

KM03 v2.2 KM02-bar plan update 6/8: current primary mechanism source is `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-KM02-BAR-PLAN.md`, with Claude.ai review request at `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-KM02bar-review-request-for-claude-ai.md`. It supersedes the Lenora supervision-fact plan as primary and defines the tuned CPAP/OSA fabricated objective-result mechanism used by the active v2.2 platform set.

KM03 v2.2 platform / Taiga update 6/8: active files are `worlds/korvin-merrow/task-setup/platform/task3/current/prompt-task3-v2.2.txt`, `worlds/korvin-merrow/task-setup/platform/task3/current/discharge_planning_summary_draft_05242026.docx`, `worlds/korvin-merrow/task-setup/platform/task3/current/golden-KM03-v2.2.docx`, and `worlds/korvin-merrow/task-setup/platform/task3/current/grader-guidelines-task3-v2.2.txt`. Task AutoQC passed 36/36 (`qcaud_fc`). Taiga job `877aa204` cleared the difficulty gate; verified local FA/GA current draft is `worlds/korvin-merrow/task-setup/task3/fa-ga/FA-GA-current.md`; no platform-entered FA/GA, PL, final review, additional upload, or AutoQC response exists.

KM04 update 6/8: v1 failed the difficulty gate after job `55ee209f` (10 runs 0.87-0.95, mean 0.912, zero sub-70). V2 cleared the difficulty gate after job `709be0e8` (mean 0.689, three sub-70, tail 0.15) on the anemia-of-CKD / absent iron-workup propagation axis. Durable records are `worlds/korvin-merrow/task-setup/task4/runs/KM04-v2-taiga-results-709be0e8.md` and `worlds/korvin-merrow/task-setup/task4/runs/KM04-v2-grading-transcripts-709be0e8.md`; post-Sang FA/GA entry uses Attempt 9 (0.30), FA/GA AutoQC passed, and KM04 PL #1-#2 are drafted locally. Do not submit PLs, run PL AutoQC, start final review, rerun Taiga, or mutate platform state without exact Alexander authorization.

KM04 PL prep update 6/8: local planning draft `worlds/korvin-merrow/task-setup/task4/preference-labeling/KM04-PL-recommended-verdicts-DRAFT.md` exists, and PL #1 and #2 backups are drafted under `worlds/korvin-merrow/task-setup/task4/preference-labeling/`. Neither is platform-submitted; no PL AutoQC has been run.

Pipeline run #1 / Step 9 closeout state:

- Output ingested at `worlds/korvin-merrow/file-review/pipeline-output/`.
- Generated files: 33 DOCX files under `pipeline-output/filesystem/`.
- Metadata: 134 `.meta` files under `pipeline-output/.meta/`.
- Initial World Files AutoQC: 74/76 pass; the two fails were access/routing failures, not inspected-content failures.
- Final Files AutoQC: 78/78 pass after revision #3.
- World created: `Healthcare_247_Merrow`, world ID `world_d50c832ac6474a68ba982a77e28a6bbe`, snapshot `snap_0fb032e95b324710b12a7432cf7da6c1`, 26 files synced.
- Active protocol: `worlds/korvin-merrow/file-review/file-review-protocol.md`.
- Active Claude-assisted triage: `worlds/korvin-merrow/file-review/findings-triage.md`.
- Candidate revision log: `worlds/korvin-merrow/file-review/file-review-log.md`.
- Revised 33-file working snapshot: `worlds/korvin-merrow/file-review/revision/filesystem/`.
- Final 26-file world-level upload set: `worlds/korvin-merrow/file-review/upload/filesystem/`.
- Seven task-level files are held out at `worlds/korvin-merrow/file-review/task-files-holdback/` for later task setup handling.
- Items marked `[A]` required Alexander physician ruling before edits; rulings and candidate edits are recorded in the file-review log.
- Do not access RL Studio, upload additional task prompts/goldens/grader guidelines, run additional agents, run additional QA, create AutoQC responses, create task setup materials, edit submitted Failure Analysis / Grader Analysis or Preference Labeling records, or mutate platform state unless Alexander explicitly authorizes the exact step.

Transcript resolution: `docs/claude-transcript-formatted.md` is the authoritative transcript upload artifact. The Claude share URL `https://claude.ai/share/d5129364-5d6c-4a2c-acb3-282f367a0040` is supporting provenance and reviewer-access support. `docs/claude-transcript.md` remains raw historical/provenance evidence only. Historical James Carter references and export encoding artifacts inside it are expected provenance, not current identity defects.

FI-W20 inventory row reconciliation is recorded at `worlds/korvin-merrow/file-inventory/reviews/fi-w20-inventory-row-reconciliation.md`. FI-S03 Trap #5 reconciliation is recorded at `worlds/korvin-merrow/file-inventory/reviews/supplementary-file-trap5-reconciliation.md`. World-Level Synthetic File Layer, Task-Level Context Files, Supplementary Files, the Entire File Ecosystem, Task Prompt Architecture, Task Prompt Construction, Expected Output Architecture, Expected Output Construction, Golden Architecture, Golden Construction, Grader Guidance Architecture, Grader Guidance Construction, AutoQC Architecture, AutoQC Construction, Packaging Architecture, Packaging Construction, and Submission Preparation are complete and locked. AutoQC Architecture v1 is locked under `worlds/korvin-merrow/autoqc-architecture/locked/` with ratification at `worlds/korvin-merrow/autoqc-architecture/ratifications/autoqc-architecture-ratification.md`. AutoQC Construction is locked under `worlds/korvin-merrow/autoqc/locked/` with ratification at `worlds/korvin-merrow/autoqc/ratifications/autoqc-construction-ratification.md`. AutoQC is complete. Packaging Architecture v1 is locked under `worlds/korvin-merrow/packaging-architecture/locked/` with ratification at `worlds/korvin-merrow/packaging-architecture/ratifications/packaging-architecture-ratification.md`. Packaging Construction is locked under `worlds/korvin-merrow/packaging/locked/` with `packaging-construction-v1.md` and `packaging-construction-validation-review.md`; ratification is recorded at `worlds/korvin-merrow/packaging/ratifications/packaging-construction-ratification.md`. Packaging is complete. Submission Preparation locked artifacts are under `worlds/korvin-merrow/submission-preparation/locked/`. Execution Preparation v1 locked artifacts are under `worlds/korvin-merrow/execution-preparation/locked/`, with ratification at `worlds/korvin-merrow/execution-preparation/ratifications/execution-preparation-ratification.md`. Task Prompt Architecture v1 is locked at `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-v1.md`, with validation review at `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-validation-review.md` and ratification at `worlds/korvin-merrow/task-prompt-architecture/ratifications/task-prompt-architecture-ratification.md`. Task Prompt Construction is locked at `worlds/korvin-merrow/task-prompts/locked/`; TP-KM01 through TP-KM06 and `task-prompt-construction-validation-review.md` are locked, with ratification recorded at `worlds/korvin-merrow/task-prompts/ratifications/task-prompt-construction-ratification.md`. Expected Output Architecture v1 is locked at `worlds/korvin-merrow/expected-output-architecture/locked/`, with ratification recorded at `worlds/korvin-merrow/expected-output-architecture/ratifications/expected-output-architecture-ratification.md`. Expected Output Construction is locked under `worlds/korvin-merrow/expected-outputs/locked/`; EO-KM01 through EO-KM06 and `expected-output-construction-validation-review.md` are locked, with ratification recorded at `worlds/korvin-merrow/expected-outputs/ratifications/expected-output-construction-ratification.md`. FI-T07 remains addendum support for EO-KM01 only; no EO-KM07 exists. Golden Architecture v1 is locked at `worlds/korvin-merrow/golden-architecture/locked/`, with audit reconciliation preserved at `worlds/korvin-merrow/golden-architecture/locked/golden-architecture-audit-reconciliation.md` and ratification recorded at `worlds/korvin-merrow/golden-architecture/ratifications/golden-architecture-ratification.md`. Golden Construction is locked at `worlds/korvin-merrow/goldens/locked/`: Golden-KM01 through Golden-KM06 plus `golden-construction-validation-review.md`. Ratification is recorded at `worlds/korvin-merrow/goldens/ratifications/golden-construction-ratification.md`. Goldens are complete. No Golden-KM07 exists. Grader Guidance Architecture v1 locked artifacts are under `worlds/korvin-merrow/grader-guidance-architecture/locked/`: `grader-guidance-architecture-v1.md` and `grader-guidance-architecture-validation-review.md`, with ratification recorded at `worlds/korvin-merrow/grader-guidance-architecture/ratifications/grader-guidance-architecture-ratification.md`. Grader Guidance Construction is locked under `worlds/korvin-merrow/grader-guidance/locked/` with GG-KM01 through GG-KM06 and `grader-guidance-construction-validation-review.md`; ratification is recorded at `worlds/korvin-merrow/grader-guidance/ratifications/grader-guidance-construction-ratification.md`. Grader Guidance is complete. No GG-KM07, scoring rubric, scoring threshold, pass/fail band, point allocation, AutoQC response, populated DOCX artifact, manifest, final submission package, upload record, or submission artifact has been created.

Brainstorm:

- Original Brainstorm submitted in RL Studio.
- RL Studio task ID: `cyau8803`.
- RL Studio status: Brainstorm approved / ready for World Spec transition.
- Original submission timestamp: `5/29/2026 2:49 PM PDT`.
- Revised Korvin Merrow Brainstorm uploaded after SEND BACK remediation.
- Brainstorm AutoQC rerun: `0 failed / 51 passed`.
- Diagnostics reviewed.
- Plan resubmitted for reviewer review.
- Human Review: GO from Stacey S after SEND BACK remediation.
- Approval source: Slack / Stacey S.
- Reviewer message: "great job! I approved your brainstorm. Next steps are to move forward with world spec and file template development."

Current blocker:

- Active blocker: no repository blocker. Task 1 final human review is complete. Task 2 / KM02 is COMPLETE / RFD (Ready for Delivery); Preference Labels were submitted with verdict B / B++ and Janette completed the final review on 6/8. Task 2 state starts at `task-setup/task2/TASK2-STATE.md`. Active platform set: `platform/task2/current/prompt-task2-escalation.txt`, `platform/task2/current/golden-KM02-v5.docx` (`2dd3e0ad`), `platform/task2/current/grader-guidelines-task2.txt`, and `platform/task2/current/discharge_summary_draft_incomplete_05242026.docx`. Tasks 3-6 may continue locally only if Alexander explicitly authorizes bounded parallel prep. Additional platform actions remain gated on explicit Alexander authorization for the exact step.

Next legal action:

- Use `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md` as the canonical Task 1 source of truth.
- Use `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md`, `worlds/korvin-merrow/task-setup/reviews/task1-final-review-ao-2026-06-06.md`, `TASK-RUNBOOK.md`, and `docs/reasoning-discipline.md` for Task 1 provenance and future task continuation.
- For Task 2, start with `worlds/korvin-merrow/task-setup/task2/TASK2-STATE.md`, `worlds/korvin-merrow/task-setup/task2/fa-ga/FA-GA-current.md`, `worlds/korvin-merrow/task-setup/task2/preference-labeling/PL-recommended-verdict-DRAFT.md`, `worlds/korvin-merrow/task-setup/task2/qa/KM02-taiga-qa-log.md`, and `worlds/korvin-merrow/task-setup/task2/runs/escalation-v3/`; use `worlds/korvin-merrow/task-setup/task2/runs/clean-pilot/` and `worlds/korvin-merrow/task-setup/task2/runs/escalation-v2/` as historical baselines only.
- For Task 3, start with `worlds/korvin-merrow/task-setup/task3/TASK3-STATE.md`, `worlds/korvin-merrow/task-setup/task3/KM03-state-log.md`, `worlds/korvin-merrow/task-setup/task3/fa-ga/FA-GA-current.md`, `worlds/korvin-merrow/task-setup/task3/runs/KM03-taiga-results-58b5f3e3.md`, `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-KM02-BAR-PLAN.md`, `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-KM02bar-review-request-for-claude-ai.md`, and `worlds/korvin-merrow/task-setup/platform/task3/current/`. Active v2.2 files are `prompt-task3-v2.2.txt`, `discharge_planning_summary_draft_05242026.docx`, `golden-KM03-v2.2.docx`, and `grader-guidelines-task3-v2.2.txt`; Task AutoQC passed (`qcaud_fc`), Taiga job `877aa204` cleared the difficulty gate, and grading transcripts are verified clean. The pre-Sang local FA/GA draft was verified against Attempt 9 but is superseded; post-Sang platform entry uses Attempt 4 (0.30), and FA/GA AutoQC passed. The KM03 v2.1 escalation set lives under `platform/task3/archive/v2.1-difficulty-failed-after-58b5f3e3/`; v2.1 is recorded as difficulty-failed in job `58b5f3e3`. Retired v1 lives under `platform/task3/archive/v1-retired-after-task-writing-reset/`; job `58b5f3e3` confirmed v1 is too easy. The Lenora final plan and reconciliation are superseded review history. Do not rerun AutoQC, run Taiga, run agents, run QA, upload additional files, submit PLs, run PL AutoQC, start final review, or mutate RL Studio without explicit Alexander authorization for that exact step.
- For Task 4, do not start from memory. First read `project/WORKSPACE_FILE_MAP.md` Navigation Rule, `worlds/korvin-merrow/task-setup/task4/TASK4-STATE.md`, `worlds/korvin-merrow/task-setup/task4/runs/KM04-taiga-results-55ee209f.md`, `worlds/korvin-merrow/task-setup/task4/build-phase-drafts/KM04-v2-plan.md`, `worlds/korvin-merrow/task-setup/task4/build-phase-drafts/KM04-v2-review-request-for-claude-ai.md`, `worlds/korvin-merrow/task-setup/task4/build-phase-drafts/KM04-v2-build-proposal.md`, `worlds/korvin-merrow/task-setup/task4/build-v2/`, and `worlds/korvin-merrow/task-setup/platform/task4/current/RUN-INSTRUCTIONS.md`. KM04 v1 has completed trajectory evidence and failed the difficulty gate; v2 cleared the difficulty gate after job `709be0e8` and has a verified local FA/GA draft. Treat `platform/task4/archive/2026-06-08-pre-clean/` as v1 evidence only. Do not submit PLs, run PL AutoQC, start final review, upload changes, rerun, or redesign further without exact Alexander authorization.
- For Task 5, do not start from memory. First read `worlds/korvin-merrow/task-setup/task5/TASK5-STATE.md` and `worlds/korvin-merrow/task-setup/task5/design/KM05-v2-design-plan-6-8.md`; read older 6/7 KM05 review files only as history unless Alexander re-selects them. KM05 is review-only reset / HOLD and not build-ready; do not build DOCX artifacts, create platform-current files, upload, run AutoQC, run Taiga, run QA, or mutate RL Studio without exact Alexander authorization.
- Use `worlds/korvin-merrow/file-review/file-review-protocol.md`, `worlds/korvin-merrow/file-review/time-strategy-and-state.md`, `worlds/korvin-merrow/file-review/findings-triage.md`, and `worlds/korvin-merrow/file-review/file-review-log.md` as the closed Step 9 audit trail.
- Treat `worlds/korvin-merrow/file-review/pipeline-output/filesystem/` as the downloaded V1 output, `worlds/korvin-merrow/file-review/revision/filesystem/` as the final revised 33-file working set, and `worlds/korvin-merrow/file-review/upload/filesystem/` as the final 26-file world-level upload set used for world creation.
- Treat `worlds/korvin-merrow/file-review/task-files-holdback/` as the seven task-level files intentionally held out of the world-level upload set for later task setup handling.
- Do not access RL Studio, upload task setup materials, run agents, run QA, create AutoQC responses, edit submitted Failure Analysis / Grader Analysis or Preference Labeling records, or mutate platform state unless Alexander explicitly authorizes the exact step.
- Do not revise locked architecture, locked canon, original final submission staging, or the original pipeline output unless Alexander explicitly authorizes reopening.

## Completed

- Brainstorm physician interview.
- Brainstorm draft assembly.
- Brainstorm internal audit.
- Claude hostile Brainstorm review triage and selective remediation.
- Brainstorm AutoQC remediation.
- Official Brainstorm template rebuild.
- Submission artifact generation: `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx`.
- RL Studio Brainstorm upload.
- Brainstorm AutoQC final pass recorded.
- Brainstorm submitted for Human Review.
- Human Review SEND BACK captured.
- Synthetic identity and World Type remediation applied locally.
- Comorbidity decision brief created and physician-approved.
- Medication decision brief created and physician-approved.
- Reviewer remediation compliance review created.
- Active Brainstorm source updated with approved comorbidity expansion and medication specificity.
- `Korvin_Merrow_Brainstorm.docx` regenerated and locally verified.
- Revised Korvin Merrow Brainstorm uploaded to RL Studio.
- Brainstorm AutoQC rerun completed: `0 failed / 51 passed`.
- Diagnostics reviewed.
- Plan resubmitted for reviewer review.
- Brainstorm Human Review GO received from Stacey S.
- Reviewer GO recorded: `worlds/korvin-merrow/reviews/reviewer-go-01.md`.
- World Spec preparation packet created.
- Official World Spec template acquired: `reference/templates/World_Spec_Template_05_06.docx`.
- World Spec AutoQC v6.3 acquired: `reference/templates/AutoQC_Section_2_World_Spec_v6.3_writer.docx`.
- 113-check AutoQC master index created: `reference/world-spec-guidelines/08_autoqc_master_index.md`.
- World Spec writer playbook created: `reference/world-spec-guidelines/09_world_spec_writer_playbook.md`.
- Reviewer response protocol created: `docs/reviewer-response-protocol.md`.
- Repository hardening and documentation completed.
- Document tooling installed and verified.
- MCP/integration audit completed.
- Claude World Spec prep review triaged: `worlds/korvin-merrow/world-spec-prep/reviews/claude-review-triage.md`.
- Workspace file map created: `project/WORKSPACE_FILE_MAP.md`.
- Post-GO interview plan created: `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/post-go-interview-plan.md`.
- World Spec kickoff packet created: `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md`.
- Workspace bloat/doctrine audit recorded inside the kickoff packet.
- Physician decision log created: `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-01.md`.
- Post-kickoff physician decisions synchronized across kickoff, status, dashboard, clinical logic, and Claude handoff files.
- Clinical Story Skeleton interview framework created.
- Clinical Story Skeleton v1 locked by Alexander.
- Clinical Story Skeleton v1 reviewed with GO recommendation.
- Clinical Story Skeleton lock recorded in `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md`.
- Clinical Story Skeleton v1 ratified after Claude hostile review minor findings.
- Ratification artifact created: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`.
- Identity Package v1 locked: `worlds/korvin-merrow/world-spec-prep/locked/identity-package-v1.md`.
- Identity Package hostile-review addendum recorded: `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md`.
- Governance Package v1 ratified: `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md`.
- Governance Package clarification recorded: `worlds/korvin-merrow/world-spec-prep/reviews/governance-package-clarification.md`.
- Governance Package ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/governance-package-ratification.md`.
- Physician Architecture Layer completed.
- Key Milestones Calendar Skeleton v1 locked: `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md`.
- Key Milestones Calendar ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md`.
- Baseline Anchor Package v1 locked after physician review: `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md`.
- Baseline Anchor Package ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/baseline-anchor-ratification.md`.
- Clinical Story Timeline Package v1 locked: `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md`.
- Clinical Story Timeline Package ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md`.
- Task Architecture Interview v1 preserved as planning scaffold: `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`.
- Task Architecture Package v1 locked: `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`.
- Task Architecture Package ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md`.
- Medication Expansion Package v1 created for candidate review: `worlds/korvin-merrow/world-spec-prep/locked/medication-expansion-package-v1.md`.
- Medication Expansion Package v1 physician decisions resolved; decision addendum created: `worlds/korvin-merrow/world-spec-prep/reviews/medication-expansion-decision-addendum.md`.
- Medication Expansion Package v1 ratified and locked: `worlds/korvin-merrow/world-spec-prep/ratifications/medication-expansion-ratification.md`.
- Comorbidity Expansion Package v1 created for candidate review and then ratified/locked: `worlds/korvin-merrow/world-spec-prep/locked/comorbidity-expansion-package-v1.md`.
- Comorbidity Expansion Package v1 ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/comorbidity-expansion-ratification.md`.
- Provider Roster Package v1 created for candidate review and then ratified/locked: `worlds/korvin-merrow/world-spec-prep/locked/provider-roster-package-v1.md`.
- Provider Roster Package v1 ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/provider-roster-ratification.md`.
- Surgical History Package v1 created for candidate review and then ratified/locked: `worlds/korvin-merrow/world-spec-prep/locked/surgical-history-package-v1.md`.
- Surgical History Package v1 ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md`.
- Daily Hospital Course Framework v1 ratified and locked: `worlds/korvin-merrow/world-spec-prep/locked/daily-hospital-course-framework-v1.md`.
- Preparation Layer completed: `worlds/korvin-merrow/world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md`.
- World Spec Skeleton v1 locked and ratified: `worlds/korvin-merrow/world-spec-construction/locked/world-spec-skeleton-v1.md`.
- World Spec v1 ratified and locked: `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md`.
- World Spec v1 ratification recorded: `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-v1-ratification.md`.
- World Spec example source documents recorded under `reference/word-spec-examples/` as local-only / gitignored reference material.
- File Inventory Architecture v1 ratified and locked: `worlds/korvin-merrow/file-inventory/locked/file-inventory-architecture-v1.md`.
- File Inventory Architecture ratification recorded: `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-architecture-ratification.md`.
- File Inventory v1 ratified and locked: `worlds/korvin-merrow/file-inventory/locked/file-inventory-v1.md`.
- File Inventory v1 ratification recorded: `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-v1-ratification.md`.
- File Inventory Planning completed.
- Synthetic World-Level File Construction Plan v1 ratified and locked: `worlds/korvin-merrow/synthetic-files/locked/synthetic-world-file-construction-plan-v1.md`.
- Synthetic World-Level File Construction Plan ratification recorded: `worlds/korvin-merrow/synthetic-files/ratifications/synthetic-world-file-construction-plan-v1-ratification.md`.
- Synthetic File Construction Governance completed.
- Batch 1 synthetic world-level files ratified and locked: FI-W01 through FI-W07 under `worlds/korvin-merrow/synthetic-files/locked/batch-1/`.
- Batch 1 ratification recorded: `worlds/korvin-merrow/synthetic-files/ratifications/batch-1-ratification.md`.
- Batch 1 validation review locked: `worlds/korvin-merrow/synthetic-files/locked/batch-1/batch-1-validation-review.md`.
- Batch 2 synthetic world-level files ratified and locked: FI-W08 through FI-W13 under `worlds/korvin-merrow/synthetic-files/locked/batch-2/`.
- Batch 2 ratification recorded: `worlds/korvin-merrow/synthetic-files/ratifications/batch-2-ratification.md`.
- Batch 2 validation review locked: `worlds/korvin-merrow/synthetic-files/locked/batch-2/batch-2-validation-review.md`.
- Collaborator session-exit discipline integrated as a standing process / handoff rule in `AGENTS.md`, `project/STATUS.md`, `docs/status-dashboard.md`, `docs/git-workflow.md`, and Claude handoff surfaces.
- Batch 3 synthetic world-level files ratified and locked: FI-W14 through FI-W16 under `worlds/korvin-merrow/synthetic-files/locked/batch-3/`.
- Batch 3 ratification recorded: `worlds/korvin-merrow/synthetic-files/ratifications/batch-3-ratification.md`.
- Batch 3 validation review locked: `worlds/korvin-merrow/synthetic-files/locked/batch-3/batch-3-validation-review.md`.
- Batch 4 synthetic world-level files locked: FI-W17 through FI-W21 under `worlds/korvin-merrow/synthetic-files/locked/batch-4/`.
- Batch 4 validation review recorded: `worlds/korvin-merrow/synthetic-files/locked/batch-4/batch-4-validation-review.md`.
- Batch 4 ratification recorded: `worlds/korvin-merrow/synthetic-files/ratifications/batch-4-ratification.md`.
- Batch 5 synthetic world-level file FI-W22 ratified and locked at `worlds/korvin-merrow/synthetic-files/locked/batch-5/FI-W22_discharge-facing-plan-snapshot-before-world-close.md`.
- Batch 5 validation review preserved at `worlds/korvin-merrow/synthetic-files/locked/batch-5/batch-5-validation-review.md`.
- Batch 5 ratification recorded at `worlds/korvin-merrow/synthetic-files/ratifications/batch-5-ratification.md`.
- World-Level Synthetic File Layer completed: FI-W01 through FI-W22 locked.
- World-Level Layer Closure Audit passed at `worlds/korvin-merrow/reviews/world-level-layer-closure-audit.md`.
- Task-Level Context File Architecture v1 ratified and locked at `worlds/korvin-merrow/task-layer-architecture/locked/task-level-context-file-architecture-v1.md`.
- Task-Level Context File Architecture v1 ratification recorded at `worlds/korvin-merrow/task-layer-architecture/ratifications/task-level-context-file-architecture-v1-ratification.md`.
- Task-Level Context Files locked: FI-T01 through FI-T07.
- Supplementary Files locked: FI-S01 through FI-S04.
- Task Prompt Architecture v1 locked.
- Task Prompt Construction locked: TP-KM01 through TP-KM06.
- Expected Output Architecture v1 locked.
- Expected Output Construction ratified and locked: EO-KM01 through EO-KM06 plus `worlds/korvin-merrow/expected-outputs/locked/expected-output-construction-validation-review.md`.
- Expected Output Construction ratification recorded at `worlds/korvin-merrow/expected-outputs/ratifications/expected-output-construction-ratification.md`.
- Golden Architecture v1 locked.
- Golden Construction ratified and locked: Golden-KM01 through Golden-KM06 plus `worlds/korvin-merrow/goldens/locked/golden-construction-validation-review.md`.
- Grader Guidance Architecture v1 ratified and locked: `worlds/korvin-merrow/grader-guidance-architecture/locked/grader-guidance-architecture-v1.md`.
- Grader Guidance Architecture validation review locked: `worlds/korvin-merrow/grader-guidance-architecture/locked/grader-guidance-architecture-validation-review.md`.
- Grader Guidance Architecture ratification recorded: `worlds/korvin-merrow/grader-guidance-architecture/ratifications/grader-guidance-architecture-ratification.md`.
- Grader Guidance Construction ratified and locked: GG-KM01 through GG-KM06 under `worlds/korvin-merrow/grader-guidance/locked/`.
- Grader Guidance Construction validation review locked: `worlds/korvin-merrow/grader-guidance/locked/grader-guidance-construction-validation-review.md`.
- Grader Guidance Construction ratification recorded: `worlds/korvin-merrow/grader-guidance/ratifications/grader-guidance-construction-ratification.md`.
- Grader Guidance status: COMPLETE.
- AutoQC Architecture v1 locked artifact: `worlds/korvin-merrow/autoqc-architecture/locked/autoqc-architecture-v1.md`.
- AutoQC Architecture v1 validation review locked artifact: `worlds/korvin-merrow/autoqc-architecture/locked/autoqc-architecture-validation-review.md`.
- AutoQC Architecture v1 ratification recorded: `worlds/korvin-merrow/autoqc-architecture/ratifications/autoqc-architecture-ratification.md`.
- AutoQC Construction locked artifact: `worlds/korvin-merrow/autoqc/locked/autoqc-construction-v1.md`.
- AutoQC Construction validation review locked artifact: `worlds/korvin-merrow/autoqc/locked/autoqc-construction-validation-review.md`.
- AutoQC Construction ratification recorded: `worlds/korvin-merrow/autoqc/ratifications/autoqc-construction-ratification.md`.
- Packaging Architecture v1 locked artifact: `worlds/korvin-merrow/packaging-architecture/locked/packaging-architecture-v1.md`.
- Packaging Architecture validation review locked artifact: `worlds/korvin-merrow/packaging-architecture/locked/packaging-architecture-validation-review.md`.
- Packaging Architecture ratification recorded: `worlds/korvin-merrow/packaging-architecture/ratifications/packaging-architecture-ratification.md`.
- Packaging Construction v1 candidate artifact: `worlds/korvin-merrow/packaging/locked/packaging-construction-v1.md`.
- Packaging Construction validation review candidate artifact: `worlds/korvin-merrow/packaging/locked/packaging-construction-validation-review.md`.

## Latest Git Checkpoints

- `af603ed checkpoint: expand world spec preparation and review workflow`
- `cf2ad14 checkpoint: install and verify document tooling stack`
- `17d6eb1 add instruction guide for new writers`
- `0d9b066 checkpoint: harden repository workflow and documentation`
- `02bb7bd checkpoint: add world spec autoqc prompt`
- `949929a checkpoint: prepare world spec operating packet`
- `b9b8766 checkpoint: submit brainstorm for human review`
- `6e8e0fd checkpoint: record brainstorm autoqc pass`
- `8820ddd checkpoint: rebuild brainstorm using official docx template`
- `96b5a68 checkpoint: address brainstorm autoqc findings`
- `6318735 checkpoint: complete Korvin Merrow identity migration`
- `1ca33f0 checkpoint: apply brainstorm reviewer remediation`
- `6e2ffb9 checkpoint: refresh reviewer remediation continuity files`
- `646f1df checkpoint: record brainstorm remediation resubmission`

## Authorized Right Now

- Task 1 AO review rework support.
- Claude-assisted review/de-hinting of Tasks 2-6 task prompts, goldens, and grader guidelines against final generated files, Task 1 lessons, and the 06/02 instruction guide.
- Local documentation updates that preserve phase boundaries.
- Drive sync planning notes only; do not mutate Drive unless explicitly authorized.
- Local documentation updates that preserve phase boundaries.
- Claude package refresh.
- Applying collaborator session-exit discipline at the end of every working session.

## Not Authorized Right Now

- Revising the locked Clinical Story Skeleton without explicit Alexander approval.
- Revising Identity Package v1 without explicit Alexander approval.
- Treating the Identity Package review addendum as permission to reopen MRN, DOB, age, anthropometrics, allergy, or code status.
- Changing Governance Package v1 without Alexander approval.
- Additional RL Studio access, task-material uploads, agent runs, QA runs, edits to submitted Failure Analysis / Grader Analysis, PL text creation/submission beyond the current authorized PL stage, or platform mutation before explicit authorization for the exact action.
- Rerunning Final Files AutoQC, uploading revisions, or using Apply to Task unless explicitly authorized for a corrective platform action.
- Applying edits labeled PROTECT.
- Editing generated DOCX files or locked task-layer artifacts before Alexander authorizes the exact change.
- Uploading task setup materials before explicit authorization.
- Creating AutoQC responses before explicit authorization.
- Creating additional supplementary files, chart notes, or downstream task outputs before explicit authorization.
- Creating milestones before Alexander authorizes that step.
- Creating medication schedules, medication reconciliation outputs, hospital medication changes, admission medication lists, or discharge medication lists before Alexander authorizes those steps.
- Creating additional synthetic patient files beyond locked Batch 1 before explicit authorization.
- Revising locked task prompts without explicit authorization.
- Reopening or modifying locked expected outputs without explicit authorization.
- Creating additional golden responses or revising candidate goldens without explicit authorization.
- Locking grader guidance before authorized review/ratification.
- Creating scoring rubrics.
- Creating scoring thresholds.
- Creating pass/fail bands.
- Creating point allocations.
- Creating failure analysis.
- Redesigning the world, reopening Governance Package v1, or changing source-of-truth hierarchy because of the Medicine Team Lead task-design guidance.
- Changing Brainstorm clinical content beyond the approved reviewer remediation.
- Modifying Brainstorm unless new reviewer feedback arrives.
- Further identity changes or task concept changes beyond the reviewer-required Korvin Merrow remediation without Alexander approval.
- Accessing RL Studio or browser operations without explicit authorization.

## Collaborator Session Exit Discipline

Standing process / handoff rule:

1. Working tree must be clean, or uncommitted state must be explicitly documented.
2. Current phase and next eligible phase must be updated.
3. Locked artifacts must remain unchanged unless Alexander explicitly authorized reopening or editing them.
4. Candidate artifacts must be clearly located and status-labeled.
5. Newly locked artifacts must move to locked paths, with ratifications created and referenced.
6. Continuity surfaces and Claude handoff files must be updated.
7. Stale active candidate paths must be removed or explicitly marked historical.
8. Unauthorized files must not be created.
9. Carry-forward watch items and future task-layer guidance must be preserved.
10. A checkpoint commit must be created for completed work unless Alexander explicitly instructs not to commit.
11. Final reports must state what changed, what did not change, current status, next eligible phase, and whether the repository is safe for another collaborator to continue.

## Claude Operating Mode

Claude remains the official Sanctum drafting assistant, but drafting is gated.

Claude may help:

- compress context;
- critique plans against AutoQC v6.3;
- identify reviewer risks;
- prepare Governance Package interview questions;
- organize physician decisions after Alexander provides them.

Claude must not replace physician judgment or originate clinical design.

## Current Prep Artifacts To Use

- `claude-package/01_SANCTUM_CORE_RULES.md`
- `claude-package/02_BRAINSTORM_GUIDE.md`
- `claude-package/03_WORLD_SPEC_GUIDE.md`
- `claude-package/04_KORVIN_MERROW_CONTEXT.md`
- `claude-package/05_EXECUTION_STATE.md`
- `claude-package/06_HANDOFF_STATE.md`
- `worlds/korvin-merrow/active/brainstorm.md`
- `worlds/korvin-merrow/active/task-map.md`
- `worlds/korvin-merrow/world-spec-prep/reviews/claude-review-triage.md`
- `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/post-go-interview-plan.md`
- `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md`
- `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-01.md`
- `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md`
- `worlds/korvin-merrow/world-spec-prep/reviews/clinical-story-skeleton-review.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/locked/identity-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md`
- `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/reviews/governance-package-clarification.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/governance-package-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`
- `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/locked/medication-expansion-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/locked/comorbidity-expansion-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/comorbidity-expansion-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/locked/provider-roster-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/provider-roster-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/locked/surgical-history-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/locked/daily-hospital-course-framework-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md`
- `worlds/korvin-merrow/world-spec-construction/locked/world-spec-skeleton-v1.md`
- `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-skeleton-ratification.md`
- `worlds/korvin-merrow/grader-guidance-architecture/locked/grader-guidance-architecture-v1.md`
- `worlds/korvin-merrow/grader-guidance-architecture/locked/grader-guidance-architecture-validation-review.md`
- `worlds/korvin-merrow/grader-guidance-architecture/ratifications/grader-guidance-architecture-ratification.md`
- `reference/world-spec-guidelines/08_autoqc_master_index.md`
- `reference/world-spec-guidelines/09_world_spec_writer_playbook.md`
- `project/WORKSPACE_FILE_MAP.md`


---
PRE-SANG SNAPSHOT 6/8 (superseded by post-Sang reruns and platform FA/GA entry below): KM02 COMPLETE / RFD (Ready for Delivery) after Janette's 6/8 final review. Both prior human reviews passed (Abi 6/7), all recorded KM02 checks are green, and Preference Labels were submitted with verdict B / B++. Golden sha 2dd3e0ad. KM03 v2.1 platform set is retained as evidence after difficulty failure; job `58b5f3e3` is recorded as the difficulty-failed trajectory run. Active KM03 v2.2 platform set is present in `platform/task3/current/` and passed Task AutoQC 36/36 (`qcaud_fc`): `prompt-task3-v2.2.txt`, `discharge_planning_summary_draft_05242026.docx`, `golden-KM03-v2.2.docx`, and `grader-guidelines-task3-v2.2.txt`. Taiga job `877aa204` cleared the difficulty gate (mean 69.0, four sub-70, six sub-90); grading transcripts are verified clean; local FA/GA drafting packet exists; verified local FA/GA current draft exists at `task3/fa-ga/FA-GA-current.md`; FA/GA subject is Attempt 9 (0.20). Retired v1 passed Task AutoQC 36/36 (`qcaud_6b`) after core metadata scrub; later job `58b5f3e3` confirmed v1 was too easy and is historical only. KM04 v1 failed the 6/8 trajectory difficulty gate (`55ee209f`, mean 0.912, zero sub-70); v1 evidence is archived under `platform/task4/archive/2026-06-08-pre-clean/`. KM04 v2 cleared the difficulty gate after job `709be0e8` (mean 0.689, three sub-70, tail 0.15); current records are `task4/runs/KM04-v2-taiga-results-709be0e8.md`, `task4/runs/KM04-v2-grading-transcripts-709be0e8.md`, and `task4/fa-ga/FA-GA-current.md`. Post-Sang KM04 FA/GA entry uses Attempt 9 (0.30), FA/GA AutoQC passed, KM04 PL #1-#2 drafts exist locally; no KM04 PL has been submitted and no final review exists yet. KM05 is review-only reset under `task-setup/task5/`; active plan is `task5/design/KM05-v2-design-plan-6-8.md` with paired review request `task5/build-phase-drafts/KM05-v2-review-request-for-claude-ai.md`; it is not built or platform-staged.


---
6/7 late plus 6/8 archive correction: KM03 v2.1 WAS ACTIVE AFTER ALEXANDER UPLOAD, then difficulty-failed and was archived at platform/task3/archive/v2.1-difficulty-failed-after-58b5f3e3/ (prompt-task3-v2.txt, care_coordination_handoff_draft_05242026.docx, golden-KM03-v2.docx, grader-guidelines-task3-v2.txt, RUN-INSTRUCTIONS.md). v1 remains preserved at platform/task3/archive/v1-retired-after-task-writing-reset/ (uploaded, AutoQC qcaud_6b pass, later job 58b5f3e3 returned too easy, retired after task-writing reset; historical only). Mechanism history: authoring posture over a de-authorized unsigned care-coordination handoff DRAFT; fair failure = promoting the draft unverified completion into a signed physician addendum. Build authority history = KM03-v2.1-LOCKED-build-plan.md. CURRENT: active KM03 v2.2 set is platform/task3/current/ (prompt-task3-v2.2.txt, discharge_planning_summary_draft_05242026.docx, golden-KM03-v2.2.docx, grader-guidelines-task3-v2.2.txt, RUN-INSTRUCTIONS.md). Task AutoQC passed 36/36 (`qcaud_fc`); Taiga job `877aa204` cleared the initial difficulty gate; local FA/GA current draft existed at that stage; later post-Sang rerun/platform FA/GA entry is recorded below. No platform-submitted KM03 PL or final review exists.

---
6/8 late Sang grader/golden review fix: KM03 and KM04 moved to Taiga trajectory rerun after grader/golden revisions. The prior KM03 `877aa204` and KM04 `709be0e8` runs remain evidence only, and their FA/GA drafts are historical. New required grader structure/length lesson: `docs/grader-guidelines-lessons.md`. This gate is now superseded by the post-fix reruns and platform FA/GA entry below; do not use old-run FA/GA, submit PLs, run PL AutoQC, or start final review from the pre-fix runs.

6/8 late KM03 post-fix rerun update: KM03 rerun job `8e97cdd7` is complete after the Sang grader/golden fix. Spread: 80, 62, 90, 30, 90, 88, 82, 87, 85, 70; mean 76.4; single lowest Attempt 4 / run `c2eea662` at 0.30. `worlds/korvin-merrow/task-setup/task3/fa-ga/FA-GA-current.md` now supersedes the pre-fix `877aa204` Attempt 9 draft. Alexander later completed platform FA/GA entry on Attempt 4; FA/GA AutoQC passed.

6/8 late KM04 post-fix rerun update: KM04 rerun job `979dccde` is complete after the Sang grader/golden fix. Spread: 95, 90, 30, 88, 78, 88, 90, 35, 30, 40; mean 66.4; lowest score 0.30 shared by Attempts 3 and 9; Attempt 9 / run `976b2b18` selected for FA/GA, with Attempt 1 / run `06d0b710` at 0.95 as catch anchor. `worlds/korvin-merrow/task-setup/task4/fa-ga/FA-GA-current.md` now supersedes the pre-fix `709be0e8` Attempt 5 draft. Alexander later completed platform FA/GA entry on Attempt 9; FA/GA AutoQC passed.

6/8 late KM03/KM04 FA-GA platform entry: Alexander entered both FA/GA records on platform. KM03 uses Attempt 4 (0.30), FA 787 chars, GA 749 chars. KM04 uses Attempt 9 (0.30), FA 902 chars, GA 807 chars. FA/GA AutoQC passed for both. PL is now active: KM03 PL #1-#3 are drafted locally under `worlds/korvin-merrow/task-setup/task3/preference-labeling/`; KM03 needs their platform submission, and KM04 PL #1-#2 are drafted locally while KM04 still needs one more PL draft/submission. Run PL AutoQC after each, then final review. PL is now active; do not proceed to final review without Alexander authorization.
