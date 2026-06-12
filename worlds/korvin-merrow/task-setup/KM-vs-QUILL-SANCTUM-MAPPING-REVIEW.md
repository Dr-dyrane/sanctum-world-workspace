# Korvin Merrow vs Quill - Sanctum Criterion Mapping Review

Date: 2026-06-11. Purpose: use the client's latest-guidance worked example (David B's `Healthcare_Hyperammonemia_Quill`, shared by King P 6/10 as reflecting current guidance) as a concrete map of what "good" looks like per Sanctum dimension, and grade Korvin Merrow (KM) against it. Goal: understand where KM satisfies the criteria, where it fell short, and what reviewer corrections to expect so we are ready before they arrive.

How to read this. Quill is ONE approved instance, not the rubric itself. The rubric is the instruction document (phases + AutoQC Sections 1-6) plus the standing reviewer rulings (Abi fairness + variety + FA/GA; Sang grader structure/length; Larry task count). Quill shows the latest-guidance INSTANTIATION of those, so it is the most useful single yardstick we have. Quill sources: `reference/templates/` (Brainstorm, WorldSpec, Task prompt, Golden, Grader, FA_GA, Preferential Labeling) + its README. KM sources: this folder's `KM-WORLD-PERFORMANCE-REPORT.md`, `KM-RETROSPECTIVE-tasks1-2.md`, the `taskN/TASKN-STATE.md` cockpits, and `docs/{task-difficulty-lessons,task-structure-dossier,grader-guidelines-lessons,clinical-voice-lessons}.md`.

Verdict key: MET (at or above standard) | PARTIAL (meets intent, with a real gap) | GAP-CORRECTED (failed, then fixed + codified) | GAP-OPEN (unresolved risk) | WATCH (format divergence from latest guidance, not yet a defect).

---

## 0. The two worlds at a glance

| | Korvin Merrow | Quill |
|---|---|---|
| Patient / axis | 62M, common-disease MIXED physiology (sepsis + steroid + CKD/HF + polypharmacy + functional decline); theme "medically improving but operationally dangerous" | 26M, RARE single-axis physiology (gut-liver-brain ammonia); "no single data point explains the crisis" |
| Snapshot / arc | 6-day admission, world close HD6 05/23, discharge 05/24 | floor-ICU-floor admission, world close 02/20 09:00, discharge to rehab |
| Tasks | 10 (target raised to 10 by Larry 6/10) | 9 (1 over the 5-8 guideline) |
| Structure spread | completion-heavy (8 of 10 are forced-inventory or draft-and-finalize); coding + CDI added late for variety | ~8 distinct structures chosen at brainstorm |
| Sequencing | world/substrate built FIRST, structures chosen after | tasks designed first, then files ("Each essential file exists because a task needs it") |
| Files | 26 world + 7 task (held back) | 15 world + 6 task + 2 supplementary (23, ~91% essential) |
| Difficulty proven | deep floors banked (KM02 59, KM05 36, KM06 60, KM09 31, KM10 ~25) | CDI floors 0.28 (one task observed) |

Headline: KM and Quill both satisfy the core Sanctum design intent (complexity from interaction, not rare-disease recall - note Quill achieves it WITH a rare disease, KM with common ones; both are valid, the criterion is interaction). KM's depth-of-difficulty is at least as strong as the exemplar. KM's shortfalls are concentrated in three places, all traceable to ONE root cause: KM chose its tasks AFTER fixing the world, the opposite of Quill's order.

---

## 1. World-level mapping

