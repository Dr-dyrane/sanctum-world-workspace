# Workspace Guardrails - Hard-Won Lessons (Korvin Merrow Execution Phase)

Date: 2026-06-04, extended 2026-06-14 (Ondina spec-review, pod-guidance, and task-mount lessons, guardrails 14-17). Standing guardrails distilled from real failures during World Spec / artifact generation. Every rule here was paid for. Collaborators (Claude, Codex, writers) must follow these. AGENTS.md should reference this file.

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

## 12. Mojibake awareness and dash discipline
**Struggle:** Text moved between tools (docx XML, JSON escapes like ·, markdown mirrors, clipboard, cp1252-default editors) risks mojibake (a middle-dot becoming "A-circumflex + dot", quotes becoming "a-circumflex-euro" sequences, U+FFFD replacement chars) that survives every structural check and only surfaces on human read. Em/en dashes are banned in SPEC-pipeline artifacts (spec, transcript, uploads) per AutoQC; generated WORLD files natively use them, so blanket dash-stripping there would create style inconsistency instead of fixing one.
**Rules:** (a) All file I/O explicit UTF-8; never round-trip docx text through default-encoding shells or editors. (b) After any edit batch, run a mojibake scan over ALL containers (paragraphs + table cells) for the marker set: A-circumflex, a-circumflex-euro sequences, accented-letter pairs, U+FFFD. (c) Dash policy is artifact-scoped: spec/transcript/notes/uploads to the spec pipeline = zero em/en dashes (use hyphen, comma, "then"); world files = match the file's native register and NEVER introduce a dash style the surrounding text doesn't already use; new insertions are checked with a dash census before save. (d) Text pasted from chat or web is normalized (straight quotes, ASCII hyphens) before entering any artifact.

## 13. Date discipline across framing changes
**Struggle:** KM02's golden shipped dated 05/23/2026 into the escalation task whose in-world today is 05/24/2026. The date was correct under the superseded clean-pilot framing and nobody re-checked it when the framing changed; the first human reviewer caught it. Dates are the easiest staleness to miss because every artifact carries them in multiple places (header line, identity-band Date cell, body mentions, filename stamps, README records) and they all "look right" in isolation.
**Rules:** (a) Pin the in-world today in one explicit line derived from the LIVE prompt before building or editing any task artifact. (b) Date audit covers ALL date locations in ALL artifacts of the task, not just the file under edit. (c) Any framing change (clean to escalation, prompt rewrite, reseed, anchor shift) resets verification: rerun the full date audit on every surviving artifact before upload. (d) Superseded prompts/artifacts move to hold/ with a SUPERSEDED name so the stale framing cannot be grabbed by mistake. Cross-refs: AGENTS.md guardrail 5, docs/reasoning-discipline.md FRAMING-CHANGE RE-AUDIT, TASK-RUNBOOK DATE AUDIT item.

## 14. The workflow menu and pod guidance are live and volatile
**Struggle:** Ondina's spec passed QC, then a pod update retired four of its ten workflows from the platform menu (discharge med rec, CDI query, specialist referral letter, patient safety event). We had also been leaning on a four-day-old snapshot of the Task Selection Categories sheet whose priorities had already drifted.
**Rules:** Keep ONE canonical workflow map (build_task_packages.py WORKFLOW) and name the workflow in every RUN-INSTRUCTIONS (KM "## Workflow type:" header + "Workflow type =" upload step 1). Verify each workflow against the LIVE Task Selection Categories sheet right before Step 10, never a snapshot. Workflow is a Step-10 selection and spec-to-task divergence is legitimate, so remap retired workflows at tasking; do not re-upload an approved or in-review spec for a change deferrable to Step 10. Keep retired-workflow designs (do not delete; may reopen). Park each deferred change at the layer that locks it: world content at generation, workflow/prompt/golden at tasking.

## 15. Three date rules, and the knowledge cutoff is not the calendar
**Struggle:** A pod "no future-dated" rule plus a "shift to pre-July-2025" nudge created confusion about whether compliant 2026 dates needed changing, even though the spec had already passed live QC and a prior review confirmed after-close anchoring.
**Rules:** Treat three date concepts as independent: after-world-close (internal ordering), no-future-vs-today (HARD, QC-blocked), pre-July-2025 (SOFT preference). The July-2025 cutoff governs the model's CLINICAL KNOWLEDGE, not encounter dates; 2026 dates are fine if no post-cutoff guideline is required, so do not reflexively redo compliant dates. While multilingual tasking is paused, all world and task files are English; a patient's language preference is an English-rendered profile attribute, not foreign-language file content.
**Prompt firewall:** In task prompts, constrain the source universe to the attached chart and any attached policy/reference files. Avoid "latest guidelines," "current standards," "most recent FDA approvals," named post-July-2025 specifications, or "current HEDIS rules" unless that exact source is attached and the workflow realistically includes it. If the chart or attached reference does not support a finding, date, value, criterion, or recommendation, the prompt should license leaving it open rather than filling it from general knowledge.

## 16. The spec doc and transcripts are sources the gate does not scan
**Struggle:** A ratified-value change (attending rename, baseline ambulation) propagated to clinical_data.py, the built world files, and the goldens, but not to the spec markdown - a separate hand-maintained source - and Spec AutoQC caught the cross-section contradiction. verify_ondina scans world/task/golden docx only.
**Rules:** On ANY ratified-value change, sweep EVERY source for the old value: the spec md/docx, the transcripts, and planning docs, not just clinical_data and the builders. Spec file table follows the KM 7-column format (no Source/Tool, a Date column, origin tagged with the four-option convention plus filename), with wide tables in a landscape section; files already engineered are tagged Writer produced so engineering does not regenerate them.

## 17. Task-file mount hygiene outranks filename-only duplicate checks
**Struggle:** OV01 job `9765ba91` looked like a world-file leak, but the actual failure was two task files mounted together: the stale old order set under `/docs/filesystem` and the new renamed order set under `/docs/.apps_data/calendar`. Because the filenames differed, duplicate-name AutoQC did not catch the same-purpose duplicate. The dirty run was invalid until Alexander deleted the old task file and re-added the current one as a plain Filesystem file.
**Rules:** Before banking any pilot, read the first trajectory's `find /docs` tree. Exactly one intended task file should appear under `/docs/filesystem`; no task-specific file should appear under `/docs/.apps_data`; no stale old filename should remain. If any item fails, delete every file from the Studio Task Files card, re-add only the current file, save, refresh, and rerun. Do not prescribe world-file fixes until the layer is proven.

## 18. Reviewer-facing graders cannot expose platform implementation fields
**Struggle:** Larry E returned OV01 because the grader Register Note included implementation wording instead of plain clinical instructions. The clinical instruction was sound, but the wording looked like accidental system language in reviewer-facing guidelines. The same review also caught that FA/GA prose can be pasted while the wrong trajectory is selected, which binds the analysis to the wrong run.
**Rules:** In grader guidelines, say the clinical thing plainly: check specific doses, dates, labs, organisms, and names against the provided chart and task file before calling them invented. Do not name platform configuration fields. Before entering FA/GA, select the intended trajectory in Studio, then verify the visible or downloaded output for that same run. If the selected run has no visible output, write the failure around the missing deliverable or the visible transcript for that run, never around a different trajectory.
