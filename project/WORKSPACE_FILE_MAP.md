# Workspace File Map

Purpose: local repository hygiene map to prevent duplicate working files and accidental edits. This is not the Sanctum World File Plan and must not be treated as a Section 3 file inventory.

Generated from local workspace file listing excluding `.git`, caches, and Python bytecode.

Current status: World Spec APPROVED after RL Studio upload, Spec AutoQC, and Stacey S Human World Spec Review. Final AutoQC board is 108/109 with the sole open flag, prednisone dose/frequency, intentionally note-justified as the central source-of-truth trap. The requested Reference File Origin routing correction was resolved and re-uploaded. Final Submission Resolution is LOCKED; Execution Artifact Generation is COMPLETE / CANONICALIZED. Execution Preparation and Transcript Resolution are complete/locked. Locked and complete layers include World Spec v1, File Inventory Architecture v1, File Inventory v1, World-Level Synthetic File Layer FI-W01 through FI-W22, Task-Level Context Files FI-T01 through FI-T07, Supplementary Files FI-S01 through FI-S04, the Entire File Ecosystem, Task Prompt Architecture v1, Task Prompts TP-KM01 through TP-KM06, Expected Output Architecture v1, Expected Outputs EO-KM01 through EO-KM06, Golden Architecture v1, Golden-KM01 through Golden-KM06, Grader Guidance Architecture v1, GG-KM01 through GG-KM06, AutoQC Architecture v1, AutoQC Construction v1, Packaging Architecture v1, Packaging Construction, Submission Preparation, Execution Preparation, and Transcript Resolution. AutoQC Architecture v1 locked artifacts are under `worlds/korvin-merrow/autoqc-architecture/locked/`: `autoqc-architecture-v1.md` and `autoqc-architecture-validation-review.md`, with ratification at `worlds/korvin-merrow/autoqc-architecture/ratifications/autoqc-architecture-ratification.md`. AutoQC Construction locked artifacts are under `worlds/korvin-merrow/autoqc/locked/`: `autoqc-construction-v1.md` and `autoqc-construction-validation-review.md`, with ratification at `worlds/korvin-merrow/autoqc/ratifications/autoqc-construction-ratification.md`. AutoQC is complete. Packaging Architecture locked artifacts are under `worlds/korvin-merrow/packaging-architecture/locked/`: `packaging-architecture-v1.md` and `packaging-architecture-validation-review.md`, with ratification at `worlds/korvin-merrow/packaging-architecture/ratifications/packaging-architecture-ratification.md`. Packaging Architecture is complete. Packaging Construction locked artifacts are under `worlds/korvin-merrow/packaging/locked/`: `packaging-construction-v1.md` and `packaging-construction-validation-review.md`; ratification is recorded at `worlds/korvin-merrow/packaging/ratifications/packaging-construction-ratification.md`. Packaging is complete. Submission Preparation locked artifacts are under `worlds/korvin-merrow/submission-preparation/locked/`: `submission-preparation-v1.md` and `submission-preparation-validation-review.md`; ratification is recorded at `worlds/korvin-merrow/submission-preparation/ratifications/submission-preparation-ratification.md`. Submission Preparation is complete. Execution Preparation locked artifacts are under `worlds/korvin-merrow/execution-preparation/locked/`: `execution-preparation-v1.md` and `execution-preparation-validation-review.md`, with ratification at `worlds/korvin-merrow/execution-preparation/ratifications/execution-preparation-ratification.md`. Transcript Resolution locked artifacts are under `worlds/korvin-merrow/transcript-resolution/locked/`: `transcript-resolution-v1.md` and `transcript-resolution-validation-review.md`. Final Submission Resolution locked artifacts are under `worlds/korvin-merrow/final-submission-resolution/locked/`: `final-submission-resolution-v1.md` and `final-submission-resolution-validation-review.md`, with ratification at `worlds/korvin-merrow/final-submission-resolution/ratifications/final-submission-resolution-ratification.md`. The authoritative transcript upload artifact is `docs/claude-transcript-formatted.md`; the Claude share URL is supporting provenance. Engineering pipeline run #1 is complete and Step 9 generated-file review / "Ready for Pipeline Fixes" is active. Pipeline output, metadata, Claude-assisted protocol, and triage live under `worlds/korvin-merrow/file-review/`. Additional Final Files AutoQC runs, AutoQC responses, scoring rubrics, scoring thresholds, pass/fail bands, point allocations, manifests, final submission packages, additional uploads, additional submissions, and RL Studio access require explicit authorization. Submission-facing DOCX/PDF artifact generation is complete/canonicalized under `korvin-merrow-final-submission-staging/`.

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
35. `worlds/korvin-merrow/file-inventory/locked/file-inventory-v1.md` for the locked planned inventory table.
36. `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-v1-ratification.md` for the File Inventory v1 lock record and carry-forward items.
37. `worlds/korvin-merrow/file-inventory/reviews/fi-t-inventory-task-layer-architecture-reconciliation.md` for FI-T metadata reconciliation and P0/P1/P2 provenance clarification.
38. `worlds/korvin-merrow/file-inventory/reviews/supplementary-file-trap5-reconciliation.md` for FI-S03 Trap #5 reconciliation.
39. `worlds/korvin-merrow/synthetic-files/locked/synthetic-world-file-construction-plan-v1.md` for locked construction governance before synthetic world-level file construction.
40. `worlds/korvin-merrow/synthetic-files/ratifications/synthetic-world-file-construction-plan-v1-ratification.md` for the lock record and next-phase boundaries.
41. `worlds/korvin-merrow/synthetic-files/locked/batch-1/batch-1-validation-review.md` for locked Batch 1 validation.
42. `worlds/korvin-merrow/synthetic-files/ratifications/batch-1-ratification.md` for Batch 1 lock record.
43. `worlds/korvin-merrow/synthetic-files/locked/batch-2/batch-2-validation-review.md` for locked Batch 2 validation.
44. `worlds/korvin-merrow/synthetic-files/ratifications/batch-2-ratification.md` for Batch 2 lock record.
45. `worlds/korvin-merrow/synthetic-files/locked/batch-3/batch-3-validation-review.md` for locked Batch 3 validation.
46. `worlds/korvin-merrow/synthetic-files/ratifications/batch-3-ratification.md` for Batch 3 lock record.
47. `worlds/korvin-merrow/synthetic-files/locked/batch-4/batch-4-validation-review.md` for locked Batch 4 validation.
48. `worlds/korvin-merrow/synthetic-files/ratifications/batch-4-ratification.md` for Batch 4 lock record.
49. `worlds/korvin-merrow/synthetic-files/locked/batch-5/batch-5-validation-review.md` for locked Batch 5 validation.
50. `worlds/korvin-merrow/synthetic-files/ratifications/batch-5-ratification.md` for Batch 5 lock record and world-level layer completion.
51. `worlds/korvin-merrow/reviews/world-level-layer-closure-audit.md` for world-level closure audit result.
52. `worlds/korvin-merrow/task-layer-architecture/locked/task-level-context-file-architecture-v1.md` for locked task-layer context file architecture.
53. `worlds/korvin-merrow/task-layer-architecture/ratifications/task-level-context-file-architecture-v1-ratification.md` for architecture ratification and next-phase boundaries.
54. `worlds/korvin-merrow/task-context-files/locked/task-context-files-validation-review.md` for locked FI-T construction validation and carry-forward watch items.
55. `worlds/korvin-merrow/task-context-files/ratifications/task-level-context-file-construction-ratification.md` for Task-Level Context File Construction lock record.
56. `worlds/korvin-merrow/task-context-files/locked/` for locked FI-T01 through FI-T07 request-framing files.
57. `worlds/korvin-merrow/supplementary-file-architecture/locked/supplementary-file-architecture-v1.md` for locked FI-S architecture.
58. `worlds/korvin-merrow/supplementary-file-architecture/locked/supplementary-file-architecture-validation-review.md` for locked FI-S architecture validation.
59. `worlds/korvin-merrow/supplementary-file-architecture/ratifications/supplementary-file-architecture-v1-ratification.md` for Supplementary File Architecture v1 lock record.
60. `worlds/korvin-merrow/supplementary-files/locked/supplementary-file-construction-validation-review.md` for locked FI-S construction validation.
61. `worlds/korvin-merrow/supplementary-files/locked/` for locked FI-S01 through FI-S04 files.
62. `worlds/korvin-merrow/supplementary-files/ratifications/supplementary-file-construction-ratification.md` for Supplementary File Construction lock record.
63. `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-v1.md` for locked task-prompt architecture.
64. `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-validation-review.md` for locked architecture validation.
65. `worlds/korvin-merrow/task-prompt-architecture/ratifications/task-prompt-architecture-ratification.md` for Task Prompt Architecture v1 ratification.
66. `worlds/korvin-merrow/task-prompts/locked/task-prompt-construction-validation-review.md` for locked TP-KM construction validation.
67. `worlds/korvin-merrow/task-prompts/locked/` for locked TP-KM01 through TP-KM06 prompts.
68. `worlds/korvin-merrow/task-prompts/ratifications/task-prompt-construction-ratification.md` for Task Prompt Construction lock record.
69. `worlds/korvin-merrow/expected-output-architecture/locked/expected-output-architecture-v1.md` for locked Expected Output Architecture v1.
70. `worlds/korvin-merrow/expected-output-architecture/locked/expected-output-architecture-validation-review.md` for locked Expected Output Architecture validation.
71. `worlds/korvin-merrow/expected-output-architecture/ratifications/expected-output-architecture-ratification.md` for Expected Output Architecture v1 lock record.
72. `worlds/korvin-merrow/expected-outputs/locked/EO-KM01.md` through `EO-KM06.md` for locked expected outputs.
73. `worlds/korvin-merrow/expected-outputs/locked/expected-output-construction-validation-review.md` for locked Expected Output Construction validation.
74. `worlds/korvin-merrow/expected-outputs/ratifications/expected-output-construction-ratification.md` for Expected Output Construction lock record.
75. `worlds/korvin-merrow/golden-architecture/locked/golden-architecture-v1.md` for locked Golden Architecture v1.
76. `worlds/korvin-merrow/golden-architecture/locked/golden-architecture-validation-review.md` for locked Golden Architecture validation review.
77. `worlds/korvin-merrow/golden-architecture/locked/golden-architecture-audit-reconciliation.md` for Golden Architecture audit reconciliation findings and corrections.
78. `worlds/korvin-merrow/golden-architecture/ratifications/golden-architecture-ratification.md` for Golden Architecture v1 ratification and lock record.
79. `worlds/korvin-merrow/goldens/locked/Golden-KM01.md` for locked Golden-KM01.
80. `worlds/korvin-merrow/goldens/locked/Golden-KM02.md` for locked Golden-KM02.
81. `worlds/korvin-merrow/goldens/locked/Golden-KM03.md` for locked Golden-KM03.
82. `worlds/korvin-merrow/goldens/locked/Golden-KM04.md` for locked Golden-KM04.
83. `worlds/korvin-merrow/goldens/locked/Golden-KM05.md` for locked Golden-KM05.
84. `worlds/korvin-merrow/goldens/locked/Golden-KM06.md` for locked Golden-KM06.
85. `worlds/korvin-merrow/goldens/locked/golden-construction-validation-review.md` for locked Golden Construction validation review.
86. `worlds/korvin-merrow/goldens/ratifications/golden-construction-ratification.md` for Golden Construction ratification and lock record.
87. `worlds/korvin-merrow/grader-guidance-architecture/locked/grader-guidance-architecture-v1.md` for locked Grader Guidance Architecture.
88. `worlds/korvin-merrow/grader-guidance-architecture/locked/grader-guidance-architecture-validation-review.md` for locked Grader Guidance Architecture validation review.
89. `worlds/korvin-merrow/grader-guidance-architecture/ratifications/grader-guidance-architecture-ratification.md` for Grader Guidance Architecture lock record.
90. `worlds/korvin-merrow/grader-guidance/locked/GG-KM01.md` for locked Grader Guidance KM01.
91. `worlds/korvin-merrow/grader-guidance/locked/GG-KM02.md` for locked Grader Guidance KM02.
92. `worlds/korvin-merrow/grader-guidance/locked/GG-KM03.md` for locked Grader Guidance KM03.
93. `worlds/korvin-merrow/grader-guidance/locked/GG-KM04.md` for locked Grader Guidance KM04.
94. `worlds/korvin-merrow/grader-guidance/locked/GG-KM05.md` for locked Grader Guidance KM05.
95. `worlds/korvin-merrow/grader-guidance/locked/GG-KM06.md` for locked Grader Guidance KM06.
96. `worlds/korvin-merrow/grader-guidance/locked/grader-guidance-construction-validation-review.md` for locked Grader Guidance Construction validation review.
97. `worlds/korvin-merrow/grader-guidance/ratifications/grader-guidance-construction-ratification.md` for Grader Guidance Construction ratification and lock record.
98. `worlds/korvin-merrow/autoqc-architecture/locked/autoqc-architecture-v1.md` for locked AutoQC Architecture v1.
99. `worlds/korvin-merrow/autoqc-architecture/locked/autoqc-architecture-validation-review.md` for locked AutoQC Architecture v1 validation review.
100. `worlds/korvin-merrow/autoqc-architecture/ratifications/autoqc-architecture-ratification.md` for AutoQC Architecture v1 ratification and lock record.
101. `worlds/korvin-merrow/autoqc/locked/autoqc-construction-v1.md` for locked AutoQC Construction v1 package.
102. `worlds/korvin-merrow/autoqc/locked/autoqc-construction-validation-review.md` for locked AutoQC Construction validation review.
103. `worlds/korvin-merrow/autoqc/ratifications/autoqc-construction-ratification.md` for AutoQC Construction ratification and AutoQC completion.
104. `worlds/korvin-merrow/packaging-architecture/locked/packaging-architecture-v1.md` for locked Packaging Architecture v1 package.
105. `worlds/korvin-merrow/packaging-architecture/locked/packaging-architecture-validation-review.md` for locked Packaging Architecture validation review.
106. `worlds/korvin-merrow/packaging-architecture/ratifications/packaging-architecture-ratification.md` for Packaging Architecture ratification and completion.
107. `worlds/korvin-merrow/packaging/locked/packaging-construction-v1.md` for locked Packaging Construction package.
108. `worlds/korvin-merrow/packaging/locked/packaging-construction-validation-review.md` for locked Packaging Construction validation review.
109. `worlds/korvin-merrow/packaging/ratifications/packaging-construction-ratification.md` for Packaging Construction ratification and Packaging completion.
110. `worlds/korvin-merrow/submission-preparation/locked/submission-preparation-v1.md` for locked Submission Preparation v1.
111. `worlds/korvin-merrow/submission-preparation/locked/submission-preparation-validation-review.md` for locked Submission Preparation validation.
112. `worlds/korvin-merrow/submission-preparation/ratifications/submission-preparation-ratification.md` for Submission Preparation ratification and completion.
113. `worlds/korvin-merrow/execution-preparation/locked/execution-preparation-v1.md` for locked Execution Preparation v1.
114. `worlds/korvin-merrow/execution-preparation/locked/execution-preparation-validation-review.md` for locked Execution Preparation validation review.
115. `worlds/korvin-merrow/final-submission-resolution/locked/final-submission-resolution-v1.md` for locked Final Submission Resolution decisions.
116. `worlds/korvin-merrow/final-submission-resolution/locked/final-submission-resolution-validation-review.md` for locked Final Submission Resolution validation review.
117. `korvin-merrow-final-submission-staging/` for generated submission-facing artifact staging. Canonical active contents are `01_spec-document/Alexander_World_Merrow_latest_6_4.docx`, `02_template-reference-files/final/` with 33 date-stamped DOCX files, Claude transcript DOCX/PDF, optional Brainstorm copy, and empty hold-not-upload folder. This is staging only; it is not a manifest, zip, AutoQC response, or scoring artifact.
118. `worlds/korvin-merrow/reviews/reviewer-spec-approval-01.md` for Stacey S World Spec approval and Reference File Origin routing correction record.
119. `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md` for historical interview basis.
120. `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md` for ratified Clinical Story Skeleton decisions and construction-lock status.
121. `reference/world-spec-guidelines/08_autoqc_master_index.md` only when exact AutoQC checks are needed.

