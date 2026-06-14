# Ondina Step Audit and Task-Build Plan

Date: 2026-06-12. Purpose: because decisions 11 to 13 collapsed the review gates to run continuous to an upload-ready spec package, this is the check-back across the canonical pipeline (world-pipeline-playbook.md, TASK-RUNBOOK.md) before the next phase, task setup. Status key: DONE (artifact in repo), GATE-COLLAPSED (a human review checkpoint intentionally removed by decision 11 to 13, work itself done), PENDING (real remaining work), EXTERNAL (Alexander-operated platform step).

## Pre-brainstorm gate (playbook B0)

| Step | Status | Evidence / note |
|---|---|---|
| Re-read live instruction doc | DONE | decision record cites 06_08 source; cockpit read order |
| Planning canvas / structures before scenario | DONE | phase-1 1a structure-selection, 1d task-architecture worksheets |
| Trap inventory + pairing + fairness at design time | DONE | phase-1 1b trap-library, 1c trap-pairing-and-fairness |
| Anchor plan at brainstorm time | DONE | decision 2 snapshot 05/21 18:00 + per-task post-snapshot anchors |
| Claim-check workflows verbatim vs live categories | DONE (re-verified 6/12) | all 10 spec workflows EXACT-match task-selection-categories-snapshot-2026-06-10.csv (232 live workflows) |
| World-file count >= 30 | DONE | 31 world-level + 3 supplementary |
| Fairness doctrine baked at design time (A0.4) | DONE at design; PENDING per-task verify | phase-1 1c; per-task A0.4 confirm belongs in task setup |

## Brainstorm

| Step | Status | Note |
|---|---|---|
| Brainstorm content + AutoQC | DONE | AutoQC passed in Studio per Alexander (priority-label patch) |
| Brainstorm Claude transcript | DONE | audited, enriched, expanded; sanitation clean |
| Human Brainstorm review GO | GATE-COLLAPSED | decision 11 accepted at-risk; still the one external sign-off not yet returned |

## World Spec + substrate

| Step | Status | Note |
|---|---|---|
| Substrate proposal pack, all values ratified | DONE | `phase-2-world-spec-and-substrate/world-spec-prep/locked/substrate-proposal-pack.md`, Alexander ratified 6/13 |
| World Spec (4 sections, 10 tasks, file plan) | DONE | built, multi-pass audited |
| Spec authoring-time preflight | DONE | spec-audit-record + AutoQC-25 defense notes |
| World Spec Claude transcript | DONE | built, expanded, sanitized |
| Spec AutoQC in Studio | EXTERNAL | Alexander-operated; not yet run |
| Human Spec review GO | GATE-COLLAPSED / EXTERNAL | decision 11 |

## Reference files (Phase 3)

| Step | Status | Note |
|---|---|---|
| 31 world + 3 supplementary + 9 task DOCX | DONE | Mode A clones, second-pass style match, both gates pass |
| Header/footer leak fix + KM-identifier gate | DONE | second-pass; verify_no_km_identifiers added |
| Two writer-produced images | DONE | EW30 wound photo, EW31 tracing (separate image step), vision constraints verified |
| File manifest + SHAs + derived-value registry | DONE | PHASE-3-FILE-MANIFEST.md |
| Pre-pilot mounted-set coherence check | PENDING | confirm exact world set under the shared mount; task files only with their task |

## Task setup (Step 10) - THE NEXT MOVE

Per task, the KM pattern produced: a task prompt, a golden response, grader guidelines, the task-level reference files, and run instructions, then trajectories, failure and grader analysis, preference labeling, and human review.

| Item | Owner | Status |
|---|---|---|
| Task-level reference files (E1-T*) | Claude build | DONE (9 files, separated, verified) |
| Task prompts | WRITER-authored; Claude drafts candidates + de-hint | PENDING |
| Golden responses (clinical determinations) | PHYSICIAN-owned (Alexander) | PENDING - not Claude's to finalize |
| Grader guidelines (scoring standard) | PHYSICIAN-owned; Claude drafts candidate in the correct structure | PENDING |
| A0.4 draft-completion fairness per task (esp. T1 order set, T10 discharge draft) | Claude verify, physician rule | PENDING |
| A0.5 fairness gate against the BUILT artifacts | Claude run | PENDING |
| A0.6 answer-key / off-text signal gate | Claude run | PENDING |
| Clinical-register gate on prompt/golden/grader/files | Claude run | PENDING |
| Task AutoQC (2.x), trajectories, FA/GA, preference labeling, final review | EXTERNAL | Alexander-operated |

## Authorship boundary (non-negotiable, restated)

The playbook and the per-task checklist are explicit and consistent with decision 12: the task prompt, the golden response, and the grader standard are physician-owned. The KM operating model was "the reviewer drafts candidates, Alexander finalizes." Claude's lane in task setup is: scaffold the per-task structure, draft prompt and grader-guideline CANDIDATES in the correct format, de-hint, run the fairness and register and answer-key gates against the built bytes, and prepare run instructions and pilot preregistration. Claude does not finalize the clinical determinations in the goldens or the scoring standard in the graders.

## What the gate-collapse actually skipped

Not artifacts, but the human review checkpoints between phases: the Brainstorm human GO, the per-sitting stops, and the pod GO. The substantive design and build work was done and self-verified against the encoded standards. The one live external sign-off still outstanding is the human Brainstorm GO; everything downstream of it (Spec AutoQC, task pilots, final review, upload) remains Alexander-operated and unstarted.

## Recommended order into task setup

1. Mounted-set coherence check (cheap, closes a Phase 3 loose end).
2. Per-task A0.4 design-time fairness confirmation (especially T1 and T10).
3. Scaffold platform/taskN folders KM-style and draft the task prompt candidates (de-hinted, self-contained) for Alexander to finalize.
4. Draft grader-guideline candidates in the three-section structure (Must be present and correct / Acceptable variation / Penalize for), naming the golden by filename, for Alexander to finalize against his goldens.
5. Run A0.5, A0.6, and the clinical-register gate on each built task package.
6. Hand to Alexander for goldens, Task AutoQC, pilots, and review.
