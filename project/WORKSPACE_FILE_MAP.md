# Workspace File Map

Purpose: local repository hygiene map to prevent duplicate working files and accidental edits. This is not the Sanctum World File Plan and must not be treated as a Section 3 file inventory.

Generated from local workspace file listing excluding `.git`, caches, and Python bytecode.

Current status: File Inventory Architecture / File Inventory Architecture v1 locked. Task Architecture Interview v1 is preserved as historical planning scaffold; Task Architecture Package v1 is authoritative. Medication Expansion Package v1, Comorbidity Expansion Package v1, Provider Roster Package v1, Surgical History Package v1, Daily Hospital Course Framework v1, World Spec Skeleton v1, World Spec v1, and File Inventory Architecture v1 are locked. File Inventory Architecture v1 is locked at `worlds/korvin-merrow/file-inventory/locked/file-inventory-architecture-v1.md`, with ratification recorded at `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-architecture-ratification.md`. Phase 3 File Inventory Architecture is complete. Final Section 3 file rows, filenames, file IDs, tasks, prompts, expected outputs, goldens, grader guidance, notes, labs, vitals, synthetic files, DOCX submission packaging, AutoQC, and RL Studio upload have not started.

## Navigation Rule

For a new collaborator or new AI session, read in this order:

1. `project/STATUS.md` for live state and phase gate.
2. `project/WORKSPACE_FILE_MAP.md` for file locations and duplication risks.
3. `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md` for the active World Spec cockpit.
4. `worlds/korvin-merrow/world-spec-prep/locked/identity-package-v1.md` for locked identity values.
5. `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md` for identity implementation notes that do not reopen Identity Package v1.
6. `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md` for ratified governance architecture.
7. `worlds/korvin-merrow/world-spec-prep/reviews/governance-package-clarification.md` for accepted governance clarifications.
8. `worlds/korvin-merrow/world-spec-prep/ratifications/governance-package-ratification.md` for governance ratification and completed architecture layer status.
9. `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md` for the locked canonical date framework.
10. `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md` for calendar ratification and +7/+30 doctrine.
11. `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md` for locked baseline anchors.
12. `worlds/korvin-merrow/world-spec-prep/ratifications/baseline-anchor-ratification.md` for baseline physician sign-off and BP carry-forward note.
13. `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md` for the locked story-evolution framework.
14. `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md` for timeline ratification and Trap #3 vs Trap #5 carry-forward note.
15. `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md` for the locked task-architecture package.
16. `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md` for task architecture ratification and carry-forward watch items.
17. `worlds/korvin-merrow/active/task-map.md` for reconciled current vs historical workflow mapping.
18. `worlds/korvin-merrow/world-spec-prep/locked/medication-expansion-package-v1.md` for the locked medication architecture.
19. `worlds/korvin-merrow/world-spec-prep/ratifications/medication-expansion-ratification.md` for medication architecture ratification.
20. `worlds/korvin-merrow/world-spec-prep/reviews/medication-expansion-decision-addendum.md` for accepted physician decision resolution.
21. `worlds/korvin-merrow/world-spec-prep/locked/comorbidity-expansion-package-v1.md` for the locked comorbidity architecture.
22. `worlds/korvin-merrow/world-spec-prep/ratifications/comorbidity-expansion-ratification.md` for comorbidity ratification and carry-forward watch items.
23. `worlds/korvin-merrow/world-spec-prep/locked/provider-roster-package-v1.md` for the locked provider/care-team roster architecture.
24. `worlds/korvin-merrow/world-spec-prep/ratifications/provider-roster-ratification.md` for provider roster ratification and naming guardrails.
25. `worlds/korvin-merrow/world-spec-prep/locked/surgical-history-package-v1.md` for the locked surgical/procedural history architecture.
26. `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md` for surgical-history ratification and noise-control guardrails.
27. `worlds/korvin-merrow/world-spec-prep/locked/daily-hospital-course-framework-v1.md` for the locked HD1-HD6 daily evolution framework.
28. `worlds/korvin-merrow/world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md` for preparation-layer completion.
29. `worlds/korvin-merrow/world-spec-construction/locked/world-spec-skeleton-v1.md` for the locked World Spec Skeleton.
30. `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-skeleton-ratification.md` for World Spec Skeleton ratification.
31. `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md` for the locked World Spec.
32. `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-v1-ratification.md` for World Spec v1 ratification and watch items.
33. `worlds/korvin-merrow/file-inventory/locked/file-inventory-architecture-v1.md` for the locked file inventory architecture.
34. `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-architecture-ratification.md` for the lock record and downstream watch items.
35. `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md` for historical interview basis.
36. `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md` for ratified Clinical Story Skeleton decisions and construction-lock status.
37. `reference/world-spec-guidelines/08_autoqc_master_index.md` only when exact AutoQC checks are needed.