Do not start by opening every prep file. Most prep files are supporting memory, not active instructions.

## Hygiene Audit 2026-05-31

Status: restructured into junction folders, purpose folders, and World Spec prep lifecycle folders.

Findings:

- Root is clean by repo-standard exception: `.gitignore`, `AGENTS.md`, and `README.md`.
- README placement is acceptable: root README plus folder-policy READMEs in `reference/source/` and `tools/`.
- `tmp/` contains generated render artifacts and is ignored by git.
- `reference/` is now a junction folder with source files moved into `reference/source/`.
- `worlds/korvin-merrow/` is now a junction folder with one README and purpose subfolders.
- `worlds/korvin-merrow/file-inventory/` is now a lifecycle folder for file inventory architecture and file-plan work; File Inventory Architecture v1 and File Inventory v1 are locked and ratified.
- World Spec prep and construction artifacts are clustered by lifecycle stage so candidate, locked, ratified, review, decision-log, and planning-scaffold files do not sit in one flat folder.
- `worlds/korvin-merrow/synthetic-files/` is now a lifecycle folder for synthetic file planning/construction. Synthetic World-Level File Construction Plan v1 is locked and ratified. Batch 1, Batch 2, Batch 3, Batch 4, and Batch 5 synthetic world-level files are locked and ratified. World-Level Synthetic File Layer is complete.
- `worlds/korvin-merrow/task-layer-architecture/` is now a lifecycle folder for task-layer architecture and boundary-setting. Task-Level Context File Architecture v1 is locked and ratified; `candidate-review/` no longer contains an active architecture artifact. Task-context files live in `worlds/korvin-merrow/task-context-files/`, not in the architecture folder.
- `worlds/korvin-merrow/task-context-files/` is now a lifecycle folder for FI-T task-context file construction. FI-T01 through FI-T07 are locked and Task-Level Context Files are complete; no FI-S files, prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission artifacts exist in this folder.
- `worlds/korvin-merrow/supplementary-file-architecture/` is now a lifecycle folder for FI-S architecture only. Supplementary File Architecture v1 is locked and ratified; no constructed FI-S files belong in the architecture folder.
- `worlds/korvin-merrow/supplementary-files/` is now a lifecycle folder for FI-S file construction. FI-S01 through FI-S04 are locked and Supplementary Files are complete.
- `candidate-review/` is reserved for active candidate artifacts only. Inactive candidate-review folders should be absent from the visible tree and recreated on demand when a new candidate artifact exists. Execution Preparation candidate-review is inactive after lock; Transcript Resolution candidate-review is inactive after lock.
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
| `docs/claude-transcript-formatted.md` | Authoritative Claude transcript upload artifact. | Current transcript artifact for RL Studio file-upload handling; preserves phase chronology, decisions, ratifications, evidence trail, and Claude share URL provenance. |
| `docs/claude-transcript.md` | Raw Claude conversation transcript for the Korvin Merrow build. | Historical/provenance evidence only. Historical James Carter references and export encoding artifacts are expected. |
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
| `reference/source/How to Upload Your Clod Transcript.mp4` | Reference/source video for Claude transcript upload handling. | Preserve as source evidence only; do not convert, summarize into governing rules, package, or submit until transcript/upload scope is explicitly authorized. |
| `reference/source/README.md` | Source material policy. | No proprietary source edits here. |

