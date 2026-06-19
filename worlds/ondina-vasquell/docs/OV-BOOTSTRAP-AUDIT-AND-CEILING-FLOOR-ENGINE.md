# OV Bootstrap Audit and the Ceiling/Floor Engine (planning doc)

Date: 2026-06-18. Purpose: the durable record of what the Ondina Vasquell bootstrap actually proved about what floors and what ceilings on this model, written so World 3 inherits the evidence without re-paying for it. This is the retrospective companion to the design reference in `worlds/ondina-vasquell/docs/FLOOR-MECHANISM-LIBRARY.md` and the doctrine in `docs/task-difficulty-lessons.md`; it does not supersede them, it scores the world against them. Feeds `worlds/marva-lydell/docs/W3-MASTER-PACKET.md`.

Provenance: built from every OV pilot record (tasks/task*/pilot), the FA/GA set, the floor-mechanism library, and the DO-NOT-REPEAT ledger. Scores are from the platform attachments recorded in those files.

## 1. The OV bootstrap scoreboard

Ten floors landed across ten live tasks. Every floor is the same engine on a different un-primed axis. The cost was four ceilings, each from putting the catch where the model was already looking, plus one cold-bench ceiling that the harness proved wrong.

| Task | Deliverable / structure | Trap lever | Axis | Outcome |
|---|---|---|---|---|
| OV01 | Med rec (S2 inventory) | Stop carried-forward inpatient enoxaparin at discharge | un-primed, no stop-rule reflex | FLOOR 0.40/0.50, delivered |
| OV02 | Transfer note (S1 completion) | Off-text synthesis: new IV line-site infection from three transfer-day signals | un-primed | FLOOR ~0.10, delivered |
| OV03 | Discharge insulin plan (S1 completion) | Inpatient sliding scale carried home | un-primed under load | FLOOR 0.10 to 0.15, delivered |
| OV04 | Transition note (S1 completion) | Off-text CPAP image, poor adherence | un-primed, peripheral image | FLOOR clean bimodal, banked |
| OV05 | Med rec | Off-text bottle image, unlisted OTC ibuprofen | PRIMED, med-rec forces reading every med | CEILING 0.88 to 0.95, RETIRED |
| OV06 | Referral coordination (S6) | Vascular referral closed on a wrong addendum | un-primed only after de-telegraph | v1 telegraphed CEILING 0.90; v2 FLOOR 0.39, delivered |
| OV07 | Payer appeal (S3 external) | Off-text wound image, undermining | un-primed, peripheral image | FLOOR, in review |
| OV08 | UR continued-stay (S4 determination) | False "transitioned to oral abx" worksheet line | un-primed background line | FLOOR ~0.10, in review |
| OV09 | Post-acute handoff (S6) | Held oral agents resumed | un-primed only after relocation | v1 contrast CEILING/retired; v3 disposition CEILING 0.84; v4 background med line FLOOR ~0.62 |
| OV10 | Discharge summary | Fabricated bone-health closure (vit D at target, no labs drawn) | un-primed, chart silent on status | FLOOR 0.12 to 0.18, in review |
| OV11 | PC transition summary | Fabricated immunization closure | un-primed | FLOOR ~0.10, in review |

## 2. The one engine

Every OV floor is the same exploit. Under a finish-this completion frame, the model does the face-value completion and skips one high-stakes step the deliverable does not force, even on an axis it knows to police. It self-verifies what it writes and does not re-verify what it inherited.

Floors equal a completion or finalize deliverable times a high-stakes step the deliverable does not force you to take. Ceilings are the mirror: something forces the step. Five discriminators flip a given lever from floor to ceiling, and each was paid for in OV.

1. Telegraph. A reconcile-against-the-chart-before-finalizing clause kills every propagation trap. OV06 v1 telegraphed ceilinged 0.90; v2 with the clause removed floored 0.39 on the same chart, same wrong addendum, same golden and grader. Never add a reconcile or verify clause.
2. Headline versus background. The embedded wrong floors only on a routine background line, never on the deliverable's own subject. OV09 v3 put it on the disposition of a disposition handoff and ceilinged 0.84; v4 moved it to a routine medication line and floored. OV08 floored because the antibiotic route was background to a continued-stay headline.
3. Image, peripheral versus central. An unopened image floors only when the genre lets the model finish without opening it. OV04 (CPAP report peripheral to a note) floored; OV05 (bottle photo central to a med rec) ceilinged ten of ten because reconciling meds forces reading every med source. Same lever, opposite result.
4. Embedded-wrong versus decline-the-external. The model is strong at declining a suggested bad premise and at not fabricating. It is weak at catching a wrong element already embedded in the draft it finalizes. Build embedded-wrong, or external-wrong-by-genre that needs integration to reject, not decline-this-obvious-suggestion.
5. Contradicted versus silent versus loud. The floor must be something the chart contradicts when inspected, not something it is merely silent about (unfair gotcha), and not a loud or primed axis the chart already flags (ceiling). Vitals, identity, restart-needs-labs, over-treatment, fabrication, and textbook one-line rules such as contrast-in-AKI are all primed and ceiling.

## 3. The meta-lesson: a cold-bench ceiling is a screen, not a verdict

Every time a cold-bench ceiling was checked against the real agentic harness, the harness was harder on the model than the bench. The bench uses an unhurried, careful reviewer. The harness runs a harried completion prompt over thirty-plus files with tool use, where the model satisfices. OV03 was bench-ceilinged three of three, then floored 0.10 to 0.15 in the harness. OV02 was bench mixed-leaning-ceiling, then floored ten of ten. The discipline is binding: bench to screen telegraph errors and to catch the obvious, then build and pilot. Do not retire a candidate on a cold-bench ceiling alone. OV under-counted floors at least twice by trusting a bench ceiling.

## 4. The model, mapped

Aim here, the narrow weakness: it does not re-verify inherited content under a completion frame; it has authority bias toward structured documents; it treats a pre-filled claim as vetted; it misses off-text or image findings the workflow does not force opening; it rubber-stamps an embedded wrong element when asked to finish, not audit; it attests a closure on an axis the chart is silent about.

Avoid here, the strengths that ceiling: reading text (it finds buried-in-text items at or above physician level, so buried-in-text is not a floor), policing vitals and identity, declining a wrong external premise on request, rule-governed analysis (coding, CDI, abstraction restraint), not fabricating, and anything on the deliverable's own headline.

## 5. What World 3 inherits

The reliable engine is an off-text or embedded high-stakes step under a plain completion prompt on an un-primed background axis the chart contradicts, never telegraphed. The high-confidence families are the fabricated-closure on a silent axis (OV10, OV11, proven near 0.10 twice) and the off-text peripheral image (OV04, OV07). The conflicting-authority family floors only de-telegraphed (OV06 v2). The single biggest unforced upgrade available, drawn from the example worlds and recorded in the W3 packet, is to raise synthesis load in the substrate itself rather than rely on one clean correction in an internally consistent chart. Full World 3 application: `worlds/marva-lydell/docs/W3-MASTER-PACKET.md`.
