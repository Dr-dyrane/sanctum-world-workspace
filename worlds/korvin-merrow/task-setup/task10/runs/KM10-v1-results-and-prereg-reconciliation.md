# KM10 v1 — pilot results and prereg reconciliation (6/10)

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

## Open watch item — reachability
The KM07-class flag, sharper here: with no observed catcher, it is unconfirmed that this model can reach the correct decline at all on this chart. Before banking KM10, confirm whether ANY of the ten runs declined. If none did, decide whether the golden's decline stance is the consensus-correct answer (deep killer, flag the low ceiling to the reviewer) or whether affirming-with-rationale is clinically defensible (then the golden/grader widen to treat a transparent affirm as acceptable variation). This is the clinical hinge recorded with Alexander on 6/10; he moved to FA/GA, which records the decline stance as correct.

## FA/GA
`task10/fa-ga/FA-GA-current.md`. FA subject = single lowest confirmed run, Attempt 8 (0f863cd1, 0.15, agreed + coded G93.41). GA is failure-only on the within-floor ordering gap (coded agreement 0.15 vs bare agreement 0.35); the absent catcher is carried as a reviewer watch item, not GA field content.

## Status / decision
PILOTED; all-floor; FA/GA drafted. Difficulty is not in question (deepest in the suite); reachability is. Next eligible step is Alexander's, pending the full-vector / catcher confirmation: if a catcher exists, enter FA/GA then 3 PLs; if not, raise the reachability question to the reviewer before banking.