## World Spec Example Source Documents

These are fetched source/reference examples, not authored Korvin Merrow content and not the Korvin Merrow World File Plan. The folder is intentionally local-only and gitignored because the example corpus is large and can confuse project-specific source-of-truth boundaries.

| File | Role | Duplication note |
| --- | --- | --- |
| `reference/word-spec-examples/` | Local-only source/reference example corpus. | Gitignored; preserve locally as reference material only, not authored project content or a source-of-truth hierarchy. |

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
| `worlds/korvin-merrow/reviews/reviewer-spec-approval-01.md` | Stacey S World Spec approval record. | Records World Spec APPROVED, Reference File Origin routing correction, re-upload resolution, onboarding gate completion, and next engineering pipeline stage. |

## Korvin Merrow Submission

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx` | Approved Brainstorm DOCX remediation artifact. | Reuploaded, AutoQC passed, and approved by reviewer. Preserve as approved Brainstorm source artifact. |

## Korvin Merrow World Spec Prep

Lifecycle clustering:

- `WORLD_SPEC_KICKOFF.md`: the only root cockpit file in `world-spec-prep/`.
- `candidate-review/`: artifacts awaiting physician decision or lock. Folder absent unless an active World Spec prep candidate exists.
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

- `candidate-review/`: active World Spec construction artifacts awaiting physician review or lock. Folder absent unless an active construction candidate exists.
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

- `candidate-review/`: active file inventory artifacts awaiting physician review or lock. Folder absent unless an active file-inventory candidate exists.
- `locked/`: locked file inventory architecture and planned inventory artifacts.
- `ratifications/`: ratification records for file inventory artifacts.
- `reviews/`: reconciliation and review records for authorized inventory governance updates.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/file-inventory/locked/file-inventory-v1.md` | Locked planned file inventory table using AutoQC v6.3 8-column structure. | Planning only; not synthetic file creation, chart-note writing, final submission packaging, task construction, prompts, expected outputs, goldens, grader guidance, AutoQC responses, or RL Studio upload. |
| `worlds/korvin-merrow/file-inventory/reviews/fi-w20-inventory-row-reconciliation.md` | Reconciliation record for the FI-W20 File Inventory row supported-tags under-specification. | Records why the FI-W20 row was expanded for secondary/collateral Trap #1 and Endocrinology vs Primary Team support without changing FI-W20 content, Batch 4 content, source-of-truth hierarchy, or prednisone hierarchy. |
| `worlds/korvin-merrow/file-inventory/reviews/fi-t-inventory-task-layer-architecture-reconciliation.md` | Reconciliation record for FI-T File Inventory metadata and Task-Level Context File Architecture v1 provenance wording. | Records why FI-T02, FI-T04, FI-T05, and FI-T06 metadata was expanded for supported secondary trap/friction coverage and why P0/P1/P2 labels are tracker-provenance metadata only. |
| `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-v1-ratification.md` | Ratification record for File Inventory v1. | Records GO reviews, accepted carry-forward items, File Inventory Planning completion, next eligible phase, and downstream boundaries. |
| `worlds/korvin-merrow/file-inventory/locked/file-inventory-architecture-v1.md` | Locked file inventory architecture defining planned world-level, task-level, and supplementary/noise file ecosystem. | Architecture only; not final Section 3 rows, filenames, file IDs, synthetic files, notes, labs, vitals, medication lists, discharge summaries, task prompts, expected outputs, goldens, grader guidance, DOCX artifacts, AutoQC responses, or RL Studio submission materials. |
| `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-architecture-ratification.md` | Ratification record for File Inventory Architecture v1. | Records GO reviews, accepted watch items, Phase 3 completion, next eligible phase, and downstream boundaries. |

## Korvin Merrow Synthetic Files

Lifecycle clustering:

