# Project Sanctum Onboarding Execution Checklist

Source of truth: `reference/New Writers Version - Instruction Guide (05_24).md`

Current onboarding scope: Steps 1-6 only.

## Setup Verification

- [ ] Confirm workspace structure exists
  - Platform: Local workspace
  - Expected output: `reference/`, `project/`, and `worlds/james-carter/` folders exist
  - Stop condition: Required folders or source guide are missing
  - Reviewer: Alexander

- [ ] Confirm official instruction guide is locally indexed
  - Platform: Local workspace
  - Expected output: Operational checklists and workflow notes exist under `reference/checklists/` and `reference/workflows/`
  - Stop condition: Source-of-truth guidance has not been read or indexed
  - Reviewer: Alexander

- [ ] Confirm active project status
  - Platform: Local workspace
  - Expected output: `project/STATUS.md` reflects current pass, blocker, and next action
  - Stop condition: Current pass is unclear
  - Reviewer: Alexander

- [ ] Confirm phase boundary
  - Platform: Local workspace
  - Expected output: Work is limited to Brainstorm through Human World Spec Review
  - Stop condition: Any work would enter synthetic generation, production task setup, golden responses, grader guidelines, or failure analysis
  - Reviewer: Alexander

## Brainstorm Creation

- [ ] Run Brainstorm clinical interview
  - Platform: Local workspace, conversation
  - Expected output: Physician-originated answers for World Setup, Major Friction Points, Major Traps, and Rough Task Ideas
  - Stop condition: Core clinical decisions are missing or AI is originating scenario/traps/task ideas
  - Reviewer: Alexander

- [ ] Identify official Brainstorm template/format
  - Platform: Local workspace and official guide
  - Expected output: Brainstorm uses the four required sections and remains a concept pitch
  - Stop condition: Draft expands into file inventory, full timeline, task prompts, golden responses, or grader work
  - Reviewer: Codex, then Alexander

- [ ] Prepare Claude-ready Brainstorm input
  - Platform: Local workspace, Claude
  - Expected output: Paste-ready input containing Alexander's clinical decisions and official Brainstorm structure
  - Stop condition: Claude is being asked to invent the scenario, traps, or task ideas
  - Reviewer: Alexander before Claude use

- [ ] Run official Claude Brainstorm drafting/check pass
  - Platform: Claude
  - Expected output: Claude-organized Brainstorm draft or critique based only on Alexander's provided clinical design
  - Stop condition: Claude introduces new clinical facts, traps, or tasks not approved by Alexander
  - Reviewer: Alexander and Codex

- [ ] Audit Claude Brainstorm output
  - Platform: Local workspace
  - Expected output: Findings against Alexander's original intent, Brainstorm checklist, and realism standards
  - Stop condition: Draft is generic, inaccurate, too zebra-driven, or not self-contained
  - Reviewer: Codex, then Alexander

- [ ] Finalize Brainstorm draft
  - Platform: Local workspace
  - Expected output: `worlds/james-carter/brainstorm.md` contains final physician-approved Brainstorm content
  - Stop condition: Alexander has not approved final language
  - Reviewer: Alexander

## Brainstorm AutoQC

- [ ] Upload Brainstorm to RL Studio
  - Platform: RL Studio
  - Expected output: Brainstorm document uploaded to the correct World Building task
  - Stop condition: Browser/RL Studio access not authorized by Alexander
  - Reviewer: Alexander

- [ ] Run Brainstorm AutoQC
  - Platform: RL Studio
  - Expected output: AutoQC diagnostics generated
  - Stop condition: AutoQC not run or diagnostics unavailable
  - Reviewer: RL Studio AutoQC, then Alexander/Codex

- [ ] Resolve Brainstorm AutoQC items
  - Platform: RL Studio and local workspace
  - Expected output: Valid feedback incorporated; false positives documented with reasoning
  - Stop condition: Any unresolved valid AutoQC item remains
  - Reviewer: Alexander; RL Studio AutoQC on rerun

- [ ] Mark diagnostics reviewed
  - Platform: RL Studio
  - Expected output: Brainstorm diagnostics marked reviewed before human review submission
  - Stop condition: Diagnostics have not been addressed or documented
  - Reviewer: Alexander

## Brainstorm Human Review

- [ ] Submit Brainstorm for Human Review
  - Platform: RL Studio, Slack as needed
  - Expected output: Task status moves to Ready for Plan Review
  - Stop condition: AutoQC has not been resolved or marked reviewed
  - Reviewer: Pod lead, peer reviewer, or assigned reviewer

- [ ] Wait for Brainstorm review decision
  - Platform: RL Studio
  - Expected output: GO/Approved or Needs Fixes/Send Back
  - Stop condition: No reviewer decision yet
  - Reviewer: Pod lead, peer reviewer, or assigned reviewer

## Brainstorm Revisions

- [ ] Review Brainstorm feedback
  - Platform: RL Studio, Slack only for clarification
  - Expected output: Reviewer comments captured in `worlds/james-carter/reviewer-feedback.md`
  - Stop condition: Feedback is unclear and needs reviewer clarification
  - Reviewer: Alexander and Codex

- [ ] Revise Brainstorm
  - Platform: Local workspace, Claude if useful for structure/checking
  - Expected output: Revised Brainstorm preserving Alexander's clinical intent
  - Stop condition: Revision would alter clinical concept without Alexander approval
  - Reviewer: Alexander

- [ ] Re-upload and rerun Brainstorm AutoQC after revisions
  - Platform: RL Studio
  - Expected output: Updated diagnostics cleared or disagreements documented
  - Stop condition: AutoQC not rerun
  - Reviewer: RL Studio AutoQC, then human reviewer

