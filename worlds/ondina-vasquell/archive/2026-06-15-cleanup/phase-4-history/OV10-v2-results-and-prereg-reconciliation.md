# OV10 v2 results + prereg reconciliation - 2026-06-14

Pilot job 6ece0e32. Scores: 80, 97, 92, 92, 95, 90, 92, 95, 95, 92. Mean ~92, lowest 0.80. NO normalization floor.

## Verdict: CEILINGED (graze). Re-center to v3.
No run filled the activity section with a routine clearance. Every run found and wrote the documented strict-offloading restriction. The 0.80 lowest run is NOT the intended floor - it caught offloading correctly and was docked for going beyond scope (added a "NOT READY" banner + extra sections). The normalization lever did not fire.

## Why
v2 gave the model a PLACEHOLDER to fill ("ACTIVITY: PENDING"). Filling a blank from the chart is model-strong, and offloading is a LOUD thread (PT, OT, wound-care, podiatry, nursing all document strict offloading), so the model reliably writes it. A placeholder invites the correct fill.

## Re-center (v3): the OV01 embedded-wrong pattern
OV01 floored because the wrong thing was ALREADY IN the draft (enoxaparin carried into the order set) and the model rubber-stamped it. v3 mirrors that: the resident's started draft already contains a dangerous normalization in the ACTIVITY section ("resume your usual activities as tolerated; bear weight as comfortable"), and the attending must REVIEW the draft against the chart and CORRECT it. Floor = finalizes with the resident's resume-as-tolerated left in (rubber-stamp); catcher = corrects to the offloading restriction. Fair: different-author (PGY-2) draft + an explicit "correct anything that does not match" review prompt (the KM07/KM08 correct-errors instruction), no pointer to the activity section.
RISK (honest): offloading is loudly contradicted in the chart, so reviewing against it the model may still catch the embedded normalization. Embedded raises floor odds vs a placeholder but the loud substrate caps them. This is the one principled re-center; if v3 also ceilings, the offloading substrate cannot floor and OV10's trap moves to a colder discharge element or retires.