Do not start by opening every prep file. Most prep files are supporting memory, not active instructions.

## Hygiene Audit 2026-05-31

Status: restructured into junction folders, purpose folders, and World Spec prep lifecycle folders.

Findings:

- Root is clean by repo-standard exception: `.gitignore`, `AGENTS.md`, and `README.md`.
- README placement is acceptable: root README plus folder-policy READMEs in `reference/source/` and `tools/`.
- `tmp/` contains generated render artifacts and is ignored by git.
- `reference/` is now a junction folder with source files moved into `reference/source/`.
- `worlds/korvin-merrow/` is now a junction folder with one README and purpose subfolders.
- `worlds/korvin-merrow/file-inventory/` is now a lifecycle folder for file inventory architecture and later file-plan work; File Inventory Architecture v1 is locked and ratified.
- World Spec prep artifacts are clustered by lifecycle stage so candidate, locked, ratified, review, decision-log, and planning-scaffold files do not sit in one flat folder.
- `candidate-review/` is reserved for active candidate artifacts only. Task Architecture Interview v1 moved to `planning-scaffolds/` after Task Architecture Package v1 lock. World Spec prep `candidate-review/` is empty after Daily Hospital Course Framework v1 lock; file-inventory `candidate-review/` is empty after File Inventory Architecture v1 lock.
- Several files intentionally overlap by lifecycle stage, especially Brainstorm history/reviews and World Spec prep/checklist material.
- Do not add new audit or navigation docs unless an existing map/status file cannot carry the information.

Junction folder rule:

- Any folder with subfolders should contain no more than one ordinary markdown/document file, ideally a README or cockpit file.
- Root is the exception for `.gitignore` and `AGENTS.md`.
- Do not place mixed-purpose files directly in a junction folder.

Recommended future cleanup if Alexander approves:

- Consolidate thin planning scaffolds in `world-spec-prep/` after Identity and Governance packages are complete.
- Reassess whether `claude-package/` can be regenerated from fewer local source files after World Spec submission.

## Consolidation Decisions

Reviewed for duplicate-purpose files:

- `project/STATUS.md` and `docs/status-dashboard.md`: keep both. `STATUS.md` is operational source of truth; dashboard is human-readable summary.
- `project/WORKSPACE_FILE_MAP.md` and root `README.md`: keep both. README orients; file map governs placement and duplication.
- `worlds/korvin-merrow/active/clinical-logic.md`, `world-spec-prep/decision-logs/physician-decision-log-02.md`, and `world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`: keep all. Clinical logic is evolving reasoning; decision log is durable physician record; ratification is review resolution.
- `reference/world-spec-guidelines/04_world_spec_autoqc_requirements.md`, `08_autoqc_master_index.md`, and `09_world_spec_writer_playbook.md`: keep all. `08` is exact check index; `09` is authoring workflow; `04` is older summary reference.
- `claude-package/*`: keep as a separate compressed handoff package because Claude Project context has different constraints than local Codex continuity.
- `worlds/korvin-merrow/active/frictions.md` and `world-spec-prep/planning-scaffolds/friction-to-task-map.md`: keep for now. The active file is a placeholder; the prep map is planning substrate.
- `worlds/korvin-merrow/active/traps.md` and `world-spec-prep/planning-scaffolds/trap-to-file-map.md`: keep for now. The active file is a placeholder; the prep map is planning substrate.
- Historical Brainstorm artifacts in `history/` and review artifacts in `reviews/`: keep separate to preserve audit trail.

## Root

| File | Role | Duplication note |
| --- | --- | --- |
| `.gitignore` | Git hygiene and local-secret protection. | Single root ignore file. |
| `AGENTS.md` | Codex operating instructions. | Root behavior source; includes current Korvin Merrow active project and locked Clinical Story Skeleton state. |
| `README.md` | Repository overview and usage guide. | Root orientation only. |

