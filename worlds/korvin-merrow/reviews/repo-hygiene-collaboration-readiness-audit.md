# Repository Hygiene and Collaboration Readiness Audit

Date: 2026-06-02

Scope: audit only. No construction work, locked artifact edits, Batch 2 files, task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission materials were created.

## Executive Summary

Status: PASS WITH MINOR ISSUES

Post-audit cleanup note: the minor issues identified here were addressed in the repository hygiene cleanup pass. `PHASE_MAP.md` and `WORLD_SPEC_KICKOFF.md` now describe synthetic construction as batch-gated, Batch 1 is locked, Batch 2 remains explicitly gated, and the old branch name is documented as a known historical branch-name mismatch rather than an active identity issue. Remaining active issues: none.

The repository is ready for a new Codex, Claude, or writer collaborator to enter cold and understand the current Korvin Merrow state from files alone.

Current state is consistently discoverable across the primary continuity surfaces:

- Preparation Layer: COMPLETE.
- World Spec Construction: COMPLETE.
- File Inventory Architecture: COMPLETE.
- File Inventory Planning: COMPLETE.
- Synthetic File Construction Governance: COMPLETE.
- Batch 1 Synthetic World-Level Files: LOCKED.
- Batch 1 Construction: COMPLETE.
- Next Eligible Phase: Batch 2 Synthetic World-Level File Construction.

No active blocker was found. The only issues are minor hygiene/documentation drift items that do not prevent collaboration.

## 1. Current State Clarity

Finding: NO ISSUE

Evidence:

- `project/STATUS.md` states Batch 1 is locked, FI-W01 through FI-W07 are locked, Batch 1 Construction is complete, and Batch 2 is the next eligible phase.
- `docs/status-dashboard.md` repeats the same phase state and paths.
- `AGENTS.md` states Batch 1 is locked and Batch 2/FI-W08 or later remain blocked without explicit Alexander authorization.
- `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md` states World Spec Construction complete, File Inventory Planning complete, Synthetic File Construction Governance complete, Batch 1 locked, and Batch 2 next.
- `worlds/korvin-merrow/README.md` gives the same active entry points and next-phase boundary.
- `claude-package/05_EXECUTION_STATE.md` and `claude-package/06_HANDOFF_STATE.md` reflect Batch 1 locked and Batch 2 gated.

Impact:

- A new collaborator can identify the current phase and next legal action without relying on chat history.

Action required:

- None before Batch 2.

## 2. Canonical Path Clarity

Finding: NO ISSUE

Canonical paths are clear:

- Active world cockpit: `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md`.
- Live status: `project/STATUS.md`.
- File map: `project/WORKSPACE_FILE_MAP.md`.
- World Spec v1: `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md`.
- File Inventory v1: `worlds/korvin-merrow/file-inventory/locked/file-inventory-v1.md`.
- Synthetic construction governance: `worlds/korvin-merrow/synthetic-files/locked/synthetic-world-file-construction-plan-v1.md`.
- Locked Batch 1 files: `worlds/korvin-merrow/synthetic-files/locked/batch-1/`.
- Batch 1 ratification: `worlds/korvin-merrow/synthetic-files/ratifications/batch-1-ratification.md`.

Candidate folder check:

- `worlds/korvin-merrow/world-spec-prep/candidate-review/`: empty.
- `worlds/korvin-merrow/world-spec-construction/candidate-review/`: empty.
- `worlds/korvin-merrow/file-inventory/candidate-review/`: empty.
- `worlds/korvin-merrow/synthetic-files/candidate-review/`: empty.

Impact:

- No unresolved candidate artifact appears to be active.
- Lifecycle folder meanings are discoverable from `WORKSPACE_FILE_MAP.md`.

Action required:

- None.

## 3. Lifecycle Hygiene

Finding: NO ISSUE

The lifecycle pattern is visible and currently satisfied:

Candidate Review -> Independent Review -> Ratification -> Locked -> Next Phase

Evidence:

- Batch 1 was moved from `synthetic-files/candidate-review/batch-1/` to `synthetic-files/locked/batch-1/`.
- Batch 1 has ratification at `synthetic-files/ratifications/batch-1-ratification.md`.
- Git recorded FI-W01 through FI-W07 as pure renames during lock, preserving content.
- Candidate-review folders are empty after lock.

