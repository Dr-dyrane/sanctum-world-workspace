# Korvin Merrow — Submission Readiness Audit

Date: 2026-06-03
Auditor: Claude (Cowork)
Scope: full-repository index and depth review against Sanctum World Spec submission requirements.

## 1. What this repository is

This is the Project Sanctum (Mercor) world-building workspace for the **Korvin Merrow World** (RL Studio task `cyau8803`) — a Typical Clinical World testing physician-level judgment on a 62-year-old man with multimorbidity, suspected urinary-source sepsis, AKI-on-CKD, polypharmacy, and discharge-readiness complexity. It is a structured authoring repo (Markdown source + governance), not a software codebase. Work proceeds through gated, ratified, "locked" phases.

## 2. Headline verdict

**Content-complete and high quality. Not yet artifact-generated.**

The entire authoring ecosystem is finished, internally consistent, and locked in Markdown. The remaining work is the deliberately-gated **Execution and Artifact Generation** phase (DOCX/PDF export + packaging), which is blocked pending Alexander's explicit authorization. Two housekeeping issues should be cleared before that phase.

## 3. Completeness check (all present and locked)

| Layer | Expected | Present | Status |
| --- | --- | --- | --- |
| World Spec v1 | 1 | 1 | LOCKED, ratified |
| File Inventory v1 (AutoQC v6.3, 8-column) | 1 | 1 | LOCKED |
| World-level synthetic files FI-W | 22 | 22 | LOCKED (5 batches, all validated/ratified) |
| Task-level context files FI-T | 7 | 7 | LOCKED |
| Supplementary files FI-S | 4 | 4 | LOCKED |
| Task prompts TP-KM | 6 | 6 | LOCKED |
| Expected outputs EO-KM | 6 | 6 | LOCKED |
| Golden responses Golden-KM | 6 | 6 | LOCKED |
| Grader guidance GG-KM | 6 | 6 | LOCKED |
| AutoQC architecture + construction | 2 | 2 | LOCKED |
| Packaging / Submission Prep / Execution Prep | 3 | 3 | LOCKED |
| Transcript Resolution | 1 | 1 | LOCKED |
| Final Submission Resolution v1 | 1 | 1 | CANDIDATE REVIEW (+ validation review) |

Every layer carries a paired validation-review and a ratification record. The governance discipline (lock → validate → ratify, cross-artifact consistency checks) is unusually rigorous and was followed consistently.

## 4. Quality assessment (spot-checked in depth)

- **World Spec v1** — clinically realistic, coherent timeline (decline 04/27 → admit 05/18/HD1 → close 05/23 18:00/HD6 → discharge 05/24 → +7 05/31 → +30 06/23), 14 comorbidities, 20 baseline meds, 3 human frictions, 5 traps, 7-role provider roster with explicit source-of-truth hierarchies. Builds only from locked architecture; no downstream leakage. **Strong.**
- **File Inventory v1** — correct AutoQC v6.3 8-column structure with Source and Tool/Origin properly separated; each row maps to workflows/traps/frictions. **Compliant.**
- **TP-KM01 / Golden-KM01** — task prompt is well-scoped and physician-voiced; golden response is genuinely physician-grade (staged, source-aware medication reconciliation; resists copy-forward; handles prednisone/adrenal-risk without forcing a "hidden diagnosis"). **Strong.**
- Internal consistency across spec ↔ inventory ↔ tasks ↔ goldens ↔ grader guidance is maintained; no canon conflicts found in the locked validation reviews.

## 5. What the references require at submission

Per `reference/world-spec-guidelines/10`, `/12`, `/11` and the Final Submission Resolution:

Required upload set (RL Studio fields):
1. **2.1 Spec Document** — single World Spec `.docx`.
2. **2.2 Template/Reference Files** — world-level FI-W (×22) and supplementary FI-S (×4) exported individually as DOCX/binary (no zip).
3. **2.3 Upload Claude Transcripts** — transcript as DOCX (source: `docs/claude-transcript-formatted.md`; share URL preserved as provenance).

Optional / hold: approved Brainstorm DOCX (already exists) as QC input; FI-T task-level files only if RL Studio asks; TP/EO/Golden/GG are later-pipeline, not part of this upload.

## 6. Gaps and blockers before submission

### A. No submission artifacts exist yet (expected, gated)
The repository holds **zero** of the required `.docx` deliverables. The only DOCX present is `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx`. The World Spec DOCX, the FI-W/FI-S template-reference exports, and the transcript DOCX must all be generated. This is intentionally blocked until Alexander authorizes **Execution and Artifact Generation**. Final Submission Resolution v1 is still in CANDIDATE REVIEW and should be ratified/locked first.

### B. Working tree is not clean (housekeeping)
20 files show uncommitted changes. They split into two kinds:
- **Legitimate pending edits** — phase-progression updates to `project/STATUS.md`, `PHASE_MAP.md`, `WORKSPACE_FILE_MAP.md`, `claude-package/*`, `AGENTS.md`, `docs/status-dashboard.md`, and a +40-line addition to `physician-decision-log-02.md`. These should be committed as a checkpoint.
- **CRLF line-ending churn** — the large diffs on `world-spec-prep/locked/provider-roster-package-v1.md` (694) and `comorbidity-expansion-package-v1.md` (612) are **line-ending normalization only**; `git diff --ignore-all-space` shows no content change. Locked content is intact, but the churn is noisy. Consider adding a `.gitattributes` (`* text=auto eol=lf` or `eol=crlf`) to stop recurring CRLF/LF flip-flop.

The project's own "session-exit discipline" requires a clean or explicitly-documented tree before handoff; right now it is dirty.

### C. Unresolved external confirmations (not blockers you can close alone)
1. **Onboarding upload-scope conflict** — the source guide says onboarding writers upload the spec *only*, while the May-20-2026 update says new writers also curate template/reference files. Unresolved in source; confirm the actual RL Studio 2.2 field / pod guidance before upload (flagged in `12_required_upload_inventory.md`).
2. **Transcript format** — resolved locally to DOCX from RL Studio screenshot evidence, but stop and re-confirm if RL Studio rejects DOCX.
3. **Branch name mismatch** — branch is `james-carter-brainstorm`; proposed rename `korvin-merrow-brainstorm` is pending Alexander approval (cosmetic/provenance only).

## 7. Recommended path to submission

1. Ratify and lock **Final Submission Resolution v1** (currently candidate review).
2. Commit the pending phase-progression edits; add `.gitattributes` to settle line endings; reach a clean tree.
3. Obtain Alexander's authorization for **Execution and Artifact Generation**.
4. Generate: World Spec `.docx` (from locked template + locked sources), FI-W×22 + FI-S×4 template/reference exports, transcript `.docx`.
5. Confirm the RL Studio 2.2 field expectation (onboarding scope conflict) before uploading template/reference files.
6. Stage per the Section 3 folder map, upload each file individually (no zip), then run World Spec AutoQC — only after explicit authorization.

## 8. Bottom line

The Korvin Merrow world is **substantively ready** — the clinical design, file ecosystem, tasks, goldens, grader guidance, and QC architecture are complete, locked, validated, and internally consistent. It is **not yet mechanically ready**: the `.docx` submission artifacts have not been produced, and that production is deliberately gated behind an authorization Alexander has not yet given. No clinical or structural rework is needed before that gate — only a clean commit and the go-ahead.
