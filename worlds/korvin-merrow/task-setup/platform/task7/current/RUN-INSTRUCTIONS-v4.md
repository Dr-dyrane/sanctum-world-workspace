# RUN INSTRUCTIONS - KM07 v4 (true placeholder; Abi 2nd review fix, 6/11)
## Workflow type: Specialist Referral Letter and Documentation Preparation
## Task: KM07 - finalize a PCP nephrology referral letter (anchor 05/26/2026)

---

## What changed from v3, and why
v3 was sent back a second time (Abi, 6/11). The built draft still listed alendronate inside "Current medications," and the prompt was finalize-only, so the same author had categorized the scored item and the model was expected to silently reverse it. Per the approved plan (design/KM07-v4-true-placeholder-plan.md), v4 is a true placeholder: alendronate appears NOWHERE in the draft, not in the current list and not in the held list, because listing it anywhere telegraphs the golden's answer. The only draft edit from v3 is the deletion of ", and alendronate 70 mg weekly (Sundays)" from the current-medications sentence; the generic "their inpatient reconciliation status remains to be completed for this letter" note stays, the held agents and prednisone are unchanged, and the prompt is unchanged. The model must reconstruct the medication picture from the chart, where the MAR is unambiguous that alendronate was not administered inpatient and is to be reconciled at discharge.

FAIRNESS GATE (run against the built draft, per runbook A0.5): the draft's medication paragraph reads "Current medications: carvedilol ... and pantoprazole. Their inpatient reconciliation status remains to be completed for this letter. Held pending your guidance: sacubitril/valsartan ... metformin ER 500 mg twice daily. Prednisone continues on its outpatient taper." Alendronate appears nowhere. There is no claim about the scored item for the model to ratify, so the construction is fair under Abi's rule.

v3 content set archived at platform/task7/archive/2026-06-11-v3-quiet-bait/.

## Staged v4 set (current/)
prompt-task7-v4.txt (finalize-only, unchanged), nephrology_referral_letter_draft_05262026.docx (true placeholder), golden-KM07-v4.docx (keeps alendronate open, asks nephrology to confirm renal trajectory; content unchanged from v3), grader-guidelines-task7-v4.txt (chart-aware five-block, names golden-KM07-v4.docx; content unchanged from v3). Build: tools/build/build-docx-km07-draft-fairfix.py.

## Pre-registered decision rule (lock a fresh prereg BEFORE the pilot, do not edit after)
From the plan, run the standard 10, then: mid-band with at least one catcher at 0.85 or above and three or more runs below 0.70, BANK; all runs at 0.90 or above, the axis is soft, take the option-3 fork (accept as a gentle clearer or retire the bone-health axis); no catcher again, run the golden self-score under the chart-aware grader before any banking talk.

## Upload sequence (Alexander operates)
1. Workflow type = Specialist Referral Letter and Documentation Preparation (verbatim sheet string).
2. Prompt: prompt-task7-v4.txt.
3. Mount draft: nephrology_referral_letter_draft_05262026.docx, then Save File Changes, then refresh and confirm UPLOADED.
4. Golden: golden-KM07-v4.docx. Grader: grader-guidelines-task7-v4.txt (chart-aware, include_input_files true, justify the Self-Contained warning, KM03/KM06 precedent).
5. Mounted-set gate: 26 world files plus the one mounted draft.
6. Task AutoQC, then notes, then pilot.

## AutoQC pre-empts
undisclosed_constraints: the open bone-health stance is disclosed by the chart the agent reads (MAR: alendronate not administered inpatient, reconcile at discharge), not by the prompt; the prompt is a minimal in-role finalize instruction. enable_anthropic_api tech issue: substantive rebuttal citing the job ID and per-run scores, never the bare words.

## Open for Alexander before entry
Read and own prompt, golden, grader. Lock a fresh v4 preregistration (v3 ran without one). 2.106 vs KM01 and KM03 medication-reconciliation family. No prompt stance instructions and no reconcile-and-correct clause (the KM06 difficulty-killer).

Boundaries: no upload, AutoQC, agent run, QA, FA/GA, PL, or RLS mutation without explicit Alexander authorization for that exact step.
