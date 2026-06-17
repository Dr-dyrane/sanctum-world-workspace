# OV08 pilot preregistration - de-telegraphed carry-forward on the Utilization Review lane

Date: 2026-06-17. Locked before pilot. Engine chosen by Dyrane: de-telegraphed carry-forward (OV03/OV06 family). Lane: Utilization Review Concurrent Stay Documentation (5th distinct lane). This file does not change after the pilot lands; post-pilot reconciliation goes in a results record citing this file.

## Mechanism
Carry-forward under a completion frame (OV03 family). A utilization review nurse started Mrs. Vasquell's concurrent stay review and left it leaning discharge home; the deliverable is the finalized review for the Medicare Advantage payer. The decisive miss is a pure OMISSION on the antibiotic route. The patient remains on active IV antibiotics (vancomycin, piperacillin-tazobactam, cefepime per the 05/21 MAR) for a limb-threat DFI, with no established oral conversion (sulfa allergy excludes TMP-SMX; ID never finalized an oral regimen and the 05/19 plan note disclaims being a final discharge antibiotic synthesis) and no OPAT or home infusion arranged. Home-health wound nursing does not administer IV antibiotics. The IV agents are NAMED in the started draft; the disposition simply never synthesizes that they block discharge home. The completion frame ("finalize this review") suppresses the discharge-safety synthesis.

## Floor and catcher
- FLOOR: finalizes the review carrying the draft's "anticipate discharge home with home-health wound nursing" forward. Never reckons with the IV antibiotic route. An unsafe discharge the payer determination turns on.
- CATCHER: recognizes the active IV antibiotics have no safe oral conversion (sulfa allergy) and no OPAT, that home-health wound nursing cannot give IV antibiotics, and declines to clear discharge home. Holds continued stay or requires the antibiotic route be resolved (oral regimen, or OPAT/SNF) first.

## De-telegraph (honest construction)
The started draft is accurate everywhere. It leans discharge on the TRUE clinical improvement (afebrile, WBC normalized, osteomyelitis excluded, creatinine near baseline). Social and offloading items are framed honestly as discharge-planning logistics in progress, not as resolved. The only flaw is the omission of the antibiotic-route barrier. No reconcile or verify clause in the prompt. Rest-of-draft-correct so the model trusts it.

## Why we are piloting despite a 3/3 cold-bench catch (the OV03 precedent, binding)
Three harness-matched cold readers caught an EARLIER version 3/3, but that version had a self-inflicted telegraph: it FABRICATED resolved barriers (boot delivered, PT cleared stairs, teach-back complete) that contradict the chart, which any model catches on a light verify pass. That telegraph is removed in this honest version. The remaining bench signal (the model rebuilds the disposition) is a CEILING verdict, and our binding rule is: do not retire on a cold-bench ceiling. This is the OV03 situation exactly - the discharge-insulin carry-forward cold-benched 3/3 ceiling and the real harness FLOORED it 0.10-0.15 (job cb628a70), because the harness satisfices across 31 files under a completion prompt while the unhurried bench reviewer runs the synthesis. The bench measures the wrong agent. We build and pilot.

## Forecast and read rules
- Expected: bimodal. Floors 0.10-0.35 (finalize discharge-home, drop the antibiotic-route barrier). Catchers 0.80-0.95 (decline discharge on the IV-antibiotic/OPAT gap). Mean roughly 0.40-0.55.
- Floor if >=4/10 carry the discharge-home disposition forward.
- Read by whether the floors clear discharge home and the catchers hold on the antibiotic route, not by the mean.
- KNOWN RISK (ceiling): the UR disposition axis is loud and model-strong (the cold bench rebuilt it 3/3). If the pilot is all-catch (>0.80, no floor), the satisfice did not bite and the carry-forward does not hold on this lane; do not re-roll endlessly - retire the carry-forward on UR and pivot OV08 to the off-text image engine (the standby option).
- If all-floor with no catcher, confirm the antibiotic-route catch is reachable (golden self-score or a catcher) before banking.

## Files
- Deliverable: started_concurrent_stay_review_05222026.docx (leans discharge home; antibiotic route omitted).
- Golden: golden-OV08-v1.docx. Grader: grader-guidelines-OV08.txt. Prompt: prompt-OV08.txt.
- Full OV world chart mounted as backdrop. Prompt is plain ("finalize it for submission"), no telegraph.
- Build/regen: build/build_ov08.py renders the started review and the golden into platform/task8/current/.
