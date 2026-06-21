---
name: sanctum-task-derivation
description: Derive a new adversarial clinical-documentation eval task end to end for a Project Sanctum world (Ondina Vasquell, Korvin Merrow, Marva Lydell, or a new one), from a faithful chart to a gate-clean, pilot-ready packet with a bimodal prediction and the FA/GA handoff. Use WHENEVER the user wants to derive, design, build, or add an eval task, a floor task, or a bimodal task, even when they only name an axis or drop a clean chart and ask what task it can carry. Triggers include "build a task on the bone-health axis," "design a floor," "derive a review task," "add a tenth task," and "make it bimodal." It bakes in the approved floor engine (primed-versus-un-primed axis, review-and-correct frame, off-text findings, never-telegraph, background-not-headline) and Larry's fairness gates (no note-completion, no planted-false, no universal floor), then walks build, local gates, the bimodal pilot-read, and the FA/GA. Not for an already-piloted run's FA/GA (use fa-ga-canonical), preference labeling, or non-Sanctum work.
---

# Sanctum task derivation (full lifecycle)

Derive a new adversarial eval task from a clean chart to a gate-clean, pilot-ready packet, then read the pilot and hand off the FA/GA. The intellectual work is choosing what floors a strong model fairly; the rest is mechanical and gated. This skill is the operational form of docs/FLOOR-MECHANISM-LIBRARY.md and reference/world-spec-guidelines/POLICY-2026-06-20-deprecated-workflows-and-task-fairness.md. Read those for depth; this is the flow.

## The one principle that unlocked the world
Floors are MANUFACTURED at the task layer on a faithful chart, not found in the world. A clean, internally-consistent chart is the ideal substrate, not a problem to fix. Do not hunt the world for a contradiction it already contains; build the wrong move into the task on top of a chart that reads true. This is the single correction that took Ondina Vasquell from a "one-task world" to ten tasks.

## Phase 0: Pick the axis (un-primed, or the catch never lands)
The model reads a clean chart at or above physician level and reflexively polices what clinicians police. It CEILINGS when the catch sits on an axis it is already scrutinizing, and FLOORS only on an axis where it has no reflex pulling it there.
- UN-PRIMED, use these: a quiet axis the chart is SILENT on the status of (bone-health and CKD mineral-bone disease on a vitamin with no workup note, OSA and CPAP adequacy, immunization or health-maintenance status, self-care competency), or a finding the deliverable does not force the model to open.
- PRIMED, never put the catch here: vitals, patient identity, held-medication restart, the deliverable's own headline problem, anything the chart explicitly flags open or unresolved, and the model's trained reflexes (do not fabricate, do not over-treat, do not restart without labs).
Write one sentence: the axis, and why the chart is silent on its status. If the chart already flags the axis open, pick another one.

## Phase 1: Choose the frame, and clear Larry's fairness gates first
The FRAME decides the distribution shape. Two approved engines:
1. REVIEW-AND-CORRECT (preferred, the reliable fair bimodal). Hand the model a COMPLETE, SIGNED note that carries one realistic, catchable error and ask it to review before sign-off, ready to sign or the correction. Auditing is now the deliverable, so a reviewer who verifies against the chart catches the line and a rubber-stamper misses it. This is the OV08 and OV10-redemption shape (0.10 to 0.95, 0.15 to 0.85). Use it for an over-attestation or an absence catch.
2. OFF-TEXT IMAGE finding under a plain prompt. The catch lives only in an image the model may not open (OV04 CPAP report, OV12 pre-discharge ECG); the unreliable read is the floor. Show raw data, never a printed interpretation. The skip-rate is a Studio-population property, measured at pilot, not at the bench.

HARD GATES (POLICY-2026-06-20, Larry; refuse to proceed if the design fails one):
- NO note-completion. Do not build "finish the started draft" or "complete this note for signature." The discharge-summary completion workflow is deprecated. Use review-and-correct, or full authorship of a non-note deliverable.
- NO planted-false the model is punished for trusting. The scored failure must be a realistic catchable error: a consultant disagreement, an accidental non-adjusted med, an accidental omission, a common mistake in a signed complete note. Never a falsehood planted in the patient's own record to be distrusted.
- NO universal floor. A task that fails about 15 percent across all ten runs is unfair. It must DISCRIMINATE: a capable model can pass.

