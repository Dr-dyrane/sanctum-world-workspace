# Project Sanctum Pass Plan

Source of truth: `reference/New Writers Version - Instruction Guide (05_24).md`

This is the local operating method. Do not advance to a later pass without explicit Alexander approval.

## Pass 0: Workspace Setup And Source Import

Goal: Establish the local workspace and ingest the official source of truth.

Inputs:

- Official New Writer Instruction Guide
- Project workspace
- Alexander's onboarding context

Actions:

- Create workspace folders and root operating instructions.
- Index operational guidance into checklists and workflows.
- Preserve source material separately from authored work.

Outputs:

- `AGENTS.md`
- `reference/checklists/`
- `reference/workflows/`
- `project/STATUS.md`

Done criteria:

- Source of truth imported.
- Operating boundaries documented.
- Ready to begin Korvin Merrow Brainstorm.

Do-not-cross boundary:

- Do not create final clinical deliverables.

## Pass 1: Brainstorm Clinical Interview

Goal: Extract physician-originated clinical reasoning for the Brainstorm.

Inputs:

- Korvin Merrow seed context
- Brainstorm checklist
- Alexander's clinical judgment

Actions:

- Interview section by section: World Setup, Major Friction Points, Major Traps, Rough Task Ideas.
- Ask targeted clinical questions.
- Challenge weak points like a reviewer.
- Separate frictions from traps.

Outputs:

- Raw physician answers
- Reviewer-risk notes
- Missing-detail list

Done criteria:

- All four Brainstorm sections have enough physician-originated content for a concept draft.
- Major reviewer risks are identified.

Do-not-cross boundary:

- Do not draft final Brainstorm language yet.
- Do not invent clinical decisions.

## Pass 2: Brainstorm Draft

Goal: Convert physician-originated answers into a concise Brainstorm draft.

Inputs:

- Pass 1 interview notes
- Brainstorm template
- Brainstorm checklist

Actions:

- Organize content into four required sections.
- Keep it a concept pitch.
- Preserve Alexander's reasoning and voice.

Outputs:

- Draft `worlds/james-carter/brainstorm.md`

Done criteria:

- Draft covers required sections.
- No final task prompts, file inventory, golden responses, grader guidelines, or failure analysis.

Do-not-cross boundary:

- Do not upload to RL Studio.
- Do not move to World Spec.

## Pass 3: Reviewer-Risk Audit

Goal: Stress-test the Brainstorm before official drafting/checking.

Inputs:

- Brainstorm draft
- Brainstorm checklist
- Reviewer failure patterns

Actions:

- Check realism, self-containment, task viability, and trap/friction separation.
- Identify likely AutoQC or reviewer flags.
- Ask Alexander for missing clinical details.

Outputs:

- Audit findings
- Revision list
- Physician decisions needed

Done criteria:

- Blockers resolved or explicitly deferred.
- Alexander approves moving to official Claude pass/check.

Do-not-cross boundary:

- Do not submit to RL Studio.

## Pass 4: Claude Official Pass/Check

Goal: Use Claude as the official Sanctum drafting assistant when recommended by the guide.

Inputs:

- Official Brainstorm prompt/template section
- Alexander-approved raw clinical decisions
- Current Brainstorm draft or structured input

Actions:

- Prepare paste-ready Claude input.
- Tell Alexander what to paste and what output to bring back.
- Ensure Claude is not asked to create scenario concept, traps, or task ideas.
- Audit returned Claude output.

Outputs:

- Claude-organized draft or critique
- Codex audit against physician intent and Sanctum checklist

Done criteria:

- Claude output is reconciled with Alexander's intent.
- Unsupported additions are removed or flagged.

Do-not-cross boundary:

- Do not let Claude originate clinical concept, traps, or task ideas.

## Pass 5: Final Physician Review

Goal: Finalize Brainstorm for upload.

Inputs:

- Audited Brainstorm draft
- Alexander's final edits

Actions:

- Present final draft for physician approval.
- Incorporate approved changes.
- Confirm no scope creep.

Outputs:

- Physician-approved Brainstorm document

Done criteria:

- Alexander explicitly approves upload-ready Brainstorm.

Do-not-cross boundary:

- Do not upload without approval.

## Pass 6: RL Studio Upload And AutoQC

Goal: Upload Brainstorm and clear AutoQC.

Inputs:

- Physician-approved Brainstorm
- RL Studio access

Actions:

- Ask before browser/RL Studio control.
- Upload Brainstorm to correct RL Studio stage.
- Run AutoQC.
- Address or document every diagnostic.
- Rerun AutoQC after edits.
- Mark diagnostics reviewed.