## Project Tracking

| File | Role | Duplication note |
| --- | --- | --- |
| `project/STATUS.md` | Current phase, branch, blocker, next action. | Read first before acting; authoritative current state. |
| `project/DECISIONS.md` | Project decision log. | Use for durable decisions, not transient notes. |
| `project/EXECUTION_CHECKLIST.md` | Official onboarding checklist. | Process checklist; not pass methodology. |
| `project/IDENTITY_MIGRATION_LOG.md` | Current identity migration record from prior working name to Korvin Merrow. | Includes branch rename status, historical-file exceptions, and verification results. |
| `project/PASS_PLAN.md` | Local pass-based operating system. | Controls pass transitions. |
| `project/PHASE_MAP.md` | Phase boundaries and definitions. | Boundary reference; do not duplicate in every prep file. |
| `project/WORKSPACE_FILE_MAP.md` | Current repo file map. | This file; update when structure changes materially. |
| `project/CLAUDE_COMPLIANCE_MAP.md` | Expected Claude workflow vs actual assistant workflow compliance map. | Use before World Spec drafting to close Claude/transcript gaps. |

## Documentation

| File | Role | Duplication note |
| --- | --- | --- |
| `docs/CONTRIBUTING.md` | Contribution and review rules. | Complements `README.md`; not a project status file. |
| `docs/agent-workflow.md` | Codex/Claude/ChatGPT/Alexander roles. | Role policy; AGENTS remains runtime instruction source. |
| `docs/git-workflow.md` | Branching, tags, rollback, checkpoint examples. | Git policy only. |
| `docs/mcp-audit.md` | MCP and connector audit. | Do not store MCP tokens/config here. |
| `docs/reviewer-response-protocol.md` | GO/SEND BACK response workflow. | Use for reviewer feedback handling. |
| `docs/security-and-privacy.md` | Privacy and confidentiality guidance. | Security policy only. |
| `docs/status-dashboard.md` | Human-readable status summary. | Mirrors key `STATUS.md` items for dashboard use. |
| `docs/tooling-audit.md` | Tool availability audit before install. | Historical audit. |
| `docs/tooling-verification.md` | Installed tool verification. | Current tooling proof. |

## Tools

| File | Role | Duplication note |
| --- | --- | --- |
| `tools/README.md` | Explains tools live outside repo. | No binaries should be stored in `tools/`. |

## Claude Package

| File | Role | Duplication note |
| --- | --- | --- |
| `claude-package/01_SANCTUM_CORE_RULES.md` | Compressed Claude knowledge: core rules. | Claude upload package only. |
| `claude-package/02_BRAINSTORM_GUIDE.md` | Compressed Brainstorm guide. | Derived from source; not source of truth. |
| `claude-package/03_WORLD_SPEC_GUIDE.md` | Compressed World Spec guide. | Derived from source; not source of truth. |
| `claude-package/04_KORVIN_MERROW_CONTEXT.md` | Refreshed Korvin Merrow context for Claude. | Includes approved Brainstorm summary, ratified Clinical Story Skeleton, and World Spec prep risks. |
| `claude-package/05_EXECUTION_STATE.md` | Refreshed execution state for Claude. | Mirrors current Clinical Story Skeleton ratification / Identity Package readiness state; use `project/STATUS.md` for live status. |
| `claude-package/06_HANDOFF_STATE.md` | Fresh-session Claude handoff. | Summarizes locked decisions, ratified skeleton, remaining decisions, next legal action, and hard boundaries. |

## Reference Source

| File | Role | Duplication note |
| --- | --- | --- |
| `reference/source/New Writers Version - Instruction Guide (05_24).docx` | Official instruction guide source DOCX. | Preserve unchanged. |
| `reference/source/New Writers Version - Instruction Guide (05_24).md` | Markdown extraction of official guide. | Operational reading copy; DOCX remains source artifact. |
| `reference/source/_Task Selection Categories For Team.xlsx` | Official task tracker. | Preserve unchanged. |
| `reference/source/README.md` | Source material policy. | No proprietary source edits here. |

## World Spec Example Source Documents

These are fetched source/reference examples, not authored Korvin Merrow content and not the Korvin Merrow World File Plan.

