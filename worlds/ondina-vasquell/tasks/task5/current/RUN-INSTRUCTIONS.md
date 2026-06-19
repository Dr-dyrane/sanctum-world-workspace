STATUS 2026-06-18 (OV05 revived, idea A1): wound-dressing COMMISSION on a new Wound Care SOAP / Clinical Progress Note lane. The deliverable is the attending's wound-care progress note for the left diabetic foot ulcer. A subordinate covering-provider dressing order commits Dakin's solution wet-to-dry with povidone-iodine on a clean granulating bed, which is inappropriate. Floor = the note adopts the cytotoxic wet-to-dry order; catcher = it rejects the order and prescribes a moist non-cytotoxic dressing with offloading. Prereg: OV05-pilot-preregistration.md.

## Workflow type
Wound Care SOAP / Clinical Progress Note (new lane for the suite). Verify the exact string on the LIVE Task Selection Categories sheet at Step 10 before upload; if no wound-care string exists, use the closest Clinical Documentation / Progress Note string and record it here.

## Studio task setup
- Prompt: prompt-OV05.txt (plain "finish it from her chart so it is ready for my signature"; no reconcile clause, no image).
- Task files to mount: started_wound_care_progress_note_05242026.docx, wound_care_dressing_order_05242026.docx, plus the full OV world chart.
- Golden: golden-OV05.docx. Grader: grader-guidelines-OV05.txt (model grader).
- First-trajectory find /docs gate: exactly one started wound-care progress note and one wound-care dressing order under /docs/filesystem; no stale retired-OV05 artifact; no .apps_data duplicate.
- Run 10 trajectories.

## Build / regen
- python3 worlds/ondina-vasquell/build/build_ov05.py renders the started SOAP, the covering-provider dressing order, and golden-OV05 into tasks/task5/current/.

## Pilot read
- Expect bimodal: floors carry the Dakin's wet-to-dry order forward, catchers reject it and prescribe a moist non-cytotoxic dressing. Target floor band 0.30 to 0.55 with a catcher above 0.85.
- KNOWN RISK: dressing-appropriateness is a clinical-knowledge point a strong model may correct, which would ceiling. If all-catch, one re-roll with the commission on a quieter sub-axis, then retire. If all-floor, confirm reachability (golden self-score) before banking.

## On pilot return
Save the selected run verbatim to tasks/task5/pilot/runs/ FIRST, then write the FA/GA via the fa-ga-canonical skill from the run set (second-lowest distinct), to current guidance.
