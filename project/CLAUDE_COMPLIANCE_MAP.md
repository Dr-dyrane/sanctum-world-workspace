# Claude Compliance Map

Purpose: compare the official Claude workflow expected by source-of-truth materials against the actual workspace workflow used so far. This is a compliance/continuity map, not clinical content and not a World Spec draft.

Primary evidence:

- `reference/New Writers Version - Instruction Guide (05_24).md`
- `reference/world-spec-guidelines/13_claude_workflow_audit.md`
- `project/STATUS.md`
- `claude-package/05_EXECUTION_STATE.md`
- `docs/agent-workflow.md`
- `worlds/korvin-merrow/reviews/`

## Current State

Brainstorm is approved. World Spec transition is allowed only after explicit Alexander authorization. World Spec drafting has not begun.

## Expected Workflow vs Actual Workflow

| Stage | Expected workflow from source | Actual workflow used | Status | Gap or action before World Spec |
| --- | --- | --- | --- | --- |
| Claude Project setup | Create Claude account/project and save Project Instructions in Claude Project. | Claude Project setup completed; compressed Claude package uploaded. Local package files exist in `claude-package/`. | Substantially aligned | Keep `claude-package/04_KORVIN_MERROW_CONTEXT.md`, `05_EXECUTION_STATE.md`, and `06_HANDOFF_STATE.md` current before new Claude sessions. |
| Brainstorm creation | Use official Brainstorm Claude prompt in a new Claude Project chat; attach Brainstorm template; Claude interviews through World Setup, Frictions, Traps, Rough Task Ideas, audits, then drafts. | Codex conducted the section-by-section physician interview locally. Claude was used later as a hostile reviewer/external critique artifact, not as the primary Brainstorm interviewer. | Outcome approved, workflow variant | No corrective action needed for approved Brainstorm. Preserve as historical workflow note. For future worlds, consider using official Claude Brainstorm prompt earlier if required by current pod expectations. |
| Brainstorm authorship | Physician remains clinical source of truth; Claude/LLMs may guide and accelerate but not originate scenario/traps/tasks. | Alexander originated clinical scenario, frictions, traps, and rough tasks. Codex structured and audited. Claude critique was selectively accepted. | Aligned | Continue same authorship discipline. |
| Brainstorm AutoQC | Upload Brainstorm to RL Studio, run AutoQC, address valid findings, document disagreements, rerun until clean. | Completed. Final Brainstorm AutoQC passed 51/51. SEND BACK remediation completed; reviewer GO received. | Aligned | None. |
| World Spec creation | After Brainstorm GO, use official World Spec Claude prompt in fresh Claude Project chat. Claude loads approved Brainstorm, interviews through all spec sections, runs audit, then drafts only after confirmation. | Not started. Post-GO interview plan exists locally. | Pending | Before drafting: Alexander must authorize Pass 8. Then prepare/paste official Claude World Spec starter, provide approved Brainstorm, and preserve output separately. |
| Template/reference file creation | Use Claude Project, preferably OPUS, with exact template/reference prompt starter. Attach finalized World Spec, DataBank, and System Prompt. Claude works in installments and produces individual template/reference files. | Not started. Submission package requirements have been indexed. | Pending | Do not begin until World Spec draft and file plan decisions exist. Confirm onboarding/template-reference upload conflict before final package. |
| Claude QC / AutoQC review | Claude self-check is encouraged, not required. Start new Claude Project chat, paste QC prompt, attach deliverable and AutoQC files. RL Studio AutoQC remains required. | Brainstorm AutoQC was run in RL Studio. Local/internal audits were performed. World Spec v6.3 index and playbook are prepared. | Partially aligned for Brainstorm; pending for World Spec | For World Spec, run official v6.3 Writer Edition in Claude before RL Studio upload, then run RL Studio AutoQC. |
| Claude transcripts | Source has video title mentioning World Spec/Template Files/Claude Transcript + AutoQC, but local text does not define requirement, format, or scope. | No transcript workflow has been formalized locally. | Gap | Before final World Spec upload, verify transcript field/format from RL Studio, upload video, or pod/reviewer guidance. Preserve the World Spec Claude chat transcript if export is available. |
| Codex role | Local workspace manager, source controller, reviewer, continuity system, git/checkpoint manager. | Codex has managed workspace, indexed source, prepared docs, audited outputs, and recorded checkpoints. | Aligned | Continue to read `STATUS.md`, `PASS_PLAN.md`, and `WORKSPACE_FILE_MAP.md` before changes. |
| ChatGPT role | Source mentions Claude and other LLMs generally; local docs permit ChatGPT as advisory if Alexander chooses. | No separate current ChatGPT artifact is required or documented for submission. | Acceptable | Treat any ChatGPT output as advisory only. Do not substitute it for Claude when source recommends Claude. |

## Compliance Gaps To Close Before World Spec Drafting

1. Start the official World Spec Claude session only after explicit Alexander authorization.
2. Use the official World Spec prompt starter and a fresh Claude Project chat.
3. Provide Claude the approved Brainstorm and current compressed context, without allowing Claude to originate new scenario, traps, tasks, clinical facts, dates, medications, or file names.
4. Preserve Claude output separately from authored work.
5. Confirm the unresolved transcript requirement before final World Spec upload.
6. Confirm the onboarding/template-reference upload conflict before final World Spec upload.

## Current Allowed Use Of Claude

Authorized now:

- Preparation and checklist review.
- Reviewer-risk analysis.
- Auditing the post-GO interview plan.
- Reviewing source-derived constraints.

Not authorized until Alexander explicitly starts Pass 8:

- Drafting the World Spec.
- Populating the World Spec template.
- Creating final file inventory rows.
- Writing task prompts.
- Generating synthetic files.
- Writing golden responses or grader guidelines.

