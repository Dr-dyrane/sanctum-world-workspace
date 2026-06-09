# KM04 Task-4 model simulation (Codex, read-only, 6/7)

Verdict: KM04 can plausibly hit a below-70 average, but only after the required "quiet cardiorenal paragraph" fix. The G3 draft concept as originally written is too loud and would test medication-error spotting, not consultant-synthesis judgment.

Read receipt: STATUS.md, TASK-RUNBOOK.md, KM03 state/log, KM04 state, design plan, gates, source audit, G1/G2/G3 drafts, mount manifest, pilot preregistration, Claude review, locked TP/EO/Golden/GG/FI-T04, key agent-read DOCX facts.

Current state at time of sim: KM03 v2.1 passed Task AutoQC qcaud_fc; Taiga intentionally held.

## Simulation
| KM04 surface | Predicted mean | Range | Interpretation |
|---|---|---|---|
| Clean KM04 | ~88 | 82-94 | Useful calibration only, likely too easy |
| Current loud G3 draft (concept) | ~77 | 64-92 | May get lows, but for the wrong reason |
| Post-fix quieted draft | ~66 | 45-88 | Feasible real discriminator |
| Pessimistic high-pass scenario | ~77 | 65-92 | If prompt over-primes skepticism |

The original draft's medication paragraph named too many specific held agents returning through discharge reconciliation; a strong model catches that from Nephrology/MAR alone, collapsing the failure into chart-reading. The post-fix version works better: the wrong move is ratifying "consultants are aligned / sufficiently reconciled for sign-off" when the chart still supports staged hospitalist ownership.

Expected low run: reuses the resident draft, says consultant tensions are sufficiently resolved, treats cardiorenal sequencing as worked through, softens steroid uncertainty, carries home-support logistics as proceeding rather than conditional.

Expected high run: says the draft is useful but not signable as written; preserves staged cardiorenal sequencing, steroid-source uncertainty, functional/cognitive constraints, family supervision limits, CM/SW pending items, and explicit hospitalist ownership.

Bottom line: below-70 average is feasible, probably the 62-68 zone, not guaranteed. Do not build from the original G3 text; apply Claude's fixes first (quiet cardiorenal restart language, port the KM03 razor, add anti-paralysis language, protect correct staged synthesis from being docked).

## Reconciliation with the staged set (Claude Code)
Codex evaluated the G3 draft concept. The four fixes it requires are already applied in `platform/task4/current/` (verified on staged bytes 6/7): the staged mounted draft has zero "can be restarted / same discharge sequence" tokens and shifts the over-claim to "the sequencing has been worked through with both services" with "sufficiently reconciled for sign-off" retained as the headline plant; the staged grader carries the ported razor, the anti-paralysis penalty, and the cannot-dock-correct-staged-synthesis guard. The staged set therefore IS Codex's "post-fix quieted draft" (~66, feasible discriminator), not the loud concept. Residual watch-item (both reviewers): the prompt's "for anything still unresolved" lightly primes skepticism; keep G1 as-is and trim only if the pilot runs high.
