# A4 - Canonical discoverability, consistency, and a next-world starter

Date: 2026-06-18. Scope: READ-ONLY audit. Confirm the canonical standard docs are discoverable from an entry point and self-consistent, then draft the minimal reusable pattern to start a new clinical-eval world cleanly. No existing file was edited, moved, or deleted. This report is the only write.

Files read for this audit: the five canonicals (`docs/fa-ga-canonical.md`, `docs/alexander-voice-dna.md`, `docs/grader-guidelines-lessons.md`, `docs/clinical-voice-lessons.md`, `docs/docx-generation-method.md`), `worlds/ondina-vasquell/OV-FLOOR-MECHANISM-LIBRARY.md`, the CLAUDE.md grounding gate, `AGENTS.md`, the EXP 06_09 instruction doc Step 14 and the FA/GA appendix, and the two skill sources (`reference/skills/failure-grader-analysis/SKILL.md`, `reference/skills/fa-ga-canonical/SKILL.md` plus its `references/worked-examples.md`).

---

## Step 2(a) - Discoverability: is each canonical pointed to from an entry point?

The two entry points are the CLAUDE.md grounding gate (the only file Cowork auto-loads) and `AGENTS.md` (the binding guardrails, which the gate tells Claude to read first). Every doc the task named as a canonical is reachable. The matrix below is mechanical (string match of `docs/<file>` in each entry point).

| Canonical | CLAUDE.md gate | AGENTS.md | Verdict |
|---|---|---|---|
| docs/fa-ga-canonical.md | yes (gate step 2, FA/GA line) | no | Reachable. See note below. |
| docs/alexander-voice-dna.md | yes (gate step 2) | yes (guardrail 12) | Reachable, double-anchored. |
| docs/grader-guidelines-lessons.md | yes (gate step 2) | yes (guardrails 5, 10) | Reachable, double-anchored. |
| docs/clinical-voice-lessons.md | yes (gate step 2) | yes (the clinical-voice paragraph) | Reachable, double-anchored. |
| docs/docx-generation-method.md | yes (gate step 2 and step 3) | yes (guardrail 1, the DOCX paragraph) | Reachable, double-anchored. |
| worlds/ondina-vasquell/OV-FLOOR-MECHANISM-LIBRARY.md | yes (gate step 2, world state) | no | Reachable via the gate. |

All five named canonicals plus the OV floor library are discoverable. No canonical exists that is unreachable from an entry point.

One ASYMMETRY worth flagging, not a dead pointer: `docs/fa-ga-canonical.md` is named in the CLAUDE.md gate but never in `AGENTS.md`. AGENTS.md is the file that calls itself the binding guardrails, and it does carry FA/GA rules inline (guardrail 4 "FA/GA under 1000 chars, two short paragraphs"; guardrail 7 the same). Those inline rules are correct but partial; the locked standard lives only in `docs/fa-ga-canonical.md`, reachable only through the gate. A Codex session that auto-loads AGENTS.md and not the gate gets the length rule but not the locked both-sides GA standard. This is the single discoverability gap. It is a candidate one-line add to AGENTS.md (cross-reference `docs/fa-ga-canonical.md` from guardrail 4 or 12), deferred to Wave 2 since this pass is read-only.

Pointer health: every `docs/...` path named in the gate and in AGENTS.md resolves to a file that exists on disk. The gate's other named docs (`task-difficulty-lessons.md`, `task-structure-dossier.md`, `reasoning-discipline.md`, `anti-hallucination.md`, `red-team-screen-prompt.md`, `WORKFLOW-MAP.md`, `DO-NOT-REPEAT.md`) all resolve. No dead links found among the audited pointers.

Stale-CONTENT pointer (not a dead path): the gate and AGENTS.md both reference `reference/skills/failure-grader-analysis/SKILL.md` indirectly through the FA/GA workflow, and that skill is now the SUPERSEDED one (see 2(b)). The path is live; the artifact it points at is deprecated in favor of `fa-ga-canonical`. The skill's own header says so, so a reader is warned, but the older skill is still installed and triggerable. Treat as a content-staleness flag, not a broken pointer.

