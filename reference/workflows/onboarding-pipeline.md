# Onboarding Pipeline

Source indexed: `reference/source/_superseded/instruction-doc/New Writers Version - Instruction Guide (05_24).md`

This workflow captures the original onboarding scope and operational gates. It is preserved as historical/source-derived workflow guidance. For Korvin's live phase after onboarding, use `project/STATUS.md`, `project/PHASE_MAP.md`, `docs/status-dashboard.md`, and `docs/world-pipeline-playbook.md`.

## Historical Onboarding Boundary

Onboarding includes Steps 1-6 only.

1. Brainstorm
2. Brainstorm AutoQC
3. Human Review: Brainstorm
4. World Spec Document
5. World Spec AutoQC
6. Human Review: World Spec

Onboarding ends after Step 6 approval.

For Korvin, approval occurred and later steps proceeded under explicit authorization. For any new world, do not continue to Steps 7-17 until explicitly approved by project leadership and the project phase is updated.

## Phase Boundaries

Phase 1: Plan Your World
- Steps 1-6.
- Design a realistic clinical scenario and document the spec.
- This is the only current onboarding scope.

Phase 2: Build Your Files and Tasks
- Steps 7-11.
- Engineering generates synthetic files from approved spec and reference templates.
- Writer reviews files and writes tasks in RLS.
- Veteran writer scope only.

Phase 3: QA Your Tasks
- Steps 12-13.
- Task AutoQC and trajectory/grading audit.
- Veteran writer scope only.

Phase 4: Evaluate the Agent
- Steps 14-17.
- Failure analysis, preference labeling, AutoQC, final review.
- Veteran writer scope only.

## Brainstorm Workflow

1. Draft a Brainstorm concept pitch with the four required sections.
2. Upload the Brainstorm document in RL Studio.
3. Run Brainstorm AutoQC.
4. Review every AutoQC item.
5. Fix valid feedback, re-upload, and rerun AutoQC.
6. Document any disagreement with AutoQC findings.
7. Mark diagnostics reviewed.
8. Submit for Human Brainstorm Review.
9. If Needs Fixes, address reviewer feedback in RLS, rerun AutoQC, and resubmit.
10. Do not proceed to World Spec until Human Review signs off with GO.

## World Spec Workflow

1. Start only after Brainstorm approval.
2. Draft the World Spec using the canonical sections.
3. During onboarding, focus on the spec document only unless instructed otherwise.
4. Upload the World Spec in RL Studio.
5. Run World Spec AutoQC.
6. Address every valid AutoQC item.
7. Re-upload and rerun AutoQC until clean or until disagreements are documented.
8. Mark diagnostics reviewed.
9. Submit for Human World Spec Review.
10. If Needs Fixes, address both current spec feedback and any unresolved planning-stage feedback, rerun AutoQC, and resubmit.
11. On Step 6 approval, onboarding is complete.

## AutoQC Expectations

- AutoQC is required at every stage.
- No deliverable moves forward until AutoQC findings are resolved or documented as false positives.
- Treat AutoQC as a trigger for focused attention, not a skim step.
- Rerun AutoQC after edits.
- Keep official feedback and resolution inside RL Studio.

## Reviewer Expectations

- Human review is binary at Brainstorm: GO or SEND BACK.
- Reviewers assess conceptual viability at Brainstorm, not full spec quality.
- Reviewers assess buildability, consistency, self-containment, realism, and task architecture at World Spec.
- Reviewer feedback must be incorporated before moving forward.
- Use Slack for quick clarification, but RL Studio is the official feedback record.

## AI Usage Rules

- AI may assist with brainstorming, boilerplate, drafting templates, structure, consistency checking, and critique.
- AI does not replace physician judgment.
- The physician expert owns all submitted work.
- The physician expert must double-check and validate AI-assisted output.
- Task prompts, golden responses, and grader guidelines are 100% human-written.
- AI may QC human-written task prompts, golden responses, or grader guidelines after they exist, but may not write them from scratch.
