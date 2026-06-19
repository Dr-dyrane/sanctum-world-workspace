# Marva Lydell Brainstorm: pre-submission fixes (proposal for Alexander's human pass)

Date 2026-06-19. These are the two gating fixes the latest Part 1 guide surfaced (reference/source/phase-1-brainstorm/). This is a PROPOSAL for the human edit pass to approve and apply; it is not applied to the brainstorm. Every workflow string and priority tier below must be confirmed against the LIVE Task Selection Categories sheet at upload (AGENTS guardrail 13); the local 06_19 copy is a snapshot.

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
- The 06_10 sheet appears to have carried a specialist-referral-letter category; it is not in the 06_19 copy. Closest current categories: "Specialty Consultation Note", "Care Coordination Referral Tracking and Closure", "Administrative Clinical Certifications & Letters".
- Recommended: first check the live sheet for a surviving specialist-referral-letter category. If gone, the cleanest physician-owned fit is "Specialty Consultation Note", reframing the deliverable as a cardiorenal consult/handoff note that routes the follow-up decisions. This is a clinical-fit call for you to lock. The task's structure (specialist handoff) and its trap are unaffected.

### Task 8 - safety review after bounceback (root cause analysis)
- Draft string (no match): "Patient Safety Event Investigation and Root Cause Analysis"
- The 06_10 sheet appears to have carried a patient-safety-event RCA category; it is not in the 06_19 copy. Closest current categories: "Peer Review Case Analysis", "Patient Safety Indicator (PSI) Analysis and Reporting", "Mortality and Quality Indicator Second-Level Review".
- Recommended: "Peer Review Case Analysis" is the closest case-level cause analysis of a single bounceback; "Patient Safety Indicator (PSI) Analysis and Reporting" is the alternative if you want the PSI framing. Clinical-fit call for you to lock. The investigation structure and the nonadherence-vs-handoff trap are unaffected.

## Notes
- Remapping 6 and 8 does not threaten the structure-variety gate; the slate still spans 9 distinct structures with one completion task.
- These two fixes plus your human edit-and-own pass are all that stand between the brainstorm and AutoQC upload, per the latest guide (no Claude transcript at the brainstorm stage).
