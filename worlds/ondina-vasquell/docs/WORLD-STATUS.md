# Ondina Vasquell - world status and running log (SINGLE SOURCE OF TRUTH)

This file governs live OV status. Update it at every step (build, upload, pilot, bank, FA/GA, PL, review, deliver). Point-in-time docs (prereg, results, FA/GA, PL, reviews) are linked from here, never a substitute for it. The full pre-2026-06-18 status log is preserved at `archive/2026-06-18-cleanup/OV-WORLD-STATUS-pre-cleanup-2026-06-17.md`. Last updated: 2026-06-18 (clean-house pass).

## Posture (2026-06-18)

Ten tasks built across seven distinct lanes. Eight confirmed floors. Five delivered (OV01, OV02, OV03, OV04, OV06). One in first human review (OV07, Larry). Two awaiting first human review (OV08, OV09; OV09 FA/GA submitted). Two running Taiga trajectories (OV05, OV10). The 34-file world is frozen and clean. Target of 8 to 10 shippable tasks across 6 to 7 lanes is met.

## Per-task lifecycle (the board)

| Task | Studio ID | Lane | Mechanism | Pilot (job) | State |
|---|---|---|---|---|---|
| OV01 | Task 1 | Medication Reconciliation | cold knowledge: stop inpatient enoxaparin at discharge | FLOOR (741ba52f) | Delivered |
| OV02 | rpfl3eac | Medical Transcription | off-text text synthesis: new IV line-site infection | FLOOR ~0.10 (d0795803) | Delivered |
| OV03 | ckrz3598 | Medical Transcription | embedded carry-forward: inpatient sliding-scale insulin sent home | FLOOR 0.05-0.20 (048aa8eb) | Delivered |
| OV04 | jqxv7246 | Medical Transcription | off-text image: CPAP poor adherence, OSA undertreated | FLOOR bimodal (dbe6f0c9) | Delivered |
| OV05 | 37cd058a | Referral Intake/Triage | conflicting subordinate input: skilled-wound-care downgrade | running Taiga | Running Taiga trajectories |
| OV06 | 1rqn2959 | Referral Intake/Triage | embedded wrong, de-telegraphed: vascular perfusion closure | FLOOR 0.39 (577effae) | Delivered |
| OV07 | ah6e821b | Claims Denial | off-text image: wound undermining, skilled-need basis | FLOOR 0.51 (a33db3d0) | In first human review (Larry) |
| OV08 | l6jo01e4 | Utilization Review | embedded wrong: IV antibiotic route, no oral conversion or OPAT | FLOOR 0.63 (d4eaa31b) | Awaiting first human review |
| OV09 | ebv61af9 | Post-Acute Coordination | embedded wrong on a background line: three held oral agents resumed | FLOOR ~0.62 (cc337773) | Awaiting first human review; FA/GA submitted |
| OV10 | ilsjf671 | Discharge Summary | over-closure via subordinate review: bone-health / CKD-MBD | running Taiga | Running Taiga trajectories |

Version history that matters: OV05 bottle-photo med-rec image retired 2026-06-16 after three ceilings, slot rebuilt 2026-06-18 on the Referral lane. OV09 v1 contrast ceiling 0.84 (e9c38261), v2 osteo-image retired, v4 held-med-resume floored. OV02 v1/v2/v3 coding-attestation history retired; current OV02 is the transcription line-infection floor.

## Lanes (7 distinct)

Medication Reconciliation (OV01); Medical Transcription (OV02, OV03, OV04); Referral Intake, Triage, and Scheduling Coordination (OV06, OV05); Claims Denial Analysis and Appeal Preparation (OV07); Utilization Review Concurrent Stay Documentation (OV08); Post-Acute Care Coordination Documentation (OV09); Discharge Summary (OV10). Two lanes carry two tasks each (Referral: OV06 + OV05; Transcription carries three: OV02/03/04).

## World

