# Next-World DFI Hour Prep Packet

Date: 2026-06-12

Status: Planning draft only. This is not a Brainstorm submission, not a World Spec, not a world build, and not a platform artifact.

Single-writer window: Codex authored this packet under Alexander authorization. Claude is expected to review the built bytes after handoff, not the plan.

## Authority And Staleness

Live program authority sits above local mirrors. The live instruction document and live Task Selection sheet were not accessed in this run because Drive access was not separately authorized. Therefore all workflow priorities and claim counts below are marked:

PROVISIONAL stamps RESOLVED 6/12 evening: verified unchanged against the live sheet (see Live Guidance Gate below and the delta memo).

Local reading order used:

1. `WORKSPACE_FILE_MAP.md`
2. `DO-NOT-REPEAT.md`
3. `AGENTS.md`
4. `reference/world-spec-guidelines/POD-ANNOUNCEMENT-2026-06-10-delivery-day-and-operating-rules.md`
5. `reference/world-spec-guidelines/POLICY-2026-06-07-selfcontainment-and-file-separation.md`
6. `reference/workflows/_history-ondina-dfi/next-world-diabetic-foot-planning-canvas.md`
7. `reference/workflows/next-world-candidate-scorecard.md`
8. `reference/workflows/next-world-selection-proposal.md`
9. `reference/workflows/internal-medicine-world-planning-canvas.md`
10. `docs/task-structure-dossier.md`
11. `docs/task-difficulty-lessons.md`
12. `docs/abi-review-protocol.md`
13. `reference/checklists/brainstorm-checklist.md`
14. `reference/checklists/world-spec-checklist.md`
15. `reference/source/_superseded/task-selection-categories/task-selection-categories-snapshot-2026-06-10.csv`

No-repeat receipt carried into this packet:

- Tasks before files. The task slate and forced slots stay upstream of substrate.
- World files must be raw material, not answer-key synthesis.
- Wound photo is substrate only. KM08 already spent photo-as-headline trap.
- Same-author draft traps need true placeholders or a correction instruction.
- Bankability comes from a legitimate clinical or material failure, not from a raw score threshold.

## Live Guidance Gate

Outcome: CLOSED FOR BRAINSTORM SCOPE (update 2026-06-12 evening, Claude, Drive read-only pass authorized by Alexander). Findings and residual open items: `live-guidance-delta-memo-2026-06-12.md` in this folder. Headline: live doc is now (06/09), modified 6/12 16:16 UTC; all 13 workflow strings, priorities, and claim counts verified unchanged for Brainstorm purposes; 30-file minimum now in-doc and AutoQC-enforced; cutoff formalized as July 31 2025; "at least 3-5 distinct workflows" phrasing supports the Option A disagreement note. Gate remains open only for: full 06/09 re-mirror before Phase 2, the new in-doc worked examples before Phase 3/4, and one undecoded alternate claim cell.

(Original 6/12 hour-run outcome, superseded: OPEN GATE. Drive access was not authorized during the hour; all workflow priorities and claim counts were marked provisional pending this verification.)

## 2.107 Workflow Options Matrix

Decision owner: Alexander. Codex is only presenting options.

Constraint tension:

- The DFI slate wants 10 clinically distinct deliverables across 7 structures.
- World Spec AutoQC check 2.107 targets 3 to 5 distinct catalog workflows per world.
- Exact clinical fit currently points toward more than 5 workflow strings.

### Base Exact-String Mapping

VERIFIED 2026-06-12 against the live Task Selection sheet: all strings verbatim, priorities and claim counts unchanged (one Option B alternate cell undecoded; snapshot value carried). Note: claim annotations trace to exemplar Worlds 001-003, not live pod contention.