| # | Sanctum criterion (per Quill + instruction doc) | KM performance | Verdict | Anticipated correction |
|---|---|---|---|---|
| A1 | Coherent scenario with a unifying physiology and plausible-but-wrong single-cause alternatives | KM has a coherent MIXED-physiology world, well-reasoned, but more diffuse than Quill's single elegant axis. Realism is strong. | MET | None expected. Quill shows a tighter axis is possible but KM's diffuse realism is on-spec ("realistic hospital complexity"). |
| A2 | Friction points (people/perspective conflicts), central + secondary, each anchored to specific notes | KM friction matrix is strong: cardiology vs nephrology, endo vs primary, family vs team, all chart-anchored. | MET | None. |
| A3 | Trap taxonomy: world-level + task-level, VARIED trap types, each locked to a source file | KM has 5 trap families + a coverage matrix, but they cluster on the source-of-truth / fabricated-fact family. The suite finding: chart-COACHED traps (#1 prednisone, #3 functional, #4 sepsis-anchoring) do NOT discriminate (the model finds them for free). Quill carries more TYPE variety (temporal, SDOH, duplication, differential-reasoning, missing-info) and locks each trap to a date + a Section 3 doc. | PARTIAL | A reviewer comparing trap TYPE diversity may note KM leans on one mechanism family. Not a defect (the family produces our deepest fair floors), but a variety observation. |
| A4 | File ecosystem: tasks-then-files, essential ratio high, world/task/supplementary separated with a litmus test | KM: 26 world + 7 task held back correctly; clean separation. BUT files were built from the world before tasks were finalized (sequencing inversion). | MET (hygiene) / see B1 for the sequencing fault | None on hygiene. |
| A5 | Clinical voice / realism of generated chart files | KM's pipeline-generated files are our gold standard (the `docs/clinical-voice-lessons.md` corpus). At or above Quill. | MET (exemplary) | None. This is a strength to protect. |
| A6 | Temporal: world snapshot fixed; every task anchor strictly post-snapshot; nothing future-dated; no pre-snapshot late-entry | KM FAILED this repeatedly: KM07 v1 golden future-dated 06/23 (banned); KM08 v3/v4 anchored pre-snapshot (HD1 05/18, HD5 05/22). Caught in review/audit and fixed. Quill nails it explicitly (world ends 09:00, tasks start 09:30). | GAP-CORRECTED | Low residual now, but this is a recurring miss class - any new task is a re-offense risk. Keep the anchor audit as a hard gate. |
| A7 | Self-containment (no post-July-2025 knowledge required, or attached) | KM clean (standard inpatient medicine). | MET | None. |

---

## 2. Task-slate mapping

| # | Sanctum criterion | KM performance | Verdict | Anticipated correction |
|---|---|---|---|---|
| B1 | Structural variety: >=5 distinct structures; completion/draft-and-finalize capped at 1-2 | KM's BIGGEST GAP. 8 of 10 tasks reduce to forced-inventory (KM01) or completion (KM02-06, KM08, KM07 v2). Abi named this verbatim: "future tasks not all follow the same structure of draft and finalize... we want variety, not monotony, this is also an ask of the client." KM09 (coding) + KM10 (CDI) were added late to diversify. Root cause: world built first, structures retrofitted (`docs/task-structure-dossier.md` section 1). Quill chose ~8 structures at brainstorm. | GAP-PARTIALLY-CORRECTED | HIGH exposure if the slate is judged as a whole. Expect a variety note. Prep: the structure dossier already maps the 8 structures + sheet candidates for World #2; for KM, KM09/KM10 are the variety answer and should be foregrounded. |
| B2 | Each task maps to an approved tracker workflow + priority | KM tasks map to verbatim workflow strings (the workflow-string-at-top-of-RUN-INSTRUCTIONS rule). | MET | None (after the KM08 wrong-string catch was fixed). |
| B3 | Tasks independent (no task needs another's output) | KM tasks are independent encounters off one shared chart. | MET | None. |
| B4 | Per-task forcing function + real difficulty (cold/forced/chart-contradicted) | KM is STRONG here: deep fair floors across KM02/05/06/09/10. Arguably deeper than the single Quill data point. | MET (strength) | None. |
| B5 | Fairness of construction: no false claim planted in the model's own draft with no instruction to correct it; a reachable catch | KM FAILED 3x - KM05, KM06, KM07 v2 - all on the planted-claim-without-instruction pattern Abi retired. All corrected (re-attribute / placeholder-synthesize); now codified in `docs/task-difficulty-lessons.md` sections 5-6 + AGENTS.md THE LAW. Quill's CDI is fair by genre (an external query is rebuttable). | GAP-CORRECTED | The single costliest pattern in rounds. Low residual now that it is gated, but every reseed must pass the fairness gate first. |
| B6 | No-moderate difficulty bar: >=1 sub-90 run on a genuine clinical failure | KM meets it on every task (KM01 floor through KM10). | MET | None. |

---

## 3. Per-task deliverable-chain mapping

| # | Sanctum criterion | KM performance | Verdict | Anticipated correction |
|---|---|---|---|---|
| C1 | Prompt: short, first-person, in-role, no enumerated constraints / no telegraph | KM prompts are short in-role (Sang trimmed KM04's trailing how-to; KM07/KM10 minimal). Matches Quill's one-sentence prompt exactly. | MET | None. Good precedent for our `undisclosed_constraints` QA rebuttals. |
| C2 | Golden: physician voice, committed dispositions, chart chrome (header/demographics/date/signature), reachable ceiling | KM goldens reach this after Task 1 round 2 + Sang (chart register, document chrome). | MET | None, except where the ceiling is unproven (KM10, see C-fair below). |
| C3 | Grader: fixed structure, ~1 page, chart-aware where the deliverable is synthesized, credit-correct-restraint, fabrication test | KM uses the Sang FIVE-BLOCK (Preamble / Register Note / A / B / C) at ~1 page, chart-aware where needed. KM07 v3 proved the chart-aware need but was retired as unfair; carry the grader lesson, not the banking verdict. Quill uses DIFFERENT LABELS (Deliverable / Register note / Non-Negotiables / Scope and Legitimate Variation / Common Failure Modes) with identical philosophy. | MET (ours passes live AutoQC) / WATCH | If the client standardizes on the Quill labels, expect a relabel request. Our five-block is the AutoQC-passing structure; do not pre-emptively switch (see reference/templates/README). |
| C4 | FA/GA format | KM uses Abi's 6/9 FAILURE-ONLY + no-section-names. Quill uses the OLDER both-sides format (notes what the model/grader did well). | WATCH (pod divergence) | If the client pushes the Quill both-sides format, our FA/GA may get a note. We are correctly following our pod lead (Abi); flag the divergence rather than silently switching. Do NOT copy Quill's both-sides shape into a KM FA/GA. |
| C5 | Preference Labeling: 3 per task, compare A vs B against the golden, justify the deciding difference | KM does 3 PLs/task (Abi 6/7) on the seven-section A4-B4 format. Quill shows a single A-vs-B on a 6-axis A+ scale. | MET (ours follows the pod rule) / WATCH | Format-label divergence only; our cadence (3/task) exceeds the single example. |
| C6 | QA / AutoQC discipline: substantive tech-issue rebuttals, descriptive EnvLinter annotations, world/task file separation | KM has the 6/11 tech-issue correction (no bare "tech issue"), descriptive annotations, correct world/task holdback. | MET | None. |

---

## 4. Where we failed - ranked, honest

1. STRUCTURAL VARIETY (B1) - the deepest and most exposed. The KM slate is completion-monotony because the world was fixed before the structures were chosen; difficulty then had only one lever (the completion wrapper). Abi flagged it; KM09/KM10 are the partial answer. This is a SLATE-level fault, visible whenever the ten tasks are read together. Root cause, not a per-task slip.

2. FAIRNESS OF CONSTRUCTION (B5) - the costliest in review rounds. Three reseeds (KM05/06/07 v2) on the same pattern: a false claim planted in the model's own draft with no instruction to correct it. Corrected and now codified, but it is the pattern that cost the most rework and the one a reviewer is most primed to re-check.

3. TEMPORAL ANCHORING (A6) - the most recurrent mechanical miss. Future-dated golden (KM07 v1), pre-snapshot anchors (KM08 v3/v4). Each was caught and fixed, but it recurred enough to be a discipline gap, not a one-off. Quill's snapshot rigor is the model to copy.

4. SEQUENCING (the meta-root of 1 and partly 3) - KM built the world, then retrofitted tasks; Quill designed tasks, then built files for them. Already captured as the World #2 pre-brainstorm gate (`docs/task-structure-dossier.md`, `docs/world-pipeline-playbook.md` B0). Nothing to fix in KM; everything to carry into World #2.

5. KM10 REACHABILITY (B5/C-fair, OPEN) - the one unresolved item. KM10 piloted all-floor with no catcher; fairness-of-spread is unproven. Quill's CDI golden is the proof-of-reachability model (it affirms what the chart supports and declines what it does not). See section 5.

6. FORMAT DIVERGENCE FROM LATEST GUIDANCE (C3/C4/C5, WATCH) - grader labels, FA/GA both-sides vs failure-only, PL axis labels. NOT failures (KM follows its own pod's standing rules), but exposure points if the client standardizes on the Quill formats. Manage by flagging the divergence, not by silently adopting.

---

## 5. KM10 vs Quill CDI - the directly comparable task (head-to-head)

These are the two CDI tasks, and the comparison is the sharpest single lesson, but they are NOT the same structure:
- Quill Task 3 = CDI query GENERATION: "go through the chart and draft any queries that are warranted." Forced-inventory-flavored; the golden produces three compliant, non-leading queries and DECLINES to over-query settled documentation (no ascites-off-diuretics query, no fourth query on a settled mood screen). Floors at 0.28 when a model omits required queries or manufactures an unsupported one.
- KM10 = CDI query RESPONSE: an external CDI specialist has asked to add metabolic encephalopathy; the deliverable agrees or pushes back. S3 ratify-or-refute. Floors when the model affirms an undocumented diagnosis under administrative pressure.

What KM10 can borrow from the Quill exemplar:
- THE REACHABLE ANSWER SHAPE. Quill's golden is the template for a passing CDI response: affirm what the record supports, decline what it does not, each with a record citation and a "clinically undetermined / insufficient documentation" out. KM10's catcher should look exactly like this - affirm the legitimately supported items while declining the unsupported encephalopathy add. If no agent produced that in 10 runs, the task is too hard or the decline path is not reachable; resolve before banking (the open flag).
- THE FAIRNESS FRAME. Both are fair by genre (a CDI query/request is supposed to be answerable with a decline), so neither needs a planted-claim fix. KM10's `undisclosed_constraints` rebuttal is on solid ground: the required stance (decline the unsupported add) is disclosed by the contemporaneous record, exactly as Quill's golden declines what the chart cannot support.
- THE GRADER. Quill's CDI grader credits the correct WITHHOLD explicitly ("declining to over-query settled documentation is correct, not incomplete"). KM10's grader must carry the same credit-the-decline pattern, or a correct restrained response gets under-scored. KM07 v3 taught the same symmetry rule on grading but not on fairness; v3's task construction remains retired.

Net: KM10 is structurally sound and fair; its OPEN risk is purely reachability-of-the-catch. The Quill golden is the concrete proof-of-reachability to build the KM10 catcher (or the golden-scores-high structural check) against before banking.

---

## 6. Anticipated corrections queue + readiness (pending Alexander authorization for any change)

| Likely correction | Trigger | Readiness today | Prep move (not yet authorized) |
|---|---|---|---|
| "Slate lacks structural variety" | reviewer reads the 10 tasks together | KM09 (coding) + KM10 (CDI) already diversify; structure dossier documents the spread | Foreground KM09/KM10 as the variety answer; have the S1-S8 map ready to show deliberate coverage |
| "Re-check fairness on any reseed" | any task sent back | fairness doctrine codified; KM05/06/07 fixes on record | Run the fairness gate (sections 5-6) before any rebuild; never add a reconcile clause to chase difficulty |
| "Anchor/date error" | new or revised task | anchor audit is a hard gate in TASK-RUNBOOK | State in-world today in one line and sweep all artifacts on every framing change |
| "KM10 has no catcher / unfair gotcha" | KM10 review | reachability is the known open flag | Build/verify a catcher against the Quill golden shape, or prove the golden scores ~0.85-0.95 under its own grader, before banking |
| "Grader/FA-GA/PL format differs from the new example" | client standardizes on Quill formats | our formats pass live AutoQC and follow Abi/Sang | Flag the divergence explicitly; switch only if the live gate or a reviewer requires it (reference/templates/README records the deltas) |
| "Catch-ceiling too low / partial-credit unreproducible" | KM07 v4 or KM10 review | KM07 v3 partial-credit notes are historical only; KM10 still needs v2 reachability proof | For KM07, use v4 pilot evidence only. For KM10, prove a catcher or high golden self-score before banking. |

---

## 7. Where we matched or exceeded the exemplar (protect these)

- Clinical voice (A5): KM's pipeline chart files are our gold standard; the `clinical-voice-lessons.md` corpus is reference-grade and at least at Quill's level.
- Difficulty depth (B4): KM has more proven deep fair floors than the single Quill data point; the cold-axis / forced-slot mechanism is well understood and reproducible.
- File hygiene + world/task separation (A4, C6): clean 26+7 holdback, single MRN/FIN, no collisions.
- Self-containment (A7): clean.
- The lessons + cockpit infrastructure: KM's per-task STATE cockpits, retrospectives, performance report, and the docs/ lesson set are more developed than a single delivered world needs - that infrastructure is why this mapping was even possible.

Bottom line: KM satisfies the Sanctum criteria on realism, clinical voice, difficulty, fairness (after correction), and hygiene. Its real, reviewer-visible shortfall is STRUCTURAL VARIETY at the slate level, with TEMPORAL ANCHORING and FAIRNESS as the two recurring correction classes (both now gated), and KM10 REACHABILITY as the one open item. All four trace to the single root cause Quill avoided by designing tasks before files - which is exactly the lesson already banked for World #2.
