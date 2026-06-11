# Reviewer Response Protocol

This is the STANDING protocol for processing any reviewer decision (Brainstorm, World Spec, or per-task human review). It is not a status file - for current status read `dashboard/km-world-dashboard.html`, `task-setup/KM-WORLD-PERFORMANCE-REPORT.md`, and the active `TASKN-STATE.md`. (Korvin Merrow is long past Brainstorm/Spec GO; the world is live and all 10 tasks have piloted. The GO/SEND-BACK workflows below apply identically at the per-task review stage.)

## GO Workflow

When reviewer returns `GO`:

1. Capture the GO decision in `worlds/korvin-merrow/reviews/reviewer-feedback.md` or a dated file under `worlds/korvin-merrow/reviews/`.
2. Update `WORKSPACE_FILE_MAP.md (root; Active task status section)`.
3. Commit a checkpoint.
4. Move to World Spec Section 1 physician interview only after Alexander authorizes.
5. Use the official World Spec template and preparation packet.
6. Do not draft final task prompts without Alexander's own wording.

## SEND BACK Workflow

When reviewer returns `SEND BACK` or `Needs Fixes`:

1. Save the full reviewer feedback exactly.
2. Do not edit clinical content immediately.
3. Classify each item using the categories below.
4. Identify which feedback is required, optional, unclear, or potentially conflicting with physician intent.
5. Ask Alexander for clinical decisions before making any clinical change.
6. Apply only approved fixes.
7. Regenerate submission artifact if needed using the official template.
8. Re-run AutoQC if required.
9. Resubmit in RL Studio only after Alexander approval.

## Feedback Classification System

- `Required structural`: template, formatting, section, or upload requirement.
- `Required clinical`: patient logic, safety, realism, or contradiction issue.
- `Required AutoQC`: automated check that is valid and should be corrected.
- `Clarification needed`: feedback is ambiguous or cannot be implemented safely without reviewer/Alexander clarification.
- `Physician judgment conflict`: reviewer suggestion may weaken clinical realism or contradict Alexander's intended reasoning.
- `Optional polish`: improves clarity but is not required for approval.
- `Out of scope`: asks for work beyond the current phase.

## Source-Of-Truth Conflict Handling

Priority order:

1. Official Sanctum source guide and templates.
2. RL Studio reviewer decision and AutoQC requirements.
3. Alexander's physician judgment for clinical content.
4. Approved Brainstorm.
5. Claude/Codex suggestions.

If two sources conflict:

- Do not silently choose.
- Document the conflict.
- Ask Alexander to decide clinical issues.
- Ask reviewer/Slack only when official workflow ambiguity remains.

## Grader Guidelines: structure and length

When a task's grader guidelines come back from review, see `docs/grader-guidelines-lessons.md`. Two standing rules from the Trigeminus pod (Sang):

1. Structure is fixed: Preamble, Register Note, Section A (must be present and correct), Section B (acceptable variation, with the verbatim two-failure-mode clause), Section C (patterns to reason about, opening verbatim, central planted failure first, plus a credit-correct-restraint pattern). Preamble names the golden file verbatim.
2. Length is capped at about one page (1.25 max), body ratio ~A 40 / B 20 / C 40. Inside the structure, compress to signal: Section C patterns are "watch for X + one-line why," never a review document with inline file walkthroughs. The grader is guidance, not a case file.

Related: the physician prompt stays a short first-person in-role instruction; meta-guidance about how to do the task belongs in the grader, not the prompt.

## Resubmission Process

Before resubmission:

- [ ] Feedback saved locally.
- [ ] Fix list mapped to reviewer items.
- [ ] Clinical changes approved by Alexander.
- [ ] Official template preserved.
- [ ] AutoQC rerun if required.
- [ ] `WORKSPACE_FILE_MAP.md (root; Active task status section)` updated.
- [ ] Checkpoint commit created.
- [ ] No phase boundary crossed.

After resubmission:

- [ ] Record RL Studio status.
- [ ] Record timestamp and task ID.
- [ ] Save AutoQC output if rerun.
- [ ] Wait for next reviewer decision.


## ABI UPDATE 2026-06-09 - EnvLinter / Taiga QA annotations must be descriptive
EnvLinter (Taiga QA) thumbs-down annotations must EXPLAIN THE ACTUAL RATIONALE for thumbing down - the substantive reason the flag is wrong, or the concrete cause if it is a tech issue. Do NOT write "Rahul/reviewer said it's okay" or otherwise appeal to a reviewer's say-so as the justification. (These annotations are client-visible; they must stand on their own reasoning.) Pairs with the FA/GA failure-only + no-section-names update in docs/grader-guidelines-lessons.md.

## TECH-ISSUE QA DISPOSITION - the 6/11 correction (KM07)
The bare words "tech issue" / "known issue" / "N/A" now FAIL the Taiga QA Feedback review as dismissive deflection - it does not engage the finding's substance. A tech-issue disagree needs a SUBSTANTIVE, fact-referenced rebuttal in BOTH the annotation box and the dismissal box: state the concrete cause and cite evidence the grader actually ran. Worked example for the recurring `enable_anthropic_api=False` false positive: "The grader did not fail or fall through. The model grader executed normally on the trajectory pilot (job <ID>) and returned valid per-run scores across all ten runs (<range>); enable_anthropic_api=False is a static configuration-preflight signal that does not reflect the actual grading run, which empirically contradicts the predicted cannot-call-the-model failure." This supersedes the older two-field "exactly tech issue" rule (KM03-era). See AGENTS.md guardrail 4 and TASK-RUNBOOK section D step 4.
