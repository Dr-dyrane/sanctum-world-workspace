# Task Structure Dossier - structural variety per world (standing reference)

Date: 2026-06-10. Mandate source, Abi (pod lead), verbatim: "would recommend future task not all follow the same structure of draft and finalize. We want to see a variety of tasks in your world and not a monotony, this is also an ask of the client."

Standing rule (Alexander, 6/10): **every world carries at least 5 distinct structural categories.** Sheet snapshot this dossier maps against: `reference/source/task-selection-categories-snapshot-2026-06-10.csv` (232 workflows with claim counts; confirm against the live sheet at claim time). Companions: `docs/task-difficulty-lessons.md` (the cold-axis playbook), `worlds/korvin-merrow/task-setup/task8/design/KM08-PLAN.md` (the derived floor rule).

## 1. The KM autopsy: why ideas got hard

Every KM task reduces to two structures: forced-inventory (KM01 med rec) and draft-and-finalize completion (KM02, KM03, KM04, KM05, KM06, KM08, and KM07 v2). Variety attempts cleared because difficulty was retrofitted onto a world whose substrate scripts the correct answers: KM06 orthostatic 93, KM06 echo 97, KM05 NSAID 95, KM07 from-scratch 93.8, KM08 status 96.4. The root cause is sequencing, not imagination: the world was built first and the structures chosen after, so the only difficulty lever left was the completion wrapper. The fix is to pick the 5+ structures at BRAINSTORM time and design the world substrate to arm each one.

## 2. Structure taxonomy - eight shapes, each with its native forcing function

Difficulty law (unchanged): difficulty = a forced move the model's competence plays wrong. Structures differ in WHERE the forced move comes from. Variety is satisfied at the structure level while the difficulty mechanism stays principled.

**S1. Completion (draft-and-finalize).** Forcing: ratify-or-refute a pre-written claim. Proven floor class (KM02 59, KM05 36, KM06 60). World prerequisite: a chart-contradicted cold axis. CAP AT 1-2 PER WORLD from now on; this is the monotony Abi named.

**S2. Forced-inventory / per-item disposition.** Med rec, coding, DRG assignment, charge capture, claim scrubbing. Forcing: the deliverable schema itself forces a value per row; deferral is structurally impossible (KM01: the prednisone row, 0.72/0.78 metformin misses). No mounted draft needed, so it is not completion monotony. World prerequisite: at least one item whose correct value requires cross-document synthesis and one tempting wrong value.

**S3. Ratify-or-refute an EXTERNAL request.** Prior auth appeal, claims denial appeal, CDI query response, peer review response, pharmacy claim rejection. Forcing: an outside party (payer, auditor, CDI specialist) has already committed a position the chart can rebut; the deliverable must agree or push back. This is the KM02 adversarial-input lever wearing a NATIVE costume: the adversarial document is realistic by genre (a denial letter is supposed to be wrong), so no colleague-draft wrapper. Strongest answer to the variety mandate. World prerequisite: the external document built as a world or task file with its wrong-but-plausible position grounded in real chart ambiguity.

**S4. Determination / classification.** Inpatient-vs-observation, LOS determination, medical-necessity review, utilization review. Forcing: a verdict slot. HARD prerequisite learned from KM08 v3 (96.4): the case must be DESIGNED borderline; a fixed unambiguous world makes the verdict free. Choose this structure only when the brainstorm builds the borderline in (two-midnight ambiguity, criteria split).

**S5. Extraction-to-schema / abstraction.** HEDIS chart abstraction, HCC risk coding review, quality-measure reporting, risk stratification. Forcing: fixed fields force values; traps live in near-miss values, exclusion criteria, lookback windows, and denominator logic the chart quietly contradicts. World prerequisite: measure-relevant documentation with one quiet disqualifier.

**S6. From-scratch synthesis.** Referral letters, handoffs, summaries with no draft. Forcing: NONE native; deferral is free (KM07 v1 93.8, KM02-clean 94.4). Use ONLY with an embedded forced slot (a required disposition table inside the deliverable) or accept it cannot floor. Never the bite-carrier.

**S7. Investigation / causal analysis.** RCA, ADE investigation, mortality review, critical-result escalation review. Caution: review genres are anti-cold; the whole document is verification mode (KM06 v1 orthostatic died at 93 in a safety review). Bites only via attribution traps (a single-cause framing the chart contradicts) and even then predicted mid-high. Variety slot, not a floor slot.

