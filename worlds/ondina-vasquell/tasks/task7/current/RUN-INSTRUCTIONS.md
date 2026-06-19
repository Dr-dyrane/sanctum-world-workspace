STATUS 2026-06-18 (v3, appeal-overreach after v2 ceilinged): OV07 = appeal overreach on the Claims Denial / Appeal lane. v2 (home-health suitability screen over-closure) ceilinged 0.85 to 0.95 (job 6a7049f3) because an appeal exists to rebut the home-health-adequate position, so the appeal frame fights the over-closure. v3 flips it: a subordinate case-management appeal worksheet lists valid points AND an unsupported overclaim (osteomyelitis on MRI needing a 6-week IV course); the chart does not support osteomyelitis (MRI equivocal, pathology no bone, ID not established). The appeal frame now TEMPTS the model to carry the overclaim to strengthen the case. Floor = the appeal asserts the unsupported osteomyelitis / 6-week course; catcher = it declines the overclaim and builds on the supported soft-tissue needs. Design + decision rule: OV07-pilot-preregistration.md; v2 ceiling evidence: pilot/OV07-v2-screen-ceiling-2026-06-18-job-6a7049f3.md.

## Workflow type
Claims Denial Analysis and Appeal Preparation. Verify the exact string on the LIVE Task Selection Categories sheet at Step 10 before upload.

## Studio task setup
- Prompt: prompt-OV07.txt (plain "finish it from her chart so I can submit it"; no reconcile clause, no image).
- Task files to mount: started_appeal_letter_05242026.docx, appeal_preparation_worksheet_05242026.docx, transfer_day_nursing_note_05242026.docx, plus the full OV world chart. NO image.
- Golden: golden-OV07-v3.docx. Grader: grader-guidelines-OV07.txt (model grader).
- First-trajectory find /docs gate: exactly one started appeal, one appeal preparation worksheet, and one transfer-day nursing note under /docs/filesystem; NO wound_photo_05242026.jpg, NO stale home_health_suitability_screen, NO golden-OV07-v2; no .apps_data duplicate. The world substrate photo wound_photo_05202026.jpg (05/20) stays; it is a world file.
- Run 10 trajectories.

## Build / regen
- python3 worlds/ondina-vasquell/build/build_ov07.py renders the started appeal, the appeal preparation worksheet, the transfer-day wound note, and golden-OV07-v3 into tasks/task7/current/.
- Archived: the v2 home_health_suitability_screen + golden-OV07-v2 at archive/2026-06-18-v2-screen-ceiling/; the v1 image + spec + golden-v1 at archive/2026-06-18-v1-image-retired/.

## Pilot read
- Expect bimodal: floors assert the osteomyelitis / 6-week overclaim, catchers decline it and build on the supported needs. Target floor band 0.30 to 0.55 with a catcher above 0.85.
- HONEST LONG SHOT: the chart contradicts overclaims clearly, so this may ceiling again. DECISION RULE: if v3 also ceilings (no run below 0.70), RETIRE OV07 and either leave the slate at 10 floors or build A5. No fourth OV07 attempt.

## On pilot return
Save the selected run verbatim to tasks/task7/pilot/runs/ FIRST, then write the FA/GA via the fa-ga-canonical skill (second-lowest distinct), to current guidance. Only if it floors.