| Task | Structure | Current deliverable | Exact tracker string option | Priority | Claims | Fit |
|---|---|---|---|---|---:|---|
| 1 | S2 forced inventory | Discharge med-rec safety table | Discharge Medication Reconciliation | P0 | 1 | Strong |
| 2 | S2 forced inventory | Physician coding attestation against HIM worksheet | Inpatient Medical Coding and DRG Assignment | P0 | 0 | Strong |
| 3 | S3 external | Attending CDI query response | Clinical Documentation Improvement (CDI) Query Response Review | P0 | 0 | Strong |
| 4 | S3 external | Physician appeal for DME, SNF, or inpatient days | Claims Denial Analysis and Appeal Preparation | P0 | 0 | Strong |
| 5 | S3 external | Physician/pharmacist response to pharmacy rejection | Pharmacy Insurance Claim Rejection Resolution | P0 | 0 | Strong |
| 6 | S4 determination | Physician advisor status or continued-stay determination | Utilization Review Concurrent Stay Documentation | P1 | 0 | Strong if the task is continued stay. Use `Inpatient vs observation determination` P1, claims 0, only if the task is admission status. |
| 7 | S5 abstraction | Fixed-field diabetes quality or HCC abstraction | HEDIS Medical Record Chart Abstraction and Review | P0 | 0 | Strong for quality abstraction. Use `Hierarchical Condition Category (HCC) Risk Coding Review` P1, claims 0, only if risk adjustment is the center. |
| 8 | S6 synthesis with embedded forced table | Vascular or wound-care referral letter | Specialist Referral Letter and Documentation Preparation | P0 | 0 | Strong |
| 9 | S7 investigation | Missed-offloading safety review | Patient Safety Event Investigation and Root Cause Analysis | P0 | 1 | Strong |
| 10 | S1 completion | Finalize discharge instructions from started draft | Medical Transcription and Clinical Documentation Completion | P0 | 1 | Strong only if the task truly finalizes a started clinical document with true placeholders. |

Distinct workflow count: 10 if every task uses the strongest exact fit.

### Option A: Clinically Exact Mapping

Use the base exact-string mapping above.

Tradeoff:

- Best clinical and reviewer clarity.
- Best defense against "workflow invented" or "wrong workflow" feedback.
- Likely conflicts with check 2.107 if it is enforced as more than a target.

Pre-drafted note if Alexander chooses this:

The world uses more than five workflow strings because the task slate intentionally spans medication reconciliation, coding, CDI response, denial appeal, pharmacy rejection, utilization review, abstraction, referral, RCA, and document completion. Consolidating these would make several deliverables less realistic and would blur physician-facing work products. The structure variety is intentional and each task still names its S-structure and forced slot.

### Option B: Strict 3 To 5 Workflow Consolidation

Consolidate related administrative tasks under broader tracker strings.

Candidate grouping:

| Workflow string | Tasks grouped |
|---|---|
| Discharge Medication Reconciliation | Task 1 |
| Inpatient Medical Coding and DRG Assignment | Task 2 and possibly Task 7 if HCC/HEDIS is redesigned as coding audit |
| Clinical Documentation Improvement (CDI) Query Response Review | Task 3 |
| Claim Denial Root Cause Analysis and Appeal Preparation | Tasks 4 and 5 if pharmacy rejection is reframed as a claim denial workqueue problem |
| Specialist Referral Letter and Documentation Preparation | Task 8 |

Tradeoff:

- Better 2.107 optics.
- Weakens Task 5 unless the pharmacy rejection is rewritten as a claim-denial workflow.
- Leaves Tasks 6, 9, and 10 needing redesign or placement under less precise strings.
- Risks monotony by hiding distinct structures under broad labels.

Alexander decision needed: whether the workflow-count gate is worth the loss of exact clinical fit.

### Option C: Hybrid With A Disagreement Note

Use exact strings for tasks where consolidation would change the deliverable, while consolidating only obvious denial-family surfaces.

Likely count: 8 or 9 distinct workflow strings.

Tradeoff:

- Preserves most clinical realism.
- Reduces the optics problem only slightly.
- Still needs a deliberate disagreement note for 2.107.

Alexander decision needed: choose Option A, B, or C after live-sheet verification.

## Canvas Gap Audit

### Supplementary File Candidates

These are noise-only candidates. They carry no trap content and must pass the removal test: deleting them should not change any correct answer.

| Candidate | Scope | Purpose | Removal test | Status |
|---|---|---|---|---|
| Generic diabetes foot-care education handout | World-level supplementary | Realistic discharge education noise | Removing it changes no medication, coding, CDI, vascular, or placement answer | OPEN FOR ALEXANDER |
| Generic hospital fall-prevention handout | World-level supplementary | Adds routine inpatient discharge packet texture | Removing it changes no offloading, DME, PT/OT, or safety-review answer | OPEN FOR ALEXANDER |
| Generic nutrition and diabetes plate-method handout | World-level supplementary | Adds common education material without patient-specific targets | Removing it changes no insulin, wound-healing, or malnutrition conclusion | OPEN FOR ALEXANDER |
| Generic home-health agency welcome sheet | World-level supplementary | Adds case-management noise without acceptance or denial facts | Removing it changes no payer, SNF, DME, or home-readiness answer | OPEN FOR ALEXANDER |

90/10 note: with 30 essential world-level files, 3 supplementary world-level files is the cleanest mix. If the essential file count lands at 32 to 33, 3 or 4 supplementary files remains acceptable.

