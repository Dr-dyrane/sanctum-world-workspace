# Marva Lydell Brainstorm: pre-submission fixes (proposal for Alexander's human pass)

Date 2026-06-19. These are the two gating fixes the latest Part 1 guide surfaced (reference/source/phase-1-brainstorm/). Every workflow string and priority tier must be confirmed against the LIVE Task Selection Categories sheet at upload (AGENTS guardrail 13); the local 06_19 copy is a snapshot.

## Applied 2026-06-19 (Alexander approved)
- Priority column ADDED to submission/Marva_Lydell_Brainstorm.md (seven P0, three P1 at Tasks 4, 6, 8; at least one P0 present).
- Task 2 -> Medication Reconciliation: APPLIED.
- Task 6 -> Specialty Consultation Note: APPLIED (the recommended pick).
- Task 8 -> Alexander chose Corrective Action Plan (CAP) Development and Tracking, not the recommended Peer Review Case Analysis. APPLIED as chosen. Note: CAP is an administrative tracking/quality genre, the same ceiling-prone family as peer review, so the Task 8 floor caveat below stands either way; it remains the slate's weakest floor bet.
- docs/BRAINSTORM-DRAFT.md marked superseded; submission/Marva_Lydell_Brainstorm.md is now canonical.
- Remaining before upload: confirm every workflow string AND priority tier against the LIVE sheet (especially the CAP and Medication Reconciliation strings and the three P1 tiers), rebuild the submission .docx from the .md, and do the final own-pass.

## Fix A: add a Priority column (P0/P1/P2)
The guide (Rough Task Ideas, Standard 1), the Soya strong-example, and your own OV brainstorm all label priority per task. The Marva table has none. At least one P0 is required and is firmly met (Claims Denial, Medication Reconciliation, Post-Acute Coordination, and CDI Query Response Review are P0 on the snapshot). Proposed tiers, to confirm against the live sheet:

| Task | Workflow | Proposed priority |
|---|---|---|
| 1 | Claims Denial Analysis and Appeal Preparation | P0 |
| 2 | (remap, see Fix B) | P0 |
| 3 | Utilization Review Concurrent Stay Documentation | P0 (verify) |
| 4 | Medical Transcription and Clinical Documentation Completion | P1 (verify) |
| 5 | Post-Acute Care Coordination Documentation | P0 |
| 6 | (remap, see Fix B) | depends on chosen category (verify) |
| 7 | Claims Denial Analysis and Appeal Preparation | P0 |
| 8 | (remap, see Fix B) | depends on chosen category (verify) |
| 9 | HEDIS Medical Record Chart Abstraction and Review | P0 (verify) |
| 10 | Clinical Documentation Improvement (CDI) Query Response Review | P0 |

## Fix B: remap the three non-verbatim workflow strings
Six of ten task workflows match the current 06_19 sheet verbatim (Tasks 1, 3, 4, 5, 7, 9, 10). Three do not and will trip the AutoQC "maps to an approved workflow" check (Common Mistake 1b). Proposed remaps:

### Task 2 - discharge medication reconciliation
- Draft string (not verbatim): "Discharge Medication Reconciliation at Care Transitions"
- Current sheet carries: "Medication Reconciliation" and "Medication Reconcilliation Documentation/Discharge Medication Reconcilliation" (the sheet itself spells it with a double-l).
- Recommended: use the discharge-specific entry verbatim as the live sheet spells it. Confirm the exact spelling on the live sheet (the typo may be fixed there). Clinical fit is exact; this is a wording-match fix only.

### Task 6 - cardiorenal follow-up letter (specialist handoff)
- Draft string (no match): "Specialist Referral Letter and Documentation Preparation"
- Closest current categories: "Specialty Consultation Note", "Care Coordination Referral Tracking and Closure", "Administrative Clinical Certifications & Letters".
- RECOMMENDATION: map to "Specialty Consultation Note" (verbatim on 06_19; confirm on live). It is the physician-owned deliverable that best carries the floor engine.
- Why (OV doctrine): the trap is a premature over-closure of a still-conditional renal/volume decision. That is exactly the OV06 v2 / OV08 / OV09 v4 engine: a STARTED note the attending FINALIZES, with the pre-filled wrong closure on a routine BACKGROUND line, no reconcile clause. Frame Task 6 as a started nephrology or cardiology consult/handoff note the hospitalist finalizes, and keep the premature "renal recovery settled / diuretic finalized / ACE restart cleared" item as a quiet background line that the nephrology note contradicts on inspection. Avoid an open "write the handoff" framing, which puts the closure on the headline and ceilings (OV09 v3). Floor confidence: HIGH (proven engine). Using the completion FRAME on a distinct deliverable does not break the completion cap; OV ran this same engine across a med list, a progress note, a transition note, and a discharge note.

### Task 8 - safety review after bounceback (root cause analysis)
- Draft string (no match): "Patient Safety Event Investigation and Root Cause Analysis"
- Closest current categories: "Peer Review Case Analysis", "Patient Safety Indicator (PSI) Analysis and Reporting", "Mortality and Quality Indicator Second-Level Review".
- RECOMMENDATION: "Peer Review Case Analysis" is the closest verbatim fit (confirm on live). But the honest OV read: this is the slate's WEAKEST floor bet, treat it as a likely catcher, not a bankable floor.
- Why (OV doctrine): RCA/peer-review is an open ANALYSIS/REVIEW genre, and OV showed the model is strong there (it runs rule-governed analysis cleanly and declines a wrong premise when asked to review one). Worse, the root cause IS the deliverable's headline, and wrong-on-headline ceilings (OV09 v3). Both signals point to a ceiling, and the analogous OV safety/RCA task landed mid, not a deep floor. To give it any floor chance, do NOT frame it as "analyze and find the root cause" (open analysis is model-strong); frame it as FINALIZING a started event note whose pre-filled conclusion blames nonadherence on a background line, with the systems-failure evidence (vendor delivery failure, unclear med ownership) left off-headline in background documents the completion frame does not force the model to assemble. Even then it is a long shot. Bench it cold first, do not retire on the bench (ceiling-error ledger), and do not rely on Task 8 for a bankable floor.

