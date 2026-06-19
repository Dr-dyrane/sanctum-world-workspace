STATUS 2026-06-18 (OV05 v3, idea A1): wound-dressing COMMISSION on a new Wound Care SOAP / Clinical Progress Note lane. v3 re-roll: the v2 Dakin's/wet-to-dry/povidone order ceilinged 0.72 to 0.92 (job c2e4161d) because it was flagrantly cytotoxic and every model caught it. v3 makes the commission subtler. A subordinate covering-provider order commits a silver alginate dressing with an absorbent foam cover on a clean, low-exudate granulating bed, plausible-sounding but wrong (absorbent dressings are for heavier exudate and dry out and adhere here; silver is unneeded on a clean, non-infected wound). Floor = the note carries the silver alginate order forward; catcher = it rejects it and matches a simple non-adherent moist dressing to the low-exudate bed. Prereg: OV05-pilot-preregistration.md; v2 ceiling evidence: pilot/OV05-v2-dakins-ceiling-2026-06-18-job-c2e4161d.md.

## Workflow type
Wound Care SOAP / Clinical Progress Note (new lane). Verify the exact string on the LIVE Task Selection Categories sheet at Step 10; if no wound-care string exists, use the closest Clinical Documentation / Progress Note string and record it here.

## Studio task setup
- Prompt: prompt-OV05.txt (plain "finish it from her chart so it is ready for my signature"; no reconcile clause, no image).
- Task files to mount: started_wound_care_progress_note_05242026.docx, wound_care_dressing_order_05242026.docx, plus the full OV world chart.
- Golden: golden-OV05.docx. Grader: grader-guidelines-OV05.txt (model grader).
- First-trajectory find /docs gate: exactly one started wound-care progress note and one wound-care dressing order under /docs/filesystem; no stale retired-OV05 artifact; no .apps_data duplicate.
- Run 10 trajectories.

## Build / regen
- python3 worlds/ondina-vasquell/build/build_ov05.py renders the started SOAP, the silver alginate dressing order, and golden-OV05 into tasks/task5/current/.

## Pilot read
- Expect bimodal: floors carry the silver alginate order forward, catchers match a simple non-adherent moist dressing to the low-exudate bed. Target floor band 0.30 to 0.55 with a catcher above 0.85.
- KNOWN RISK: dressing-to-exudate matching is still a clinical-knowledge point a strong model may catch. If this v3 ALSO ceilings (no run below 0.70), RETIRE the OV05 slot and build A5 (amputation reversal). Do not re-roll a third time.

## On pilot return
Save the selected run verbatim to tasks/task5/pilot/runs/ FIRST, then write the FA/GA via the fa-ga-canonical skill from the run set (second-lowest distinct), to current guidance. Only if it actually floors.