- `candidate-review/`: active synthetic-file construction artifacts awaiting physician review or lock. Folder absent unless an active synthetic-file candidate exists.
- `locked/`: locked synthetic-file construction governance and locked construction units.
- `ratifications/`: ratification records for synthetic-file construction governance or future construction units.
- This area must not contain synthetic chart contents unless Alexander explicitly authorizes that phase.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/synthetic-files/locked/synthetic-world-file-construction-plan-v1.md` | Locked construction strategy for the 22 locked world-level files FI-W01 through FI-W22. | Governance/planning only; not filenames, synthetic file contents, chart notes, admission notes, consultant notes, nursing notes, therapy notes, discharge summaries, labs, vitals, medication lists, medication schedules, task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission materials. |
| `worlds/korvin-merrow/synthetic-files/ratifications/synthetic-world-file-construction-plan-v1-ratification.md` | Ratification record for Synthetic World-Level File Construction Plan v1. | Records GO reviews, accepted carry-forward items, Synthetic File Construction Governance completion, Batch 1 next eligible phase, and downstream boundaries. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-1/FI-W01_ed-triage-initial-intake.md` | Locked synthetic world-level file FI-W01. | ED triage/intake documentation only. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-1/FI-W02_ed-provider-assessment.md` | Locked synthetic world-level file FI-W02. | ED provider assessment only. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-1/FI-W03_admission-history-and-physical.md` | Locked synthetic world-level file FI-W03. | Admission H&P only. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-1/FI-W04_initial-medication-reconciliation-note.md` | Locked synthetic world-level file FI-W04. | Initial medication reconciliation note only; not a discharge medication list or final reconciliation output. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-1/FI-W05_pharmacy-refill-history-report.md` | Locked synthetic world-level file FI-W05. | Pharmacy/refill provenance only; not proof of actual ingestion or discharge appropriateness. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-1/FI-W06_outpatient-rheumatology-prednisone-provenance.md` | Locked synthetic world-level file FI-W06. | Outpatient rheumatology prednisone provenance only; not an inpatient consult or steroid answer file. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-1/FI-W07_primary-care-outpatient-baseline-summary.md` | Locked synthetic world-level file FI-W07. | Primary care baseline/provenance only; not a disposition decision or hospital-course trend file. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-1/batch-1-validation-review.md` | Locked validation review for Batch 1 FI-W01 through FI-W07. | Review artifact only; not a synthetic chart file, task prompt, golden, grader guidance, AutoQC response, or submission artifact. |
| `worlds/korvin-merrow/synthetic-files/ratifications/batch-1-ratification.md` | Ratification record for Batch 1 Synthetic World-Level File Construction. | Records GO reviews, accepted carry-forward items, Batch 1 lock, Batch 1 Construction completion, Batch 2 next eligible phase, and downstream boundaries. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-2/FI-W08_hd1-hd2-hospitalist-progress-documentation.md` | Locked synthetic world-level file FI-W08. | HD1-HD2 hospitalist progress documentation only; not a final discharge summary, not a task prompt, and not a grader artifact. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-2/FI-W09_hd3-hospitalist-progress-documentation.md` | Locked synthetic world-level file FI-W09. | HD3 hospitalist progress documentation only; not a final functional source, not a task prompt, and not a grader artifact. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-2/FI-W10_hd4-hospitalist-progress-documentation.md` | Locked synthetic world-level file FI-W10. | HD4 hospitalist progress documentation only; preserves FI-W06 HD4 availability and is not an answer file. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-2/FI-W11_hd5-hd6-hospitalist-discharge-planning-progress-documentation.md` | Locked synthetic world-level file FI-W11. | HD5-HD6 pre-close discharge-planning progress documentation only; not a completed discharge outcome and not a final medication plan. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-2/FI-W12_objective-renal-infection-hemodynamic-trend-summary-source.md` | Locked synthetic world-level file FI-W12. | Objective trend source only; not a final infection-source answer and not a discharge-readiness decision. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-2/FI-W13_medication-administration-inpatient-medication-action-source.md` | Locked synthetic world-level file FI-W13. | MAR/inpatient medication action source only; not a discharge medication list and not a final restart plan. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-2/batch-2-validation-review.md` | Locked validation review for Batch 2 FI-W08 through FI-W13. | Review artifact only; not a synthetic chart file, task prompt, golden, grader guidance, AutoQC response, or submission artifact. |
| `worlds/korvin-merrow/synthetic-files/ratifications/batch-2-ratification.md` | Ratification record for Batch 2 Synthetic World-Level File Construction. | Records GO reviews, accepted carry-forward items, Batch 2 lock, Batch 2 Construction completion, Batch 3 next eligible phase, and downstream boundaries. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-3/FI-W14_nephrology-consultation-documentation.md` | Locked synthetic world-level file FI-W14. | Nephrology consultation documentation only; not a discharge summary, not a final medication plan, and not an answer file. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-3/FI-W15_cardiology-consultation-documentation.md` | Locked synthetic world-level file FI-W15. | Cardiology consultation documentation only; not a final GDMT restart plan and not an answer file. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-3/FI-W16_endocrinology-consultation-documentation.md` | Locked synthetic world-level file FI-W16. | Endocrinology consultation documentation only; not proof of adrenal insufficiency, not a final steroid taper, and not an answer file. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-3/batch-3-validation-review.md` | Locked validation review for Batch 3 FI-W14 through FI-W16. | Review artifact only; not a synthetic chart file, task prompt, golden, grader guidance, AutoQC response, or submission artifact. |
| `worlds/korvin-merrow/synthetic-files/ratifications/batch-3-ratification.md` | Ratification record for Batch 3 Synthetic World-Level File Construction. | Records GO reviews, accepted carry-forward items, Batch 3 lock, Batch 3 Construction completion, Batch 4 next eligible phase, and downstream boundaries. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-4/FI-W17_bedside-nursing-observation-notes-flowsheet-summary.md` | Locked synthetic world-level file FI-W17. | Bedside nursing observation summary only; not a final disposition decision and not an answer file. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-4/FI-W18_physical-therapy-assessment.md` | Locked synthetic world-level file FI-W18. | Physical Therapy assessment only; not a final therapy/discharge order and not an answer file. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-4/FI-W19_occupational-therapy-assessment.md` | Locked synthetic world-level file FI-W19. | Occupational Therapy assessment only; not a final medication reconciliation, final disposition answer, or answer file. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-4/FI-W20_family-communication-care-conference-documentation.md` | Locked synthetic world-level file FI-W20. | Family communication documentation only; not a final disposition decision, steroid answer, or source-of-truth override. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-4/FI-W21_case-management-social-work-discharge-planning-note.md` | Locked synthetic world-level file FI-W21. | Case Management / Social Work discharge-planning note only; not a completed discharge plan, final service authorization, or final disposition decision. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-4/batch-4-validation-review.md` | Locked validation review for Batch 4 FI-W17 through FI-W21. | Review artifact only; not a synthetic chart file, task prompt, golden, grader guidance, AutoQC response, or submission artifact. |
| `worlds/korvin-merrow/synthetic-files/ratifications/batch-4-ratification.md` | Ratification record for Batch 4 Synthetic World-Level File Construction. | Records GO reviews, FI-W20 reconciliation completion, Batch 4 lock, Batch 4 Construction completion, Batch 5 next eligible phase, and downstream boundaries. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-5/FI-W22_discharge-facing-plan-snapshot-before-world-close.md` | Locked synthetic world-level file FI-W22. | Discharge-facing plan snapshot before world close only; visible and useful but incomplete, not a final discharge summary, final disposition decision, final medication reconciliation, or answer file. |
| `worlds/korvin-merrow/synthetic-files/locked/batch-5/batch-5-validation-review.md` | Locked validation review for Batch 5 FI-W22. | Review artifact only; not a synthetic chart file, task prompt, golden, grader guidance, AutoQC response, submission artifact, or task artifact. |
| `worlds/korvin-merrow/synthetic-files/ratifications/batch-5-ratification.md` | Ratification record for Batch 5 Synthetic World-Level File Construction. | Records GO reviews, Batch 5 lock, FI-W22 lock, Batch 5 Construction completion, World-Level Synthetic File Layer completion, the historical next eligible Task-Level Context File Architecture phase after Batch 5 lock, and downstream boundaries. |

## Korvin Merrow Task-Layer Architecture

Lifecycle clustering:

- `candidate-review/`: active task-layer architecture artifacts awaiting physician/reviewer review or lock. Folder absent unless an active task-layer architecture candidate exists.
- `locked/`: locked task-layer architecture artifacts.
- `ratifications/`: ratification records for task-layer architecture artifacts.
- This area is architecture only unless Alexander explicitly authorizes a later construction phase.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/task-layer-architecture/locked/task-level-context-file-architecture-v1.md` | Locked architecture governing future FI-T01 through FI-T07 task-level context files. | Defines scope, FI-T inventory architecture, trap/friction coverage, physician workflow mapping, world-necessity safeguards, source-of-truth safeguards, boundaries, and roadmap. Does not create FI-T files, FI-S files, task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or task outputs. |
| `worlds/korvin-merrow/task-layer-architecture/ratifications/task-level-context-file-architecture-v1-ratification.md` | Ratification record for Task-Level Context File Architecture v1. | Records Reviewer A recertification LOCK READY / GO, Reviewer B LOCK READY / GO, reconciliation completion, architecture lock, Task-Level Context File Architecture completion, next eligible Task-Level Context File Construction phase, and downstream boundaries. |

## Korvin Merrow Task Context Files

Lifecycle clustering:

- `candidate-review/`: active task-context files awaiting review or lock. Folder absent unless an active task-context candidate exists.
- `locked/`: locked task-context files after ratification. FI-T01 through FI-T07 are locked here.
- `ratifications/`: ratification records for task-context file construction batches.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/task-context-files/locked/FI-T01_discharge-medication-reconciliation-request-context.md` | Locked FI-T01 task-context file. | Request-framing file for discharge medication reconciliation; not a final medication list, task prompt, expected output, golden, or grader artifact. |
| `worlds/korvin-merrow/task-context-files/locked/FI-T02_discharge-summary-drafting-request-context.md` | Locked FI-T02 task-context file. | Request-framing file for discharge summary synthesis; not an actual discharge summary, task prompt, expected output, golden, or grader artifact. |
| `worlds/korvin-merrow/task-context-files/locked/FI-T03_discharge-readiness-care-coordination-request-context.md` | Locked FI-T03 task-context file. | Request-framing file for discharge readiness / care coordination; not a final disposition order, services authorization, task prompt, expected output, golden, or grader artifact. |
| `worlds/korvin-merrow/task-context-files/locked/FI-T04_consultant-synthesis-interdisciplinary-care-plan-request-context.md` | Locked FI-T04 task-context file. | Request-framing file for interdisciplinary consultant synthesis; not a completed care plan, consultant winner, task prompt, expected output, golden, or grader artifact. |
| `worlds/korvin-merrow/task-context-files/locked/FI-T05_early-post-discharge-follow-up-assessment-request-context.md` | Locked FI-T05 task-context file. | Request-framing file for +7 follow-up reassessment; adds no new post-world clinical facts and is not a task prompt, expected output, golden, or grader artifact. |
| `worlds/korvin-merrow/task-context-files/locked/FI-T06_patient-safety-readmission-risk-review-request-context.md` | Locked FI-T06 task-context file. | Request-framing file for +30 safety/readmission-risk review inside Discharge Planning Documentation; not a standalone risk workflow, RCA, outcome, task prompt, expected output, golden, or grader artifact. |
| `worlds/korvin-merrow/task-context-files/locked/FI-T07_medication-safety-handoff-task-context-addendum.md` | Locked FI-T07 task-context file. | Focused medication-safety handoff addendum; not a final medication reconciliation, final home regimen, task prompt, expected output, golden, or grader artifact. |
| `worlds/korvin-merrow/task-context-files/locked/task-context-files-validation-review.md` | Locked validation review for FI-T01 through FI-T07. | Verifies authorized file creation, cross-artifact consistency, synthesis requirements, anti-answer-file boundaries, trap/friction preservation, source hierarchy, physician-perspective framing, unauthorized artifact checks, and carry-forward prompt-layer watch items. |
| `worlds/korvin-merrow/task-context-files/ratifications/task-level-context-file-construction-ratification.md` | Ratification record for Task-Level Context File Construction. | Records Reviewer A/B outcomes, no true/architecture/governance defects, lock approval, locked path, carry-forward watch items, and downstream boundaries. |

## Korvin Merrow Task Prompt Architecture

Lifecycle clustering:

- `candidate-review/`: active task-prompt architecture artifacts awaiting review or lock. Folder absent unless an active candidate architecture exists.
- `locked/`: locked task-prompt architecture artifacts after ratification.
- `ratifications/`: ratification records for task-prompt architecture artifacts.
- This area is architecture only unless Alexander explicitly authorizes a later prompt-construction phase.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-v1.md` | Locked architecture for future task prompts. | Defines six future prompt families, workflow/trap/friction/file dependency matrices, prompt packaging rules, and boundaries. Does not create prompt text, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission artifacts. |
| `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-validation-review.md` | Locked validation review for Task Prompt Architecture v1. | Verifies locked-source alignment, six-family prompt structure, FI-T07 addendum handling, and absence of prohibited downstream artifacts. |
| `worlds/korvin-merrow/task-prompt-architecture/ratifications/task-prompt-architecture-ratification.md` | Ratification record for Task Prompt Architecture v1. | Records unanimous LOCK READY review consensus, six prompt-family architecture approval, FI-T07 addendum architecture approval, verified workflow/trap/friction/hierarchy/file-dependency coverage, lock, Task Prompt Architecture completion, and next eligible Task Prompt Construction phase. |

