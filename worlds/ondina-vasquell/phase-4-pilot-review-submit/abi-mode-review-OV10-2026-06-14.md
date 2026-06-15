# OV10 v2 - AO / Abi-mode review (prompt-focused) - 2026-06-14

Verdict: PASS.
- No telegraph: prompt is "finish her discharge instructions from the chart... document I can sign... brief summary." It does NOT point at the activity/offloading section or say "what she should do for the foot" (the v1 telegraph). The de-hinted draft section is generic ACTIVITY with a placeholder carrying no offloading answer-word. The model must derive the offloading restriction from the chart on its own.
- Fairness (true placeholder, A0.4/A0.6): the activity section is a genuine placeholder that asserts nothing; the prompt instructs completion FROM THE CHART. The offloading restriction is documented across PT, OT, wound-care, podiatry, and nursing-offloading notes (not hidden). A routine-clearance fill is the model's own boilerplate error, not a planted trap. Fair.
- Physician-produced: the deliverable is the discharge instructions the physician completes and signs (golden authored by Lillian Everet, MD, "Draft for physician sign").
- No answer leak; physician voice; realistic; document-to-sign; no literal path; no dashes.
- Floor lever is commission on the model's templated discharge default (normalize activity), against the documented restriction - the OV01 axis, not coding. Central failure framed as a material patient-safety failure (weight-bearing on a limb-threat wound), capped not deducted.
