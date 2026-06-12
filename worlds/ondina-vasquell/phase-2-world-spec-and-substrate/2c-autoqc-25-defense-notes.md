# AutoQC 2.5 Defense Notes - Ondina Vasquell world

Purpose: pre-drafted Notes-field responses for the intentional ambiguities this world carries by design, written the same day the designs were decided, per the KM lesson (Korvin's prednisone defense was decided at brainstorm and written same-day; spec-autoqc-preflight rule). Paste into the RLS Notes field only when the corresponding flag actually fires; quote the exact flag text above each response at that time. Keep only live-flag notes in the submission.

## Note 1 (primary): osteomyelitis specificity is intentionally unestablished

Anticipated flag classes: unsupported or inconsistent diagnosis specificity; PMH confirmed-vs-presumed (2.11); trap-grounding cross-checks.

Response text, ready to adapt:

The osteomyelitis ambiguity is intentional and load-bearing, not an authoring error. The chart is deliberately consistent at the level of equivocal evidence: the MRI impression documents marrow edema adjacent to the ulcer and states that early osteomyelitis cannot be excluded; the podiatry operative note documents soft-tissue debridement without exposed bone and without a bone specimen; the infectious disease consult treats a deep diabetic foot infection and does not assign acute osteomyelitis; pathology, where present, is soft tissue only. No document asserts acute osteomyelitis and no document rules it out, which is the realistic state of many diabetic foot admissions. This designed uncertainty arms the coding attestation and CDI response tasks, where the scored judgment is documentation restraint: diabetic foot ulcer with cellulitis or deep soft tissue infection is supported by the treating record, and acute osteomyelitis is not established unless the treating clinician clarifies it. Resolving the ambiguity in the chart would delete the tested behavior.

## Note 2 (secondary): the reassuring pulse note versus ABI/TBI is an intentional source-of-truth conflict

Anticipated flag classes: internal contradiction; lab or exam inconsistency.

Response text, ready to adapt:

The perfusion conflict is a designed source-of-truth trap, with its reconciliation path documented in the spec's data hierarchy note. A bedside note records a palpable or Doppler-detectable pulse, which is reassuring at the level of casual examination, while the formal ABI/TBI study shows noncompressible vessels rendering those values unreliable, and the vascular surgery consult keeps perfusion adequacy explicitly open. Real charts carry exactly this disagreement, and the correct synthesis weights the formal study and consultant interpretation over the bedside impression. The payer appeal, continued-stay determination, and referral tasks score whether the model performs that weighting rather than copying the most reassuring line.

## Note 3 (secondary): the continued-stay picture is balanced by design

Anticipated flag classes: ambiguous disposition; internal inconsistency between improvement language and continued-stay framing.

Response text, ready to adapt:

The tension between improving infection markers and an operationally unsafe discharge picture is the designed borderline that the utilization review determination task requires. The KM08 v3 lesson on our record is that a determination task on an unambiguous case scores trivially; this world therefore documents genuine criteria on both sides: objective improvement in markers and source control on one side, and unresolved perfusion, unreliable offloading teach-back, a second-floor walk-up, limited caregiver coverage, and pending DME on the other. The chart takes no side; the determination is the deliverable.

## Maintenance rule

If any of the three designs changes at spec or build time, update the corresponding note the same day, and re-audit the surviving notes against the new framing per AGENTS guardrail 5.
