# Abi-mode review: KM09 v2 packet - 2026-06-12

Scope, cold-read order: prompt-task9-v2.txt, him_preliminary_inpatient_coding_summary_05252026.docx extracted from the built bytes, golden-KM09-v2.docx, grader-guidelines-task9-v2.txt, RUN-INSTRUCTIONS-v2.md, and task9/runs/KM09-v2-pilot-preregistration.md.

Trigger: AO returned v1.1 on 6/12 because the task asked for a coding addendum with no original coding document to addend, so this pass reviews the v2 reseed.

Posture confirmation: read against the built bytes, not the plan. This is not a fully cold read because the reviewer recommended the v2 shape, so the final fairness call on the worksheet remains Alexander-owned or fresh-pass-owned.

Verdict: PASS. No blocking findings. v2 fixes the missing-attachment defect and closes the v1 grader-chart-access gap without introducing a same-author fairness violation. One difficulty watch item is raised for the re-pilot.

## Blocking Findings

None.

## Lens-by-Lens

1. Model's-seat fairness / built-artifact rule: PASS. The mounted worksheet is authored by Ilyana Rook, CCS, Health Information Management, a different author from the attesting physician, Elian Vossmere. The worksheet is marked preliminary for attending review and not final coding until physician addendum is signed. It carries the wrong severity-forward answer, including A41.9 sepsis, G93.41 metabolic encephalopathy, I50.23 acute-on-chronic systolic heart failure, and a septicemia or severe sepsis family with MCC tier. The golden does not countersign it and instead says the worksheet's proposed A41.9 sepsis principal diagnosis is not attested. This is fair external-document rebuttal, not the KM07/KM08 same-author plant class.

2. Genre purpose: PASS. A physician coding attestation certifies the final code set from the documented record, accepting or rejecting coder preliminary work. The golden declines sepsis on documentation grounds, not on a procedural basis.

3. Answer the why: PASS. The golden gives documented-basis reasons for each rejection: sepsis physiology is not a confirmed sepsis diagnosis, no infection-linked organ dysfunction is documented, AMS is symptom-level only, heart failure is chronic without admission acuity, and cultures remain pending.

4. Voice anchor: PASS. The answer is a first-person attesting physician document from Hospital Medicine, using the full documented record as the attestation base.

5. Structural realism: PASS. The worksheet carries a realistic HIM format, CCS author, department, encounter block, preliminary principal and secondary diagnoses, preliminary DRG family, open items, and HIM services footer. Dates are 05/18, 05/24, and 05/25/2026. No register or architecture words appear in the docx.

6. Answer-giving scaffolding: PASS with a watch item. The worksheet teaches the wrong answer and must be rejected, so it does not inflate the correct answer. Its open-items section names the exact scored decisions, which is realistic and fair but may cue the model to scrutinize those items.

7. Difficulty and symmetric spread: reachability PASS, floor pending re-pilot. v1.1 job df5ba05c was bimodal with scores 20, 15, 15, 15, 85, 15, 93, 20, 15, 20. v2 is a new construction and needs a fresh pilot; v1.1's banked pilot is retired.

8. Alignment after change: PASS. Prompt references the mounted summary; golden reviews and declines it; grader names the HIM worksheet; Register Note states the summary is not authoritative; run instructions and prereg require include_input_files=true. v1.1 FA/GA is stale and must be rebuilt from the v2 pilot.

9. Mechanism precision and self-standing records: PASS. Grader scores against golden-KM09-v2.docx plus chart verification, not independent investigation. FA/GA should be rebuilt failure-only from the v2 pilot.

## Non-Blocking Improvements

- The worksheet's open-items section enumerates the exact scored questions. Keep it for the pilot. If v2 over-catches, make the worksheet assert its codes more confidently and trim the open-items enumeration so the model must find the over-capture itself. Do not soften the grader.
- Freeze the v2 preregistration before the re-pilot and do not edit it after.
- Retire the v1.1 FA/GA and banked pilot for submission purposes. Rebuild FA/GA from the v2 pilot, using the single lowest genuine ratify-the-worksheet run.

## Mechanical Pass

- Dates: PASS. Golden and worksheet carry 05/18, 05/24, and 05/25/2026 only.
- Banned characters: PASS across golden, worksheet, grader, and prompt.
- Metadata: PASS. Core author and last_modified_by are empty on golden and worksheet.
- Prompt-to-file reference: PASS. Prompt names the preliminary coding summary and one matching file is mounted.
- Workflow string: Inpatient Medical Coding and DRG Assignment. Confirm against the live tracker sheet at upload.
- Grader chart-access: PASS. include_input_files=true is specified in run instructions and preregistration.
- Names: PASS. Ilyana Rook, CCS has no collision in the 26 world files.
- Register and architecture leak: PASS. No trap, anchor, snapshot, placeholder, or architecture words in either docx.

## Reachability Status

Catcher not yet observed for v2 because the construction is new. Two catchers were observed in v1.1 at 0.85 and 0.93. Recommended pre-bank checks: lock and freeze the v2 preregistration, run the mount-coherence gate on trajectory 1, read a catcher transcript rather than only the mean, and rebuild FA/GA from the v2 result.
