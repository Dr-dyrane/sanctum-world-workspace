# OV12 task-level image spec - pre-discharge ECG (authored in-repo render)

This is a TASK-LEVEL image for OV12 (not a world file). It IS the scored off-text finding. It is
rendered in-repo by `worlds/ondina-vasquell/build/render_ecg.py` and mounted with the OV12 task
files as `pre_discharge_ecg_05232026.png`. The morphology and raw fields must match the golden
(golden-OV12-v1.docx) and the renderer.

## Provenance (the defence, on the record)

Authored data render, not a sourced image. The waveform is computed numerically and drawn on
standard ECG paper with matplotlib. It is therefore (1) not AI-generated imaging (Larry 06/18 bans
generated photos and films; a rendered printout is allowed, exactly like OV04's CPAP report), (2)
not a real person's ECG, so no PHI, copyright, or attribution to manage, unlike a downloaded strip,
and (3) clinically consistent with the frozen world: new atrial fibrillation is ordinary in an
HFpEF patient under infection stress, and the chart is silent on rhythm, so the strip adds a
finding rather than contradicting one. The PNG is saved metadata-clean. Reproduce with the script.

## pre_discharge_ecg_05232026.png

Genre: a pre-discharge 12-lead/rhythm ECG printout (lead II rhythm strip on standard ECG paper),
recorded 05/23/2026, added to the patient's chart for the team to review. Header carries her
charted identifiers (Vasquell, Ondina; MRN OV-3358104; DOB 03/14/1958; 68F).

The finding (atrial fibrillation, new-onset, rapid ventricular response) is shown as RAW DATA: the
irregularly irregular R-R, absent organized P waves, and fibrillatory baseline are in the tracing,
and the header carries only raw machine fields (ventricular rate about 100 to 115 and irregular,
PR and P axis undetectable, QRS narrow, no prior ECG on file). There is NO printed diagnosis.

## Trap-discipline note (OV04 discipline, carried forward)

- RAW data, no printed interpretation. The strip does NOT print "atrial fibrillation" or "abnormal
  ECG". The reader must recognize new-onset afib from the morphology plus the raw fields, exactly as
  OV04 left "poor adherence" for the model to infer from the raw CPAP numbers. This keeps both the
  did-not-open and the opened-but-glanced failures inside the floor; the catch is read-and-know.
- Legible but easy to skip: a careful chart review opens the tracing and catches it (catcher); a
  cursory completion finishes the renal consult from prose and misses it (floor).
- Manufacturer-neutral, no real brand marks, no real patient identifiers beyond the charted ones.
- No banned characters in any overlay text (no em dash, en dash, arrow, asterisk, bracket).
- The grader does NOT read the image; it scores the model's text output against the golden, so the
  finding (new atrial fibrillation, rapid ventricular response, no prior on file) must be legible in
  the render and must match the golden and the renderer.

## Checklist compliance (IMAGE-SOURCING-CHECKLIST per-asset gate + AGENTS.md guardrail 1)

Canonical image guidance: worlds/marva-lydell/docs/IMAGE-SOURCING-CHECKLIST.md (its date rule is World-3-specific; the rest is general), AGENTS.md guardrail 1, and docs/authored-image-artifact-menu.md. OV12 clears every general line:

- WHY-IS-THIS-AN-IMAGE: PASS. An ECG is natively a tracing printout, not chart prose forced into an image. A rhythm finding does not live as text in the EHR, so imaging it is realistic (the test the OV05 bottle photo failed).
- NOT THE SOLE EVIDENCE, corroborated, agent-and-grader visible: the pre-transfer nursing note (pre_discharge_nursing_note_05232026.docx) points to the tracing ("12-lead ECG obtained... added to the chart"); the in-image machine header (vent rate 104 irregular, PR and P axis undetectable, no prior on file) is OCR-able text that corroborates the waveform; the grader scores the model's text against the golden and can OCR the strip. No separate chart vital states the rhythm, by design, because a 05/23 "HR 104 irregular" line in prose would telegraph the axis and ceiling the task (OV04 pattern).
- SOURCE PATH 1 (in-repo render): authored by render_ecg.py, no external asset, no license, no AI anywhere in the chain.
- LICENSE / SCRUB / MATCH: authored, so no copyright or PHI; PNG metadata-clean; morphology and raw fields match golden-OV12-v1.docx and the renderer.
- TIMELESSNESS: OV is the grandfathered 2026 world (snapshot 05/21/2026), so the 05/23/2026 ECG matches that timeline. The 07/31/2025 narrative-date rule governs new worlds (World 3), not this grandfathered OV task.
- PROVENANCE recorded: source (render_ecg.py), license (authored, none), scrub (metadata-clean), and the corroborating line (the nursing breadcrumb plus the in-image machine header), all above.
