# Stacey Corrections Recovery Report

Date: 2026-06-03
Type: Findings-only audit. No files modified, no ratifications created, no architecture created.
Method: Located every reviewer/Stacey/correction/feedback/reconciliation signal in the workspace, then verified each correction against current **locked** Korvin Merrow artifacts. Corrections were not assumed resolved.

Search surface covered: `worlds/korvin-merrow/reviews/`, `worlds/korvin-merrow/remediation/`, `world-spec-prep/reviews/`, ratifications, `reviewer-feedback.md`, `reviewer-go-01.md`, claude-package handoff files, physician decision logs, `active/clinical-logic.md`, `WORLD_SPEC_KICKOFF.md`, `AGENTS.md`, `STATUS.md`, transcript artifacts, and keyword sweeps for Stacey / reviewer / correction / feedback / required change / reconciliation / audit finding / SEND BACK.

---

## A. Stacey S - Human Brainstorm Review: SEND BACK (the primary corrections)

Source file: `worlds/korvin-merrow/reviews/reviewer-feedback.md` (lines 24-38)
Date: 2026-05-29
Reviewer: Stacey S - RL Studio status "Writer Actions / Start Plan Fixes"

Four required revisions were issued. Each is assessed below.

### A1 - Replace patient name with unmistakably fictional "Korvin Merrow"
Quoted: *"Replace prior common patient name with unmistakably fictional name 'Korvin Merrow' and update all references including document title."*

- Resolution Status: **RESOLVED**
- Resolution Evidence:
  - `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md` section 1 Patient Profile - "Patient name | Korvin Merrow", "MRN | KM-6427819".
  - `worlds/korvin-merrow/world-spec-prep/locked/identity-package-v1.md` (LOCKED identity).
  - `worlds/korvin-merrow/history/rename-audit.md` (James Carter -> Korvin Merrow migration audit); `project/IDENTITY_MIGRATION_LOG.md`.
  - All FI-W/FI-T/FI-S locked files use "Korvin Merrow".
- Remaining Impact: None. Spec population uses the locked name throughout.

### A2 - Add formal declaration: World Type: Typical Clinical World
Quoted: *"Add formal declaration: `World Type: Typical Clinical World`."*

- Resolution Status: **RESOLVED**
- Resolution Evidence: `world-spec-v1.md` section 1 Patient Profile table - "World Type | Typical Clinical World"; also stated in section 1 Big Picture Summary.
- Remaining Impact: None.

### A3 - Expand comorbidity burden above the 10+ threshold
Quoted: *"Expand comorbidity burden above the 10+ threshold. Reviewer suggested hyperlipidemia, anemia of CKD, osteoporosis from chronic prednisone, sleep apnea, and diabetic peripheral neuropathy."*

