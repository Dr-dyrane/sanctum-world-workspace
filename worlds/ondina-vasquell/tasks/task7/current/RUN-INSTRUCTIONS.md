STATUS 2026-06-16 (v1): OV07 = off-text image floor on the Claims Denial / Appeal Preparation lane (fresh P0). OV04 family. The deliverable is an appeal of a skilled nursing facility level-of-care denial; the decisive skilled-need evidence (2.0 cm wound undermining) lives in a transfer-day wound photo the appeal can be finished without opening. Floor = misses the photo, appeal rests on routine dressings; catcher = surfaces the undermining and builds the skilled-need case. The appeal-CONCESSION lever on this lane is retired (ceiling 0.92-0.97); OV07 is a different mechanism (off-text image), not a revival.

## Studio task setup
- Prompt: prompt-OV07.txt (plain "finish it so I can submit it").
- Task files to mount: started_appeal_letter_05242026.docx, transfer_day_nursing_note_05242026.docx, wound_photo_05242026.jpg (Codex render; must match the locked 2.0 cm undermining), plus the full OV world chart.
- Golden: golden-OV07-v1.docx. Grader: grader-guidelines-OV07.txt (model grader).
- Run 10 trajectories.

## Build / regen
- python3 worlds/ondina-vasquell/build/build_ov07.py renders the deliverable, the nursing breadcrumb note, and the golden into tasks/task7/current/.
- The image is produced by Codex from wound-photo-image-spec.md; values are locked to the golden (2.0 cm undermining, probe negative for bone, 05/24/2026).

## Pilot read
- Expect bimodal (OV04 parity): floors miss the undermining, catchers build on it. Target floor 0.10-0.40 with a catcher above 0.85.
- KNOWN RISK: the appeal genre may prime a wound re-check and force the image open (ceiling). If all-catch, one re-roll moving the finding to a more peripheral axis, then retire. If all-floor, confirm reachability before banking.
- Prereg: OV07-pilot-preregistration.md.