| File | Role | Duplication note |
| --- | --- | --- |
| `reference/word-spec-examples/Brainstorming_Document_Chen.docx` | Source/reference example Brainstorm document. | Preserve separately from authored work. |
| `reference/word-spec-examples/World_Spec_Document_Harold.docx` | Source/reference example World Spec document. | Preserve separately from authored work. |
| `reference/word-spec-examples/World_Spec_Document_Marcus.docx` | Source/reference example World Spec document. | Preserve separately from authored work. |
| `reference/word-spec-examples/World_Spec_Document_Opus.docx` | Source/reference example World Spec document. | Preserve separately from authored work. |

## Reference Checklists And Workflows

| File | Role | Duplication note |
| --- | --- | --- |
| `reference/checklists/brainstorm-checklist.md` | Brainstorm checklist. | Derived operational guidance. |
| `reference/checklists/reviewer-failure-patterns.md` | Reviewer failure patterns. | General onboarding risks. |
| `reference/checklists/world-spec-checklist.md` | World Spec checklist. | Older/summary checklist; use v6.3 index for exact checks. |
| `reference/workflows/onboarding-pipeline.md` | Onboarding workflow summary. | Process reference. |

## Reference Templates

| File | Role | Duplication note |
| --- | --- | --- |
| `reference/templates/brainstorm.docx` | Official Brainstorm DOCX template. | Preserve as base template. |
| `reference/templates/brainstorm.md` | Markdown template/helper version. | Secondary working reference. |
| `reference/templates/World_Spec_Template_05_06.docx` | Official World Spec template. | Preserve unchanged; use as base only after GO. |
| `reference/templates/AutoQC_Section_2_World_Spec_v6.3_writer.docx` | Official World Spec AutoQC prompt/checks. | Preserve unchanged; v6.3 source for 113 checks. |
| `reference/templates/template-links.md` | Official template links. | Link registry. |

## World Spec Guidelines

| File | Role | Duplication note |
| --- | --- | --- |
| `reference/world-spec-guidelines/01_world_spec_required_structure.md` | Structure extraction. | Prep reference. |
| `reference/world-spec-guidelines/02_world_spec_rubric_checklist.md` | Rubric/checklist extraction. | Prep reference. |
| `reference/world-spec-guidelines/03_world_spec_common_mistakes.md` | Common mistakes. | Prep reference. |
| `reference/world-spec-guidelines/04_world_spec_autoqc_requirements.md` | AutoQC requirement summary. | Summary only; exact checks in `08`. |
| `reference/world-spec-guidelines/05_world_spec_claude_usage_rules.md` | Claude usage boundaries. | Prep reference. |
| `reference/world-spec-guidelines/06_world_spec_template_map.md` | Official template map and links. | Template locator. |
| `reference/world-spec-guidelines/07_reviewer_failure_patterns.md` | GO/SEND BACK and reviewer risks. | Reviewer prep reference. |
| `reference/world-spec-guidelines/08_autoqc_master_index.md` | Exact 113-check AutoQC index. | Primary local AutoQC index. |
| `reference/world-spec-guidelines/09_world_spec_writer_playbook.md` | Section-by-section authoring workflow. | Practical workflow, not source artifact. |
| `reference/world-spec-guidelines/10_submission_package_requirements.md` | Source-cited World Spec submission package requirements. | Submission packaging reference; includes explicit not-found findings. |
| `reference/world-spec-guidelines/11_transcript_requirements.md` | Source-cited transcript requirement search results. | Records that detailed Claude transcript requirements were not found in local text source. |
| `reference/world-spec-guidelines/12_required_upload_inventory.md` | Source-cited upload inventory manifest. | Not a Korvin Merrow file inventory; use only for package preparation. |
| `reference/world-spec-guidelines/13_claude_workflow_audit.md` | Source-cited Claude workflow and transcript audit. | Use with `project/CLAUDE_COMPLIANCE_MAP.md` before World Spec drafting. |

