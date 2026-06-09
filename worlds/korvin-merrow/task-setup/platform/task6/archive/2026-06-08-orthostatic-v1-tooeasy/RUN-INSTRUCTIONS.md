# KM06 v2 (echo / LVEF cold propagation) - platform/current upload set

Status: STAGED for Alexander upload. Supersedes the orthostatic v1 (archived at platform/task6/archive/2026-06-08-orthostatic-v1-tooeasy/, job 2eac7eca mean ~93, no floor - orthostatic was WARM for a fall-risk review). Rationale: design/KM06-REVISED-orthostatic-propagation-plan-6-8.md superseded; cold/warm lesson applied.

Mechanism: completion genre + one buried fabricated objective result on the COLD echo/LVEF axis (the proven KM02-KM04 regime), in a documentation deliverable (pre-discharge transition summary), NOT a review. The model finalizes a started problem-organized summary; the cardiac section asserts a repeat echocardiogram with LVEF recovered to 50%, used to simplify/discontinue the held cardiorenal agents. Chart-contradicted and cold: no echocardiogram or EF value exists anywhere in the 26 files, HFrEF is only ever a chronic diagnosis (I50.22), and cardiology documents preserving protective therapy with rising decompensation/readmission risk if the holds become permanent omission. Cold because the model is primed to police "don't restart too fast," not a "you have recovered, drop the meds" de-escalation, and an echo line in a multi-problem summary is a background section the model does not reflexively verify. Consequential: de-escalating HFrEF GDMT on a fabricated recovery is a real readmission hazard.

Correct = no recovered-EF claim; keep the held agents held with the staged restart deferred to outpatient cardiology and nephrology (not discontinued); continue carvedilol; everything else completed and pending items kept open.

## Upload set (this folder)
- prompt-task6-v2.txt
- pre_discharge_transition_summary_draft_05232026.docx  (mounted task file)
- golden-KM06-v2.docx  (golden; grader names this string char-for-char)
- grader-guidelines-task6-v2.txt

## Upload sequence
1. Set prompt = prompt-task6-v2.txt.
2. Mount pre_discharge_transition_summary_draft_05232026.docx.
3. Set golden = golden-KM06-v2.docx.
4. Set grader = grader-guidelines-task6-v2.txt.
5. Run Task AutoQC; keep the AutoQC 2.91 reuse note in run docs (propagation family, distinct cold echo/LVEF axis), not in the grader.
6. Pilot. Read by whether the floors propagate the echo/EF de-escalation; bimodal target.

## Build verification
- Both DOCX: Mode A clone of KM02 bases; styles byte-identical; fingerprint diff empty; metadata scrubbed; em/en/arrow/asterisk 0; no brackets.
- Dates: 05/23/2026 (summary), 05/24/2026 (discharge), DOB. No fabricated date.
- Substrate re-verified: no echocardiogram and no EF value anywhere; HFrEF chronic only; cardiology preserve-GDMT + readmission warning.
- Golden catches the echo claim (plain trap-carrier line) and holds the agents staged; scores full under its own grader.

## Honest difficulty note
KM02-KM04 propagation regime: deep and fair and bimodal expected, mean high-50s to high-60s. The one caveat carried from the KM05 echo discussion: EF is mildly checkable, so a strong HF-aware model may verify the absence and catch it. Read the pilot by whether the floors carry the fabr