## Step 2(b) - Consistency: are the canonicals mutually consistent?

Short answer: yes, with one historical-supersession pattern that is deliberate and well-documented, and no live contradiction between the locked doc and the two skills.

### docs/fa-ga-canonical.md vs docs/alexander-voice-dna.md
Consistent and cross-referenced. The voice DNA explicitly defers to the FA/GA structural canon ("FA/GA: keep failure-only and no-section-names (Abi, 2026-06-09). Alexander voice is HOW the failure is stated"), and the FA/GA canonical defers back to the voice doc for register ("Write the way an attending speaks... see docs/alexander-voice-dna.md"). Both carry the same 2026-06-18 "plain clinical language, not compressed nomenclature" rule with the identical worked example ("only noted that the attending should decide on restart," not "added a decide-restart-versus-hold instruction"). No conflict.

### docs/fa-ga-canonical.md vs the EXP 06_09 FA/GA definition
The locked doc deliberately SUPERSEDES three points of the EXP 06_09 text, and it names each supersession with provenance. This is evolution, not contradiction. Quoting the EXP doc verbatim against the canonical:

1. Lowest vs second-lowest run. EXP 06_09 Step 1: "select the lowest-scoring run. For this QC project you analyze one run only." Canonical: "Bind the FA to ONE run... the SECOND-lowest distinct score (King P, 2026-06-14; supersedes the older lowest run)." Deliberate, attributed override.
2. "What the Agent Got Right" as an FA component. EXP 06_09 Step 14 template lists "What the Agent Got Right (4-6 sentences)" as a required FA block. Canonical: "The FA stays failure-only; no standalone praise paragraph (Ahmad's override of the 06_09 what got right component)." Deliberate, attributed override.
3. GA section-naming. EXP 06_09 is internally tense on its own: its drafting box says the GA covers "What Section A, Section B, and Section C handled correctly," while its writing-standards box says "Do not name Section A, B, or C from your grader guidelines." The canonical resolves the tension cleanly to the stricter reading: "No grader-section names. Do not write Section A/B/C; state the content." Consistent with the EXP standard's own writing-standards box, and it removes the EXP doc's internal ambiguity.

On the GA's core duty the canonical AGREES with and sharpens EXP 06_09. EXP says the GA must cover "Where the grader under-penalized or over-penalized" and "Concrete recommended edits to the grader, including any failure modes that should be added," and "Distinguish grader misses from grader mis-scores." The canonical's mandatory move 2 ("what the grader got wrong or could improve... label a shortfall a MISS or a MIS-SCORE") is exactly this requirement, made non-optional. No contradiction; the canonical enforces what EXP recommends.

### The two skill sources vs docs/fa-ga-canonical.md
Both skills point at the canonical as the supreme authority and do not contradict it.

- `fa-ga-canonical` SKILL.md is the corrected, current skill. Its header: "This is the locked standard, derived from the Project Sanctum instruction document (EXP 06_09, Step 14)... Earlier skill versions encoded an affirm-only GA... That is incomplete and gets sent back." Its mandatory-both-moves rule, its second-lowest-run binding, its gate-trap list (banned credit phrases, no section names, no rating line, no dashes, two paragraphs, sub-1000 chars) all match the doc line for line. Fully consistent.
- `failure-grader-analysis` SKILL.md is the OLDER skill, and it self-identifies as subordinate: "CANONICAL (LOCKED): docs/fa-ga-canonical.md is the single standard... If this guide or any skill-cache template disagrees, the canonical wins." Where it once diverged it has been reconciled; for example it now carries Ahmad's 2026-06-17 grader-audit correction and the both-sides gate trap. No LIVE contradiction with the doc.

The one residual TENSION between the two skills (not with the doc) is which to use. `fa-ga-canonical`'s own description says "This is the corrected, canonical replacement for any older failure-grader-analysis skill; prefer it," and the skill picker lists BOTH as installed and triggerable on nearly identical phrases ("write the FA/GA", "draft the failure analysis"). So both fire on the same request and the writer must know to prefer the newer one. This is a deprecation-not-removed issue, the same one flagged under pointer health in 2(a). It is a discoverability and tidy-up item, not a doctrinal inconsistency: the two skills do not teach conflicting rules, they teach the same rules with one being the leaner corrected version.