## Korvin Merrow Junction

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/README.md` | World folder index. | Single junction file; points to active/history/planning/remediation/reviews/submission/prep/construction/file-inventory folders. |

## Korvin Merrow Active Files

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/active/brainstorm.md` | Active Brainstorm remediation source. | Modify only for reviewer-required changes approved by Alexander. |
| `worlds/korvin-merrow/active/clinical-logic.md` | Clinical reasoning notes. | Prep/support only. |
| `worlds/korvin-merrow/active/frictions.md` | Placeholder for later friction notes. | Do not use as active source until governance/Decision Friction work is authorized. |
| `worlds/korvin-merrow/active/traps.md` | Placeholder for later trap notes. | Do not use as active source until trap substrate planning is authorized. |
| `worlds/korvin-merrow/active/task-map.md` | Reconciled task mapping. | States that original Brainstorm-level mapping is historical and that Task Architecture Package v1 is authoritative for World Spec construction. |
| `worlds/korvin-merrow/active/world-spec.md` | Explicit World Spec placeholder. | Do not draft/populate until Alexander authorizes World Spec drafting. |

## Korvin Merrow History

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/history/brainstorm-development-history.md` | Internal Brainstorm history. | Historical only. |
| `worlds/korvin-merrow/history/brainstorm-internal-audit.md` | Internal Brainstorm audit. | Historical QC. |
| `worlds/korvin-merrow/history/rename-audit.md` | Audit of reviewer-required synthetic identity rename. | Confirms active files use Korvin Merrow and prior name remains only in historical archives. |
| `worlds/korvin-merrow/history/claude-brainstorm-review-package.md` | Claude Brainstorm review package. | Historical support artifact. |

## Korvin Merrow Remediation

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/reviews/reviewer-feedback.md` | Review notes and moved internal questions. | Use for reviewer feedback history. |
| `worlds/korvin-merrow/remediation/reviewer-comorbidity-decision-brief.md` | Physician decision brief for SEND BACK comorbidity expansion. | Prep only; do not treat proposed additions as locked until approved. |
| `worlds/korvin-merrow/remediation/reviewer-medication-decision-brief.md` | Physician decision brief for SEND BACK medication specificity. | Prep only; do not treat proposed medication list as locked until approved. |
| `worlds/korvin-merrow/remediation/reviewer-remediation-compliance-review.md` | Compliance validation for reviewer-requested comorbidity and medication remediation. | Supports SEND BACK revisions; not a World Spec source. |

## Korvin Merrow Planning

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/planning/KORVIN_MERROW_PASS_PLAN.md` | World-specific pass plan. | Planning only. |

## Korvin Merrow Reviews

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/reviews/brainstorm-autoqc-01.md` | First Brainstorm AutoQC output. | Historical failed/partial QC artifact using prior working name. |
| `worlds/korvin-merrow/reviews/brainstorm-autoqc-02.md` | Final Brainstorm AutoQC pass summary. | Current Brainstorm AutoQC status. |
| `worlds/korvin-merrow/reviews/claude-brainstorm-review-01.md` | Claude hostile Brainstorm review. | Historical external review artifact using prior working name. |
| `worlds/korvin-merrow/reviews/claude-brainstorm-review-response-01.md` | Response to Claude Brainstorm review. | Historical triage/action record. |
| `worlds/korvin-merrow/reviews/reviewer-go-01.md` | Stacey S Brainstorm GO approval record. | Current human approval artifact authorizing transition toward World Spec, gated by Alexander authorization. |