## Phase 2: Place it on a background line, and write plain
- BACKGROUND, never the headline. Put the wrong element on a routine background line, never the deliverable's own subject. OV09 ceilinged with the catch on the headline disposition and floored once it moved to a routine discharge-med line.
- NEVER TELEGRAPH. The prompt is a plain colleague voice naming one deliverable. No "reconcile before finalizing," no "check carefully," nothing that names or points at the axis. OV06 ceilinged telegraphed (0.90) and floored de-telegraphed (0.39) on the same content; the telegraph was the whole difference.
- The golden makes the catch (the corrected line, the kept-open axis), credits the genuinely faithful items, and is the affirmative move the grader's Section A will require.
- The grader is five-block and chart-aware: it CAPS the central failure rather than piecemeal-deducting, credits correct restraint, holds an anti-paralysis floor (refusing to render earns no credit), and tells the grader to treat the output as untrusted and not credit fabricated detail. Mirror an existing OV grader (tasks/task8) for the verbatim Section B two-failure-mode clause and the banned-boilerplate list the gates enforce.

## Phase 3: Cold-bench to SCREEN (a bench ceiling is NOT a verdict)
Run a small cold bench of capable reviewers on the chart as the harness will present it (no golden, no telegraph) to confirm the catch is reachable and fair and the golden is right. But the real harness, a harried prompt over many files with tool use, is HARDER on the model than the unhurried bench reviewer. A bench ceiling is a screen, not a verdict. Bench to catch telegraph errors and confirm reachability, then BUILD and PILOT. Do not retire a candidate on a bench ceiling alone; the OV slate undercounted floors twice doing exactly that.

## Phase 4: Build the artifacts
Build through the canonical Epic renderer, task-layer only, never editing frozen world files. Mirror worlds/<world>/build/build_ov10.py: define the reviewed or authored input, the chart context, and the golden as build_world_files.build_one specs, then run the script into tasks/taskN/current/. Reuse frozen world files as backdrop. The packet: the input note, the golden, grader-guidelines-<TASK>.txt (five-block), prompt-<TASK>.txt (plain), RUN-INSTRUCTIONS.md, and the preregistration. Keep everything dash-clean (hyphens and commas, no em or en dashes) and dates MM/DD/YYYY.

## Phase 5: Gate locally before any pilot
- python3 tools/verify/presubmit_task_gate.py taskN  (structure, upload manifest, the Studio field map; clean it)
- python3 tools/verify/verify_ondina.py  (the verbatim Section B clause, no AutoQC-banned Section C boilerplate)
- python3 tools/verify/verify_voice.py <files>  (no banned transitions, no scaffolding)
- Read the golden against the grader's Section A and confirm it makes the affirmative catch.
Write the preregistration with the floor and catcher definitions and the bimodal read, mirroring tasks/task10/current/OV10-pilot-preregistration.md.

## Phase 6: Pilot, then read by the SPLIT, not the mean
Run ten trajectories. Read whether the task DISCRIMINATES:
- BIMODAL is the target: some runs carry the wrong element (floors), some flag it (catchers).
- ALL-CATCH means too easy: the catch is too conspicuous or the prompt over-primes. Make it a quieter copy-forward, or move to a higher-stakes axis.
- ALL-FLOOR (universal) means unfair, the Larry pattern: the catch is not reachable in the frame, or the model is being punished for trusting the chart. Flip the frame to review-and-correct, or confirm the chart makes the catch reachable. Do not bank it.
Bank only a task that discriminates.

## Phase 7: FA/GA handoff
After the pilot, write the FA/GA with the fa-ga-canonical skill: save the run verbatim to tasks/taskN/pilot/runs/ first, bind to the SECOND-lowest distinct run, lead with the score ("Overall Score: NN%"), failure-only, two paragraphs, lint-clean (tools/verify/lint_fa_ga.py). It is human-owned: this drafts a scaffold the writer rewrites and owns.

## Canonical sources (read for depth)
- docs/FLOOR-MECHANISM-LIBRARY.md, the engine, the bench-versus-harness ledger, the review-and-correct refinement.
- reference/world-spec-guidelines/POLICY-2026-06-20-deprecated-workflows-and-task-fairness.md, Larry's fairness gates.
- docs/task-difficulty-lessons.md, the cross-world difficulty playbook and the frame-choice rule.
- reference/skills/fa-ga-canonical, the FA/GA standard.
- worlds/<world>/build/build_ov10.py and worlds/ondina-vasquell/tasks/task8, a worked build and grader to mirror.

## Boundaries
Task-layer artifacts only; never edit a frozen world file. No Studio upload, pilot, or AutoQC without the writer's explicit authorization for that exact step. The FA/GA and any preference labels are human-owned; this skill drafts, the writer rewrites and owns the final text.