- Resolution Status: **RESOLVED** (exceeds requirement)
- Resolution Evidence: `world-spec-v1.md` section 1 Comorbidity Profile - "contains 14 conditions." All five reviewer-suggested additions present: hyperlipidemia (#4), diabetic peripheral neuropathy (#7), obstructive sleep apnea (#8), anemia of CKD (#10), osteoporosis/osteopenia from chronic steroid exposure (#11). Cross-checked against `world-spec-prep/locked/comorbidity-expansion-package-v1.md` and `remediation/reviewer-comorbidity-decision-brief.md`.
- Remaining Impact: None. 14 >= 10 threshold.

### A4 - Add specific medication names and doses
Quoted: *"Add specific medication names and doses because current traps mention medication categories but no specific agents."*

- Resolution Status: **PARTIALLY RESOLVED** - this is the one open item with downstream impact.
- What IS resolved:
  - Specific medication **names** are locked: `world-spec-v1.md` section 1 Medication Architecture lists 20 named agents; `world-spec-prep/locked/medication-expansion-package-v1.md` (20 medications, "18-22 target range") - satisfies the polypharmacy (15+) marker.
  - Doses with route/frequency were approved at **Brainstorm level**: `remediation/reviewer-remediation-compliance-review.md` (lines 77-90) - e.g., sacubitril/valsartan 24/26 mg BID, carvedilol 12.5 mg BID, furosemide 40 mg daily, spironolactone 25 mg daily, empagliflozin 10 mg daily, aspirin 81 mg, atorvastatin 40 mg, metformin ER 500 mg BID, insulin glargine 18 units nightly, alendronate 70 mg weekly, gabapentin 300 mg nightly. These are also in `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx`.
- What is NOT yet resolved:
  - The **locked World Spec architecture deliberately omits doses.** `world-spec-v1.md` Medication Architecture: *"does not create final medication doses, frequencies, schedules."* `medication-expansion-package-v1.md` carries no dose/route/frequency/indication. Verified: locked synthetic files FI-W04 (initial med rec) and FI-W05 (pharmacy refill) contain **no numeric dose tokens** - medications are listed by name only, and prednisone dose is intentionally ambiguous (Trap #1 substrate).
  - World Spec AutoQC v6.3 **check 2.12** requires the World Spec home-medication list to include **every drug with dose, route, frequency, and indication** (cited in `reviewer-remediation-compliance-review.md` line 15; `reference/world-spec-guidelines/08_autoqc_master_index.md`).
- Remaining Impact Assessment:
  - Affects spec population? **YES.** The World Spec DOCX must include a complete home-medication table with dose/route/frequency/indication, sourced from the brainstorm-approved doses - except prednisone, whose dose ambiguity must remain (intentional trap).
  - Affects task generation? No (task prompts/goldens are locked and dose-aware at reasoning level).
  - Affects AutoQC? **YES** - World Spec AutoQC 2.12 will flag a dose-less medication list.
  - Affects submission? Indirectly - World Spec must pass AutoQC before/at upload.

---

## B. Stacey S - Human Brainstorm Review: GO (approval record)

Source: `worlds/korvin-merrow/reviews/reviewer-go-01.md` and `reviewer-feedback.md` (lines 3-22)
Date: 2026-05-30
Quoted: *"great job! I approved your brainstorm. Next steps are to move forward with world spec and file template development."*

- Status: Approval, not a correction. SEND BACK remediation accepted; AutoQC rerun 0 failed / 51 passed (`reviews/brainstorm-autoqc-02.md`). No further Stacey corrections were issued after GO.
- Note: No **World Spec** human review by Stacey exists yet (World Spec not yet submitted). Any post-World-Spec Stacey corrections are **NOT FOUND IN WORKSPACE** because that review has not occurred.

---

## C. Claude Hostile-Reviewer Pass 01 - accepted corrections (reviewer-risk pre-emption)

Source: `worlds/korvin-merrow/reviews/claude-brainstorm-review-01.md` (findings) and `claude-brainstorm-review-response-01.md` (applied changes). These are reviewer-style corrections accepted by Codex to pre-empt a predicted send-back; verified against locked World Spec.

### C1 - Reclassify "Trap 7" as a discharge source-hierarchy trap distinct from Trap 3
Quoted (response): *"Reframed as discharge plan source-hierarchy trap... a reassuring discharge planning artifact may be misleading if read without meds, consultant recs, PT/nursing, and family communication."*
- Status: **RESOLVED** - `world-spec-v1.md` section 4 Trap #5 "Discharge Source-Hierarchy," with explicit text: *"This trap is distinct from Trap #3."*

### C2 - Merge redundant Trap 4 into Trap 2 (HF-AKI + time-sensitive consultant)
- Status: **RESOLVED** - `world-spec-v1.md` section 4 Trap #2 "HF/AKI Medication Reconciliation And Time-Sensitive Consultant Logic."

### C3 - Fold generic Trap 5 into sepsis anchoring
- Status: **RESOLVED** - `world-spec-v1.md` section 4 Trap #4 "Sepsis Anchoring After Partial Improvement" (absorbs trend/snapshot mechanism). Net result: exactly 5 traps, no redundancy.

### C4 - Confirm Endocrinology as a friction (advocacy), not a documentation trap
Quoted: *"Endocrinology friction requires explicit consult recommendation or documented position; steroid record ambiguity remains Trap 1."*
- Status: **RESOLVED** - `world-spec-v1.md` section 3 "Endocrinology vs Primary Team": *"The steroid-record discrepancy is a trap, not a friction participant. The human friction is risk interpretation between Endocrinology and the Primary Team."* Endocrinology advocacy carried in locked FI-W16 (Endocrinology consult).

### C5 - Steroid reveal guardrail (no hidden adrenal insufficiency)
- Status: **RESOLVED** - `world-spec-v1.md` Trap #1 and section 6: *"avoids making adrenal insufficiency the hidden answer"*; mixed-physiology design preserved (infection, AKI, meds, deconditioning, steroid one contributor).

### C6 - Task competency separation
- Status: **RESOLVED** - `worlds/korvin-merrow/active/task-map.md` and `world-spec-prep/locked/task-architecture-package-v1.md`: 6 tasks across 4 distinct workflows with distinct competencies/requesters/anchors.

### C7 - Open structural items: workflow mapping + P0/P1 labels; earlier-course task
Quoted: *"confirm approved-workflow mapping and P0/P1 labels... and confirm each discharge-cluster task tests a distinct competency or spread the temporal anchoring."*
- Status: **RESOLVED / CLARIFIED**
  - Workflow mapping locked in `task-map.md` (4 authoritative workflows).
  - P0/P1/P2 labels: clarified as **tracker-provenance metadata only, not governing architecture** (`project/STATUS.md`; `task-map.md` "Historical Brainstorm-Level Mapping").
  - "Add an earlier-course task": **deferred by design** (`claude-brainstorm-review-response-01.md` "Suggestions Not Applied" - adding a task would exceed locked physician decisions). This is an intentional decision, not an unresolved defect.
- Remaining Impact: None blocking. Task generation already complete and locked.

---

## D. Identity Package Hostile-Review Addendum - carry-forward corrections

Source: `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md` (2026-05-31, carry-forward notes; Identity Package v1 remains LOCKED).

### D1 - Treat lisinopril cough as ACE-inhibitor intolerance; avoid accidental restart
- Status: **RESOLVED** - `world-spec-v1.md` section 1 "Allergy / intolerance | Lisinopril (cough)"; `medication-expansion-package-v1.md` notes sacubitril/valsartan "Fits established HFrEF and prior ACE-inhibitor intolerance history." Avoid-restart is preserved as a design rule in the locked medication architecture.

### D2 - ARNI therapy needs a coherent prior ACE-inhibitor transition history
- Status: **RESOLVED** - ACE-inhibitor/ARNI/lisinopril transition history is represented in locked synthetic files FI-W01, FI-W03 (admission H&P), and FI-W07 (primary-care baseline), plus the medication package.

### D3 - Baseline anchors must be explicitly placed
- Status: **RESOLVED** - `world-spec-v1.md` section 1 baseline anchors: creatinine 1.6-1.8 mg/dL, eGFR ~40-50, hemoglobin 10.5-11.5 g/dL, A1c 7.6-8.2%, dry weight ~97 kg, baseline mobility/cognition. Source: `world-spec-prep/locked/baseline-anchor-package-v1.md`.

---

## E. Internal Submission Notes - carry-forward corrections for World Spec

Source: `worlds/korvin-merrow/reviews/reviewer-feedback.md` (lines 74-87, "Internal Submission Notes").

### E1 - Confirm workflow mapping and P0/P1 labels once tracker available
- Status: **RESOLVED** - labels assigned in `active/task-map.md` from `reference/source/_Task Selection Categories For Team.xlsx`; P0/P1 clarified as provenance metadata (see C7).

### E2 - Keep the world snapshot at/near discharge so tasks branch after the course
- Status: **RESOLVED** - `world-spec-v1.md` world close HD6 05/23/2026 18:00 during discharge planning; post-world task anchors (05/24, 05/31, 06/23).

### E3 - Avoid an over-authoritative final discharge synthesis in the World Spec
- Status: **RESOLVED** - Trap #5 design keeps the discharge-facing artifact "reassuring but incomplete"; locked FI-W22 is the visible-but-incomplete snapshot. `governance-package-v1.md` carries the rule.

### E4 - Define exact lab trends, medication changes, consultant-note timing, and discharge-artifact hierarchy in the World Spec
- Status: **PARTIALLY RESOLVED**
  - Resolved structurally: consultant timing, source-of-truth hierarchies, and trend *structure* are defined in `world-spec-v1.md` section 2 / section 1, and concrete numeric lab trends exist in locked FI-W12 (renal/infection/hemodynamic trend source) and FI-W13 (MAR/medication-action source).
  - Open: exact **medication-change doses** are not in the World Spec prose (ties directly to A4). The World Spec references trend values via FI-W12 rather than enumerating them in the spec body.
  - Remaining Impact: Affects spec population (whether AutoQC wants concrete trend/medication anchors surfaced in the spec). Same dose-table action as A4; trend values themselves are available in locked files.

---

## NOT FOUND IN WORKSPACE

- Any **World Spec-stage** Stacey/pod-lead correction: NOT FOUND - the World Spec has not been submitted for human review yet, so no such review exists.
- Any reviewer correction issued **after** the 2026-05-30 GO: NOT FOUND - GO was the last reviewer action; only internal/Claude hostile-review and carry-forward notes follow.
- No `reconciliations/` top-level folder exists; reconciliation items live under `file-inventory/reviews/` (FI-T, FI-W20, supplementary trap-5 reconciliations) and were checked - they are internal consistency reconciliations, not Stacey corrections, and are all marked resolved/locked.

---

## Final Summary Table

| Correction | Source (date) | Status | Evidence (locked) | Action Required |
| --- | --- | --- | --- | --- |
| A1 Fictional name "Korvin Merrow" | reviewer-feedback.md (05-29) | RESOLVED | world-spec-v1 section 1; identity-package-v1; rename-audit | None |
| A2 World Type: Typical Clinical World | reviewer-feedback.md (05-29) | RESOLVED | world-spec-v1 section 1 Patient Profile | None |
| A3 Comorbidity 10+ | reviewer-feedback.md (05-29) | RESOLVED | world-spec-v1 section 1 (14 conditions); comorbidity-expansion-package-v1 | None |
| A4 Specific medication names + doses | reviewer-feedback.md (05-29) | PARTIALLY RESOLVED | Names: world-spec-v1 section 1 (20 meds). Doses: brainstorm compliance-review only; absent from locked spec & FI-W04/05 | **Add full home-med dose/route/frequency/indication table during World Spec population (AutoQC 2.12); keep prednisone dose ambiguous** |
| B Brainstorm GO | reviewer-go-01.md (05-30) | RESOLVED (approval) | brainstorm-autoqc-02 (0/51); reviewer-go-01 | None |
| C1 Trap reclassification (Trap 5 vs 3) | claude-brainstorm-review-01 | RESOLVED | world-spec-v1 section 4 Trap #5 | None |
| C2 Merge Trap 4->Trap 2 | claude-brainstorm-review-01 | RESOLVED | world-spec-v1 section 4 Trap #2 | None |
| C3 Fold Trap 5->sepsis anchoring | claude-brainstorm-review-01 | RESOLVED | world-spec-v1 section 4 Trap #4 | None |
| C4 Endocrinology = friction (advocacy) | claude-brainstorm-review-01 | RESOLVED | world-spec-v1 section 3; FI-W16 | None |
| C5 Steroid reveal guardrail | claude-brainstorm-review-01 | RESOLVED | world-spec-v1 Trap #1 / section 6 | None |
| C6 Task competency separation | claude-brainstorm-review-01 | RESOLVED | task-map.md; task-architecture-package-v1 | None |
| C7 Workflow/P0-P1 + earlier task | claude-brainstorm-review-01 | RESOLVED / CLARIFIED | task-map.md; STATUS.md | None (earlier-task intentionally deferred) |
| D1 ACE-I intolerance (no restart) | identity-package-review-addendum | RESOLVED | world-spec-v1 section 1 allergy; medication-expansion-package-v1 | None |
| D2 ARNI transition history | identity-package-review-addendum | RESOLVED | FI-W01/W03/W07; medication-expansion-package-v1 | None |
| D3 Baseline anchors placed | identity-package-review-addendum | RESOLVED | world-spec-v1 section 1; baseline-anchor-package-v1 | None |
| E1 Confirm workflow + P0/P1 | reviewer-feedback.md notes | RESOLVED | task-map.md | None |
| E2 Snapshot near discharge | reviewer-feedback.md notes | RESOLVED | world-spec-v1 (HD6 close) | None |
| E3 No over-authoritative discharge synthesis | reviewer-feedback.md notes | RESOLVED | world-spec-v1 Trap #5; FI-W22; governance-package-v1 | None |
| E4 Exact lab trends/med changes/timing/hierarchy | reviewer-feedback.md notes | PARTIALLY RESOLVED | Trends in FI-W12/W13; hierarchy in world-spec-v1; doses absent from spec | Surface medication doses + any required trend anchors at spec population (see A4) |

## Bottom line

Of the recovered corrections, **all are resolved except A4 and the dose-portion of E4**, which are the same underlying item: the brainstorm-approved medication **dose/route/frequency/indication** detail has not been carried into the locked World Spec (by design), and World Spec AutoQC check 2.12 will require it. This is the one correction that materially affects World Spec population and World Spec AutoQC. The prednisone dose must intentionally remain ambiguous (Trap #1). No reviewer correction is unaccounted for; no World Spec-stage reviewer corrections exist yet because that review has not occurred.
