# DO NOT REPEAT - the cold-start mistakes ledger

Read this FIRST, cold, before any task or world work. It is the concentrated list of every mistake Korvin Merrow actually made, each written as a rule so it cannot be re-made by someone starting fresh. If you do nothing else, do not re-do these. Each line: the mistake, where it bit, then FIX. Deeper detail is in the linked docs.

How to use it: before building anything, state three relevant lines from this ledger as your "no-repeat receipt" (AGENTS.md guardrail 8). If you cannot, you have not read in yet.

Last updated: 2026-06-12. Sources distilled here: `docs/task-difficulty-lessons.md`, `docs/task-structure-dossier.md`, `docs/grader-guidelines-lessons.md`, `docs/clinical-voice-lessons.md`, `docs/reviewer-response-protocol.md`, `docs/git-workflow.md`, `TASK-RUNBOOK.md`, `reference/source/Raising_Task_Difficulty_Worked_Example.pdf`, and the `KM-vs-QUILL-SANCTUM-MAPPING-REVIEW.md`. KM08 AO first review added the bright-line draft-fairness wording; the Raising Task Difficulty worked example added the answer-key / noise / off-text signal gate; King P's 6/12 note added the legitimate-failure-over-raw-score gate. None of these are new mistakes; they are the ones we already paid for.

---

## 1. Sequencing and scope (the root cause of most of the rest)

- Built the world/chart FIRST and chose task structures AFTER, so difficulty had only the completion wrapper left and 8 of 10 tasks became the same shape (Abi: "monotony"). FIX: pick 5+ distinct structures at brainstorm, THEN build substrate to arm each; cap completion/draft-and-finalize at 1-2 per world. (`docs/task-structure-dossier.md`)
- Brainstormed traps apart from the task surfaces that force them. FIX: before any new internal medicine Brainstorm, fill `reference/workflows/internal-medicine-world-planning-canvas.md` so each task has a structure, forced slot, trap, source route, fairness route, grader mode, and reachability plan before the patient documents are imagined.
- Designed files before the tasks needed them. FIX: design tasks first; each essential file exists because a task needs it for a correct answer (the Quill order).
- Left an answer-key synthesis in shared world files, so the model only had to transcribe the conclusion (Raising Task Difficulty worked example). FIX: world files provide raw material; completed synthesis belongs out of the shared world layer unless every task legitimately needs it. If one task needs it, scope it as a task-level file and explain why the user lacks it.
- Planned against the old 15-20 world-file range after the 06/10 update. FIX: new worlds need at least 30 world-level files; task-level files are separate and do not count toward that minimum.
- Tried to ship a too-easy task as "moderate" (KM03 v1/v2.1 ~93-94; KM05 early). FIX: no moderate tasks. Every task needs >=1 genuine sub-90 failure, or redesign and re-pilot. Do not relabel "too easy" as "moderate."
- Overanchored on the percentage instead of the trajectory content. FIX: a task banks on at least one legitimate model failure that materially lowers deliverable quality or creates patient-harm or malpractice risk, not on the raw score alone. A high score can still contain a bankable failure; a low score is useless if the only issue is cosmetic.

## 2. Fairness of construction (Abi retired three tasks for this; the costliest pattern)