## Korvin Merrow Task Prompts

Lifecycle clustering:

- `candidate-review/`: active task prompts awaiting review or lock. Folder absent unless an active candidate exists.
- `locked/`: locked task prompts and task-prompt construction validation after ratification.
- `ratifications/`: ratification records for task prompt construction.
- This area must not contain expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or submission materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/task-prompts/locked/TP-KM01.md` | Locked task prompt TP-KM01. | Locked prompt only; not an expected output, golden, grader guidance, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/task-prompts/locked/TP-KM02.md` | Locked task prompt TP-KM02. | Locked prompt only; not an expected output, golden, grader guidance, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/task-prompts/locked/TP-KM03.md` | Locked task prompt TP-KM03. | Locked prompt only; not an expected output, golden, grader guidance, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/task-prompts/locked/TP-KM04.md` | Locked task prompt TP-KM04. | Locked prompt only; not an expected output, golden, grader guidance, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/task-prompts/locked/TP-KM05.md` | Locked task prompt TP-KM05. | Locked prompt only; not an expected output, golden, grader guidance, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/task-prompts/locked/TP-KM06.md` | Locked task prompt TP-KM06. | Locked prompt only; not an expected output, golden, grader guidance, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/task-prompts/locked/task-prompt-construction-validation-review.md` | Locked validation review for TP-KM01 through TP-KM06. | Review artifact only; not an expected output, golden, grader guidance, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/task-prompts/ratifications/task-prompt-construction-ratification.md` | Ratification record for Task Prompt Construction. | Records Reviewer A/B LOCK READY / GO, STRONG clinical prompt quality, contributor validation PASS, no true/governance/canon defects, prompt lock, Task Prompts completion, and next eligible Expected Output Architecture phase. |

## Korvin Merrow Expected Output Architecture

Lifecycle clustering:

- `candidate-review/`: active expected-output architecture artifacts awaiting review or lock. Folder absent unless an active candidate exists.
- `locked/`: locked expected-output architecture artifacts after ratification.
- `ratifications/`: ratification records for expected-output architecture artifacts.
- This area is architecture only and must not contain actual expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or submission materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/expected-output-architecture/locked/expected-output-architecture-v1.md` | Locked expected-output architecture. | Defines EO-KM01 through EO-KM06 structure, deliverable surfaces, reasoning domains, source dependencies, trap/friction/hierarchy handling, and boundaries. Does not create actual expected-output text, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission artifacts. |
| `worlds/korvin-merrow/expected-output-architecture/locked/expected-output-architecture-validation-review.md` | Locked validation review for Expected Output Architecture v1. | Verifies locked-source alignment, one-to-one prompt mapping, file dependency preservation, hierarchy preservation, and absence of actual expected outputs/goldens/grader guidance/downstream artifacts. |
| `worlds/korvin-merrow/expected-output-architecture/ratifications/expected-output-architecture-ratification.md` | Ratification record for Expected Output Architecture v1. | Records Reviewer A/B LOCK READY / GO, STRONG clinical architecture, six EO-KM slots approved, FI-T07 addendum preservation, no true/governance/canon defects, Expected Output Architecture lock, Expected Output Architecture completion, and next eligible Expected Output Construction phase. |

## Korvin Merrow Expected Outputs

Lifecycle clustering:

- `candidate-review/`: active expected-output drafts awaiting review or lock. Folder absent unless an active expected-output candidate exists.
- `locked/`: locked expected-output drafts after ratification. EO-KM01 through EO-KM06 are currently here.
- `ratifications/`: ratification records for expected-output construction.
- This area must not contain golden responses, grader guidance, rubrics, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or submission materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/expected-outputs/locked/EO-KM01.md` | Locked expected output for TP-KM01. | Expected output only; not a golden response, grader guidance, rubric, AutoQC response, DOCX artifact, or submission artifact. FI-T07 remains addendum support for this EO only. |
| `worlds/korvin-merrow/expected-outputs/locked/EO-KM02.md` | Locked expected output for TP-KM02. | Expected output only; not a golden response, grader guidance, rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/expected-outputs/locked/EO-KM03.md` | Locked expected output for TP-KM03. | Expected output only; not a golden response, grader guidance, rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/expected-outputs/locked/EO-KM04.md` | Locked expected output for TP-KM04. | Expected output only; not a golden response, grader guidance, rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/expected-outputs/locked/EO-KM05.md` | Locked expected output for TP-KM05. | Expected output only; not a golden response, grader guidance, rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/expected-outputs/locked/EO-KM06.md` | Locked expected output for TP-KM06. | Expected output only; not a golden response, grader guidance, rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/expected-outputs/locked/expected-output-construction-validation-review.md` | Locked validation review for EO-KM01 through EO-KM06. | Confirms construction alignment and prohibited-artifact boundaries; not a golden response, grader guidance, rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/expected-outputs/ratifications/expected-output-construction-ratification.md` | Ratification record for Expected Output Construction. | Records Reviewer A/B LOCK READY / GO, STRONG clinical expected-output quality, six expected outputs approved, no EO-KM07, FI-T07 addendum preservation, no true/governance/canon defects, Expected Output Construction lock, Expected Outputs completion, and next eligible Golden Architecture phase. |

## Korvin Merrow Golden Architecture

Lifecycle clustering:

- `candidate-review/`: inactive after Golden Architecture v1 lock; folder absent unless a future candidate is explicitly authorized.
- `locked/`: locked Golden Architecture artifacts after ratification.
- `ratifications/`: ratification records for Golden Architecture.
- This area is architecture only and must not contain golden responses, grader guidance, scoring rubrics, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or submission materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/golden-architecture/locked/golden-architecture-v1.md` | Locked architecture for future golden responses. | Defines Golden-KM01 through Golden-KM06 count, IDs, EO/TP mapping, evidence dependencies, reasoning requirements, hierarchy handling, friction/trap-domain handling, quality standards, prohibition classes, and boundary protections. It does not create golden response text, grader guidance, rubric language, AutoQC responses, DOCX artifacts, or submission artifacts. |
| `worlds/korvin-merrow/golden-architecture/locked/golden-architecture-validation-review.md` | Locked validation review for Golden Architecture v1. | Confirms alignment with locked prompts, expected outputs, governance, file dependencies, hierarchy rules, watch items, and prohibited-artifact boundaries. It is not a golden response, grader document, rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/golden-architecture/locked/golden-architecture-audit-reconciliation.md` | Audit reconciliation review for Golden Architecture v1. | Resolves independent cold-audit findings, records classifications and canon-supported corrections, and confirms no golden response, grader guidance, rubric, AutoQC response, DOCX artifact, or submission artifact was created. |
| `worlds/korvin-merrow/golden-architecture/ratifications/golden-architecture-ratification.md` | Ratification record for Golden Architecture v1. | Records LOCK READY / GO review outcome, Golden-KM01 through Golden-KM06 approval, six-golden architecture approval, one-to-one TP -> EO -> Golden mapping, FI-T07 addendum preservation, workflow/hierarchy/friction/information-problem fidelity, uncertainty preservation, multi-path physician-answer principle, golden-leakage boundary, FI-W22 and FI-S guardrails, Golden Architecture lock, Golden Architecture completion, and next eligible Golden Construction phase. |