Impact:

- A new collaborator should not mistake a candidate package for current canonical content.

Action required:

- None.

## 4. Collaborator Onboarding Readiness

Finding: NO ISSUE

Reviewed surfaces:

- `AGENTS.md`
- `project/STATUS.md`
- `docs/status-dashboard.md`
- `project/WORKSPACE_FILE_MAP.md`
- `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md`
- `worlds/korvin-merrow/README.md`
- `claude-package/05_EXECUTION_STATE.md`
- `claude-package/06_HANDOFF_STATE.md`
- `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md`
- `worlds/korvin-merrow/active/clinical-logic.md`

These explain:

- what is locked;
- what must not be changed;
- what the next eligible action is;
- where to find canonical source packages;
- which phase boundaries are active.

Impact:

- A new collaborator can resume safely by reading `STATUS.md`, `WORKSPACE_FILE_MAP.md`, `WORLD_SPEC_KICKOFF.md`, the locked file inventory, the locked construction plan, and Batch 1 ratification.

Action required:

- None.

## 5. Synthetic Construction Guardrail Visibility

Finding: PASS WITH MINOR ISSUES

Guardrails visible:

- No task prompts yet.
- No expected outputs yet.
- No goldens yet.
- No grader guidance yet.
- No AutoQC responses yet.
- No Studio submission package for this phase yet.
- No Batch 2 files yet.
- No FI-W08 through FI-W22 files created.
- FI-W22 must remain last and avoid answer-file drift.
- Trap #3 vs Trap #5 distinction is documented.
- Prednisone hierarchy is documented.
- Batch 2 must preserve prednisone uncertainty, infection-vs-mixed-physiology uncertainty, medication-restart uncertainty, baseline-vs-admission-value separation, and hierarchy ordering.
- FI-W06 availability remains governed by HD4 timing during future construction.

Minor hygiene issue:

- `WORLD_SPEC_KICKOFF.md` still has a generic Stop Conditions section saying to stop before "Synthetic file construction or downstream file contents" and "Synthetic file generation." This is historically protective language, but now slightly broad because Batch 1 synthetic construction has already been explicitly authorized, completed, and locked.

Classification:

- MINOR HYGIENE ISSUE.

Impact:

- Low. The same file also clearly states Batch 1 is locked and Batch 2 is next but gated. A new collaborator is unlikely to be blocked if they read the current-state section first.

Action required:

- Optional future cleanup: narrow that stop condition to "Batch 2 or later synthetic file construction unless explicitly authorized."

## 6. Git / Versioning Readiness

Finding: PASS WITH MINOR ISSUES

Git state at audit:

- Working tree before report creation: clean.
- Active branch: `james-carter-brainstorm`.
- Remote tracking: `origin/james-carter-brainstorm`.
- Branch state: ahead by 34 commits.
- Recent commits are understandable and checkpoint-based:
  - `5c48194 checkpoint: ratify batch 1 synthetic world files`
  - `b25d7c9 checkpoint: construct batch 1 synthetic world files`
  - `83e6ddf checkpoint: ratify synthetic world file construction plan v1`
  - `6a1fc49 checkpoint: create synthetic world file construction plan v1`
  - `91eacf5 checkpoint: ratify file inventory v1`
  - `1051baf checkpoint: create file inventory v1`
  - `e4b735d checkpoint: ratify file inventory architecture v1`
  - `d12607d checkpoint: create file inventory architecture v1`

Minor hygiene issue:

- Branch name remains `james-carter-brainstorm`, while active patient identity is Korvin Merrow. This is already documented in `project/STATUS.md` as pending branch rename approval because the branch tracks `origin/james-carter-brainstorm` and is ahead by local commits.

Classification:

- MINOR HYGIENE ISSUE.

Impact:

- Low to moderate. A new collaborator may notice the old branch name, but `STATUS.md`, `AGENTS.md`, and `WORKSPACE_FILE_MAP.md` clearly state current identity and branch rename status.

Action required:

- Optional future cleanup: after remote/push strategy is approved, rename branch to `korvin-merrow-brainstorm` or another current branch name.

## 7. Stale Reference and Drift Check

### Stale candidate-review references

Finding: NO ISSUE

Search found no current references to:

