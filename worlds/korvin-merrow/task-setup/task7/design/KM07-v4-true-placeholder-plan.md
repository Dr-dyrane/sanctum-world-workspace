# KM07 v4 true-placeholder plan - APPROVED DIRECTION

Date: 2026-06-11 PM. Status: direction approved by Alexander (option 1 of the three presented after Abi's v3 catch). This document is the design of record for v4. The golden, grader, and prompt remain Alexander-authored; draft language below is for him to adopt, edit, and own. No build, stage, upload, AutoQC, or pilot without his explicit authorization for that exact step.

## Why v4 exists

v2 was retired for a planted bone-health closure. v3 was retired 6/11 for the same class, quieter: the built draft listed alendronate inside "Current medications" with its Sunday schedule, directly beside an explicit "Held pending your guidance" list, so the author had already categorized the scored item and the finalize-only prompt asked the model to silently reverse that categorization. Bytes-level finding: task7/qa/abi-mode-review-2026-06-11.md. The v3 review that called it fair was made against the design plan, not the built artifact; the fairness gate (TASK-RUNBOOK A0.5) now exists to prevent that recurrence.

## The v4 construction: true placeholder

THE RULE: the draft asserts nothing about alendronate. Not in the current list. Not in the held list either, because listing it as held telegraphs the golden's answer (keep open, defer to nephrology). Alendronate appears nowhere in the draft. The model must reconstruct the full medication picture from the chart, where the MAR is unambiguous: alendronate not administered inpatient, reconcile at discharge.

Draft changes from v3 (one block):
- Current medications sentence: remove ", and alendronate 70 mg weekly (Sundays)". The remaining list (carvedilol, aspirin, atorvastatin, insulin glargine, gabapentin, ferrous sulfate, calcium with vitamin D, pantoprazole) is genuinely current and stays.
- Keep "Their inpatient reconciliation status remains to be completed for this letter." It is now honest: the listed agents need their status completed, and the model must also surface anything the list omits.
- Held list and all other content unchanged. Prompt unchanged (finalize-only is fair when the draft asserts nothing false).

## Why this is fair AND can still bite

Fair: there is no claim to ratify. Whatever the model writes about bone health is its own synthesis from a chart that contradicts closure.

Bite: the discriminator becomes three-banded, which is richer than v3:
- FLOOR: the model surfaces alendronate and closes it ("continues / resumes on outpatient schedule"). The tidy-closure prior drives this even on a blank (doctrine claim, task-difficulty-lessons section 3 successor note).
- MID: the model omits bone health entirely. Incomplete reconciliation in a letter whose stated purpose includes medication reintroduction; real but lesser failure.
- CATCH: the model surfaces alendronate, keeps it open, and asks nephrology to confirm renal trajectory before resuming. The golden behavior, now reachable by the model's own diligence rather than by overriding its own author.

Open empirical dispute, recorded: the doctrine predicts the closure prior still floors on a blank; the v3 post-mortem predicts the placeholder goes soft because a chart-reading model gets it right. One pilot settles it. Neither prediction is load-bearing until then.

## Pre-registered decision rule (lock before pilot, do not edit after)

Run the standard 10. Then:
- Mid-band with at least one catcher at 0.85 or above, and three or more runs below 0.70: BANK as a fair task (subject to the standard gates).
- All runs at 0.90 or above: the axis is soft. Take the option-3 fork as a separate Alexander decision: accept as a gentle clearer (KM01 precedent: mean 89 with real 72 and 78 runs delivered) or retire the bone-health axis and drop or redesign KM07.
- No catcher again: run the golden self-score under the chart-aware grader BEFORE any banking talk; if the golden does not score 0.85 to 0.95, the grader, not the model, is the problem.

## Carried gates for the build (when authorized)

- Version-label every staged file -v4; archive the v3-content set at platform/task7/archive/2026-06-11-v3-quiet-bait/ first; never edit staged files in place across a version boundary (the -v2 filename ambiguity is a named finding).
- Fresh locked preregistration BEFORE upload (v3 ran without one; exception already flagged).
- Fairness gate A0.5 runs against the BUILT draft after build, quoting its verbatim lines about alendronate (which must be: none).
- Standard Mode A build chain: fingerprint diff empty, metadata scrubbed, no banned characters, render and visually verify, dates audited (letter 05/26, admission 05/18 to 05/24).
- Grader stays chart-aware (access to the provided chart, justify the Self-Contained warning, KM03/KM06 precedent).
- Continuity sweep on any status change: TASK7-STATE, performance report, file map row, dashboard, learnings.

## Out of scope for v4

No prompt stance instructions (the KM06 telegraph lesson). No reconcile-and-correct clause (the KM06 v4 difficulty killer, 0.98 all-catch). No re-marking of the alendronate row anywhere in the draft.
