# Clean-House and Standardization Pass (2026-06-18)

Context: ten OV tasks are built. Delivered: OV01, OV02, OV03, OV04, OV06. In or awaiting first human review: OV07, OV08, OV09. Running Taiga trajectories now: OV05 (revived, skilled-wound-care downgrade) and OV10 (bone-health over-closure). While the two pilots run, this pass cleans the repo, audits OV against the guardrails, reconciles the OV file tree with KM, makes the canonicals discoverable, and leaves a reusable flow for the next world.

## Goals
1. Find and fix where OV drifts from the guardrails (AGENTS.md, the docs canon, the EXP 06_09 instruction).
2. Establish ONE canonical world file-tree pattern (KM and OV currently differ) and align OV's safe-to-move parts to it.
3. Make the status, logs, and continuous docs accurate and current, with a single running status.
4. Ensure the canonicals are discoverable from the entry points and self-consistent.
5. Produce a next-world starter so the next world begins clean.

## Hard constraints (do not break)
- Frozen world: never edit the 34 OV world files.
- Delivered tasks (OV01, 02, 03, 04, 06): do not change content or move their platform/task*/current/ artifacts (Studio-referenced, graded).
- In-review and piloting tasks (OV05, 07, 08, 09, 10): do not change task content.
- Safe to change: planning, status, and log docs; the floor library; WORKFLOW-MAP; the canonical docs; README; AGENTS and CLAUDE pointers; and reorganization of LOOSE non-deliverable docs only.
- Git hygiene: mask the PAT, clear stale locks, stage specific paths, never git add -A.

## The pass (multi-agent)
Wave 1, four read-only audit agents in parallel (no edits, each writes one report to worlds/ondina-vasquell/cleanup-2026-06-18/):
- A1 Guardrail compliance: audit every OV grader, prompt, golden, FA/GA against AGENTS.md plus the docs canon plus EXP 06_09; list violations with file, text, rule, and a fix, tagged blocker/major/minor.
- A2 File-tree reconciliation: map KM vs OV trees, propose ONE canonical pattern, mark Studio-referenced or frozen paths that must not move versus a safe-reorg list.
- A3 Status, logs, continuous docs: inventory every status/log/prereg/design/results doc, cross-check against the actual ten-task state, list the specific updates needed; recommend a single running status doc.
- A4 Canonical discoverability and next-world readiness: verify each canonical is referenced from the entry points and self-consistent; draft the next-world starter.

Wave 2, central and sequential (one writer, conflict-free):
- Synthesize the four reports into one findings doc.
- Execute the SAFE fixes (status and log updates, canonical pointers, clear guardrail fixes, safe doc reorg).
- Flag risky items (task-artifact moves) for confirmation; do not execute unilaterally.

Wave 3, verification:
- A read-only verification agent confirms gates still pass, no broken references, status docs accurate, canonicals discoverable. Then commit.

## Deliverables
- One consolidated findings and compliance report.
- Updated, accurate status, logs, and canonical pointers (committed).
- A documented canonical tree pattern and a next-world starter.
- A short list of risky reorg items flagged for your call.