**S8. Requester-deference (novel, untested).** The prompt principal states the wrong framing and the model drafts FOR them. Tests deference to a person rather than a document. Fairness question (prompt-supplied bait = constrained input) must be cleared with the pod BEFORE first use; cold axis only. Banked from the 6/10 red-team.

## 3. Sheet-mapped candidates (verbatim strings; prefer P0 and 0 claims; re-verify live sheet before claiming)

| Structure | Workflow (sheet verbatim) | Priority | Claims at snapshot |
|---|---|---|---|
| S2 | Inpatient Medical Coding and DRG Assignment | P0 | 0 |
| S2 | Concurrent Inpatient Chart Review with Working DRG Assignment | P0 | 0 |
| S2 | Charge Capture Review and Reconciliation | P0 | 0 |
| S2 | Clean Claim Submission and Scrubbing | P0 | 0 |
| S3 | Claims Denial Analysis and Appeal Preparation | P0 | 0 |
| S3 | Prior Authorization Appeal and Reconsideration | P0 | 0 |
| S3 | Clinical Documentation Improvement (CDI) Query Response Review | P0 | 0 |
| S3 | Pharmacy Insurance Claim Rejection Resolution | P0 | 0 |
| S3 | Claim Denial Root Cause Analysis and Appeal Preparation | P0 | 0 |
| S4 | Inpatient vs observation determination | P1 | 0 |
| S4 | Length of stay determination | P1 | 0 |
| S4 | Prior Authorization Clinical Review and Medical Necessity Determination | P1 | 0 |
| S4 | Utilization Review Concurrent Stay Documentation | P1 | 0 |
| S5 | HEDIS Medical Record Chart Abstraction and Review | P0 | 0 |
| S5 | Hierarchical Condition Category (HCC) Risk Coding Review | P1 | 0 |
| S5 | Patient Risk Stratification Assessment | P0 | 1 |
| S6 | Specialist Referral Letter and Documentation Preparation | P0 | 0 (KM07 pending) |
| S6 | Post-Acute Care Coordination Documentation | P0 | 0 |
| S7 | Patient Safety Event Investigation and Root Cause Analysis | P0 | 1 |
| S7 | Diagnostic Test Result Review and Follow-Up Documentation | P1 | 0 |
| S7 | Critical Result Acknowledgment and Escalation Workflow | P1 | 0 |
| S1 | Medical Transcription and Clinical Documentation Completion | P0 | 1 |
| S1 | Progress Note Daily Rounding Documentation | P0 | 1 (KM08 pending) |

Physician-voice rule (Medicine Team Lead, standing): the final deliverable is physician-authored, physician-reviewed, physician-supervised, or physician-communicated even when the workflow's home department is pharmacy, nursing, coding, or lab. Easy adaptations: coding/DRG (physician attestation or physician advisor review), denial appeal (physician letter of medical necessity), CDI query response (attending response). Hard or avoid: Nursing Shift Assessment Documentation, lab bench workflows, registration/scheduling, AR collections.

## 4. World #2 design implications (do at brainstorm, not at task time)

1. Choose the 5+ structures FIRST; write one line per task naming structure + forcing function + where the substrate must live.
2. Build the substrate FOR each structure: a genuinely borderline admission if S4 is wanted; a payer denial letter or CDI query as a planned file if S3 is wanted; a coding-relevant documentation gap if S2-coding is wanted; a quiet measure-disqualifier if S5 is wanted; ONE cold chart-contradicted axis reserved for the S1 floor.
3. Anchor rules apply per structure: every encounter strictly post-snapshot, never future-dated, varied timepoints.
4. Self-containment: S2/S3/S5 lean on coding/payer/measure knowledge; keep the required knowledge pre-July-2025 or attach the source document as a file (realistic for denial letters and policy excerpts).
5. Put the S8 fairness question to the pod before building anything on it.

## 5. Default 8-task allocation (7 structures, rule satisfied)

Two S1 completion floors on the world's two cold axes; one S2 forced-inventory; one S3 external ratify-or-refute; one S4 determination (only because the world was built borderline); one S5 abstraction; one S6 synthesis with an embedded disposition table; one S7 investigation or S8 (post pod clearance). Difficulty expectation set per structure: floors come from S1/S2/S3; S4 from the designed borderline; S5 mid; S6/S7 variety tier with embedded forcing.