- Planted a false claim in the model's OWN draft with no instruction to correct it, then floored the model for propagating it (KM05, KM06, KM07 v2, KM08 v4.1). FIX, canonical AO 6/11 rule: before turning in any finalize-the-draft task, either prompt the model to correct errors in the draft or use placeholders in the draft for the model to complete in the finalized version. Prefer placeholders when preserving difficulty. (`docs/task-difficulty-lessons.md` sections 5-6)
- Treated re-attribution as a universal draft fix. FIX: re-attribution works for external or weak-source documents, not for a same-author started draft the prompt asks the model to finalize. Same-author draft traps need true placeholders or an explicit correct-errors instruction.
- Added a reconcile-and-correct clause to a propagation task and killed the difficulty (KM06 v4 went to ~0.98 all-catch). FIX: reserve the reconcile clause for genuine judgment traps; never add it (or stance hints to the prompt) to chase a clean board.
- Re-attributed a claim but added an "unverified" caveat, telegraphing the catch. FIX: attribution only; no caveat, or you hand the model the answer.
- Treated an all-floor spread as automatically bankable. FIX: if the clinical stance is contestable, prove the catch is reachable with a catcher run or the golden scoring ~0.85-0.95 under its own grader. If the trajectory shows a legitimate external-query failure and the correct answer is structurally reachable, bank on the real failure rather than the mean.
- Answered a CDI or external query by declining on PROCEDURAL grounds ("a diagnosis cannot be added after discharge") instead of CLINICAL grounds, restated the absence of a diagnosis without explaining why, and built the decline on ancillary observations (nursing, OT) rather than the treating physician's own documented assessment (KM10 v1, reseeded by Abi 6/11). FIX: a CDI query is answered post-discharge by design, so the integrity-correct answer engages the indicators and explains WHY the record does not support the diagnosis, in the treating clinician's voice anchored on the treating note. Write the golden and FA as a reasoned clinical determination, not a bare "symptoms only, decline."
- Called a rebuilt task fair by reviewing the DESIGN PLAN'S description of the draft instead of the built artifact; the plan said "placeholder" while the built draft listed the trap item under "Current medications" beside an explicit held list (KM07 v3, caught by Abi 6/11; the v3 "fix" re-planted the v2 lie quietly). FIX: fairness review runs against the built draft's extracted bytes and QUOTES its verbatim lines about the scored item; runbook gate A0.5; reviewing a plan is not reviewing a task.
- De-telegraphed a draft by making the trap item "look as routine as the others," which is the same act as asserting it (KM07 v3 current-meds listing; KM08 v4.1 pre-written uptitration order surviving the de-telegraph pass). FIX: a true placeholder asserts NOTHING about the trap item anywhere in the draft; looking routine = asserting; a status disclaimer does not un-assert membership; a pre-written plan order is an assertion.
- Cleared the rest of the queue by memory after one task failed a fairness class, instead of re-running the test on every sibling construction (KM07 post-mortem cleared KM10 by genre but never re-checked KM08, whose built draft pre-writes the scored gabapentin order with a finalize-only prompt). FIX: when a construction class fails once, run the gate on the built bytes of every staged or in-review sibling the same day; findings to taskN/qa/.
- Treated a duplicate mounted-file leak as a filename problem when the real problem was an extra Studio volume (KM07 v4 job 6b687360: main `/docs/filesystem` draft plus unexpected `/docs/.apps_data/calendar` draft disagreed on alendronate; KM10 v2 job 138e90a2 confirmed the same calendar-volume defect with the CDI query memo). FIX: fairness review includes the agent-visible filesystem after upload: `find /docs -type f`, `/docs/filesystem`, `.apps_data`, filenames, duplicate preloaded volumes, and any file whose name says clean/fixed/revised/reviewer. Exactly one task file may be visible, under the intended filesystem volume. If `.apps_data/calendar` contains a task file, delete that Studio volume; do not rename around it.

## 3. Difficulty (these make a task too easy and get it bounced)

- Put the plant on the WARM/headline axis the model is already hunting (KM06 orthostatic 93, echo 97; KM03 v1 restart 94; KM07 v1 from-scratch 93.8). FIX: cold/background axis only; the deliverable's own subject is warm by default.
- Used a from-scratch synthesis or an unambiguous determination with no forced move (KM07 v1; KM08 v3 inpatient-vs-obs 96 because the case was not borderline). FIX: a task floors only with a forced slot (a required disposition the schema forces); design determinations genuinely borderline or do not use the structure.
- Planted on something the chart is merely SILENT about, not something it CONTRADICTS (KM05 v4-pilot1 floored every run but unfairly). FIX: floor only on a claim the record contradicts or explicitly mandates.
- Used a +N-day interval claim the chart cannot reach (KM05 v2). FIX: a post-chart claim is propagated or declined for free; put the forced judgment inside the same encounter the chart governs.
- Gave the model one clean prose path to every non-negotiable. FIX: force reconciliation across multiple raw sources, add realistic task-level noise or a required template, and consider an off-text critical signal such as a photo or handwritten list when clinically realistic. If the central miss would be indefensible in care, the grader must make it a hard error.
- Counted cosmetic or nonclinical misses as difficulty. FIX: missing a logo, minor formatting, or polish does not count as a legitimate failure. The failure has to be clinical, safety-relevant, coding or documentation integrity relevant, or otherwise material to the deliverable.

## 4. Temporal anchors (the most recurrent mechanical miss)

- Future-dated the golden (KM07 v1 golden dated 06/23). BANNED, non-negotiable. FIX: pin in-world today from the live prompt; nothing future-dated, ever.
- Anchored a task pre-snapshot / as a late-entry note (KM08 v3 HD1 05/18, v4 HD5 05/22). The pipeline does NOT catch this; only human review does. FIX: every encounter AND deliverable strictly after the world snapshot.
- Let a framing change leave surviving artifacts unverified (KM02 shipped a 05/23 golden into a 05/24 escalation). FIX: on ANY framing change (clean->escalation, reseed, date/mechanism shift) re-audit EVERY surviving artifact's dates, voice, status fields, and the grader's chart-access setting. "It passed under the old framing" is not verification. (AGENTS.md guardrail 5)

## 5. Build / DOCX (mechanical, each cost a round)

- Verified world facts against the markdown / .meta convenience copies instead of the agent-read docx (recurred in KM01 and KM02). FIX: verify on the agent-read docx at `file-review/upload/filesystem/` with python-docx INCLUDING table cells - the layer the model actually reads.
- Built a task docx from a blank `Document()` or from `generate_reference_files.py`, causing fingerprint drift and a re-injected "Synthetic training document" footer (KM01; KM08 v1). FIX: Mode A clone a proven approved artifact, styles.xml byte-identical, scrub core metadata, fingerprint-diff to zero.
- Scanned only document.xml for banned tokens and missed the footer string in footer1.xml (KM02, KM08). FIX: scan ALL xml parts; RENDER and visually view every docx before staging.
- Left an em/en-dash, arrow, bracket, or asterisk in a task docx. FIX: zero banned characters in authored content; swap chrome em-dashes to hyphens.
- Trusted a truncated sandbox read or an interrupted write (KM02 builder; the 6/10 mass truncation). FIX: integrity-gate after every save (EOCD + styles.xml + opens) and confirm the last section is present.

