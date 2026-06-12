# 00 - START HERE: internal-medicine world playground

A blank, clone-and-fill launchpad for the next internal-medicine world. Copy this whole `_skeleton/` directory to `worlds/<new-world-name>/` and work the phases in order. Nothing in here is world-specific; fill it in.

## The one rule this playground exists to enforce

Korvin Merrow's costliest mistake, named by Abi and recorded in `docs/task-structure-dossier.md`: the world and chart were built FIRST and the task structures chosen AFTER, so the only difficulty lever left was the completion wrapper, and eight of ten tasks became the same shape ("monotony"). Then the traps had to be retrofitted, which produced the unfair planted-claim floors that Abi retired (KM05, KM06, KM07, KM08).

So the discipline is structural, not a thing you have to remember:

DESIGN THE TASKS AND THEIR TRAPS BEFORE ANY CHART SUBSTRATE EXISTS.

Phase 1 produces 5+ distinct task structures, each with a chosen trap, a passed fairness gate, and a difficulty forecast, with zero chart files written. Only then does Phase 2 build the world substrate to ARM those traps. The directory numbering is the rail: do not create a single clinical file until Phase 1 is signed off.

## The phases (work in order)

1. `phase-1-design-tasks-and-traps/` - no substrate yet. Pick 5+ structures from the S1-S8 menu (1a), choose each one's trap from the trap library (1b), pair and fairness-gate them (1c), and write the per-task architecture plus difficulty forecast (1d). Output: a locked task-and-trap plan.
2. `phase-2-world-spec-and-substrate/` - build the world spec and chart files so each Phase-1 trap is armed by a documented contradiction or mandate. The substrate-arming map (2a) is the bridge: every file exists because a task needs it for a correct answer.
3. `phase-3-build-task-artifacts/` - per task: golden, grader, prompt, any task file. Mode A clone build, mechanical gates.
4. `phase-4-pilot-review-submit/` - locked prereg before each pilot, read rules, FA/GA, three preference labels, Abi-mode review, AutoQC, submission.

## Cold-start receipt (before you touch anything)

Per AGENTS guardrail 8, state three relevant lines from `DO-NOT-REPEAT.md` as your no-repeat receipt. If you cannot, you have not read in yet. The three that bit hardest:

1. Sequencing: pick 5+ distinct structures at brainstorm, then build substrate to arm each; cap completion / draft-and-finalize at 1-2 per world.
2. Fairness: never floor a model for propagating a false claim planted in its own same-author draft with no instruction to correct; use a true placeholder or a different-author wrong-by-genre document instead.
3. Difficulty: floor only on what the chart CONTRADICTS or MANDATES, on a cold background axis, with reachability proven by a live catcher or the golden self-scoring high under its own grader.

## What "imaginative" means here

Brainstorm the clinical world as freely as you like: who is this patient, what is the admission arc, what could plausibly go wrong in the documentation, which specialties collide. The rails are not on imagination, they are on SEQUENCE. Imagine the traps first, then build a world rich and ambiguous enough to make each trap real and fair. A good world is one where every trap is something a careful clinician could get wrong and the chart can rebut.

## Reference map

`REFERENCE-MAP.md` indexes every standing doc, lesson, template, and gate, with what each is for and when to open it.