### Source Board Leakage Audit

| Source-board row or group | Leakage risk | Action |
|---|---|---|
| 11 MRI foot report or radiology addendum | High if it declares osteomyelitis definitively while the task depends on uncertainty | Keep raw radiology wording. Do not write final coding conclusion into the report. |
| 12 bedside wound photo | High if used as headline trap again | Use as substrate only. It supports wound context but is not the central scored failure. |
| 16 pathology report | High if it resolves osteomyelitis before CDI/coding tasks need uncertainty | Decide osteomyelitis posture first. If pathology resolves it, use that resolution only for tasks anchored after the result would exist. |
| 19 infectious disease consult | High if it becomes the final antibiotic answer key | Keep it recommendation-level and time-bound. Avoid a polished final discharge antibiotic plan in shared world files. |
| 28 payer communication note | High if it writes the appeal answer into world files | Put actual denial or criteria pressure at task level unless every task needs it. |
| 29 CDI query draft or CDI note | High if shared world-level | Hold task-level for the CDI response task. Do not mount shared if it pre-answers the stance. |
| 30 HIM preliminary coding worksheet | High if shared world-level | Hold task-level for the coding task. External worksheet is fair by genre when scoped to that task. |
| 33 discharge planning checklist | Medium if it becomes a final disposition answer | Keep as raw checklist of incomplete equipment and teaching steps, not a final readiness conclusion. |

### Snapshot And Anchor Options

Exact dates are OPEN FOR ALEXANDER. These are timing patterns, not decisions.

| Option | Pattern | Pros | Risks |
|---|---|---|---|
| A | Snapshot at discharge morning, with same-day afternoon tasks plus later post-discharge administrative tasks | Natural for med rec, discharge instructions, referral, payer/DME, and pharmacy rejection | Must be careful that same-day tasks occur strictly after snapshot by time of day |
| B | Snapshot one day after debridement, with all tasks after a frozen post-op record | Good for source-control uncertainty and continued-stay review | May weaken discharge and post-acute payer tasks unless the timeline is extended |
| C | Snapshot at medically improving but operationally unstable point, with tasks in the following week | Strong for UR, payer, DME, and safety-review surfaces | Requires careful world-file chronology so no task sees future documents |

Anchor pattern for a 10-task slate:

- Immediate post-snapshot: med rec, coding attestation, discharge instructions.
- 2 to 5 days post-snapshot: CDI response, pharmacy rejection, utilization review or payer appeal.
- 1 to 3 weeks post-snapshot: quality abstraction, referral, RCA.

## Phase 1 Worksheets

Derivation rule: rows below are derived from the canvas, scorecard, and proposal. Cells requiring new clinical facts are marked OPEN FOR ALEXANDER.

### 1a. Structure And Forced-Slot Worksheet

| Task | Structure | Forced slot | Derived from | Open item |
|---|---|---|---|---|
| 1 med rec | S2 forced inventory | Every medication row needs continue, hold, change, stop, or defer | Canvas task 1 and trap ledger renal dosing | Exact med list and antibiotic choices OPEN FOR ALEXANDER |
| 2 coding | S2 forced inventory | Principal diagnosis, POA, code family, and support status per row | Scorecard task 2 and canvas code-family trap | Coding rows and exact external HIM stance OPEN FOR ALEXANDER |
| 3 CDI response | S3 external | Agree, decline, unable to determine, or clarify item by item | Scorecard task 3 and KM10 lesson | Query items and clinical stance OPEN FOR ALEXANDER |
| 4 payer appeal | S3 external | Appeal, accept, or narrow appeal | Scorecard task 4 and canvas payer friction | Appeal center OPEN FOR ALEXANDER |
| 5 pharmacy rejection | S3 external | Substitute, appeal, hold, or exception request | Scorecard task 5 and renal substitute trap | Drug, formulary alternative, and contraindication OPEN FOR ALEXANDER |
| 6 status or continued stay | S4 determination | Binding status, level-of-care, or continued-stay verdict | Scorecard task 6 and designed borderline note | Choose continued stay versus inpatient/observation OPEN FOR ALEXANDER |
| 7 abstraction | S5 abstraction | Each field needs value, exclusion, or unable to determine | Scorecard task 7 and lookback trap | Choose HEDIS versus HCC center OPEN FOR ALEXANDER |
| 8 referral | S6 synthesis with table | Required disposition table forces source control, perfusion, antibiotics, offloading, and follow-up status | Scorecard task 8 and KM07 table lesson | Receiving service and table fields OPEN FOR ALEXANDER |
| 9 safety review | S7 investigation | Attribution and prevention finding | Scorecard task 9 and offloading safety trap | Event definition OPEN FOR ALEXANDER |
| 10 completion | S1 completion | Started draft has true placeholders for the scored decision | Scorecard task 10 and A0.4/A0.5 | Draft genre and placeholder line OPEN FOR ALEXANDER |