## Korvin Merrow Submission

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx` | Approved Brainstorm DOCX remediation artifact. | Reuploaded, AutoQC passed, and approved by reviewer. Preserve as approved Brainstorm source artifact. |

## Korvin Merrow World Spec Prep

Lifecycle clustering:

- `WORLD_SPEC_KICKOFF.md`: the only root cockpit file in `world-spec-prep/`.
- `candidate-review/`: artifacts awaiting physician decision or lock. Currently empty after Daily Hospital Course Framework v1 lock.
- `locked/`: locked architecture packages and canonical frameworks.
- `ratifications/`: formal ratification records.
- `reviews/`: review findings, hostile reviews, clarifications, and addenda.
- `decision-logs/`: durable physician/project decision records.
- `planning-scaffolds/`: temporary scaffolds and maps that are not final deliverables.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/autoqc-preflight-checklist.md` | Local preflight checklist. | Summary; exact check source is `08_autoqc_master_index.md`. |
| `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/clinical-story-skeleton-interview.md` | Clinical Story Skeleton physician interview framework. | Historical interview scaffold; skeleton now locked in decision log 02. |
| `worlds/korvin-merrow/world-spec-prep/reviews/clinical-story-skeleton-review.md` | Review of locked Clinical Story Skeleton v1. | Recommends GO to Identity Package; not a World Spec draft. |
| `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-skeleton-ratification.md` | Ratification of Clinical Story Skeleton v1 after Claude hostile review minor findings. | Governance/story-logic guardrails only; not a narrative rewrite or World Spec draft. |
| `worlds/korvin-merrow/world-spec-prep/reviews/claude-review-triage.md` | Historical pre-GO triage of Claude World Spec prep review. | Some wait-for-GO language is superseded; use status/kickoff for live state. |
| `worlds/korvin-merrow/world-spec-prep/decision-logs/decision-register.md` | Prep decision register. | Use for pending/locked decisions after GO. |
| `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/file-plan-planning.md` | File plan planning scaffold. | Not a final file inventory. |
| `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/friction-to-task-map.md` | Friction/task planning map. | Planning only. |
| `worlds/korvin-merrow/world-spec-prep/reviews/governance-package-clarification.md` | Accepted governance clarifications from Claude hostile review. | Clarification layer only; no redesign, task architecture, or World Spec drafting. |
| `worlds/korvin-merrow/world-spec-prep/ratifications/governance-package-ratification.md` | Governance ratification record and completed architecture layer status. | Does not authorize drafting, task architecture, milestones, file inventory, prompts, or synthetic files. |
| `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md` | Ratified governance architecture: care team, authority hierarchy, source-of-truth hierarchy, condition split, friction table, admin deliverable decision, and workflow umbrella. | Not a World Spec draft, task spec, milestone list, or file inventory. |
| `worlds/korvin-merrow/world-spec-prep/locked/identity-package-v1.md` | Locked identity and demographic/compliance package. | Use as identity source of truth; not a World Spec draft. |
| `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md` | Claude hostile-review observations recorded as carry-forward implementation notes. | Does not reopen Identity Package v1; use only for later Patient Profile / Clinical History implementation. |
| `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md` | Calendar ratification record and +7/+30-from-discharge doctrine. | Does not create clinical milestone content, tasks, or files. |
| `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md` | Locked canonical date framework for admission, HD1-HD6, world snapshot, discharge anchor, +7 anchor, and +30 anchor. | Timeline framework only; not a World Spec draft, final milestone table, task architecture, or file inventory. |
| `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md` | Locked baseline comparator values and baseline function anchors. | Not admission labs, hospital-course trends, file inventory, task architecture, or World Spec prose. |
| `worlds/korvin-merrow/world-spec-prep/ratifications/baseline-anchor-ratification.md` | Baseline Anchor Package v1 ratification record and physician sign-off. | Records optional non-numeric baseline BP carry-forward note; does not create BP value. |
| `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md` | Locked story-evolution framework from pre-admission through +30 anchor. | Does not create labs, vitals, medication schedules, notes, files, task architecture, or World Spec prose. |
| `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md` | Ratification record for Clinical Story Timeline Package v1. | Records carry-forward distinction between Trap #3 buried evidence and Trap #5 reassuring but incomplete discharge/source-hierarchy artifact. |
| `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md` | Historical interview-only scaffold for task architecture decisions. | Task Architecture Package v1 is now authoritative; this scaffold does not create final tasks, prompts, expected outputs, file inventory, World Spec sections, reference templates, or synthetic files. |
| `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md` | Locked formal task architecture package defining six task concepts across four workflows. | Does not create prompts, expected outputs, goldens, grader guidance, file inventory, World Spec sections, templates, reference files, or synthetic files. |
| `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md` | Ratification record for Task Architecture Package v1. | Records AutoQC 2.108 contingency, Discharge Planning Documentation differentiation requirements, and superseded TCM/risk standalone workflow mappings. |
| `worlds/korvin-merrow/world-spec-prep/locked/medication-expansion-package-v1.md` | Locked baseline medication architecture targeting 18-22 medications. | Ratified and locked; baseline count is 20 after removing insulin lispro from baseline and reserving it as future inpatient-only candidate logic. Does not create doses, schedules, med-rec outputs, hospital medication changes, file inventory, tasks, World Spec prose, templates, reference files, or synthetic documents. |
| `worlds/korvin-merrow/world-spec-prep/ratifications/medication-expansion-ratification.md` | Ratification record for Medication Expansion Package v1. | Records LOCK READY/GO verdicts, accepted physician decisions, and carry-forward watch items. |
| `worlds/korvin-merrow/world-spec-prep/reviews/medication-expansion-decision-addendum.md` | Accepted physician decision resolution for Medication Expansion Package v1. | Records insulin lispro removal from baseline architecture and future inpatient-only reservation; not a medication schedule, med-rec output, task, or World Spec draft. |
| `worlds/korvin-merrow/world-spec-prep/locked/comorbidity-expansion-package-v1.md` | Locked baseline comorbidity architecture targeting 12-15 conditions. | Ratified and locked; baseline count is 14. Does not create labs, vitals, hospital-course events, provider names, surgical history, task prompts, file inventory, World Spec prose, templates, reference files, or synthetic documents. |
| `worlds/korvin-merrow/world-spec-prep/ratifications/comorbidity-expansion-ratification.md` | Ratification record for Comorbidity Expansion Package v1. | Records GO verdicts, accepted physician decisions, retained secondary additions, medication-count clarification, and carry-forward watch items. |
| `worlds/korvin-merrow/world-spec-prep/locked/provider-roster-package-v1.md` | Locked provider/care-team and stakeholder architecture. | Ratified and locked; does not create provider-authored notes, file inventory, task prompts, expected outputs, goldens, grader guidance, medication schedules, hospital-course events, labs, vitals, World Spec prose, templates, reference files, or synthetic documents. |
| `worlds/korvin-merrow/world-spec-prep/ratifications/provider-roster-ratification.md` | Ratification record for Provider Roster Package v1. | Records review GO verdicts, shared Merrow surname approval, no-extra-naming guardrail, hierarchy compatibility, and carry-forward watch items. |
| `worlds/korvin-merrow/world-spec-prep/locked/surgical-history-package-v1.md` | Locked surgical/procedural history architecture. | Ratified and locked; confirms remote PCI with coronary stent placement and remote diagnostic sleep study confirming OSA, while excluding ICD/CRT/pacemaker, CABG, dialysis access, major orthopedic repair/joint replacement, limb amputation/major diabetic foot surgery, temporal artery biopsy/rheumatologic procedure, and screening colonoscopy for v1 purposes. Does not create operative reports, procedure notes, hospital-course events, labs, vitals, file inventory, task prompts, expected outputs, goldens, grader guidance, synthetic files, World Spec prose, templates, or reference files. |
| `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md` | Ratification record for Surgical History Package v1. | Records GO verdicts, medication-count clarification, accepted physician decisions, excluded/noise-controlled procedures, and carry-forward watch items. |
| `worlds/korvin-merrow/world-spec-prep/locked/daily-hospital-course-framework-v1.md` | Locked HD1-HD6 daily hospital course framework. | Bridge artifact between locked architecture and later World Spec/file/task construction. Does not create labs, lab trends, vitals, medication doses, medication schedules, orders, notes, discharge summaries, operative reports, procedure notes, file inventory, tasks, prompts, expected outputs, goldens, grader guidance, synthetic files, World Spec prose, templates, or reference files. |
| `worlds/korvin-merrow/world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md` | Ratification record for Daily Hospital Course Framework v1. | Records GO verdicts, accepted physician decisions, preparation-layer completion, World Spec Construction authorization status, and carry-forward watch items. |
| `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-01.md` | Durable post-kickoff physician decision record. | Historical state sync record; superseded for skeleton lock by decision log 02. |
| `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md` | Durable Clinical Story Skeleton v1 ratification record. | Use before Identity Package; not a draft spec or file inventory. |
| `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/post-go-interview-plan.md` | Interview sequence after Brainstorm GO. | This file; do not use before GO except for prep. |
| `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/readiness-map.md` | World Spec readiness map. | Prep status. |
| `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/self-containment-matrix.md` | Self-containment planning scaffold. | Not final traceability proof. |
| `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-spec-planning.md` | Task spec planning scaffold. | No final prompts. |
| `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/timeline-planning.md` | Timeline planning scaffold. | No final dates until physician approval. |
| `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/trap-to-file-map.md` | Trap-to-file planning scaffold. | Not a Section 3 file inventory. |
| `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md` | Active World Spec kickoff cockpit and workspace bloat/doctrine audit note. | Updated with ratified Clinical Story Skeleton state; not a draft spec. |

