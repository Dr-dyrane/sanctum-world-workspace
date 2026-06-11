# Abi-mode review: KM07 v3 staged packet - 2026-06-11

Scope: platform/task7/current/ read cold in protocol order: prompt-task7-v2.txt, nephrology_referral_letter_draft_05262026.docx (text extracted from the built bytes), then golden and grader. Protocol: docs/abi-review-protocol.md.
Posture confirmations: read cold before opening golden/grader: yes. Built artifact read directly, not the design plan.
Verdict: SEND BACK (confirms Abi's catch; two independent blocking grounds)

## Findings (blocking)

1. [Lens 1, fairness of construction] The built draft asserts alendronate as a current medication. Verbatim from the bytes: "Current medications: carvedilol 12.5 mg twice daily, aspirin 81 mg daily, atorvastatin 40 mg nightly, insulin glargine 18 units nightly, gabapentin 300 mg nightly, ferrous sulfate, calcium with vitamin D, pantoprazole, and alendronate 70 mg weekly (Sundays). Their inpatient reconciliation status remains to be completed for this letter." The same block then lists "Held pending your guidance:" with five other agents. The author has already sorted every medication into current versus held and placed alendronate in current, with its dosing day. The prompt says only "Finish it and finalize it so it is ready to send." Same-author draft, false categorization on the scored item, no instruction to correct: the planted-claim class, quieter. The reconciliation-status sentence does not rescue it; it blanks the status field, not the membership claim. Forward rule: a disclaimer about status does not un-assert membership, and looking routine is the same act as asserting.

2. [Lens 7, symmetric spread] Independent of construction, the v3 spread fails the two-sided gate on its own: 0.45 to 0.60 tight, no catcher, zero of ten runs produced the golden keep-open behavior, and the golden self-score reachability check was never run (the structural pass is not a scored proof). "Bankable pending reachability" was carrying the entire verdict. Forward rule: a verdict that depends on an unrun check is not a verdict.

3. [Lens 8, surviving artifacts] The staged set's files are named -v2 (prompt-task7-v2.txt, golden-KM07-v2.docx, grader-guidelines-task7-v2.txt, RUN-INSTRUCTIONS-v2.md) while every continuity doc calls the staged design v3; the grader and draft were edited in place. This ambiguity is part of how a plan got reviewed instead of an artifact. Forward rule: version-label staged sets to match the continuity docs; never edit a staged file in place across a version boundary.

## Improvements (non-blocking)

- The review that called v3 fair was performed against the design plan's description ("no longer states any closure"), not the built draft. The fairness gate (runbook A0.5) now requires quoting the built artifact's verbatim lines about the scored item.

## Mechanical pass

Dates PASS (letter 05/26, admission 05/18 to 05/24). Banned chars PASS on extracted text. Prompt-file refs PASS (prompt references the saved draft, which exists). Workflow string not re-checked here. Grader chart-access PASS (chart-aware per v3 fix, validated dba6c34f). Names PASS (Quenor, Solthar established). Prereg FAIL carry-forward: v3 ran without a standalone locked prereg (known exception, already flagged).

## Reachability status

No catcher observed (max 0.60). Golden self-score under its own chart-aware grader: NOT RUN. Both moot for v3 (retired); carry the requirement into v4 as a pre-bank gate.

## Disposition

Abi's catch confirmed on the bytes. v3 retired as unfair alongside v2. Approved direction: v4 true placeholder per task7/design/KM07-v4-true-placeholder-plan.md (Alexander approval 2026-06-11 PM).
