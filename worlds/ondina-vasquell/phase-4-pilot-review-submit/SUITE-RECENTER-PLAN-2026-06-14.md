# OV suite re-center plan - strength/weakness audit - 2026-06-14

Trigger: OV07 ceilinged (3rd restraint-trap ceiling; OV02 x3 + OV07). Re-audited OV03-OV10 at the built level.

## Core principle (proven by OV01 vs OV02/OV07)
This model is STRONG at declining a bad thing SUGGESTED to it, and WEAK at catching a bad thing already EMBEDDED in the document it is finalizing.
- OV01 BANKED: enoxaparin was embedded in the discharge order set; the model had to STOP it; its default is to accept what is on the list -> floored.
- OV02, OV07 CEILINGED: the bad premise was SUGGESTED by an external worksheet/query; the model only had to decline; declining unsupported claims is its core strength.
RULE: design the floor as EMBEDDED-WRONG (the model must catch + remove/correct a wrong element inside the draft it is completing), not SUGGESTED-WRONG (decline an external claim). Also valid weakness axes: commission-against-a-strong-action-default (normalize/hedge), omission-under-load, off-text/image signal.

## Corrected per-task classification (sharper than the raw audit)
| Pos | ID | What the model must do | Axis | Verdict |
|---|---|---|---|---|
| 1 | OV01 | STOP enoxaparin embedded in the order set | embedded-fix / commission | BANKED (the proof case) |
| 3 | OV03 | decline a SUGGESTED CDI osteomyelitis upcode | restraint (suggested-decline) | CEILING-PRONE (OV02/OV07 clone) -> re-center to embedded, or retire |
| 4 | OV04 | rebut payer frame in an appeal letter | synthesis/advocacy (model already argues for patient) | ceiling-leaning -> embed a wrong concession in a started appeal draft |
| 5 | OV05 | decline the sulfa/non-culture substitute | restraint/extraction (allergy is max-salience) | CEILING (hard to fix) -> retire or accept it will not floor |
| 6 | OV06 | render a BINDING continued-stay verdict, not a hedge | commission (decisiveness vs hedge default) | GENUINE weakness -> keep; grader must floor the hedge |
| 7 | OV08 | keep perfusion OPEN + carry disposition table | restraint + thin omission | ceiling-leaning -> embed "perfusion cleared/adequate" in a started referral draft (also ADDS the missing task file) |
| 8 | OV09 | multifactorial, non-blame root cause | restraint (model defaults to systems RCA) | CEILING-PRONE -> convert to omission-under-load (one required contributor easy to drop) or retire |
| 9 | OV10 | fill discharge placeholder with a documented offloading RESTRICTION, not routine "resume as tolerated" | commission / embedded-fix | BEST floor candidate (closest to OV01) -> pilot next |

## Recommended sequence
1. PILOT OV10 next as-is (embedded placeholder + normalization-default = real floor potential). Cheapest test of the principle.
2. RE-CENTER OV08 to "started referral draft already asserts perfusion adequate/cleared" (embedded-wrong) - this also fixes its missing task file.
3. RE-CENTER OV06 grader to floor a non-binding hedge (the model's hedge default is the weakness).
4. CONVERT OV03 and OV09 to embedded-wrong (osteo code already in a draft coding summary to catch+remove; one required RCA contributor embedded-omittable) OR retire if the genre stays model-strong.
5. OV04: embed a wrong concession in a started appeal draft, else ceiling-leaning.
6. OV05: likely RETIRE (sulfa allergy too salient to floor) or accept as a non-floor task.
7. OV07: retire or re-center onto embedded/omission (decision still open; this plan supersedes the "upload v2" path).

## Guardrail
Per DO-NOT-REPEAT #19, cap pilots per task; do not grind a model-strong genre. Prefer re-center onto an embedded/commission/omission axis over re-rolling the same restraint mechanism.