### The worked-examples reference vs the canonical
Consistent. `references/worked-examples.md` carries the OV09 held-medication GA as the shape-to-match (grader audit with the improvement move) and explicitly marks the OV04 GA as "the older, simpler clinical register that affirms the score without an explicit improvement move... Prefer the OV09 GA shape." That matches the doc's "an affirm-only GA is incomplete." Note the OV04 GA reproduced there and in the voice DNA worked exemplar is preserved as an approved historical example precisely because it predates the both-sides rule; it is labeled as such in both places, so it does not read as a counter-rule.

### Voice/grader/clinical-voice cross-consistency
`grader-guidelines-lessons.md` and `clinical-voice-lessons.md` both open with a one-line banner deferring prose voice to `alexander-voice-dna.md` and naming `verify_voice.py` as the enforcer. `docx-generation-method.md` section 5 (off-text report images) is mirrored almost verbatim in AGENTS.md guardrail 1, the CLAUDE.md gate step 3, and OV-FLOOR-MECHANISM-LIBRARY.md (the OV09 render method). The four copies agree (author through build_one, soffice to pdf, pdftoppm to png, crop, mount only the image; reserve generative render for true photos/films). No drift between the copies on the method itself.

## Step 2(c) - Duplicated canon with drift between copies

No harmful drift found. The repeated canon is consistent across its copies. Specifics:

- Off-text image render method: stated in `docx-generation-method.md` sec 5 (the canonical long form), and summarized in AGENTS.md guardrail 1, CLAUDE.md gate step 3, and OV-FLOOR-MECHANISM-LIBRARY.md. All four carry the same steps and the same fairness caveat ("why is this report an image"). The summaries correctly point back to the long form. Consistent.
- FA/GA length and shape: the locked rule is in `docs/fa-ga-canonical.md`; AGENTS.md guardrails 4 and 7 each restate "FA/GA under 1000 chars, two short paragraphs." The restatements are a strict subset of the doc and do not contradict it, but they are PARTIAL (length only, not the both-sides GA standard), which is the asymmetry flagged in 2(a). Partial-copy, not drift.
- Alexander voice DNA: the full DNA is duplicated in two places by design - `docs/alexander-voice-dna.md` (the canonical) and the body of CLAUDE.md below the gate (the "Dr. Alexander Voice DNA" block). I compared them: same core identity, same review pattern, same banned-transition list, same final test. The CLAUDE.md copy is the prose-only version and omits the repo-enforcement layer (the effective-date/grandfathering rule and the `verify_voice.py` hook) that the docs copy adds. That is appropriate division (CLAUDE.md teaches the voice, the doc adds enforcement), but it is a genuine two-copy situation to watch: a future edit to the voice standard must touch both or they will drift. Flag for the maintainer, not a current defect.
- Five-block grader structure: defined once in `grader-guidelines-lessons.md` and referenced (not re-copied) from AGENTS.md guardrails 10 and 13(f). No duplication, so no drift. Good.

Net: the canon is single-sourced where it matters, with summaries that point home. The only true two-copy item is the Alexander voice DNA (docs vs CLAUDE.md body), and the two copies currently agree.

---

## Step 3 - NEXT-WORLD STARTER (the minimal reusable pattern)

The goal is to start a new clinical-eval world (call it World N) cleanly, inheriting the Ondina speed and the locked standards, without re-deriving anything. This is the practical short form; the long form lives in `docs/world-factory-playbook.md` (brainstorm-to-spec) and `docs/task-difficulty-lessons.md` plus `OV-FLOOR-MECHANISM-LIBRARY.md` (why a task is hard and fair).

### Recommended directory tree

Mirror the OV layout. Two phase folders plus a small set of living world docs at the world root:

