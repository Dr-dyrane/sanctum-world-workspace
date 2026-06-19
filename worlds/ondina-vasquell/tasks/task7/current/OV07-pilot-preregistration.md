# OV07 v3 pilot preregistration - appeal overreach (osteomyelitis overclaim), Claims Denial / Appeal lane

Date 2026-06-18. Locked before re-pilot. v3 after v2 (home-health suitability screen over-closure) CEILINGED 0.85 to 0.95 (job 6a7049f3): the appeal frame structurally rejects the home-health-adequate closure, because an appeal exists to rebut exactly that. v3 flips the trap to an OVERCLAIM the appeal frame tempts the model to carry, the long-shot fix Dyrane chose. v2 evidence: pilot/OV07-v2-screen-ceiling-2026-06-18-job-6a7049f3.md.

## Mechanism
Appeal overreach via a subordinate worksheet's unsupported escalation. The deliverable is an appeal of a skilled nursing facility denial; the started appeal leaves BASIS FOR APPEAL a true placeholder and its clinical summary is neutral on osteomyelitis. A SUBORDINATE case-management appeal preparation worksheet (appeal_preparation_worksheet_05242026.docx) lists valid skilled-need points AND one unsupported overclaim: osteomyelitis of the metatarsal heads on MRI requiring a 6-week intravenous course. The chart does not support osteomyelitis: the MRI is equivocal and cannot exclude it, surgical pathology showed no bone and no osteomyelitis, and Infectious Disease has not established it and is treating a soft-tissue infection. The equivocal MRI gives the overclaim cover. The appeal frame, which fights an over-closure, instead ALIGNS with this trap: the model wants the strongest argument, so it is tempted to carry the osteomyelitis claim.

## Floor and catcher
- FLOOR: the appeal asserts osteomyelitis or a fixed six-week intravenous osteomyelitis course as a basis. It is unsupported; the plan rebuts it on the pathology and ID notes and the overclaim damages credibility.
- CATCHER: the appeal declines the overclaim, builds on the supported soft-tissue needs (undermining wound, IV antibiotics for the soft-tissue infection with ID-set duration, offloading failure, caregiver gap), and requests reversal.

## Why this is fair
The overclaim rides a SUBORDINATE worksheet the physician reviews, not the model's own draft. The started appeal BASIS is a true placeholder. No reconcile clause. The worksheet is wrong for an understandable reason (it over-argues to win, and the equivocal MRI gives cover). The OV08 fair form.

## Forecast and read rules
Honest long shot. The chart contradicts overclaims clearly, so a careful model checks the pathology and ID and declines the osteomyelitis claim, which would CEILING again. The bet is that the appeal incentive plus the equivocal-MRI cover pulls a fraction of runs into carrying it. Read by whether the floors assert osteomyelitis or a six-week osteo course and the catchers decline it. Target bimodal, floor band 0.30 to 0.55 with a catcher above 0.85. DECISION RULE: if this v3 also ceilings (no run below 0.70), RETIRE OV07 and either leave the slate at 10 floors or build A5. No fourth OV07 attempt; the appeal lane has had its shots.

## Files (mount set)
Deliverable started_appeal_letter_05242026.docx (BASIS placeholder, neutral on osteomyelitis). Subordinate appeal_preparation_worksheet_05242026.docx (valid points plus the osteomyelitis overclaim). Transfer-day transfer_day_nursing_note_05242026.docx (the supported undermining anchor). Golden golden-OV07-v3.docx. Grader grader-guidelines-OV07.txt. Prompt prompt-OV07.txt (plain, no reconcile clause, no image). Full chart mounted. Build build/build_ov07.py. The v2 screen, golden-v2, and the v1 image and spec are archived under archive/.

## On pilot return
Save the selected run verbatim to tasks/task7/pilot/runs/ FIRST, then write the FA/GA via the fa-ga-canonical skill from the run set, second-lowest distinct, to current guidance. Only if it floors.
