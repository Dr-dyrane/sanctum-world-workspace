# Clean-house pass summary (2026-06-18)

What this pass found, what it fixed, and what it deliberately deferred. Full audit detail is in A1 through A4 in this folder. Plan: `docs/clean-house-pass-2026-06-18.md`.

## Audits (Wave 1)

- A1 guardrail compliance: graders and prompts are CLEAN across all ten tasks (five-block structure in order, golden named verbatim, at or under 540 words, no AI or eval leakage, no dashes). Every violation sits in the FA/GA layer (see Deferred A).
- A2 file-tree: KM groups by pipeline stage, OV by lifecycle phase. OV is the cleaner base. Proposed one canonical pattern (the OV phase model plus a single `docs/` home and per-task `design/` and `pilot/` folders). Classified must-not-move (Studio packets, world-files, the two name-referenced design docs) versus safe-to-reorg.
- A3 status/logs: no single accurate running status existed; WORKFLOW-MAP contradicted itself; the live Studio board IDs were absent from every tracker; lifecycle vocabulary was stale throughout.
- A4 canonicals: all discoverable and mutually consistent; one gap (fa-ga-canonical not cross-referenced from AGENTS.md). Next-world starter drafted (A4 Step 3).

## Fixes executed (Wave 2, safe and in place)

1. OV-WORLD-STATUS.md rewritten as the single source of truth: a ten-task lifecycle table with live Studio IDs, lanes, mechanisms, pilot outcomes, and states; a seven-lane summary; and a compact activity log with the 2026-06-18 events backfilled. The full prior 160-line log is preserved at `archive/2026-06-18-cleanup/OV-WORLD-STATUS-pre-cleanup-2026-06-17.md`.
2. WORKFLOW-MAP.md rewritten: a ten-row lane table (was seven rows and self-contradictory), seven lanes, Utilization Review removed from the open list because OV08 now uses it, live Studio IDs added.
3. 00-START-HERE.md cockpit: status line, lanes list, next-action, and submission status all updated to the 06-18 reality and pointed at the SSOT.
4. Supersede and pointer banners so status stops being duplicated across docs: OV-CANDIDATE-QUEUE, OV-TASK-IDEA-AUDIT, OV-FRESH-TASK-IDEAS, and OV-FLOOR-MECHANISM-LIBRARY now defer live status to OV-WORLD-STATUS.md.
5. AGENTS.md guardrail 4 now cross-references `docs/fa-ga-canonical.md` and names the `fa-ga-canonical` skill (closes the A4 gap).
6. Removed the four empty `.gitkeep`-only stub dirs under phase-3 (goldens, grader-guidance, task-prompts, task-context-files); the live artifacts of those types live in the task packets.

No frozen world file, delivered task artifact, grader, prompt, or golden was touched.

## Deferred deliberately (flagged for your call)

A. FA/GA tightening on delivered and in-review tasks. A1 found drift in OV01 and OV02 (minor; the canonical allows the affirm-plus-caveat form for a sound grader), OV03 (FA 1017 chars; GA missing the grader-improvement move), OV06 (GA 1225 chars), and OV07 (GA missing the grader-improvement move). OV01, OV02, OV03, and OV06 are DELIVERED and their FA/GA were accepted by reviewers; OV07 is in first human review. Rewriting the repo copies now would diverge them from what was delivered and from the Studio copy under review, and the canonical postdates their delivery. Recommendation: leave them as the accepted historical record; if OV07 bounces back from Larry, redo its FA/GA through the fa-ga-canonical skill then. The clean both-sides GA exemplars to copy are OV06, OV08, and OV09.

B. Full tree migration to the A2 canonical pattern (loose root docs into `docs/`, `platform/taskN` to `tasks/taskN`, per-task `design/` and `pilot/`). This touches Studio-referenced paths and name-referenced docs, so it should be done atomically with reference updates and a re-gate. Best adopted fresh in the next world (A4 next-world starter) and applied to OV as a dedicated migration once its tasks are all delivered. Not safe to do piecemeal mid-review.

C. OV05 and OV10 FA/GA are absent because both are still piloting (running Taiga). Author each on the second-lowest distinct run via the fa-ga-canonical skill once the trajectories return, per each prereg's read rules.

## Pending (normal pipeline)

- OV05 and OV10 trajectories, then FA/GA, then bank or swap.
- OV07 first human review with Larry.
- OV09 preference labels.
