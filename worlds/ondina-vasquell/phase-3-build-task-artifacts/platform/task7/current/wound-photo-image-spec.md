# OV07 (TS7) task-level image spec - transfer-day wound photo with undermining (Codex / Nanobanana)

This is a TASK-LEVEL image for OV07 (not a world file). Like OV04's CPAP report, this image IS the scored off-text finding. Generate it, then mount it with the OV07 task files as `wound_photo_05242026.jpg`. It is DISTINCT from the substrate EW30 photo `wound_photo_05202026.jpg` (05/20, granulating, no scored finding); this one is the 05/24 transfer-day re-photograph that newly documents undermining. The finding values MUST match the golden (golden-OV07-v1.docx) and build_ov07.py.

Lane / mechanism: Claims Denial Appeal (skilled nursing facility placement denied, payer says home health suffices). Off-text image miss, OV04 family. Floor = the model finishes the appeal from the 05/20 wound prose and misses this transfer-day photo; catcher = opens it and makes the undermining the decisive skilled-need argument.

Shared rules:
- No banned characters in any overlay text (no em dash, en dash, arrow, asterisk, bracket).
- No real patient identifiers; no patient face; only the foot and wound. No real brand marks.
- Clinically faithful to the chart: granulating base, no exposed bone (matches the 05/20 wound care note). The ONLY new finding is the undermining tract.
- The finding must be LEGIBLE (it is the scored catch) but shown as a plain raw transfer-day chart photo, not highlighted or interpreted.

## wound_photo_05242026.jpg

Genre: a bedside clinical wound-care photograph taken at transfer on 05/24/2026 and added to the chart, the kind a CWOCN takes when re-photographing a wound before a level-of-care decision.

Generation prompt (give to Codex imagegen):
"A clinical close-up photograph of the plantar left forefoot of an older adult patient, taken at the bedside for the chart on transfer day 05/24/2026. A single diabetic foot ulcer over the first-to-second metatarsal head, about 3 centimeters across, with a clean red granulating base and no exposed bone. A sterile cotton-tipped applicator is inserted under the proximal heel-side wound margin and disappears beneath the skin edge, demonstrating a tract under the skin. A disposable paper wound ruler lies beside the wound for scale. A plain typed white annotation strip across the bottom reads exactly: WOUND PHOTO 05/24/2026  Undermining 2.0 cm at 12 oclock, tracks proximally. Probe to bone negative. Even diffuse clinical lighting, neutral blue drape underneath, documentary medical-photography style, sharp focus, true color, no patient face, no instruments other than the applicator."

Hard constraints / negative prompt:
- The annotation strip text MUST be present and legible (Undermining 2.0 cm at 12 oclock, tracks proximally; probe to bone negative; dated 05/24/2026). It is the scored finding.
- Show the applicator tracking UNDER the proximal margin so the undermining is visually evident, not a flat ulcer.
- Keep the base granulating with no exposed bone, consistent with the 05/20 description. The only NEW finding is the undermining tract.
- No interpretive words anywhere (no "skilled care needed", "home health inadequate", "severe", "deteriorating", "worsening"). Raw measurement only; the clinical interpretation is the model's job.
- No patient face or identifiers; no brand marks; clinical-documentation realism, not a graphic or sensational image.

Trap-discipline note: this image carries the OV07 scored finding (wound undermining / tunneling means skilled CWOCN packing and assessment that home health cannot provide, so the denied SNF skilled placement is justified). The grader does NOT read the image; it scores the model's appeal text against golden-OV07-v1.docx. Make it a plain transfer-day chart photo, legible-but-easy-to-skip, so a careful read catches the undermining (catcher) and a cursory "finish the letter" completion misses it (floor). The undermining value (2.0 cm at 12 o'clock, tracks proximally, probe to bone negative, dated 05/24/2026) must match golden-OV07-v1.docx and build_ov07.py exactly.

Placement: mount as a task-level file with the OV07 task files as `wound_photo_05242026.jpg`. The started appeal and the chart carry one quiet transfer-day breadcrumb ("wound re-photographed at transfer 05/24, image added to chart"), so the finding is fair to reach but not forced.