## Korvin Merrow Goldens

Lifecycle clustering:

- `candidate-review/`: inactive after Golden Construction lock; folder absent unless a future candidate is explicitly authorized.
- `locked/`: locked golden artifacts after ratification.
- `ratifications/`: ratification records for Golden Construction.
- This area must not contain grader guidance, scoring rubrics, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or submission materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/goldens/locked/Golden-KM01.md` | Locked golden response for TP-KM01 / EO-KM01. | Medication reconciliation recommendation only; preserves FI-T07 as addendum support for Golden-KM01 and does not create a final signed discharge medication list, grader guidance, rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/goldens/locked/Golden-KM02.md` | Locked golden response for TP-KM02 / EO-KM02. | Discharge summary synthesis only; does not invent culture data, final steroid diagnosis, final medication plan, completed discharge outcome, grader guidance, rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/goldens/locked/Golden-KM03.md` | Locked golden response for TP-KM03 / EO-KM03. | Discharge-readiness assessment only; preserves FI-W22 as incomplete and does not create a discharge order, final disposition decision, services authorization, grader guidance, rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/goldens/locked/Golden-KM04.md` | Locked golden response for TP-KM04 / EO-KM04. | Interdisciplinary care plan only; preserves consultant tensions and does not create a new workflow, final medication list, grader guidance, rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/goldens/locked/Golden-KM05.md` | Locked golden response for TP-KM05 / EO-KM05. | Early follow-up assessment only; does not invent post-discharge facts, services, labs, adherence, outcomes, grader guidance, rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/goldens/locked/Golden-KM06.md` | Locked golden response for TP-KM06 / EO-KM06. | Safety/readmission-risk review only; does not create an RCA conclusion, blame finding, readmission event, post-discharge outcome, grader guidance, rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/goldens/locked/golden-construction-validation-review.md` | Locked validation review for Golden Construction. | Confirms mapping, source alignment, hierarchy preservation, boundary protection, and prohibited-artifact checks; not a grader document, scoring rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/goldens/ratifications/golden-construction-ratification.md` | Ratification record for Golden Construction. | Records Reviewer A/B LOCK READY / GO, STRONG clinical golden quality, HIGH benchmark integrity, six-golden approval, no Golden-KM07, FI-T07 addendum preservation, fidelity checks, lock, Goldens completion, and next eligible Grader Guidance Architecture phase. |

## Korvin Merrow Grader Guidance Architecture

Lifecycle clustering:

- `candidate-review/`: inactive after Grader Guidance Architecture v1 lock; folder absent unless a future candidate is explicitly authorized.
- `locked/`: locked grader-guidance architecture artifacts after ratification.
- `ratifications/`: ratification records for Grader Guidance Architecture.
- This area is architecture only and must not contain actual grader guidance, scoring rubrics, scoring thresholds, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or submission materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/grader-guidance-architecture/locked/grader-guidance-architecture-v1.md` | Locked architecture for future grader guidance. | Defines GG-KM01 through GG-KM06 count, IDs, TP/EO/Golden mapping, grading philosophy, acceptable/unacceptable-answer principles, reasoning dimensions, hierarchy/friction/uncertainty expectations, and boundary protections. It does not create actual grader guidance, scoring rubrics, scoring thresholds, AutoQC responses, DOCX artifacts, or submission artifacts. |
| `worlds/korvin-merrow/grader-guidance-architecture/locked/grader-guidance-architecture-validation-review.md` | Locked validation review for Grader Guidance Architecture v1. | Verifies alignment with locked goldens, expected outputs, prompts, governance, file dependencies, hierarchy rules, multi-path defensibility, and prohibited-artifact boundaries. It is not grader guidance, a scoring rubric, an AutoQC response, a DOCX artifact, or a submission artifact. |
| `worlds/korvin-merrow/grader-guidance-architecture/ratifications/grader-guidance-architecture-ratification.md` | Ratification record for Grader Guidance Architecture v1. | Records LOCK READY / GO review outcome, six-slot GG architecture approval, TP -> EO -> Golden -> GG chain verification, FI-T07 preservation, anti-verbatim-matching principle, multi-path defensibility, lock, architecture completion, and next eligible Grader Guidance Construction phase. |

## Korvin Merrow Grader Guidance

Lifecycle clustering:

- `candidate-review/`: inactive after Grader Guidance Construction lock; folder absent unless a future candidate is explicitly authorized.
- `locked/`: locked grader guidance artifacts after ratification.
- `ratifications/`: ratification records for Grader Guidance Construction.
- This area contains locked grader guidance only and must not contain scoring rubrics, scoring thresholds, pass/fail bands, point allocations, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or submission materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/grader-guidance/locked/GG-KM01.md` | Locked grader guidance for TP-KM01 / EO-KM01 / Golden-KM01. | Locked guidance only; preserves FI-T07 as addendum support for GG-KM01 only. Not a scoring rubric, point key, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/grader-guidance/locked/GG-KM02.md` | Locked grader guidance for TP-KM02 / EO-KM02 / Golden-KM02. | Locked guidance only; not a scoring rubric, point key, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/grader-guidance/locked/GG-KM03.md` | Locked grader guidance for TP-KM03 / EO-KM03 / Golden-KM03. | Locked guidance only; not a scoring rubric, discharge authorization key, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/grader-guidance/locked/GG-KM04.md` | Locked grader guidance for TP-KM04 / EO-KM04 / Golden-KM04. | Locked guidance only; not a scoring rubric, consultant-winner key, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/grader-guidance/locked/GG-KM05.md` | Locked grader guidance for TP-KM05 / EO-KM05 / Golden-KM05. | Locked guidance only; protects against invented +7 facts. Not a scoring rubric, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/grader-guidance/locked/GG-KM06.md` | Locked grader guidance for TP-KM06 / EO-KM06 / Golden-KM06. | Locked guidance only; not an RCA rubric, outcome-scoring artifact, AutoQC response, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/grader-guidance/locked/grader-guidance-construction-validation-review.md` | Locked validation review for GG-KM01 through GG-KM06. | Review artifact only; confirms no GG-KM07, no rubrics, no thresholds, no pass/fail bands, no AutoQC responses, no DOCX artifacts, and no submission artifacts. |
| `worlds/korvin-merrow/grader-guidance/ratifications/grader-guidance-construction-ratification.md` | Ratification record for Grader Guidance Construction. | Records Reviewer A/B LOCK READY / GO, STRONG guidance quality, HIGH benchmark integrity, six-file approval, no GG-KM07, TP -> EO -> Golden -> GG chain verification, fidelity checks, no scoring leakage, lock, and Grader Guidance completion. Current downstream state is Execution Preparation next eligible after Submission Preparation lock. |

## Korvin Merrow AutoQC Architecture

Lifecycle clustering:

- `candidate-review/`: inactive after AutoQC Architecture v1 lock; folder absent unless a future candidate is explicitly authorized.
- `locked/`: locked AutoQC Architecture v1 artifacts after ratification.
- `ratifications/`: ratification records for AutoQC Architecture.
- This area is architecture only. It must not contain AutoQC responses, executed AutoQC results, scoring rubrics, scoring thresholds, pass/fail bands, point allocations, DOCX artifacts, RL Studio submission artifacts, or submission materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/autoqc-architecture/locked/autoqc-architecture-v1.md` | Locked architecture for future AutoQC organization. | Defines AutoQC scope, artifact IDs, relationship to locally available World Spec AutoQC v6.3, boundary to the not-yet-local Section 6 Grader Guidelines AutoQC prompt, task/file/prompt/expected-output/golden/grader-guidance/packaging QC boundaries, and carry-forward watch items. It does not run AutoQC or create AutoQC responses. |
| `worlds/korvin-merrow/autoqc-architecture/locked/autoqc-architecture-validation-review.md` | Locked validation review for AutoQC Architecture v1. | Verifies alignment with locked sources and the ecosystem comparison audit, confirms required watch items, and preserves prohibitions against AutoQC responses, scoring artifacts, DOCX artifacts, and submission artifacts. |
| `worlds/korvin-merrow/autoqc-architecture/ratifications/autoqc-architecture-ratification.md` | Ratification record for AutoQC Architecture v1. | Records LOCK READY / GO review outcome, STRONG architecture quality, HIGH governance fidelity, no defects, lock, AutoQC Architecture completion, and next eligible AutoQC Construction phase. |

## Korvin Merrow AutoQC

Lifecycle clustering:

- `candidate-review/`: inactive after AutoQC Construction v1 lock; folder absent unless a future AutoQC candidate is explicitly authorized.
- `locked/`: locked AutoQC Construction v1 artifacts after ratification.
- `ratifications/`: ratification records for AutoQC Construction.
- This area is AutoQC preparation only. It must not contain AutoQC run outputs, platform responses, AutoQC response drafts, scoring rubrics, scoring thresholds, pass/fail bands, point allocations, DOCX artifacts, RL Studio submission artifacts, or submission materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/autoqc/locked/autoqc-construction-v1.md` | Locked AutoQC preparation package. | Organizes future execution order, AQC-KM01 through AQC-KM07 inputs, blocked dependencies, official prompt dependencies, response routing, reconciliation routing, packaging routing, and carry-forward watch items. It does not run AutoQC or draft responses. |
| `worlds/korvin-merrow/autoqc/locked/autoqc-construction-validation-review.md` | Locked validation review for AutoQC Construction v1. | Verifies alignment with locked AutoQC Architecture v1 and boundary preservation. It is not an AutoQC response, scoring artifact, DOCX artifact, or submission artifact. |
| `worlds/korvin-merrow/autoqc/ratifications/autoqc-construction-ratification.md` | Ratification record for AutoQC Construction. | Records independent review completion, AQC-KM01 through AQC-KM07 verification, no AQC-KM08, routing verification, transcript carry-forward, lock, AutoQC completion, and next eligible Packaging Architecture phase. |

