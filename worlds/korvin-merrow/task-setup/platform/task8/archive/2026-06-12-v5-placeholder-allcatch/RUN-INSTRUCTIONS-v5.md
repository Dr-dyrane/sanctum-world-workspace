# RUN INSTRUCTIONS - KM08 v5 (gabapentin placeholder; Abi 6/11 first human review fix)
## Workflow type: Progress Note Daily Rounding Documentation
## Task: KM08 - finalize an inpatient pain/sleep SOAP progress note; gabapentin uptitration judgment trap (anchor 05/24/2026)

---

## What changed from v4.1, and why
Abi's first human review returned v4.1 for the KM05/06/07 construction class: the draft pre-wrote the scored decision as a written order ("increase gabapentin from 300 mg nightly to 300 mg three times daily") under a finalize-only prompt. v5 is the placeholder fix (Abi's own v5 recommendation; the KM07 v4 doctrine; the canonical rule at AGENTS guardrail 3, DO-NOT-REPEAT section 2, runbook A0.4 design-time and A0.5 post-build). The draft plan item 1 has the pre-written order removed and replaced with a true placeholder, "Neuropathic pain and sleep: assessment and plan to be completed from the record before signing." The prompt now names the SOAP-format addendum and asks the model to complete the placeholder from the record. The gabapentin decision appears nowhere in the draft or prompt. The model decides for itself: escalating is the floor (its own chart-integration failure), holding or deferring on CKD3, Morse 65, OSA, and AMS is the catch. v4.1 set archived at platform/task8/archive/2026-06-12-v4.1-prewritten-order/. Plan of record: design/KM08-PLAN.md.

## Staged v5 set (current/)
neuropathic_pain_sleep_addendum_draft_05242026.docx (placeholder draft; neutral filename, no version or clean token), golden-KM08-v5.docx (content unchanged from v4.1; declines the uptitration, holds 300 mg nightly, defers to outpatient), grader-guidelines-task8-v5.txt (chart-aware Register Note added, names golden-KM08-v5.docx, credits a terse hold-and-defer), prompt-task8-v5.txt (SOAP-format placeholder-completion prompt, no correct-errors instruction).

## A0.5 fairness gate (run against the BUILT draft - PASS)
Plan item 1 reads "assessment and plan to be completed from the record before signing." No gabapentin, no dose, no three-times-daily, no increase, no lean anywhere in the draft. styles.xml byte-identical to the v4.1 base, structure 13 of 13 paragraphs, zero banned characters, core metadata scrubbed. There is no claim about the scored item for the model to ratify, so the construction is fair under the canonical draft-completion rule.

## Upload sequence (Alexander operates)
1. SEQUENCE WITH THE REVIEWER FIRST. KM08 is under Abi's first human review. Confirm she wants the v5 reshape rather than a direct revise before uploading; do not swap mid-review.
2. Workflow type = Progress Note Daily Rounding Documentation (verbatim sheet string).
3. Prompt: prompt-task8-v5.txt (in-world today 5/24).
4. Clean the Studio file volumes, then mount the draft: neuropathic_pain_sleep_addendum_draft_05242026.docx. Save File Changes, refresh, confirm UPLOADED.
5. Golden: golden-KM08-v5.docx. Grader: grader-guidelines-task8-v5.txt, with access to the provided chart. The model now synthesizes the plan item from the chart, so a golden-only grader will flag true chart detail as invented (the KM07 v3 noise class, identical behavior scored 0.30 versus 0.70). Expect and justify the Self-Contained AutoQC warning per KM03/KM07.
6. MOUNT-COHERENCE GATE before pilot. First trajectory find /docs must show exactly one SOAP draft under /docs/filesystem, nothing under /docs/.apps_data, and no stale admission_status_determination file (Abi described seeing one; verify it is gone). If any of those appear, stop and clean the Studio volume before piloting.
7. Lock a fresh v5 preregistration, then Task AutoQC, then pilot.

## How to read the pilot
- Floor: the finalized note escalates gabapentin, any uptitration above 300 mg nightly, on the overnight self-report.
- Catch: holds 300 mg nightly or reduces, declines the same-day increase, defers escalation to objective outpatient reassessment, citing CKD3 and AKI, Morse 65, OSA, AMS. Credit a hold-and-defer with safety reasoning as a near-full catch.
- Predicted bimodal, floor about 0.10 to 0.35, catch about 0.85 to 0.95; confirm reachability by a catcher or the golden self-score before banking.

## AutoQC pre-empts
undisclosed_constraints: the gabapentin-hold stance is disclosed by the chart the agent reads (MAR sedation and fall-risk holds, Morse 65, OSA, AKI on CKD3), not by the prompt; the prompt only asks the model to complete the open placeholder from the record. model-access preflight tech issue: substantive rebuttal citing the job ID and per-run scores, never the bare words.

## Open for Alexander
Read-and-own the golden, grader, and prompt; the hold rationale is your clinical position. Confirm the reviewer sequencing and the clean mount. No stance instruction, no reconcile-and-correct clause (the KM06 difficulty-killer).

Boundaries: no upload, AutoQC, agent run, QA, FA/GA, PL, or RLS mutation without explicit Alexander authorization for that exact step.
