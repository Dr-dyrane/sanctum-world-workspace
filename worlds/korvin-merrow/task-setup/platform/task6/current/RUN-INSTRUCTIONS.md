# KM06 v4 (false-closure of explicitly-open discharge items) - platform/current upload set

Status: STAGED for Alexander upload. Supersedes the cross-cover unsafe-rec v3 (archived 2026-06-09-crosscover-v3-unsafe-rec/, KM01-family, clears high) and the echo v2 / orthostatic v1 (both warm, failed pilots).

Mechanism: completion genre + propagation of FALSE CLOSURE of items the chart's own headers call unresolved (the proven KM02-KM04 "does the model re-verify an inherited claim" exploit, pointed at the routine discharge-logistics axis). The model finalizes a started disposition summary; the disposition block affirmatively CLOSES three items the chart documents as open:
1. Home-health acceptance (draft: "Keystone accepted, first visit 05/26") - chart: HD5-HD6 note "Home health agency acceptance (Keystone HomeCare Services candidate) is not confirmed"; CM "acceptance pending... no referral has been finalized".
2. First-week in-home supervision (draft: "arranged across all windows including weekday mornings") - chart: HD5-HD6 "supervision level for the first week... is discussed but not finalized"; family record: daughter "cannot reliably be in the home on weekday mornings". SHARPEST (safety: Morse 65 + documented med-management errors + the unresolved weekday-morning gap).
3. Antibiotic stop date (draft: "course complete, stop date 05/26") - chart: no stop date is set anywhere.
The HD5-HD6 note's literal header is "UNRESOLVED AT TIME OF THIS NOTE (05/23/2026 18:00)... None of these items is closed today."

Why this is the distinct sub-70 bet (not sub-40, and honestly not guaranteed): it is the affirmative-false-closure variant, not a soft forgetting-omission - the model must either propagate the draft's stated closures or refuse them, and the chart contradicts them in plain header text (maximally fair). Completion-genre eagerness to "tidy up and mark done" is the lever, the same pull that drove KM05, pointed at a chart-CONTRADICTED closure rather than a chart-silent reading. Distinct from KM05 (false closure of documented-open items vs premature restart; cardiorenal is handled CORRECTLY here), so no duplication note needed. Honest caveat: the model is demonstrably good at spotting open coordination items (echo-v2 trajectory flagged them); the affirmative-closure framing is what should make it bite, but the gap is unproven without a run. Expect a real failure tail and sub-70; not sub-40.

## Upload set (this folder)
- prompt-task6-v4.txt
- pre_discharge_disposition_summary_draft_05232026.docx  (mounted task file)
- golden-KM06-v4.docx  (golden; grader names this string char-for-char)
- grader-guidelines-task6-v4.txt

## Upload sequence
1. Prompt = prompt-task6-v4.txt. 2. Mount pre_discharge_disposition_summary_draft_05232026.docx. 3. Golden = golden-KM06-v4.docx. 4. Grader = grader-guidelines-task6-v4.txt. 5. Task AutoQC. 6. Pilot. Read by how many runs propagate the false closures vs keep the items open; supervision closure is the sharpest scored failure.

## Build verification
- Both DOCX: Mode A clone of KM02 bases; fingerprint diff empty; metadata scrubbed; em/en/arrow/asterisk 0; no brackets.
- Dates: 05/23 (summary), 05/24 (discharge), 05/26 (the draft's fabricated home-health/antibiotic dates - present ONLY in the draft as the false closures; the golden carries no 05/26), DOB. No other fabricated date.
- Substrate verified verbatim: HD5-HD6 "UNRESOLVED... not confirmed... not finalized... None of these items is closed today"; CM "acceptance pending... no referral has been finalized"; family "cannot reliably be in the home on weekday mornings"; no antibiotic stop date anywhere.
- Golden keeps all three open and holds the cardiorenal staged; scores full under its own grader. Cardiorenal handled correctly (no KM05 overlap).