- [ ] Obtain Brainstorm GO
  - Platform: RL Studio
  - Expected output: Human review signs off with GO/Approved
  - Stop condition: No GO; do not proceed to World Spec
  - Reviewer: Pod lead, peer reviewer, or assigned reviewer

## World Spec Drafting

- [ ] Confirm Brainstorm approval
  - Platform: RL Studio and local status
  - Expected output: `project/STATUS.md` reflects Brainstorm approval
  - Stop condition: Brainstorm does not have GO
  - Reviewer: Alexander

- [ ] Identify official World Spec template/format
  - Platform: Official guide, local workflow notes, Claude prompt starter
  - Expected output: Spec uses Clinical Scenario, Task Specifications, World File Plan, and World Summary
  - Stop condition: Template is unavailable or structure is unclear
  - Reviewer: Codex, then Alexander

- [ ] Run World Spec interview
  - Platform: Local workspace, conversation
  - Expected output: Physician-originated decisions for clinical scenario, task architecture, file needs, and summary
  - Stop condition: Clinical decisions are missing or AI is inventing scenario/traps/tasks
  - Reviewer: Alexander

- [ ] Prepare Claude-ready World Spec input
  - Platform: Local workspace, Claude
  - Expected output: Paste-ready official prompt and Alexander's approved Brainstorm/decisions
  - Stop condition: Prompt asks Claude to invent task prompts, traps, or scenario concept
  - Reviewer: Alexander before Claude use

- [ ] Run Claude World Spec drafting support
  - Platform: Claude
  - Expected output: Structured World Spec draft assistance based on Alexander's inputs
  - Stop condition: Claude invents unsupported clinical facts, task prompts, traps, or source material
  - Reviewer: Alexander and Codex

- [ ] Audit World Spec draft
  - Platform: Local workspace
  - Expected output: Findings against physician intent, World Spec checklist, self-containment, realism, and consistency
  - Stop condition: Required sections incomplete or facts inconsistent
  - Reviewer: Codex, then Alexander

- [ ] Final physician review of World Spec
  - Platform: Local workspace
  - Expected output: Physician-approved World Spec ready for RL Studio
  - Stop condition: Alexander has not approved content
  - Reviewer: Alexander

## World Spec AutoQC

- [ ] Upload World Spec to RL Studio
  - Platform: RL Studio
  - Expected output: World Spec uploaded to approved Brainstorm task/stage
  - Stop condition: Browser/RL Studio access not authorized by Alexander
  - Reviewer: Alexander

- [ ] Run World Spec AutoQC
  - Platform: RL Studio
  - Expected output: Spec-stage AutoQC diagnostics generated
  - Stop condition: AutoQC not run
  - Reviewer: RL Studio AutoQC, then Alexander/Codex

- [ ] Resolve World Spec AutoQC items
  - Platform: RL Studio and local workspace
  - Expected output: Valid feedback incorporated; false positives documented
  - Stop condition: Any valid AutoQC item remains unresolved
  - Reviewer: Alexander; RL Studio AutoQC on rerun

- [ ] Mark diagnostics reviewed
  - Platform: RL Studio
  - Expected output: Diagnostics marked reviewed before human review submission
  - Stop condition: Diagnostics have not been addressed or documented
  - Reviewer: Alexander

## World Spec Human Review

- [ ] Submit World Spec for Human Review
  - Platform: RL Studio, Slack as needed
  - Expected output: Task status moves to Ready for Spec Review
  - Stop condition: World Spec AutoQC has not been resolved
  - Reviewer: Pod lead, peer reviewer, or assigned reviewer

- [ ] Wait for World Spec review decision
  - Platform: RL Studio
  - Expected output: Approved or Needs Fixes
  - Stop condition: No reviewer decision yet
  - Reviewer: Pod lead, peer reviewer, or assigned reviewer

## World Spec Revisions

- [ ] Review World Spec feedback
  - Platform: RL Studio, Slack only for clarification
  - Expected output: Feedback captured in `worlds/james-carter/reviewer-feedback.md`
  - Stop condition: Feedback is unclear and needs reviewer clarification
  - Reviewer: Alexander and Codex

- [ ] Revise World Spec
  - Platform: Local workspace, Claude if useful for structure/checking
  - Expected output: Revised World Spec preserving physician intent
  - Stop condition: Revision would change clinical concept without Alexander approval
  - Reviewer: Alexander

- [ ] Re-upload and rerun World Spec AutoQC
  - Platform: RL Studio
  - Expected output: Updated diagnostics cleared or disagreements documented
  - Stop condition: AutoQC not rerun
  - Reviewer: RL Studio AutoQC, then human reviewer

- [ ] Obtain World Spec approval
  - Platform: RL Studio
  - Expected output: Step 6 Human World Spec Review signs off
  - Stop condition: No Step 6 approval
  - Reviewer: Pod lead, peer reviewer, or assigned reviewer

## Onboarding Completion

- [ ] Record onboarding completion
  - Platform: Local workspace
  - Expected output: `project/STATUS.md` updated to World Spec approved/onboarding complete
  - Stop condition: Step 6 approval not received
  - Reviewer: Alexander

- [ ] Stop at onboarding boundary
  - Platform: Local workspace
  - Expected output: No work begins on synthetic file generation, production task setup, golden responses, grader guidelines, or failure analysis
  - Stop condition: Alexander explicitly updates project phase after approval
  - Reviewer: Alexander

