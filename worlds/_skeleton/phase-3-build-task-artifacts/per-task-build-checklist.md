# Phase 3 - Per-task build checklist (golden, grader, prompt, task files)

One pass per task, after its substrate is armed (Phase 2). Templates: `reference/templates/` (Golden Response, Grader Guidelines, Task prompt, FA_GA). Full build gates: `task-setup/TASK-RUNBOOK.md` (gates A0.4 design-time and A0.5 against built bytes), `docs/grader-guidelines-lessons.md`, `docs/clinical-voice-lessons.md`, `docs/docx-generation-method.md`.

## Authorship boundary (non-negotiable)

Prompt, golden, and grader are WRITER-authored (the physician owns the clinical content and dispositions). Claude's role is de-hinting, format translation, build hygiene, and review. Do not let the model write the determinations.

## Prompt

- [ ] Writer-authored, first-person, a plain clinical ask. No reconcile-and-correct clause unless the trap specifically needs one (it usually does not, and it kills propagation difficulty).
- [ ] No pointer that telegraphs the scored item; de-hint without deleting the cue that makes the task fair.
- [ ] References only files that are actually mounted; anything it calls "attached" must be uploaded and saved.

## Golden

- [ ] Terse chart register; committed first-person dispositions; numbered to mirror the deliverable.
- [ ] Realistic header, demographics, date, allergies, signature block where the genre calls for a clinical note or memo.
- [ ] Placeholders over fabrication ("[No documented baseline weight available]").
- [ ] No meta-commentary paragraph reviewing its own reasoning.
- [ ] Scores full marks under its own grader (self-score check); if any trajectory beats it, improve the golden first.

## Grader (Sang five-block)

- [ ] Preamble names the golden file by its exact uploaded filename.
- [ ] Register Note (chart-aware: include_input_files=true whenever the deliverable is built from the chart; say true chart and photo detail is credited, not flagged invented).
- [ ] Section A: must be present and correct (the non-negotiables), self-contained wording.
- [ ] Section B: acceptable variation, including the verbatim two-failure-mode clause; self-contained wording.
- [ ] Section C: patterns to reason about, central failure first, plus a credit-correct-restraint line; self-contained wording.
- [ ] No numeric weights, score caps, pass bands, or A/B/C classification labels (these trip AutoQC). Where a missed finding should cap the score, state it as a band ceiling in prose.
- [ ] Mechanism-agnostic: score output against the golden and guidelines; do not litigate grader mechanism.

## Task docx build (Mode A)

- [ ] Clone a proven approved artifact; styles.xml byte-identical; never a blank Document() or generator script (re-injects the synthetic footer).
- [ ] Scrub core metadata (author, last_modified_by, title empty); fingerprint-diff to zero against the base.
- [ ] Scan ALL xml parts for banned characters (em dash, en dash, arrow, bullet, asterisk, bracket), including footers; render to PNG and view.
- [ ] New names checked for collisions across the 26+ world files.

## A0.5 fairness gate (against the BUILT bytes, by a non-builder)

- [ ] Extract the built draft/input bytes and QUOTE its verbatim lines about the scored item (if absent, state "none").
- [ ] Confirm: same-author draft is a true placeholder, OR the adversarial input is a different-author wrong-by-genre document. Looking routine is asserting; a status disclaimer does not un-assert; a pre-written order is an assertion to countersign.
- [ ] Inspect the agent-visible filesystem: exactly the intended task files under /docs/filesystem, no /docs/.apps_data duplicate, no meta-answer filename (clean, fixed, reviewer, v_clean).

Next: `phase-4-pilot-review-submit/gates-and-templates.md`.