## Korvin Merrow Packaging Architecture

Lifecycle clustering:

- `candidate-review/`: inactive after Packaging Architecture v1 lock; folder absent unless a future candidate is explicitly authorized.
- `locked/`: locked Packaging Architecture artifacts after ratification.
- `ratifications/`: ratification records for Packaging Architecture.
- This area is packaging architecture only. It must not contain populated DOCX artifacts, manifests, submission packages, AutoQC responses, scoring artifacts, or RL Studio materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/packaging-architecture/locked/packaging-architecture-v1.md` | Locked packaging architecture package. | Defines packaging scope, PKG-KM01 through PKG-KM08, DOCX strategy, upload sequencing strategy, manifest strategy, transcript strategy, reference/template handling, reconciliation handling, and authorization boundaries. It does not create packaging artifacts. |
| `worlds/korvin-merrow/packaging-architecture/locked/packaging-architecture-validation-review.md` | Locked validation review for Packaging Architecture v1. | Verifies alignment with locked AutoQC Construction, source-derived submission requirements, transcript ambiguity handling, and prohibited artifact boundaries. |
| `worlds/korvin-merrow/packaging-architecture/ratifications/packaging-architecture-ratification.md` | Ratification record for Packaging Architecture v1. | Records template fidelity, official template/source structure preservation, Source/Tool separation, single-DOCX requirement, transcript and AutoQC boundaries, reconciliation routing, lock, Packaging Architecture completion, and next eligible Packaging Construction phase. |

## Korvin Merrow Packaging

Lifecycle clustering:

- `candidate-review/`: inactive after Packaging Construction lock; folder absent unless a future candidate is explicitly authorized.
- `locked/`: locked Packaging Construction artifacts after ratification.
- `ratifications/`: ratification records for Packaging Construction.
- This area is packaging preparation only. It must not contain populated DOCX artifacts, manifests, final submission packages, AutoQC responses, scoring artifacts, RL Studio upload records, or submission materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/packaging/locked/packaging-construction-v1.md` | Locked Packaging Construction package. | Maps PKG-KM01 through PKG-KM08, execution order, dependency order, blocked dependencies, required inputs, future output targets, transcript/DOCX/manifest/upload/reconciliation workflows, authorization gates, and stop points. It does not create packaging artifacts. |
| `worlds/korvin-merrow/packaging/locked/packaging-construction-validation-review.md` | Locked validation review for Packaging Construction v1. | Verifies alignment with locked Packaging Architecture, locked sources, submission-reference materials, transcript boundary, DOCX boundary, manifest boundary, upload boundary, AutoQC boundary, and locked-artifact protection. |

## Korvin Merrow Submission Preparation

Lifecycle clustering:

- `candidate-review/`: inactive after Submission Preparation lock; folder absent unless a future candidate is explicitly authorized.
- `locked/`: locked Submission Preparation artifacts after ratification.
- `ratifications/`: ratification records for Submission Preparation.
- This area is submission-preparation planning only. It must not contain populated DOCX artifacts, final manifests, submission packages, AutoQC responses, scoring artifacts, RL Studio upload records, or submitted materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/submission-preparation/locked/submission-preparation-v1.md` | Locked Submission Preparation v1 package. | Records decision register, unresolved dependency register, official-source evidence register, stop-point register, and proposed next execution order before any DOCX population, manifest creation, AutoQC run, upload, or submission. |
| `worlds/korvin-merrow/submission-preparation/locked/submission-preparation-validation-review.md` | Locked validation review for Submission Preparation v1. | Verifies preparation-only scope, template fidelity, unresolved source conflicts, transcript boundaries, RL Studio boundaries, AutoQC boundaries, and prohibited artifact protection. |
| `worlds/korvin-merrow/submission-preparation/ratifications/submission-preparation-ratification.md` | Ratification record for Submission Preparation. | Records independent review completion, register verification, transcript/reference/template fidelity handling, blocked reconciliation points, authorization gates, lock, Submission Preparation completion, and next eligible Execution Preparation phase. |

## Korvin Merrow Execution Preparation

Lifecycle clustering:

- `candidate-review/`: inactive after Execution Preparation lock; folder absent unless a future candidate is explicitly authorized.
- `locked/`: locked Execution Preparation artifacts after ratification.
- `ratifications/`: ratification records for Execution Preparation.
- This area is execution preparation only. It must not contain AutoQC run outputs, AutoQC responses, populated DOCX artifacts, manifests, final submission packages, scoring artifacts, upload records, or submitted materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/execution-preparation/locked/execution-preparation-v1.md` | Locked Execution Preparation v1 package. | Records execution readiness, dependency, external-system, authorization, stop-point, and final execution-order registers. It does not perform execution, run AutoQC, populate DOCX, create a manifest, upload, submit, modify locked artifacts, or create scoring artifacts. |
| `worlds/korvin-merrow/execution-preparation/locked/execution-preparation-validation-review.md` | Locked validation review for Execution Preparation v1. | Verifies coverage of the twelve readiness surfaces, required registers, transcript/template/reference evidence handling, and prohibited-artifact boundaries. |

## Korvin Merrow Transcript Resolution

Lifecycle clustering:

- `candidate-review/`: absent after Transcript Resolution lock.
- `locked/`: locked Transcript Resolution v1 artifacts.
- `ratifications/`: absent; Transcript Resolution was locked by Alexander's explicit decision rather than a separate ratification artifact.
- This area is transcript-resolution preparation only. It must not contain formatted transcript packages, DOCX artifacts, manifests, AutoQC responses, scoring artifacts, upload records, or submitted materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/transcript-resolution/locked/transcript-resolution-v1.md` | Locked Transcript Resolution v1 package. | Records current Studio file-upload evidence, stale-video supersession, authoritative transcript artifact, Claude share URL provenance, and boundary preservation. It does not upload, submit, populate DOCX, create manifests, run AutoQC, or create scoring artifacts. |
| `worlds/korvin-merrow/transcript-resolution/locked/transcript-resolution-validation-review.md` | Locked validation review for Transcript Resolution v1. | Verifies alignment with Execution Preparation, source-derived transcript guidance, current Studio screenshot evidence, stale-video limits, Alexander's locked transcript decision, and prohibited-artifact boundaries. |

## Korvin Merrow Final Submission Resolution

Lifecycle clustering:

- `candidate-review/`: absent after Final Submission Resolution lock.
- `locked/`: locked Final Submission Resolution v1 artifacts.
- `ratifications/`: absent until explicit ratification/lock authorization.
- This area is resolution architecture only. It must not contain generated DOCX/PDF files, manifests, final packages, AutoQC responses, scoring artifacts, RL Studio upload records, or submitted materials unless Alexander explicitly authorizes a later phase.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/final-submission-resolution/locked/final-submission-resolution-v1.md` | Locked Final Submission Resolution v1 package. | Defines required/optional/do-not-upload sets, folder mapping, execution inventory, DOCX population blueprint, export matrix, transcript export decision, FI-W/FI-T/FI-S upload boundaries, and stop points. It does not create DOCX/PDF artifacts, manifests, packages, uploads, submissions, AutoQC responses, or scoring artifacts. |
| `worlds/korvin-merrow/final-submission-resolution/locked/final-submission-resolution-validation-review.md` | Locked validation review for Final Submission Resolution v1. | Verifies alignment with official template evidence, RL Studio evidence, example package structure, locked Korvin artifacts, Transcript Resolution, source-derived upload inventory, and prohibited boundaries. |

## Korvin Merrow Supplementary File Architecture

Lifecycle clustering:

