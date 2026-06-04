# Workspace Guardrails - Hard-Won Lessons (Korvin Merrow Execution Phase)

Date: 2026-06-04. Standing guardrails distilled from real failures during World Spec / artifact generation. Every rule here was paid for. Collaborators (Claude, Codex, writers) must follow these. AGENTS.md should reference this file.

## 1. Environment split: sandbox view is NOT ground truth
**Struggle:** The Claude sandbox mount repeatedly served truncated copies of real files (AGENTS.md cut mid-word, a 25 KB World Spec DOCX missing its ZIP central directory) while the same files were complete in the real environment. We nearly "restored" healthy files and nearly committed truncated ones.
**Rules:** Verify file health in the real environment before acting on sandbox evidence. Never `git add -A`, bulk-stage, or renormalize from the sandbox. Stage explicit paths only. When sandbox and Codex reports disagree, the real environment wins.

## 2. Git operations belong to the real environment
**Struggle:** Stale `.git/index.lock`/`HEAD.lock` could not be unlinked from the sandbox (EPERM); one commit succeeded but left locks that blocked everything after.
**Rules:** Commits, mv, rm, renormalization run in the real environment (Codex/Alexander). The sandbox creates and overwrites files and documents exact commit messages for later application.

## 3. The mount blocks deletions
**Struggle:** `rm` fails with Operation not permitted even outside `.git`; superseded candidate-review copies could not be removed in-place.
**Rules:** Sandbox workflow is create/overwrite-only. Mark superseded files clearly and list deletions for the real environment.

## 4. DOCX integrity gate is mandatory
**Struggle:** Generated DOCX files were twice found truncated (no end-of-central-directory, missing `styles.xml`/`numbering.xml`) - unopenable in Word, discovered only on review.
**Rules:** After every save: (a) python-docx opens it, (b) `word/styles.xml` and `word/numbering.xml` present, (c) `PK\x05\x06` EOCD present, (d) LibreOffice renders a PDF, (e) eyeball at least page 1. A file that fails any check is not "done," whatever the generator printed.

## 5. No silent invented clinical specificity
**Struggle:** A polished spec build silently filled 7 supportive-medication doses that traced to no physician-approved source - the exact failure mode reviewers punish ("polished output with invented specificity").
**Rules:** No dose, lab value, vital, or numeric clinical fact enters any artifact unless it traces to locked canon or a signed approval-sheet row. Intentional ambiguities (prednisone taper) stay ambiguous. When canon lacks a needed value: propose, flag NEEDS APPROVAL, stop.

## 6. Edit DOCX through the object model, not regex splicing
**Struggle:** A raw-XML regex splice (blank-page fix) produced invalid XML and corrupted the deployed spec. Recovery worked only because a valid copy existed.
**Rules:** Structural edits via python-docx (object model). Raw-XML regex only for value substitutions (colors, sizes), never for moving/inserting block structure. Always keep the last-valid copy until the new file passes the section 4 gate.

## 7. Verify conventions against source, not memory or guesses
**Struggle:** We assumed a "synthesized" label belonged top-right; the guide specifies banners centered top AND bottom. We styled navy before finding the house standard is `#4472C4`; used em dashes the style guide bans; nearly missed that clinical templates default to Courier New.
**Rules:** Before styling/formatting decisions, grep the instruction guide and inspect example packages/screenshots. Record verified conventions in the relevant design doc with the source line.

## 8. Template fidelity is measured, not eyeballed
**Struggle:** A regenerated spec "looked close" but a fingerprint diff exposed 6-7.5 pt text, 138 hard black borders, off-palette fills, and a wrong title treatment.
**Rules:** Compare candidate vs template by extracting and diffing: font sizes (`w:sz`), border colors, shading fills, styles.xml, margins, callout presence. Fix to the template's exact values. Visual render check comes after the numeric diff passes. Template furniture judgment: substantive callouts (Terminology, Self-Containment) stay; authoring-instruction callouts (Optional Sections, Additional Tasks) are removed in a finished spec.

## 9. Drive connector limits and confidentiality
**Struggle:** Binary uploads require base64 through the conversation; the transcript exceeded the per-message ceiling. An internal README was briefly placed in the shared Drive root, exposing process details; deletion required manual action because the connector cannot delete.
**Rules:** Connector use = folder trees, native text docs, search, verification. Binaries move by human drag-and-drop. Nothing internal-facing (manifests, governance notes, approval sheets) goes into shared Drive. Links are Anyone-with-link Viewer at most - never discoverable-public (benchmark contamination risk). Public-link substitution for uploads applies only to genuinely public documents.

## 10. Voice and prohibited-content scans before any "done"
**Struggle:** Benchmark/architecture language ("the world tests", "locked workflows", "this artifact", "submission candidate") repeatedly leaked into final-facing prose.
**Rules:** Scan every final-facing artifact for benchmark/workspace register and prohibited classes (scoring, rubrics, goldens-as-answers). Template-native occurrences (e.g., the Self-Containment box's own wording) are exempt - verify provenance before "fixing" template text.

## 11. Session continuity
**Struggle:** Interruptions mid-generation left half-built artifacts whose state was unclear to the next session.
**Rules:** Maintain a continuation log with per-step status before starting multi-step generation; log completions immediately; every handoff states what changed, what did not, and exact pending commits.