## 6. Grader

- Ran a golden-only grader on a SYNTHESIS task, so it flagged true chart detail as fabrication and turned the spread into noise (KM07 v3: identical behavior scored 0.30 vs 0.70). FIX: chart-aware grader (include_input_files=true) whenever the deliverable is built from the chart; golden-only only for a planted-artifact catch. (`docs/grader-guidelines-lessons.md` Lesson 3)
- Wrote the grader in the instruction-doc A/B/C format and tripped the AutoQC gate (KM01). FIX: the Sang five-block - Preamble (names the golden file verbatim) / Register Note / Section A / Section B (with the verbatim two-failure-mode clause) / Section C (verbatim "patterns to reason about" opener, central failure first, plus a credit-correct-restraint pattern). ~1 page, no numeric weights / score caps / pass bands.
- Let the grader penalize something the golden itself does, or dock a correct withhold. FIX: never penalize what the golden does; explicitly credit keeping the trap item open/unverified.
- Let prompt/golden/grader quality vary while testing the trap (Sang: "the whole frame matters"). FIX: build all four surfaces to standard before reading a pilot, or the spread does not reflect the trap.

## 7. FA / GA / PL / QA annotations

- Wrote FA/GA in the both-sides format and named "Section A/B/C" (pre-Abi 6/9). FIX: failure-only (what the model did poorly / what the grader did poorly); spell out the section's content, never its name; single lowest run; each part under ~1000 chars.
- Wrote FA around the lowest score when the score did not represent the real failure. FIX: read the output and grading transcript first. FA needs a defensible clinical or material deliverable failure; if the lowest run is cosmetic but another trajectory carries the real miss, escalate and document the selection rationale before writing.
- Used the bare words "tech issue" / "known issue" / "N/A" on a QA flag - failed as dismissive deflection (KM07 6/11). FIX: substantive, fact-referenced rebuttal in both boxes, citing that the grader actually ran (job id + per-run scores).
- Justified a QA thumbs-down with "the reviewer said it's okay." FIX: annotations are client-visible and must stand on their own reasoning.
- Drafted PL without the actual A/B pair, or skipped the cadence. FIX: three PLs per task from KM03 on, each on a different trajectory, against the golden; run PL AutoQC after each.

## 8. Process / hygiene / git

- Re-piloted without a locked preregistration (KM07 v3), forcing a post-hoc reconciliation. FIX: lock the prereg (forecast + read rules) BEFORE every pilot; never edit it after.
- Put .py files or loose planning .md at task-folder roots. FIX: scripts in `tools/`; planning in `design/`/`runs/`/`fa-ga/`; uploadable sets only in `platform/taskN/current/`.
- Told the user git was impossible when `rm`/commit failed with "Operation not permitted." FIX: the sandbox is create/overwrite-only until you call `mcp__cowork__allow_cowork_file_delete`; once approved, full git works (`docs/git-workflow.md`).
- Ran `git add -A` and swept unrelated working-tree changes (an in-progress dashboard rewrite) into an unrelated commit (KM10 v2, 6/11). FIX: stage the specific paths you actually changed (`git add path1 path2 ...`), never `-A`, so someone else's WIP is not bundled under the wrong commit message. Run `git status` first and look at what is modified before staging.
- Wrote a rule in instance-shape right after one error, so its siblings re-bit (the markdown/docx, framing-date, and template misses each fixed only their own case). FIX: write every rule at the CLASS it belongs to, not the single instance.

---

The meta-lesson behind all of these: none was a one-off slip. Each was a class of error we now have a gate for. The point of this file is that the gate travels with the repo, so a cold start inherits the scar tissue without paying for it again.

## Canonical docx template rule (added 2026-06-12, paid for twice)
- Built a project docx OUTSIDE the one canonical Epic renderer: the world files first pass used a gray/black approximation, and the OV01 golden v1 was hand-built as a plain Table-Grid note. Both diverged from the KM Epic template and had to be rebuilt. FIX, now a CANONICAL RULE: every docx in this project - world files, supplementary, task-level files (E1-T*), and task-setup goldens - is rendered through the single Epic template via build_world_files.build_one / epic.py (KM design system: Arial, navy/blue/light-blue, masthead, blue bar, patient storyboard, PATIENT/ENCOUNTER block, blue table headers, clean Ondina running header and footer). KM applies this same chrome to its world AND task-level files, with the issuer named in the title and filing line for external surfaces. NEVER hand-build a docx with a bare Document(); if a new docx type is needed, add a spec and route it through build_one. Verify fills and colors are a subset of the world-file vocabulary before calling any docx done.