### 1b. Trap Pairing And Fairness Worksheet

| Task | Primary trap pairing | Fairness route | Reviewer-risk control |
|---|---|---|---|
| 1 | Renal antibiotic dosing plus culture provenance | Forced inventory | Chart must clearly contradict copied admission eGFR dose or unsafe substitute |
| 2 | Diabetic ulcer versus pressure injury plus osteomyelitis POA | Forced inventory with external HIM surface if task-level | Do not make sepsis-to-principal the core |
| 3 | Unsupported osteomyelitis specificity or sepsis severity language | External CDI query wrong by genre | Must answer why the record does or does not support the condition |
| 4 | Vascular adequacy and offloading logistics underweighted by denial | External payer denial wrong by genre | Denial must be plausible but rebuttable from raw PT/OT, vascular, and case-management sources |
| 5 | Formulary substitute unsafe for renal function, QT, allergy, or interaction | External pharmacy rejection wrong by genre | Must not depend on post-July-2025 drug or policy knowledge unless attached |
| 6 | Improvement after debridement mistaken for safe lower level of care | Determination slot | Case must be genuinely borderline, not obvious |
| 7 | Quiet lookback-window or denominator disqualifier | Forced abstraction fields | Must be chart-contradicted, not chart-silent |
| 8 | Pleasant referral omits unresolved limb-threat disposition | Embedded forced table | Referral cannot be pure from-scratch synthesis |
| 9 | Single-person blame when chart shows system/process causes | Investigation attribution | Review genre is warm, so expect mid difficulty unless forced attribution is sharp |
| 10 | Same-author draft closure on unsafe or unsupported decision | True placeholder or correction instruction | Built-byte fairness gate must quote no scored assertion |

### 1c. Three-Condition Floor Check

Condition set: cold, forced, chart-contradicted or chart-mandated.

| Task | Cold plan | Forced plan | Contradiction needed | Floor confidence before build |
|---|---|---|---|---|
| 1 | Renal dosing is background to infection narrative | Med rows force decision | Updated eGFR and ID/pharmacy notes must contradict copied dose | Medium-high |
| 2 | Code-family distinction is quieter than limb infection headline | Coding rows force values | Treating documentation must support one family and not the other | High |
| 3 | Specificity pressure hides inside query language | Query forces stance | Imaging/pathology/treating notes must not support over-specific diagnosis | High if query is balanced |
| 4 | Payer denial focuses on cost or criteria, not full function | Appeal forces stance | PT/OT/offloading/vascular evidence must rebut denial | High |
| 5 | Formulary substitute looks administratively easy | Reject response forces action | Renal/QT/allergy/interaction evidence must rebut substitute | Medium-high |
| 6 | Post-procedure improvement warms the discharge direction | Verdict slot forces classification | Functional or vascular data must contradict readiness | Medium |
| 7 | Measure lookback is quiet | Fixed fields force values | Date or exclusion must contradict naive capture | Medium-high |
| 8 | Referral prose can drift high unless table forces dispositions | Table forces unresolved statuses | Chart must show at least one unresolved limb-threat item | Medium |
| 9 | Review genres are warm by nature | Attribution finding forces conclusion | Timeline must contradict single-cause blame | Medium-low |
| 10 | Completion can be cold if placeholder is neutral | Draft slot forces closure | Chart must mandate restraint and draft must assert nothing | Medium if built cleanly |

### 1d. Difficulty Forecast And KM Sibling Risk

| Task | Likely difficulty | KM sibling risk | Risk mitigation |
|---|---|---|---|
| 1 | Medium-high | KM01 med rec and KM07 held-med closure | Use renal antibiotic/culture hierarchy, not a held-med soft closure |
| 2 | High | KM09 sepsis-to-principal | Center diabetic-ulcer code family and osteomyelitis POA, not sepsis sequencing |
| 3 | High | KM10 CDI overreach | Avoid encephalopathy-style query. Make the why explicit in golden later |
| 4 | High | None major | Payer denial is fresh if grounded in DME, offloading, SNF, or vascular risk |
| 5 | Medium-high | Medication safety can become too warm | Hide the risk in substitute selection, not obvious recall |
| 6 | Medium | KM08 inpatient-vs-observation too easy | Must design a true borderline case if using this structure |
| 7 | Medium-high | None major | Measure logic should be fixed-field and date-dependent |
| 8 | Medium | KM07 from-scratch synthesis too easy | Embed disposition table so deferral is not free |
| 9 | Medium-low | KM06 safety-review axis too warm | Treat as variety slot unless attribution is sharply forced |
| 10 | Medium | KM07 and KM08 draft-fairness | True placeholder only, built-byte gate before any pilot |

