# KM08 Task Design — Agent Execution Prompt
## Target model: Claude 4 Opus (codebase + extended thinking)
## Mode: Analysis only. No build. No file mutation outside the deliverable.

---

You are a clinical AI training specialist embedded in Project Sanctum. Your job is to design an 8th evaluation task for the Korvin Merrow world that makes a frontier model **fail fair and square** — a genuine sub-60 floor, not a ~0.85-0.96 clearer.

You have read access to this workspace. **Do not trust summaries. Grep the primary bytes yourself.**

---

## Phase 1 — Read (do not skip; cite what you read)

**Spec + process:**
- `reference/source/[EXP] Project Sanctum Instruction Document (06_08).md` (workflow categories, failure-design principles, the 8+ task rule)
- `worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md`
- `worlds/korvin-merrow/task-setup/KM-RETROSPECTIVE-tasks1-2.md`

**Every task state file (the failure ledger):**
- `task-setup/task1-lifecycle-log.md`
- `task-setup/task2/TASK2-STATE.md`
- `task-setup/task3/TASK3-STATE.md`
- `task-setup/task4/TASK4-STATE.md`
- `task-setup/task5/TASK5-STATE.md`
- `task-setup/task6/TASK6-STATE.md`
- `task-setup/task7/TASK7-STATE.md`
- `task-setup/task8/TASK8-STATE.md`

**KM08 v3 (the failed pilot):**
- `platform/task8/current/prompt-task8-v3.txt`
- `platform/task8/current/grader-guidelines-task8-v3.txt`
- `platform/task8/current/RUN-INSTRUCTIONS.md`

**Chart substrate (agent-read DOCX layer — THE primary source):**
- `worlds/korvin-merrow/file-review/upload/filesystem/` (all 26 files; python-docx including table cells)

---

## Phase 2 — Derive the pattern (from the bytes, not my brief)

Answer in your own words, with file+line citations:
1. Which mechanisms **floored** the model (sub-60) and why? (KM02, KM05 v4, KM06 v5)
2. Which mechanisms **cleared** (~0.85-0.97) and why? (KM03 v1/v2.1, KM04 v1, KM05 v3, KM06 v1/v2, KM08 v3)
3. State the **single structural rule** that separates floor from clear on THIS chart.
4. Confirm or refute my hypothesis: *the only floor-class left is "unverified self-report → eager medication action against documented contraindications."*

---

## Phase 3 — Verify substrate for candidate mechanisms

For each candidate, grep the chart and report present/absent with citations:

**Gabapentin uptitration candidate:**
- gabapentin dose + indication (MAR, med rec)
- CKD stage / renal dosing language (nephrology)
- Morse fall score (PT/OT)
- OSA (sleep study)
- confusion/AMS episodes (nursing/hospitalist)
- Is there ANY pain scale or functional pain measure documented?

**Any alternative you propose:** same substrate-verification discipline.

---

## Phase 4 — Design (the deliverable)

Produce a **1-2 page plan**. Propose 2-3 mechanisms ranked, each with:
- **Workflow** (exact name from Task Selection Categories; P0 preferred; flag if already used in KM01-KM07)
- **Artifact type** + timeline anchor (HD#/date)
- **Mechanism** (what cognitive failure it forces)
- **Draft content** (the wrong move planted, attributed fairly)
- **Golden direction** (correct restraint, chart-cited)
- **Predicted spread** (honest; bimodal? mean? floor depth?)
- **Fairness justification** (can we defend the floor WITHOUT a reconcile clause in the prompt? — note: KM06 v4 died at ~0.98 the moment a reconcile instruction was added, so the trap must survive a fully-reconciling model)
- **Distinctness** (how it differs from KM06's insulin judgment trap and KM05's restart trap — must pass AutoQC 2.106 distinct-capability)

---

## Hard constraints

- 8+ tasks required; shipping at 7 is **not** an option.
- Must be distinct from KM01-KM07 (capability + axis), not just re-skinned.
- Target genuine sub-60; a ~0.85 clearer is a failure of this task.
- Fair = chart-grounded + plain prompt; no telegraphing, no reconcile clause.
- **Do not build, stage, upload, or edit platform/world files.** Output the plan only.

---

## Output format

A single markdown plan. Lead with your **derived structural rule** (Phase 2.3), then the **ranked mechanisms**, then a **one-line recommendation**. End with **open risks** (where you're uncertain the floor will hold).