- `candidate-review/`: active supplementary architecture artifacts awaiting lock. Folder absent unless an active supplementary architecture candidate exists.
- `locked/`: locked supplementary architecture artifacts.
- `ratifications/`: ratification records for supplementary architecture.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/supplementary-file-architecture/locked/supplementary-file-architecture-v1.md` | Locked architecture governing future FI-S01 through FI-S04 supplementary files. | Defines supplementary necessity, exact FI-S count, file purposes, workflow/trap/friction relationships, hierarchy constraints, prohibited content classes, anti-answer-file protections, and FI-S/FI-T interaction rules. Does not create FI-S files, prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission artifacts. |
| `worlds/korvin-merrow/supplementary-file-architecture/locked/supplementary-file-architecture-validation-review.md` | Locked validation review for Supplementary File Architecture v1. | Verifies cross-artifact consistency, locked FI-S count, inventory alignment, workflow/trap/friction/source hierarchy preservation, world necessity, unauthorized artifact checks, and closed FI-S03 Trap #5 reconciliation. |
| `worlds/korvin-merrow/supplementary-file-architecture/ratifications/supplementary-file-architecture-v1-ratification.md` | Ratification record for Supplementary File Architecture v1. | Records independent review completion, FI-S03 Trap #5 reconciliation completion, lock approval, Supplementary File Architecture completion, next eligible Supplementary File Construction phase, and downstream boundaries. |
| `worlds/korvin-merrow/file-inventory/reviews/supplementary-file-trap5-reconciliation.md` | Reconciliation record for FI-S03 Trap #5 secondary support. | Records TRUE INCONSISTENCY, authoritative FI-S03 row, minimal Trap Coverage Matrix update, verification, finding closure, and Supplementary File Architecture lock readiness before ratification. |

## Korvin Merrow Supplementary Files

Lifecycle clustering:

- `candidate-review/`: active supplementary FI-S files awaiting review or lock. Currently no active candidate artifacts after Supplementary File Construction lock.
- `locked/`: locked supplementary files.
- `ratifications/`: ratification records for supplementary file construction.
- This area must not contain task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission materials unless Alexander explicitly authorizes those later phases.

| File | Role | Duplication note |
| --- | --- | --- |
| `worlds/korvin-merrow/supplementary-files/locked/FI-S01_remote-pci-coronary-stent-provenance-summary.md` | Locked FI-S01 supplementary file. | Remote PCI/CAD provenance only; not a GDMT restart answer, medication reconciliation, consultant synthesis, or discharge plan. |
| `worlds/korvin-merrow/supplementary-files/locked/FI-S02_remote-sleep-study-osa-provenance-summary.md` | Locked FI-S02 supplementary file. | Remote OSA provenance only; not an explanation for functional decline, near-fall, acute presentation, or discharge readiness. |
| `worlds/korvin-merrow/supplementary-files/locked/FI-S03_home-support-equipment-logistics-reference.md` | Locked FI-S03 supplementary file. | Home support/equipment logistics only; secondary Trap #5 texture, not a final discharge plan, services authorization, or safe/unsafe discharge answer. |
| `worlds/korvin-merrow/supplementary-files/locked/FI-S04_problem-list-past-history-snapshot.md` | Locked FI-S04 supplementary file. | Low-authority problem-list/history texture only; not a prednisone source, final diagnosis list, final medication reconciliation, or copy-forward answer file. |
| `worlds/korvin-merrow/supplementary-files/locked/supplementary-file-construction-validation-review.md` | Locked validation review for FI-S01 through FI-S04. | Verifies architecture alignment, inventory alignment, trap/friction/hierarchy preservation, anti-answer-file protections, FI-W22 incompleteness, and absence of prompts/outputs/goldens/grader guidance/AutoQC/DOCX/submission artifacts. |
| `worlds/korvin-merrow/supplementary-files/ratifications/supplementary-file-construction-ratification.md` | Ratification record for Supplementary File Construction. | Records Reviewer A/B LOCK READY / GO, no true/governance/architecture defects, FI-S03 reconciliation closure, Supplementary File Construction lock, Supplementary Files completion, Entire File Ecosystem completion, and next eligible Task Prompt Architecture phase. |

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
## Korvin Merrow Final Submission Staging
Purpose: generated local staging structure for submission-facing artifacts. This folder is not a manifest, zip, final package, upload record, submission record, AutoQC response, or scoring artifact.
Status: Execution Artifact Generation COMPLETE / CANONICALIZED.
Path: korvin-merrow-final-submission-staging/.
Subfolders:
- 01_spec-document/: contains the canonical submitted spec `Alexander_World_Merrow_latest_6_4.docx`.
- 02_template-reference-files/final/: contains the canonical 33-file date-stamped reference/task upload set.
- 03_claude-transcript/: contains Korvin_Merrow_Claude_Transcript.docx and optional Korvin_Merrow_Claude_Transcript.pdf.
- 04_optional-qc-inputs/: contains copied approved Brainstorm DOCX when present.
- 05_hold-not-upload/: empty by design; TP/EO/Golden/GG artifacts were not exported.

## Post-Submission Remediation And Reproducibility
Purpose: provenance and repeatability records from the final World Spec remediation and submission-preparation push.
Files:
- `docs/workspace-guardrails-lessons.md`: operational guardrails from the Korvin execution phase.
- `docs/docx-generation-method.md`: mandatory DOCX generation/editing method for future Word artifacts; records the recon/build/integrity/render/diff loop and Korvin failure-to-fix lessons.
- `docs/world-pipeline-playbook.md`: future-stage and future-world pipeline recipe.
- `reference/checklists/spec-autoqc-preflight.md`: Spec AutoQC preflight checklist.
- `tools/generate_reference_files.py`: reference-file generation utility.
- `worlds/korvin-merrow/autoqc-remediation/`: AutoQC remediation notes, response language, and world-spec DOCX bring-home plan.
- `worlds/korvin-merrow/reference-file-design/`: Epic-style reference-file design system and approved sample artifacts.
- `worlds/korvin-merrow/reviews/stacey-corrections-recovery-report.md`: recovered reviewer-correction audit.
- `project/archive/git-cleanup-plan-2026-06-04.md`: consumed cleanup plan preserved as historical execution context.

## Future World Skeleton
Purpose: lightweight lifecycle folder scaffold for World #2+ so a new world can start from the proven Korvin tree without copying Korvin content.
Path: `worlds/_skeleton/`.
Status: infrastructure only; contains `.gitkeep` placeholders and no clinical, task, submission, or source-of-truth content.

## Local Drive Mirror
Purpose: local mirror of the reviewer-convenience Google Drive package.
Path: `korvin-merrow-drive-package/`.
Status: gitignored and non-canonical. Use it for Drive sync verification only; do not treat it as repository source of truth.

## Korvin Merrow File Review
Purpose: Step 9 generated-file review / "Ready for Pipeline Fixes" working area after engineering pipeline run #1.
Path: `worlds/korvin-merrow/file-review/`.
Status: active. Alexander is reviewing generated files with Claude assistance. Candidate revision work has been prepared locally and logged, but platform upload/apply/AutoQC steps remain gated on explicit Alexander authorization.
Key files:
- `worlds/korvin-merrow/file-review/time-strategy-and-state.md`: current state, 6-hour strategy, and Claude kickoff prompt.
- `worlds/korvin-merrow/file-review/file-review-protocol.md`: review protocol, trap-fidelity checklist, platform-verbatim requirements, and revision workflow.
- `worlds/korvin-merrow/file-review/findings-triage.md`: active Claude-assisted B2 triage packet. Items marked `[A]` require Alexander ruling before edits.
- `worlds/korvin-merrow/file-review/file-review-log.md`: candidate revision log for pipeline run #1, including Alexander rulings, object-model edit notes, integrity/render checks, and remaining platform steps.
- `worlds/korvin-merrow/file-review/pipeline-output/`: downloaded pipeline run #1 output, including 33 generated DOCX files under `filesystem/` plus metadata under `.meta/`.
- `worlds/korvin-merrow/file-review/revision/`: working revision snapshot when candidate edits are prepared. Do not upload or treat as final without Alexander authorization.
- `worlds/korvin-merrow/file-review/upload/filesystem/`: candidate 26-file world-level upload set prepared from the revised files. Do not upload without Alexander authorization.
- `worlds/korvin-merrow/file-review/task-files-holdback/`: seven task-level files intentionally held out of the world-level upload set for later task setup handling.
- `worlds/korvin-merrow/file-review/claude-package/cold-audit-prompt.txt`: Claude cold-audit prompt for independent review of the 26-file upload candidate. The paired ZIP remains ignored/local.
- `worlds/korvin-merrow/file-review/pipeline-output.zip`: ignored local download archive; the extracted `pipeline-output/` tree is the review surface.
Boundaries:
- Do not apply edits labeled PROTECT.
- Do not run Final Files AutoQC, upload revisions, Apply to Task, create task setup materials, create AutoQC responses, or access RL Studio unless Alexander explicitly authorizes the exact step.
- Claude assistance should be tracked as phase-specific review/remediation provenance in this folder, not appended to the original onboarding transcript.