```
worlds/<world-N>/
  00-START-HERE.md                # one-screen orientation + live status pointer
  WORKFLOW-MAP.md                 # the ONE canonical workflow-label map (verify vs live sheet)
  <WORLD>-FLOOR-MECHANISM-LIBRARY.md   # copy OV's, reset the bench ledger to this world
  <WORLD>-WORLD-STATUS.md         # moment-to-moment task state (the live source of truth)
  phase-3-build-task-artifacts/
    build/                        # epic.py + build_world_files.py + build_<worldNN>.py + clinical_data.py + task_data.py + build_goldens.py
    world-files/                  # the >=30 locked world-level chart files
    task-files/  task-context-files/  supplementary-files/  synthetic-files/
    goldens/  grader-guidance/  task-prompts/
    platform/taskN/current/       # the uploadable set per task (prompt, golden, grader, mounted inputs, DESIGN-grounding, prereg, RUN-INSTRUCTIONS)
    platform/taskN/archive/       # superseded sets, dated-reason folders
    platform/_retired/  platform/_paused/
  phase-4-pilot-review-submit/
    results/  fa-ga/  preference-labeling/  recordings/
  archive/  reviews/  submission/
```

Placement rules to carry over (AGENTS.md guardrail 11 / 6): all Python lives in `tools/` or the world's `build/`, never inside a task folder; one uploadable set per task under `platform/taskN/current/`; superseded sets archive with a dated-reason; no loose planning .md at folder roots.

### Canonical docs to carry over (they are world-agnostic; do NOT fork them)

These five plus the playbooks stay in the repo-level `docs/` and serve every world. Do not copy them into the world folder; reference them.

- `docs/fa-ga-canonical.md` - the locked FA/GA standard (both-sides GA, second-lowest run, failure-only FA).
- `docs/alexander-voice-dna.md` - the output-voice standard for all authored text. Enforced by `tools/verify/verify_voice.py`.
- `docs/grader-guidelines-lessons.md` - the five-block grader (Preamble, Register Note, Section A, Section B with the verbatim two-failure-mode clause, Section C with the verbatim opener and the credit-restraint pattern). Partly linted by `verify_ondina.py`.
- `docs/clinical-voice-lessons.md` - the chart-prose standard for world files and goldens (the ten patterns; plus the caveat that trap-carrier sections get the plainest prose).
- `docs/docx-generation-method.md` - the measured DOCX loop and section 5 (off-text image render).
- Playbooks: `docs/world-factory-playbook.md` (the phase spine + the six physician decision gates), `docs/task-difficulty-lessons.md` (PRIMED vs UN-PRIMED, fairness), `DO-NOT-REPEAT.md` (the cold-start mistakes ledger).

World-LEVEL docs that get a fresh copy per world (the OV originals are the template): the floor-mechanism library (reset the bench ledger), the workflow map, START-HERE, and WORLD-STATUS.

### The build-to-deliver flow, in order

Author every artifact through the canonical builder, never a bare `Document()`. The builder is `build_world_files.build_one` (the Epic renderer in `phase-3.../build/epic.py` + `build_world_files.py`), called from a per-world `build_<worldNN>.py`. Goldens go through `build_goldens.py`. Run all three gates before any handoff: `tools/verify/verify_ondina.py`, `tools/verify/presubmit_task_gate.py taskN`, `tools/verify/verify_voice.py`.

