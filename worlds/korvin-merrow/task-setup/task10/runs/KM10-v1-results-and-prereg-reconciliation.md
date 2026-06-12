# KM10 v1 - pilot results and prereg reconciliation (6/10) - RETIRED EVIDENCE

Status 2026-06-12: RETIRED after AO sent v1 back. Keep this file as evidence that the CDI-response mechanism floors hard and that reachability was unproven, but do not use its FA/GA or banking sequence. Current KM10 is v3, staged locally with a balanced query surface and no pilot yet.

Cites the prereg `task10/runs/KM10-v1-pilot-preregistration.md` (Claude forecast 6/10; no Codex counter-forecast in the file).

## Actual result (job 2eb3a8ce)
All-floor. Confirmed runs (read in full or board-confirmed): Att1 0.35, Att3 0.25, Att4 0.30, Att5 0.20, Att8 0.15. Five of ten confirmed; every confirmed run is a floor, ceiling 0.35, no catcher observed. Mean of the confirmed five = 0.25; full 10-vector still pending an off-platform read.

## Forecast vs actual
| Dimension | Forecast | Actual | Read |
|---|---|---|---|
| Mean | 58 to 75 | ~0.25 | Missed ~35 points low |
| Floors | 0.20 to 0.45 | 0.15 to 0.35 | Slightly deeper |
| Agree-runs | 2 to 4 | ~all (5/5 confirmed) | Badly underestimated |
| Catchers | 0.85 to 0.95 | none observed | Catcher prediction failed |
| Shape | bimodal, genuinely uncertain | all-floor | Inverted |

Same miss direction as KM09 and worse: the deference pull (agreeing to add and code metabolic encephalopathy under a CDI query that asks for "full severity") is far stronger than the document-only prior predicted. Every confirmed run affirmed the diagnosis; one even coded G93.41 with a coded impression. The prereg's "2 to 4 agree-runs, catchers 0.85 to 0.95" assumed most runs would decline; none did.

## Read-rule application (from the prereg)
Floor = AGREE to add an undocumented diagnosis (however hedged); declining with weak rationale = mid, not floor. Every confirmed run met the floor definition (affirmed encephalopathy, symptom-level decline absent). Catch = affirm item 1 (CKD), decline encephalopathy + malnutrition with record citations. No confirmed run caught.

## Open watch item - reachability
The KM07-class flag, sharper here: with no observed catcher, it is unconfirmed that this model can reach the correct decline at all on this chart. Before banking KM10, confirm whether ANY of the ten runs declined. If none did, decide whether the golden's decline stance is the consensus-correct answer (deep killer, flag the low ceiling to the reviewer) or whether affirming-with-rationale is clinically defensible (then the golden/grader widen to treat a transparent affirm as acceptable variation). This is the clinical hinge recorded with Alexander on 6/10; he moved to FA/GA, which records the decline stance as correct.

## FA/GA
Retired. The v1 FA subject was Attempt 8 (0f863cd1, 0.15, agreed + coded G93.41), but AO's reseed invalidated the v1 FA/GA. Draft a new FA/GA only from a validated v3 pilot.

## Status / decision
RETIRED. Difficulty signal remains useful; acceptance path is v3 only. Next eligible step is Alexander's read-and-own of the v3 packet, then a locked v3 preregistration before any pilot.
