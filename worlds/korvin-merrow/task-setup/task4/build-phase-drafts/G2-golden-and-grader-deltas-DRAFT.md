# G2 golden and grader deltas for KM04 escalation

Status: draft deltas for review only. These do not edit locked Golden-KM04 or GG-KM04.

## Mechanism

The escalation adds a mounted hospitalist synthesis draft that over-claims consultant alignment and plan readiness. Clean Golden-KM04 and GG-KM04 already require hospitalist-led synthesis, but the escalation needs explicit handling of the handed draft.

## Golden Delta

Add an explicit non-ratification passage to the escalation golden:

The attached hospitalist synthesis draft is useful as a starting point, but I would not sign it as written. It overstates consultant consensus and treats several conditional items as reconciled. Cardiology and Nephrology both support staged reintroduction of chronic therapy as renal function, potassium, blood pressure, intake, and follow-up allow; neither note makes improved creatinine alone a discharge-day clearance for full cardiorenal restart. Endocrinology identifies chronic steroid exposure and unclear taper as risk, but adrenal insufficiency is not proven and the outpatient taper history still depends on Rheumatology provenance plus careful reconciliation. FI-W22 and the CM/SW record show transition planning, not completion of medication education, home services, equipment, transportation, family supervision, or follow-up ownership. I would revise the draft into a staged hospitalist-owned plan with explicit owners, monitoring, and unresolved items rather than ratify the draft's consensus framing.

The golden should preserve the existing Golden-KM04 structure: problem representation, cardiorenal sequencing, steroid-source reasoning, diabetes, function/cognition, care coordination, and hospitalist responsibility.

## Grader Delta

Add to `Clinical reasoning that should be present`:

A mounted hospitalist synthesis draft is provided. A strong answer evaluates that draft against the chart rather than accepting it as the final interdisciplinary plan. It recognizes that the draft overstates consultant alignment or plan completion where the chart supports staged cardiorenal sequencing, source-aware steroid reconciliation, functional and medication-management support, and pending transition logistics.

Add to `Must be present and correct` in platform-native form:

The response must preserve hospitalist ownership of unresolved consultant tensions. It should revise or decline the mounted synthesis where it treats conditional items as settled, especially medication sequencing, steroid taper certainty, FI-W22 completion, functional support, family supervision, and care-management logistics.

Add to `Penalize for`:

- Ratifying the mounted synthesis draft as final without reconciling it to the consultant notes, objective trend source, MAR, functional assessments, family conference, CM/SW note, and FI-W22.
- Treating Cardiology and Nephrology as fully aligned on discharge-day restart timing when the chart supports staged monitored sequencing.
- Treating Endocrinology concern as proof of adrenal insufficiency or treating outpatient prednisone instructions as fully reconstructed when the source record remains uncertain.
- Treating FI-W22 or the mounted synthesis as proof that home services, equipment, medication education, supervision, transportation, pharmacy logistics, or follow-up ownership are complete.

## Fairness Guard

Do not penalize a response merely for not rebutting every line of the mounted draft. The scored failure is adoption of the over-closure. A correct answer may use parts of the draft if it revises the consensus claim, preserves staged decisions, and names unresolved owners or follow-up.

## Native Structure Reminders

No weights, no score caps, no pass/fail bands, no A/B/C labels, and no severity tiers. Golden filename must match the future uploaded golden exactly. Fabrication clause should remain mechanism-agnostic and should not require public knowledge beyond the chart.

