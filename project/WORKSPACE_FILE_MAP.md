# Workspace File Map

Purpose: local repository hygiene map to prevent duplicate working files and accidental edits. This is not the Sanctum World File Plan and must not be treated as a Section 3 file inventory.

Generated from local workspace file listing excluding `.git`, caches, and Python bytecode.

Current status: State synchronized / ready for Clinical Story Skeleton preparation. Clinical Story Skeleton and World Spec drafting have not started.

## Root

| File | Role | Duplication note |
| --- | --- | --- |
| `.gitignore` | Git hygiene and local-secret protection. | Single root ignore file. |
| `AGENTS.md` | Codex operating instructions. | Root behavior source; do not duplicate in docs. |
| `CONTRIBUTING.md` | Contribution and review rules. | Complements `README.md`; not a project status file. |
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
| `claude-package/04_KORVIN_MERROW_CONTEXT.md` | Refreshed Korvin Merrow context for Claude. | Includes submitted Brainstorm summary, locked decisions, and World Spec prep risks. |
| `claude-package/05_EXECUTION_STATE.md` | Refreshed execution state for Claude. | Mirrors current Brainstorm approval / World Spec transition state; use `project/STATUS.md` for live status. |
| `claude-package/06_HANDOFF_STATE.md` | Fresh-session Claude handoff. | Summarizes locked decisions, remaining decisions, next legal action, and hard boundaries. |

## Reference Source

| File | Role | Duplication note |
| --- | --- | --- |
| `reference/New Writers Version - Instruction Guide (05_24).docx` | Official instruction guide source DOCX. | Preserve unchanged. |
| `reference/New Writers Version - Instruction Guide (05_24).md` | Markdown extraction of official guide. | Operational reading copy; DOCX remains source artifact. |
| `reference/_Task Selection Categories For Team.xlsx` | Official task tracker. | Preserve unchanged. |
| `reference/source/README.md` | Source material policy. | No proprietary source edits here. |

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

## Korvin Merrow Core Authored Files

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/brainstorm.md` | Active Brainstorm remediation source. | Modify only for reviewer-required changes approved by Alexander. |
| `worlds/korvin-merrow/brainstorm-development-history.md` | Internal Brainstorm history. | Historical only. |
| `worlds/korvin-merrow/brainstorm-internal-audit.md` | Internal Brainstorm audit. | Historical QC. |
| `worlds/korvin-merrow/clinical-logic.md` | Clinical reasoning notes. | Prep/support only. |
| `worlds/korvin-merrow/frictions.md` | Friction notes. | Source for later Decision Friction planning. |
| `worlds/korvin-merrow/traps.md` | Trap notes. | Source for later trap substrate planning. |
| `worlds/korvin-merrow/task-map.md` | Rough task mapping. | Brainstorm-level mapping; not final World Spec task architecture. |
| `worlds/korvin-merrow/world-spec.md` | Placeholder/skeleton. | Do not draft/populate before GO. |
| `worlds/korvin-merrow/reviewer-feedback.md` | Review notes and moved internal questions. | Use for reviewer feedback history. |
| `worlds/korvin-merrow/reviewer-comorbidity-decision-brief.md` | Physician decision brief for SEND BACK comorbidity expansion. | Prep only; do not treat proposed additions as locked until approved. |
| `worlds/korvin-merrow/reviewer-medication-decision-brief.md` | Physician decision brief for SEND BACK medication specificity. | Prep only; do not treat proposed medication list as locked until approved. |
| `worlds/korvin-merrow/reviewer-remediation-compliance-review.md` | Compliance validation for reviewer-requested comorbidity and medication remediation. | Supports SEND BACK revisions; not a World Spec source. |
| `worlds/korvin-merrow/rename-audit.md` | Audit of reviewer-required synthetic identity rename. | Confirms active files use Korvin Merrow and prior name remains only in historical archives. |
| `worlds/korvin-merrow/KORVIN_MERROW_PASS_PLAN.md` | World-specific pass plan. | Planning only. |
| `worlds/korvin-merrow/claude-brainstorm-review-package.md` | Claude Brainstorm review package. | Historical support artifact. |

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

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/world-spec-prep/autoqc-preflight-checklist.md` | Local preflight checklist. | Summary; exact check source is `08_autoqc_master_index.md`. |
| `worlds/korvin-merrow/world-spec-prep/claude-review-triage.md` | Triage of Claude World Spec prep review. | Decision queue; not clinical content. |
| `worlds/korvin-merrow/world-spec-prep/decision-register.md` | Prep decision register. | Use for pending/locked decisions after GO. |
| `worlds/korvin-merrow/world-spec-prep/file-plan-planning.md` | File plan planning scaffold. | Not a final file inventory. |
| `worlds/korvin-merrow/world-spec-prep/friction-to-task-map.md` | Friction/task planning map. | Planning only. |
| `worlds/korvin-merrow/world-spec-prep/physician-decision-log-01.md` | Durable post-kickoff physician decision record. | Use before Clinical Story Skeleton development; not a draft spec. |
| `worlds/korvin-merrow/world-spec-prep/post-go-interview-plan.md` | Interview sequence after Brainstorm GO. | This file; do not use before GO except for prep. |
| `worlds/korvin-merrow/world-spec-prep/readiness-map.md` | World Spec readiness map. | Prep status. |
| `worlds/korvin-merrow/world-spec-prep/self-containment-matrix.md` | Self-containment planning scaffold. | Not final traceability proof. |
| `worlds/korvin-merrow/world-spec-prep/task-spec-planning.md` | Task spec planning scaffold. | No final prompts. |
| `worlds/korvin-merrow/world-spec-prep/timeline-planning.md` | Timeline planning scaffold. | No final dates until physician approval. |
| `worlds/korvin-merrow/world-spec-prep/trap-to-file-map.md` | Trap-to-file planning scaffold. | Not a Section 3 file inventory. |
| `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md` | Active World Spec kickoff cockpit and workspace bloat/doctrine audit note. | Use first for World Spec transition orientation; not a draft spec. |

## Duplication Watchlist

- `brainstorm.md`, `submission/Korvin_Merrow_Brainstorm.docx`, and `brainstorm-development-history.md` intentionally overlap. During SEND BACK remediation, only reviewer-required changes should be made.
- `reference/world-spec-guidelines/04_world_spec_autoqc_requirements.md`, `08_autoqc_master_index.md`, and `09_world_spec_writer_playbook.md` overlap by design. Use `08` for exact checks and `09` for workflow.
- `task-map.md` and `world-spec-prep/task-spec-planning.md` overlap by design. `task-map.md` is Brainstorm-level; `task-spec-planning.md` is World Spec prep.
- `traps.md`, `trap-to-file-map.md`, and future Section 3 work may overlap. Do not convert planning maps into final file inventory before GO.
- `frictions.md` and `friction-to-task-map.md` overlap. Use them later to build the Decision Friction Table only after GO.
- `claude-package/*` is a compressed Claude context copy. Do not treat it as the current source of truth.
- `WORLD_SPEC_KICKOFF.md` now reduces navigation bloat by serving as the active cockpit. Older prep docs remain supporting references.

## Update Rule

Update this map when:

- A new top-level workflow folder is added.
- A new official source/template is imported.
- A submission artifact is created or replaced.
- A prep file becomes obsolete or superseded.
- A duplicate-purpose file is discovered.
