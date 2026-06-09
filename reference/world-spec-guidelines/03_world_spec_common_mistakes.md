# World Spec Common Mistakes

## Source-Of-Truth Rule

These are operational failure patterns extracted from the source guide and should be checked before drafting, before Claude use, and before upload.

## Structure Mistakes

- Changing the official World Spec template structure.
- Changing section numbers, headings, column names, IDs, or naming conventions.
- Following example specs when they conflict with the official template.
- Treating the World Spec as multiple disconnected documents rather than one single source of truth.

## Timeline Mistakes

- Letting dates float outside the Key Milestones table.
- Referencing a task, trap, file, or prompt date that is not in Key Milestones.
- Anchoring tasks inside the world timeline rather than after the world snapshot.
- Creating a task that depends on another task's output.
- Treating task order as one shared future timeline instead of independent branch encounters.

## Task Mistakes

- Allowing Claude or Codex to write final task prompts from scratch.
- Writing task prompts like test questions rather than real clinical requests.
- Hinting in the task prompt that a trap exists.
- Fusing multiple deliverables into one task.
- Using a workflow not present in the approved task tracker.
- Creating vague expected outputs that graders cannot score consistently.

## File Plan Mistakes

- Designing files before tasks.
- Creating a file because it is realistic noise when it actually carries answer-changing content.
- Marking a file supplementary even though removing it would change a correct answer.
- Letting a single file fully resolve a task.
- Omitting file source or template/reference origin.
- Inconsistent filename dates versus Key Milestones.
- Confusing final synthetic filenames with reference/template filenames.

## Trap Mistakes

- Mixing traps and frictions.
- Making traps artificial instead of arising naturally from clinical workflow.
- Depending on rare disease recognition rather than chart synthesis.
- Letting one changed date, dose, or fact break a trap.
- Creating a source-of-truth trap without a discoverable source hierarchy or reconciliation path.

## Claude Mistakes

- Letting Claude move too quickly or produce everything at once.
- Accepting Claude-invented clinical facts, templates, or file content.
- Letting Claude use em dashes, en dashes, arrows, or AI-sounding phrasing.
- Treating Claude's draft as authoritative over physician judgment.