- `candidate-review/batch-1`
- `Batch 1 review and ratification`
- `Batch 1 ... CANDIDATE REVIEW`
- `constructed for candidate review`

### Stale counts

Finding: ACCEPTABLE HISTORICAL REFERENCE

Search found historical mention of the prior 20 vs 21 medication-count issue in `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md`.

Impact:

- No drift. The same ratification records that the issue was already resolved and the canonical baseline medication count is 20.

Action required:

- None.

### Obsolete workflow references

Finding: ACCEPTABLE HISTORICAL REFERENCE

Search found TCM and Patient Risk Stratification language in historical/planning artifacts:

- `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`
- `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-spec-planning.md`
- locked task-architecture ratification noting that standalone TCM / Patient Risk Stratification mappings are superseded.

Impact:

- No active contradiction. `task-architecture-package-v1.md` and `task-architecture-ratification.md` make the current four-workflow architecture authoritative.

Action required:

- None.

### Outdated phase-map language

Finding: MINOR HYGIENE ISSUE

`project/PHASE_MAP.md` still says synthetic file generation is out of scope until approval. This was accurate earlier and remains generally safe, but it does not reflect that Alexander has since explicitly authorized and locked Batch 1 synthetic world-level construction.

Impact:

- Low. `AGENTS.md`, `STATUS.md`, `WORKSPACE_FILE_MAP.md`, and `WORLD_SPEC_KICKOFF.md` all supersede it with the current Batch 1 locked / Batch 2 gated state.

Action required:

- Optional future cleanup: add a short note to `PHASE_MAP.md` that Korvin Merrow has explicit local authorization through Batch 1, while Batch 2 and downstream work remain gated.

### References to deleted/moved artifacts

Finding: NO ISSUE

No active references to moved Batch 1 candidate paths were found.

## 8. Collaboration Risk Assessment

Overall risk: LOW

Potential risks:

- MINOR HYGIENE ISSUE: old branch name `james-carter-brainstorm` may mildly confuse a new collaborator.
- MINOR HYGIENE ISSUE: `PHASE_MAP.md` still speaks broadly about synthetic generation being out of scope until approval.
- MINOR HYGIENE ISSUE: `WORLD_SPEC_KICKOFF.md` generic Stop Conditions section still says to stop before synthetic construction/generation, while its current-state sections correctly say Batch 1 is locked and Batch 2 is gated.
- ACCEPTABLE HISTORICAL REFERENCE: historical planning scaffolds still mention candidate states, TCM, and Patient Risk Stratification; they are clearly superseded by locked packages.
- NO ISSUE: current canonical paths and next eligible action are clear in the live status surfaces.

No hidden reliance on chat history was found for the current state.

## 9. Recommendations

Immediate fixes required before another collaborator can continue:

- None.

Optional hygiene improvements:

- Narrow `WORLD_SPEC_KICKOFF.md` Stop Conditions language from "synthetic file construction/generation" to "Batch 2 or later synthetic construction unless explicitly authorized."
- Add a current-state note to `project/PHASE_MAP.md` acknowledging explicit authorization through locked Batch 1 while preserving the Batch 2 gate.
- Rename branch only after Alexander approves the remote strategy.

No-action-needed items:

- Keep historical TCM / Patient Risk Stratification references because they document superseded workflow analysis.
- Keep the 20 vs 21 medication-count clarification because it preserves ratification history.
- Keep planning scaffolds in `planning-scaffolds/`; they are not active candidate artifacts.

Recommended next prompt after hygiene is confirmed:

```text
Batch 2 Synthetic World-Level File Construction authorized.

Use the locked Synthetic World-Level File Construction Plan v1 and locked File Inventory v1.
Construct only FI-W08 through FI-W13.
Preserve Batch 1 uncertainties, prednisone hierarchy, infection-vs-mixed-physiology uncertainty, medication-restart uncertainty, baseline-vs-admission-value separation, and all hierarchy ordering.
Do not create FI-W14 or later, task files, prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission materials.
```

## Final Determination

Repository Hygiene and Collaboration Readiness Audit

Status:
PASS WITH MINOR ISSUES

Recommended Next Action:
Proceed to Batch 2 Synthetic World-Level File Construction only after explicit Alexander authorization, or optionally perform the two minor documentation cleanups first.