## Floor-reliability read (applying OV doctrine)
OV proved floors come from ONE engine: a COMPLETION frame plus a pre-filled or inherited wrong move on a COLD BACKGROUND axis, the chart contradicting it on inspection, with no telegraph and no reconcile clause (FLOOR-MECHANISM-LIBRARY sections 1 and 8). The model satisfices under "finish this": it rubber-stamps inherited content and skips the high-stakes step the deliverable does not force. Analysis, review, decline-external, coding, and abstraction genres are where the model is strong, and they ceiling. Mapping that onto the Marva slate:
- Reliable floor bets (completion plus a background embedded-wrong): Task 2 (med rec carrying admission renal-dose logic forward onto a background row), Task 4 (transition note completion), and Task 6 as recommended (started consult note over-closing the conditional renal/volume decision).
- Ceiling-prone (model-strong genres): Tasks 1 and 7 (appeals; declining an external denial is model-strong unless the trap is an OVERCLAIM the appeal frame tempts the model to CARRY, the OV07 long shot), Task 3 (UR determination; decisiveness ceilings), Task 8 (RCA; analysis plus headline axis), Task 9 (HEDIS abstraction; rule-governed), Task 10 (CDI response; coding genre).
- Action: lean the world's bankable floors on the completion plus embedded-wrong tasks; build the review and analysis tasks de-telegraphed, bench them cold, and expect several to land mid. This matches OV, where all eight floors came from the completion engine, not the analysis genres. Bench before piloting, but never retire on a cold-bench ceiling alone (the harness is consistently harder than the bench).

## Notes
- Remapping 6 and 8 does not threaten the structure-variety gate; the slate still spans at least five distinct structures, with the completion frame reused across distinct deliverables (which OV did, and which the cap permits).
- These two fixes plus your human edit-and-own pass are all that stand between the brainstorm and AutoQC upload, per the latest guide (no Claude transcript at the brainstorm stage).

## Regression audit vs the KM brainstorm corrections (2026-06-19)
Checked Marva against the KM brainstorm-lifecycle corrections (worlds/korvin-merrow/reviews/reviewer-feedback.md, the Stacey S send-back of 2026-05-29, plus brainstorm-autoqc-01). The two you named map exactly to KM revisions 3 and 4.

CLEARED (KM was corrected; Marva already complies):
- Fictional, non-celebrity patient name (KM rev 1): Marva Lydell. OK.
- "World Type: Typical Clinical World" declaration (KM rev 2): present. OK.
- Requester named on every task (autoqc-01 flag): all 10 have one. OK.
- Distinct task-level trap per task (autoqc-01 flag): each task carries its own clinical trap. OK.
- Letter-O "PO" vs P0 artifact (autoqc-01 flag): zero letter-O tokens in the built docx. OK.
- No over-authoritative final synthesis (internal note): the brainstorm states "no single summary that states the final readiness conclusion." OK.
- Workflow mapping + P0/P1 labels (internal note): applied and live-sheet verified. OK.

REPEAT RISK (RESOLVED 2026-06-19: both fixed via the ratified COMORBIDITY-MEDICATION-EXPANSION-PROPOSAL v2; World Setup now carries 15 named comorbidities and ~17 named baseline agents; docx rebuilt):
1. Comorbidity list (KM rev 3, "expand comorbidity burden above the 10+ threshold"). Marva's World Setup names 8 chronic conditions: CHF, AFib, CKD 3b-4, COPD, OSA, T2DM, HTN, obesity. AutoQC treated under-10 as borderline at concept stage, but the KM human reviewer still sent it back, so pre-empt it. Recommend expanding to at least 10 with cardiorenal-coherent, common (non-zebra) conditions; physician to ratify from, e.g.: hyperlipidemia, anemia of CKD, CKD-MBD or secondary hyperparathyroidism, diabetic peripheral neuropathy, coronary artery disease, peripheral arterial disease, hypothyroidism, gout.
2. Medications (KM rev 4, "add specific medication names ... current traps mention categories but no specific agents"). Marva names only classes (ACE inhibitor, SGLT2 inhibitor, metformin, diuretic, anticoagulant). The Soya strong-example names specific agents, and KM was sent back for exactly this. Recommend naming specific agents in the World Setup (doses belong in the World Spec); physician to ratify from, e.g.: torsemide or furosemide, metoprolol succinate or carvedilol, apixaban, sacubitril-valsartan or lisinopril, empagliflozin, metformin (held in AKI), insulin glargine, atorvastatin, spironolactone, a potassium binder, ferrous sulfate or an ESA, tiotropium plus albuterol, cholecalciferol or calcitriol.

Both items are physician-owned clinical content, so the brainstorm is not edited here. Ratify the comorbidity and medication picks and I will apply them to submission/Marva_Lydell_Brainstorm.md and rebuild the docx through the gated builder.