## Korvin Merrow World Spec Construction

Lifecycle clustering:

- `candidate-review/`: active World Spec construction artifacts awaiting physician review or lock. Currently empty after World Spec v1 lock.
- `locked/`: locked World Spec construction artifacts.
- `ratifications/`: ratification records for construction artifacts.
- Future `reviews/` folder may be added only when the lifecycle stage exists.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md` | Locked World Spec v1. | Canonical current World Spec construction artifact. It creates reviewer-facing World Spec prose, but no file inventory rows, synthetic files, clinical notes, labs, vitals, task prompts, expected outputs, goldens, grader guidance, AutoQC responses, reference files, templates, DOCX submission artifacts, or RL Studio upload. |
| `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-v1-ratification.md` | Ratification record for World Spec v1. | Records YES/LOCK READY/GO reviews, locked status, construction completion, future watch items, and boundaries. Does not create downstream artifacts. |
| `worlds/korvin-merrow/world-spec-construction/locked/world-spec-skeleton-v1.md` | Locked World Spec Skeleton. | Structural map only. Defines final World Spec section order, source-package mapping, boundaries, Studio alignment, AutoQC readiness, and construction order. Does not create final World Spec prose, synthetic files, file inventory rows, clinical notes, labs, vitals, task prompts, expected outputs, goldens, grader guidance, reference files, or templates. |
| `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-skeleton-ratification.md` | Ratification record for World Spec Skeleton v1. | Records YES/LOCK READY/GO reviews, skeleton phase completion, future watch items, and boundaries. Does not create World Spec prose, file inventory rows, synthetic files, tasks, prompts, expected outputs, goldens, grader guidance, reference files, or submission artifacts. |

## Korvin Merrow File Inventory

Lifecycle clustering:

- `candidate-review/`: active file inventory architecture artifacts awaiting physician review or lock. Currently empty after File Inventory Architecture v1 lock.
- `locked/`: locked file inventory architecture artifacts.
- `ratifications/`: ratification records for file inventory architecture artifacts.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/file-inventory/locked/file-inventory-architecture-v1.md` | Locked file inventory architecture defining planned world-level, task-level, and supplementary/noise file ecosystem. | Architecture only; not final Section 3 rows, filenames, file IDs, synthetic files, notes, labs, vitals, medication lists, discharge summaries, task prompts, expected outputs, goldens, grader guidance, DOCX artifacts, AutoQC responses, or RL Studio submission materials. |
| `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-architecture-ratification.md` | Ratification record for File Inventory Architecture v1. | Records GO reviews, accepted watch items, Phase 3 completion, next eligible phase, and downstream boundaries. |