1. Brainstorm. Physician originates the scenario, traps, and task ideas (CLAUDE.md: Claude never originates these). Pick the structural variety up front: at least 5 distinct task structures across the world, completion/draft-and-finalize capped at 1-2 (task-structure-dossier). Run Brainstorm AutoQC, then human review.
2. World spec. Assemble the spec via the factory spine. Ratify every clinical value in the substrate pack (decision gate). World needs at least 30 world-level files (AGENTS.md guardrail 6). Run Spec AutoQC, then human spec review.
3. World-file build. Build the >=30 chart files through `build_one`. Author them in the clinical voice at authoring time (clinical-voice-lessons) so generation has less to fix; keep trap-carrier sections in plain prose. Gate each file (DOCX integrity + voice). Upload ONLY world files when RLS asks for world files.
4. Task design - choose a floor mechanism. For each task, pick a mechanism from the floor library. The live engine on this model is an OFF-TEXT FINDING under a plain completion prompt on an UN-PRIMED axis (the chart is silent on its status), fair by construction, never telegraphed. Put the catch on a cold axis; force one wrong move so caution is not free; make the chart contradict the wrong move when inspected; do not add a reconcile clause. Choose the workflow label from the LIVE categories sheet and record it in WORKFLOW-MAP.md and the RUN-INSTRUCTIONS.
5. Deliverable + any subordinate input. Build the started draft or mounted instrument (and any off-text image via the render method, mounting only the image). Frozen-world rule: task-layer artifacts only, never edit locked world files.
6. Golden. Write through `build_goldens.py`, in the committed chart register, terse. The golden is one defensible set, not the only one.
7. Five-block grader. Write per `grader-guidelines-lessons.md`: about one page, A40/B20/C40, chart-aware Register Note when the deliverable is synthesized from the chart, the central planted failure named first in Section C, a credit-restraint pattern, severity tracking clinical stakes. No scoring bands (they trip the live gate). Run `verify_ondina.py` to lint the structure.
8. Plain prompt. Short, first-person, in-role. Set the scene and ask for the deliverable; stop. No meta-guidance, no "reconcile before finalizing," no "use the latest guidelines."
9. Gates. `verify_ondina.py` + `presubmit_task_gate.py taskN` + `verify_voice.py`, all clean. Then a golden self-score under the task's own grader (golden should score high).
10. Pilot. Bench cold first (a cold-bench ceiling is a SCREEN, not a verdict - the harness is harsher; CEILING-ERROR LEDGER). Then run the real harness. TASK MOUNT HYGIENE is a banking gate: inspect the first trajectory's `find /docs` tree, exactly one intended task file under `/docs/filesystem`, no stale same-purpose file. The difficulty gate is mean at or about 70 with several sub-70 runs and a low tail, AND at least one trajectory with a real FA-able clinical failure. A clean bimodal split (floors + catchers) is the ideal evidence.
11. FA/GA via the canonical. Bind to the second-lowest distinct run; pull that run's full output AND its grading transcript. FA failure-only, four components, severity-ordered. GA does both mandatory moves (what the grader got right, what it got wrong or could improve) then calibration. No section names, no rating line in the file (rating goes in the Studio field), no dashes, sub-1000 chars, two paragraphs. Gate with `verify_voice.py` + `presubmit_task_gate.py`. Use the `fa-ga-canonical` skill, not the older `failure-grader-analysis` skill.
12. Preference labels. Three PLs per task from KM03 onward (AGENTS.md guardrail 9), each a different trajectory, A/B in the house seven-section format. Run PL AutoQC after each.
13. Review. Final human review (TL / pod lead / EPM). Nothing uploads, runs, or submits without Alexander's authorization for that exact step.

Keep one active cockpit, one live status source (WORLD-STATUS.md), one workflow map, and clearly separated historical evidence. That is the whole pattern.

---

## Summary of findings

- Discoverability: all five named canonicals plus the OV floor library are reachable from the CLAUDE.md gate; four are double-anchored in AGENTS.md too. No dead pointers among audited paths. One gap: `docs/fa-ga-canonical.md` is reachable only through the gate, not from AGENTS.md, which carries only the partial length rule inline. Candidate one-line cross-reference add (deferred to Wave 2).
- Consistency: the canonicals are mutually consistent. `fa-ga-canonical.md` deliberately and verifiably SUPERSEDES three EXP 06_09 points (second-lowest run, failure-only FA, no section names) with named provenance, and AGREES with EXP on the GA's core audit duty. Both skills subordinate themselves to the doc and carry no live contradiction.
- Duplication/drift: no harmful drift. The off-text image method agrees across its four copies. The only true two-copy item is the Alexander voice DNA (docs vs CLAUDE.md body); the copies currently agree but must be edited together in future.
- Tidy-up flags (read-only pass, no action taken): (1) AGENTS.md does not point to `docs/fa-ga-canonical.md`; (2) the older `failure-grader-analysis` skill is still installed and triggers on the same phrases as the preferred `fa-ga-canonical` skill, a deprecation-not-removed item.
- Next-world starter drafted above: directory tree, carry-over canonicals, and the 13-step build-to-deliver flow.

Report path: `worlds/ondina-vasquell/cleanup-2026-06-18/A4-canonicals-nextworld.md`
