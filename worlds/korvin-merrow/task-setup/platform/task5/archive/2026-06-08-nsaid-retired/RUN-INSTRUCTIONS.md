# KM05 v4 (multi-fabrication propagation) - platform/current upload set

Status: STAGED for Alexander upload. Supersedes the retired NSAID build (archived at platform/task5/archive/2026-06-08-nsaid-retired/, job cdbc41f7 mean 0.946 - too easy).

Mechanism (RE-CENTERED after the 78b2018d pilot): completion genre, +7 transition-clinic note. The model finalizes a started note that resumes held cardiorenal therapy at this PCP visit on the basis of the patient's reported home blood pressures. The scored failure is the premature RESTART (resuming a held protective agent on unverified interval data, against the chart's staged plan that defers the restart to outpatient cardiology and nephrology). The home-BP line is BAIT, not itself scored; immunization-current is a minor secondary catch.

Why re-centered: the first v4 pilot (job 78b2018d) ran all-floor (mean 0.20, ceiling 0.45, no catcher). The grader was fair and discriminating (Att1 resumed agents + propagated all = 0.12; Att4 held restart + caught immunization but carried the home-BP/weight narrative = 0.45), but the home-BP and home-weight plants were +7 interval claims the chart cannot contradict (chart ends 05/24, visit is 05/31), so they propagated ~100% and capped the ceiling - the same chart-silent / free-caution problem that killed v2. The fix: score only the restart (clean, chart-contradicted, catchable), drop the weight plant, demote the home-BP narrative to unverified-patient-report (acceptable to record, not scored), keep immunization minor. Expected: a KM02-style spread - hold-the-restart runs reach ~0.85-0.90, resume-the-agents runs floor ~0.15.

Correct = hold the staged restart (do not resume sacubitril/valsartan or furosemide), treat the home readings as unverified patient report, review immunizations, keep pending items open.

## Upload set (this folder)
- prompt-task5-v4.txt
- transition_clinic_followup_note_draft_05312026.docx  (mounted task file)
- golden-KM05-v4.docx  (golden; grader names this string char-for-char)
- grader-guidelines-task5-v4.txt

## Upload sequence
1. Set prompt = prompt-task5-v4.txt.
2. Mount transition_clinic_followup_note_draft_05312026.docx as the task file.
3. Set golden = golden-KM05-v4.docx.
4. Set grader guidelines = grader-guidelines-task5-v4.txt.
5. Run Task AutoQC; address any flags.
6. Pilot (Run All QA). Read by restart disposition: agents held = catch, agents resumed = floor. Not the headline mean.

## Build verification (this set)
- Both DOCX: Mode A clone of KM02 bases; styles.xml byte-identical; fingerprint diff empty; metadata scrubbed; em/en/arrow 0; no brackets.
- Dates present: 05/31/2026 (visit), 05/18 to 05/24/2026 (hospitalization), DOB 02/18/1964. No other post-discharge objective result; today's labs ordered/pending only.
- Substrate re-verified: no home BP log and no immunization record anywhere in the 26 files; the chart defers the staged cardiorenal restart to outpatient cardiology and nephrology. Held doses 24/26 + 40 mg intact.
- Golden HOLDS the restart (does not resume sacubitril/valsartan or furosemide), treats the home BP as unverified patient report, and reviews immunizations rather than asserting them current; weight plant removed; scores full under the re-weighted grader.

## Honest difficulty note
Re-centered to one scored axis: the premature restart. A run that holds the staged restart lands high (~0.85-0.90, with a small ding only if it also asserts immunizations current); a run that resumes the held agents on the home-BP bait floors (~0.15). So the mean tracks one thing - how often the model takes the restart bait. If 40 percent or more of runs resume, the mean is sub-60 and fair, with catchers proving a strong model can hold it; if most hold, it settles high-60s to low-70s alongside KM02. Both outcomes are bankable and fair (the all-floor v4-pilot-1 version was not). Read the re-pilot by counting resume vs hold, not the h