- Live name: Healthcare_297_Vasquell. Studio world id: world_ab51f33a691648d08f5ca681375fe2a1.
- 34 golden world files (32 docx + 2 images), writer-produced restore at `file-review/revision/filesystem`. No task files in the world. MAR carries enoxaparin (OV01 substrate).
- Snapshot: 05/21/2026 18:00. All world files at or before the snapshot; task encounters and deliverables strictly after.
- Frozen during tasking: task-layer artifacts only, never the 34 world files (DO-NOT-REPEAT #21).

## Working files (per task)

- Packets: `tasks/task{1..10}/current/` (task5 = revived OV05, task6 = OV06).
- FA/GA: `tasks/taskN/pilot/FA-GA-OVNN-current.md` (OV01-04 and 06-09 done; OV05 and OV10 pending their pilots).
- Preference labels: `tasks/taskN/pilot/OVNN-PLx-A-vs-B.md`.
- Results: `tasks/taskN/pilot/` per task; cross-task benches in `tasks/_benches/`.
- OV05 retired bottle-photo packet: `tasks/task5/archive/2026-06-16-retired/`.
- Cleanup archives: `archive/2026-06-15-cleanup/`, `archive/2026-06-18-cleanup/`.

## Validated build template (apply to every task, from OV01)

One cold verification-asymmetry plant on a distinct axis (physician-ratified, clinically accurate, chart-grounded wrong, not a KM duplicate), off the loud world threads; de-telegraphed routine surface; one plain Filesystem task file, clean filename, first-trajectory `find /docs` mount gate (DO-NOT-REPEAT #16); grader floors the cold miss; golden self-scores high; NEW locked prereg per pilot; two-paragraph failure-only FA/GA from the 2nd-LOWEST distinct run (King P 2026-06-14, DO-NOT-REPEAT #20, not the lowest, which is often the noisy outlier). Warm secondary misses may remain; the cold plant is the floor lever. FLOOR CANON: approval needs one legitimate critical or material failure in a trajectory, not a numeric sub-70 gate. DESIGN target: a floor-worthy failure landing about 0.30 to 0.55 with at least one catcher above 0.85, so the material signability failure is reliable and clears review with margin. Judge a run by the legitimacy and materiality of its failure, not the number; a 0.62 to 0.68 graze means the mechanism is too soft (re-center or retire, never tune the grader to fake depth). See docs/task-difficulty-lessons.md.

## Key linked records

- FA/GA standard (LOCKED): `docs/fa-ga-canonical.md`. Use the `fa-ga-canonical` skill, not the older `failure-grader-analysis`.
- Floor design: `docs/FLOOR-MECHANISM-LIBRARY.md`. Workflow labels: `docs/WORKFLOW-MAP.md`. Mistakes ledger: `DO-NOT-REPEAT.md`.
- Voice standard: `docs/alexander-voice-dna.md` (enforced by `tools/verify/verify_voice.py`).
- Clean-house pass (2026-06-18) audit reports and next-world starter: `cleanup-2026-06-18/A1-guardrail-compliance.md`, `A2-file-tree.md`, `A3-status-logs.md`, `A4-canonicals-nextworld.md`.

## Open reviewer item

- OV07 in first human review with Larry (ah6e821b). Nothing uploads, runs, or submits without Alexander's authorization for that exact step.

## OV mount-hygiene rule (every upload or rerun)

The 2026-06-14 dirty rerun was not a world leak. It was a two-task-file mount: an old order set in `/docs/filesystem` plus the new order set under `/docs/.apps_data/calendar`. For every Ondina task upload or rerun, inspect the first trajectory's `find /docs` tree before using scores. Require exactly the intended task file under `/docs/filesystem`, no `/docs/.apps_data`, and no stale filename. If the gate fails, delete every file from the Studio Task Files card and re-add only the current plain Filesystem file.

## Activity log (append-only, newest last; pre-2026-06-18 entries archived)

- 2026-06-16 OV06 v2 de-telegraphed re-pilot floored (577effae, mean 0.39, bimodal); banking.
- 2026-06-16 OV05 bottle-photo med-rec route retired after three ceilings; packet archived.
- 2026-06-17 OV07 floored (a33db3d0, off-text wound undermining); FA/GA done. OV08 built and floored (d4eaa31b, 0.63). OV-TASK-IDEA-AUDIT written.
- 2026-06-17 fa-ga-canonical standard locked (docs/fa-ga-canonical.md); new fa-ga-canonical skill built, packaged, installed.
- 2026-06-18 OV09 v3 disposition-headline ceiling 0.84 (e9c38261); re-cut to v4 held-med-resume on a background med line, floored about 0.62 (cc337773); FA/GA written and submitted.
- 2026-06-18 OV10 built (Discharge Summary, bone-health / CKD-MBD over-closure via a subordinate chronic-disease review); gated and prereg.
- 2026-06-18 OV05 revived; rebuilt on the Referral lane as a skilled-wound-care downgrade (OV06 conflicting-authority engine, 2nd task on the lane); gated and prereg.
- 2026-06-18 Five Studio uploads live: OV05 (37cd058a) and OV10 (ilsjf671) running Taiga; OV07 (ah6e821b) in review; OV08 (l6jo01e4) and OV09 (ebv61af9) awaiting review.
- 2026-06-18 OV01, OV02, OV03, OV04, OV06 transitioned to Delivered on the board.
- 2026-06-18 Canonical tree migration: 8 root design docs moved into docs/ with generic names; phase-3 build dirs flattened to the world root (build, world-files, supplementary-files, synthetic-files, task-files); platform/taskN renamed to tasks/taskN, each with a per-task pilot/ (FA/GA, preference labels, results); cross-task benches in tasks/_benches/; phase-3 and phase-4 wrappers removed. Build scripts and the three gates repointed; verify_ondina and verify_voice green, presubmit byte-identical to baseline. The world root now holds only 00-START-HERE.md plus folders.
- 2026-06-18 Clean-house pass: status consolidated to this file as the single source of truth; four audit reports landed in `cleanup-2026-06-18/`; the four empty `.gitkeep` stub dirs under phase-3 removed; AGENTS.md now cross-references `docs/fa-ga-canonical.md`; supersede and pointer banners added to WORKFLOW-MAP, 00-START-HERE, OV-CANDIDATE-QUEUE, OV-TASK-IDEA-AUDIT, OV-FRESH-TASK-IDEAS, OV-FLOOR-MECHANISM-LIBRARY.