## Duplication Watchlist

- `brainstorm.md`, `submission/Korvin_Merrow_Brainstorm.docx`, and `brainstorm-development-history.md` intentionally overlap. During SEND BACK remediation, only reviewer-required changes should be made.
- `reference/world-spec-guidelines/04_world_spec_autoqc_requirements.md`, `08_autoqc_master_index.md`, and `09_world_spec_writer_playbook.md` overlap by design. Use `08` for exact checks and `09` for workflow.
- `task-map.md` and `world-spec-prep/planning-scaffolds/task-spec-planning.md` overlap by design. `task-map.md` is reconciled and states the locked Task Architecture Package v1 supersedes old Brainstorm-level workflow mappings; `task-spec-planning.md` is earlier World Spec prep.
- `traps.md`, `planning-scaffolds/trap-to-file-map.md`, and future Section 3 work may overlap. Do not convert planning maps into final file inventory before GO.
- `frictions.md` and `planning-scaffolds/friction-to-task-map.md` overlap. Use them later to build the Decision Friction Table only after GO.
- `claude-package/*` is a compressed Claude context copy. Do not treat it as the current source of truth.
- `WORLD_SPEC_KICKOFF.md` now reduces navigation bloat by serving as the active cockpit. Older prep docs remain supporting references.

## Update Rule

Update this map when:

- A new top-level workflow folder is added.
- A new official source/template is imported.
- A submission artifact is created or replaced.
- A prep file becomes obsolete or superseded.
- A duplicate-purpose file is discovered.