## Decision Pack For Alexander

STATUS UPDATE 2026-06-12 late: all five blocking decisions RESOLVED by Alexander. Decisions recorded verbatim in `next-world-dfi-decision-record-2026-06-12.md`; Brainstorm drafted from them at `next-world-dfi-brainstorm-draft-v1.md` (awaiting his read-and-own pass). Summary: 68F Spanish-preferred, MA plus Medicaid dual, second-floor walk-up, night-shift daughter support; snapshot Pattern C at HD6 evening (improving but operationally unsafe); workflow Option A exact mapping with disagreement note; payer axis is the MA SNF-authorization denial; osteomyelitis stays equivocal and unsupported unless the treating clinician clarifies. The tables below are retained as the option history.

### Blocks Brainstorm

| Decision | Why it blocks | Options to choose or revise |
|---|---|---|
| Patient identity basics | Brainstorm world setup needs patient shape | Age, sex, language, insurance, home setting, caregiver context |
| World snapshot and task anchor pattern | Temporal anchoring is a hard gate | Choose one timing pattern from the snapshot options or supply another |
| Workflow consolidation posture | Determines rough task table and 2.107 risk | Option A clinically exact, Option B strict 3 to 5, Option C hybrid |
| Payer appeal center | Task 4 and source geometry depend on it | SNF days, DME/offloading device, wound VAC, home health, or inpatient days |
| Osteomyelitis uncertainty design | CDI and coding traps depend on whether osteomyelitis is unsupported, uncertain, or confirmed late | Unsupported specificity, equivocal imaging, pending pathology, or confirmed after a later anchor |

### Can Wait Until World Spec

| Decision | Why it can wait |
|---|---|
| Exact provider names and roster | Brainstorm needs stakeholder classes, not names |
| Exact lab values and medication doses | Brainstorm should not carry file-level values |
| Exact vascular modality | Brainstorm can say vascular study/perfusion evidence unless Alexander wants ABI/TBI locked early |
| Photo creation or acquisition method | Modality can defer. The guardrail is already set: photo is substrate only and needs agent plus grader visibility later |
| Exact supplementary file filenames | Brainstorm should not include file inventory |
| Exact task-level external document filenames | Brainstorm can name document types only |

## Verification Log

Checks performed locally:

- Brainstorm checklist alignment: PASS for concept scope if this packet is compressed before submission. The packet itself is too detailed for Brainstorm, as intended.
- World Spec checklist preflight: PASS as a planning surface. Still not a spec. The 30 world-level file minimum is carried.
- Workflow exact-name scan: PASS for options matrix, with all claim counts marked provisional.
- Structural variety: PASS. S1, S2, S3, S4, S5, S6, and S7 are represented. Completion capped at one task.
- Draft-fairness guardrail: PASS as a plan. Task 10 remains placeholder-only and OPEN FOR ALEXANDER.
- Cross-world redundancy guardrail: PASS as a plan. No photo-as-headline, no sepsis-to-principal core, no encephalopathy-style CDI core.
- Answer-key leakage scan: PASS as a plan. High-risk world-level files are identified for raw-only or task-level treatment.
- Supplementary-file removal test: PASS for listed candidates, pending Alexander approval.
- Banned dash scan: PASS for this packet. `WORKSPACE_FILE_MAP.md` contains pre-existing navigation arrows and dash characters from older repo register; Codex did not normalize the full map during this no-build hour.
- World-folder leak check: PASS. No new diabetic-foot or DFI world folder was created.
- File-map indexing: PASS. This packet is indexed in `WORKSPACE_FILE_MAP.md`.

## Handoff State

Branch at start: `korvin-merrow-brainstorm`

HEAD at start: `eec790e641f35774e6db0888ce39d6af78302360`

Live-doc diff: OPEN GATE. No Drive access used.

Commit status: no commit authorized.

Platform status: no platform action taken.

Build status: no world folder, DOCX, prompt, golden, grader, image, or task artifact created.

Uncommitted state note: this packet and the file-map index update are uncommitted. Several unrelated modified files and untracked next-world planning files were already present at start of run and are preserved.