Outputs:

- AutoQC-cleared Brainstorm submission

Done criteria:

- Valid AutoQC items resolved.
- Diagnostics marked reviewed.
- Submitted for Human Brainstorm Review.

Do-not-cross boundary:

- Do not proceed to World Spec until Brainstorm Human Review gives GO.

## Pass 7: Brainstorm Reviewer Revisions

Goal: Incorporate human reviewer feedback until Brainstorm is approved.

Inputs:

- RL Studio reviewer comments
- Brainstorm draft

Actions:

- Capture feedback in `worlds/james-carter/reviewer-feedback.md`.
- Clarify feedback if needed.
- Revise locally.
- Re-upload and rerun AutoQC.
- Resubmit.

Outputs:

- Approved Brainstorm

Done criteria:

- Human Review signs off with GO.

Do-not-cross boundary:

- Do not begin World Spec before GO.

## Pass 8: World Spec Interview

Goal: Extract physician-originated decisions for the full World Spec.

Inputs:

- Approved Brainstorm
- World Spec checklist
- Alexander's clinical decisions

Actions:

- Walk through Clinical Scenario, Task Specifications, World File Plan, and World Summary.
- Design tasks before files.
- Confirm task independence and world snapshot.
- Identify source-of-truth hierarchies and key milestones.

Outputs:

- Raw World Spec decision set
- Missing clinical detail list

Done criteria:

- Enough physician-originated material exists for a structured spec draft.

Do-not-cross boundary:

- Do not let AI invent task prompts, traps, or clinical anchors.

## Pass 9: World Spec Draft

Goal: Build a structured World Spec draft from Alexander's decisions.

Inputs:

- Pass 8 interview notes
- Official World Spec template
- Approved Brainstorm

Actions:

- Prepare Claude-ready official input when recommended.
- Use Claude for structure and document volume, not clinical origination.
- Bring output back into local workspace.

Outputs:

- Draft `worlds/james-carter/world-spec.md`

Done criteria:

- Four canonical World Spec sections are present.
- Draft preserves physician intent.

Do-not-cross boundary:

- Do not produce synthetic files.
- Do not create golden responses or grader guidelines.

## Pass 10: World Spec Audit

Goal: Stress-test the World Spec before upload.

Inputs:

- World Spec draft
- World Spec checklist
- Reviewer failure patterns

Actions:

- Audit for self-containment, consistency, timeline, file plan integrity, trap fidelity, and realism.
- Confirm tasks are independent and anchored after world snapshot.
- Confirm files are designed after tasks.

Outputs:

- Audit findings
- Revision list
- Physician decisions needed

Done criteria:

- Alexander approves upload-ready World Spec.

Do-not-cross boundary:

- Do not upload before physician approval.

## Pass 11: World Spec RL Studio Upload And AutoQC

Goal: Upload World Spec and clear AutoQC.

Inputs:

- Physician-approved World Spec
- RL Studio access

Actions:

- Ask before browser/RL Studio control.
- Upload World Spec.
- Run World Spec AutoQC.
- Address or document every diagnostic.
- Rerun AutoQC after edits.
- Mark diagnostics reviewed.
- Submit for Human World Spec Review.

Outputs:

- AutoQC-cleared World Spec submission

Done criteria:

- Valid AutoQC items resolved.
- Submitted for Human World Spec Review.

Do-not-cross boundary:

- Do not move into synthetic generation.

## Pass 12: World Spec Reviewer Revisions

Goal: Incorporate human reviewer feedback until World Spec is approved.

Inputs:

- RL Studio reviewer comments
- World Spec draft

Actions:

- Capture feedback locally.
- Revise with Alexander's clinical approval.
- Use Claude for structure/consistency if useful.
- Re-upload and rerun AutoQC.
- Resubmit.

Outputs:

- Approved World Spec

Done criteria:

- Step 6 Human World Spec Review signs off.

Do-not-cross boundary:

- Do not proceed to Steps 7-17.

## Pass 13: Onboarding Completion

Goal: Record Step 6 approval and stop at the onboarding boundary.

Inputs:

- World Spec approval
- Project status

Actions:

- Update `project/STATUS.md`.
- Record completion and remaining boundaries.
- Wait for explicit phase update before downstream work.

Outputs:

- Onboarding completion status

Done criteria:

- Step 6 approval recorded.
- No downstream work begins without approval.

Do-not-cross boundary:

- No synthetic generation, production task setup, golden responses, grader guidelines, failure analysis, preference labeling, or agent evaluation.

