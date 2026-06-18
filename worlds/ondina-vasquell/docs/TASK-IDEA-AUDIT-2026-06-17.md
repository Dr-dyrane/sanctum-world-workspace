# OV Task-Idea Audit and Workflow Map (2026-06-17)

SNAPSHOT 2026-06-17, SUPERSEDED 2026-06-18: this is a dated point-in-time audit. For live counts and status see docs/WORLD-STATUS.md (OV10 was built and OV05 revived after this snapshot, so the slate is now ten tasks across seven lanes with eight floors). Deep audit of the Ondina Vasquell slate. Sources reconciled: docs/WORKFLOW-MAP.md, docs/FLOOR-MECHANISM-LIBRARY.md, DO-NOT-REPEAT.md, docs/FRESH-TASK-IDEAS.md, reference/approved-workflows-and-guidance-2026-06-13.md, every results/ pilot log, and the platform task mounts. World is frozen; all candidates are task-layer only.

## 1. Where we stand

Seven confirmed floors built and floored. OV09 is the pilot-ready eighth. OV05 retired. Six distinct workflow lanes in use. Target is 8 to 10 shippable tasks across 6 to 7 lanes, so we need OV09 to land plus one more floor on a seventh distinct lane to reach the comfortable middle of the target.

| Task | Lane (live) | Mechanism | Outcome |
|---|---|---|---|
| OV01 | Medication Reconciliation at Care Transitions | cold knowledge (stop inpatient enoxaparin at discharge) | FLOOR, banked |
| OV02 | Medical Transcription and Clinical Documentation Completion | off-text text synthesis (new line-site infection) | FLOOR, banked |
| OV03 | Medical Transcription and Clinical Documentation Completion | embedded carry-forward (discharge insulin / stop home sliding scale) | FLOOR 0.10-0.15 (job cb628a70) |
| OV04 | Medical Transcription and Clinical Documentation Completion | off-text image (CPAP adherence printout) | FLOOR, banked bimodal |
| OV05 | Medication Reconciliation (retired packet) | off-text image in a med-rec (OTC bottle photo) | CEILING 10/10, RETIRED |
| OV06 | Referral Intake, Triage, and Scheduling Coordination | embedded wrong, de-telegraphed (perfusion closure) | FLOOR 0.39 (job 577effae) |
| OV07 | Claims Denial Analysis and Appeal Preparation | off-text image (wound undermining) | FLOOR 0.51 (job a33db3d0) |
| OV08 | Utilization Review Concurrent Stay Documentation | embedded wrong (antibiotic route, no OPAT) | FLOOR 0.63 (job d4eaa31b) |
| OV09 | Post-Acute Care Coordination Documentation | v3 on disposition CEILINGED 0.84 (headline); v4 held-med-resume (background) FLOORED bimodal ~0.62, FA/GA done | FLOOR (banking) |

Mechanism coverage so far: cold-knowledge x1, off-text text synthesis x1, off-text image x2, embedded-wrong carry-forward x3 (OV03, OV06, OV08), plus OV09 embedded-wrong pending.

## 2. Workflow map: used vs open

Lanes carrying a task (6):

1. Medication Reconciliation at Care Transitions (OV01)
2. Medical Transcription and Clinical Documentation Completion (OV02, OV03, OV04, the concentration)
3. Referral Intake, Triage, and Scheduling Coordination (OV06)
4. Claims Denial Analysis and Appeal Preparation (OV07)
5. Utilization Review Concurrent Stay Documentation (OV08)
6. Post-Acute Care Coordination Documentation (OV09)

Open lanes, with floor-viability from the bench evidence:

| Open lane | Tier | Floor viability |
|---|---|---|
| Wound Care SOAP / Clinical Progress Note | (progress-note family) | FLOOR-FRIENDLY: commission genre, Harold-proven, embedded-wrong fits |
| Operative / Procedure Planning or Surgical Referral | P1-ish | FLOOR-FRIENDLY with ceiling risk (amputation is a warm axis) |
| Patient Education / Discharge Instruction | P1 | CONDITIONAL: the obvious gaps (offloading, interpreter) are loud and ceiling; needs an off-text angle |
| Inpatient Medical Coding and DRG Assignment | P0 | MODEL-STRONG, ceiling-prone (OV02 coding ceilinged x3); floors only as a commitment/hedge trap |
| Pharmacy Insurance Claim Rejection Resolution | P0 | MODEL-STRONG analysis, ceiling-prone unless an off-text/embedded engine is bolted on |
| HEDIS Medical Record Chart Abstraction and Review | P0 | MODEL-STRONG, ceiling-prone (rule-governed abstraction) |
| CDI Query Response Review | P1 | MODEL-STRONG, ceiling-prone (KM10 CDI was an all-floor killer) |
| Patient Safety Indicator (PSI) Analysis and Reporting | P2 | MODEL-STRONG analysis, ceiling-prone |

The pattern: the easy-to-name open lanes are mostly the analysis genres this model is good at. They floor only if the off-text-finding or embedded-wrong engine is bolted on, never as a clean analysis task.

## 3. Bucket A: untouched ideas (never built, never benched) - 6

| # | Idea | Candidate lane | Mechanism | Floor odds |
|---|---|---|---|---|
| A1 | Wound-dressing commission in a SOAP (silver/alginate/cytotoxic on a clean granulating post-debridement bed, or over-staging) | Wound Care SOAP / Progress Note (NEW 7th lane) | embedded-wrong commission | MED, some ceiling risk (wound is the headline axis) |
| A2 | Bone-health / CKD-MBD over-closure (on cholecalciferol, no DEXA or bone-status note; draft falsely closes "bone health addressed, vit D adequate, no workup") | Progress Note / Care Plan | embedded over-closure on an un-primed axis | MED-HIGH (the proven CPAP-over-closure recipe on a fresh silent axis) |
| A3 | Health-maintenance / immunization over-closure (chart silent on status) | Progress Note / Care Plan | embedded over-closure, un-primed | MED |
| A4 | Foot-care self-management competency over-closure | Patient Education / Progress Note | embedded over-closure, un-primed | MED (adjacent to the offloading/education axis that benched ceiling) |
| A5 | Premature amputation reversal (started surgical/limb-salvage plan pre-lists amputation; reverse to revascularization-first on unsettled perfusion) | Operative/Procedure Planning or Surgical Referral (NEW lane) | embedded-wrong commission | MED with ceiling risk (warm high-stakes axis) |
| A6 | HFpEF aggressive-fluid commission | Progress Note / Order set | embedded-wrong commission | LOW (adjacent to renal thread, low novelty) |

The two un-primed over-closure axes (A2 bone-health, A3 health-maintenance) are the highest-confidence untouched ideas, because they are the exact recipe that produced OV04 on a fresh axis the chart is silent on.

## 4. Bucket B: diversified open lanes (workflow whitespace) - 8

Counted in section 2. Of the eight, two are floor-friendly as-is (Wound Care SOAP, Operative/Surgical Referral), one is conditional (Patient Education, needs an off-text angle), and five are model-strong analysis lanes (Coding, Pharmacy Rejection, HEDIS, CDI, PSI) that floor only with an engine bolted on. For a clean seventh lane to diversify away from the Transcription concentration, Wound Care SOAP (with A1) or Operative/Surgical Referral (with A5) are the realistic picks.

## 5. Bucket C: ceilinged, modifiable to floor - 5

The proven transformation: remove the telegraph, move the catch to an un-primed or off-text axis, and embed the wrong element as routine in a draft the model finalizes. OV06 is the proof: v1 telegraphed and ceilinged 0.90, v2 de-telegraphed the same content and floored 0.39.

| # | Ceilinged idea | Why it ceilinged | The fix to floor it | Odds after fix |
|---|---|---|---|---|
| C1 | Premature amputation (as decline-an-external-rec) | declining an external premise ceilings | re-cut as embedded-wrong: amputation pre-listed as a routine line in a started plan, plain finish prompt | MED (OV06 v2 logic) |
| C2 | Held-med restart (metformin/empagliflozin/lisinopril) | "no restart without labs" reflex is primed | embed a pre-filled restart in a started discharge med plan | MARGINAL: chart says "hold, reassess" explicitly, so it stays semi-telegraphed |
| C3 | Interpreter / health-equity omission | loud (reviewers spontaneously flag interpreter + teach-back) | only if the equity gap is genuinely off-text, not a plain omission | MARGINAL |
| C4 | Over-coding / CDI decline-the-upgrade | coding/CDI genre is model-strong | reframe as a commitment/hedge trap: leave an unsupported option signable rather than analyze | HARD |
| C5 | Prelim-imaging buried finding | text is always read and recognized | only floors as an off-text IMAGE (OV04 engine), and report-as-image carries the fairness caveat | MARGINAL |

## 6. Dead on this frozen chart (not modifiable) - for completeness

- Contrast-order-in-AKI: the frozen admission H&P says "avoid nephrotoxins and contrast," so the catch is a one-line lookup. Piloted, ceilinged 0.89 (job 21e12fc3).
- Anemia over-closure: EW18 explicitly flags anemia as an open item, so the axis is loud.
- Vitals / in-range-but-deranged number: vitals are the most-primed axis, caught every framing.
- Bottle-photo / med-rec image: the med-rec genre forces reading every med source, so the image is not off-text (OV05 ceilinged 10/10).
- C. diff text synthesis: zero stool/diarrhea/GI signal anywhere, chart-silent, unfair.
- Offloading against-the-grain: loud across five notes. Note: re-cut as the embedded-wrong offloading-adequacy claim, this became OV09.

## 7. The count

- Confirmed floors built: 7. Pilot-ready eighth: OV09. Retired: 1 (OV05).
- Distinct lanes used: 6. Distinct open lanes catalogued: 8 (2 floor-friendly, 1 conditional, 5 model-strong).
- Untouched ideas: 6 (Bucket A).
- Ceiling-to-floor modifiable ideas: 5 (Bucket C), of which 1 is MED odds (amputation re-cut) and 4 are marginal or hard.
- Dead on this chart: 6 (section 6).

## 8. Recommendation to reach 8 to 10 across 7 lanes

1. Land OV09 (in flight). That is task 8 on lane 6.
2. For the seventh distinct lane and a ninth floor, build A2 (bone-health/CKD-MBD over-closure) on a Progress Note, or A1 (wound-dressing commission) on a Wound Care SOAP. A2 is the higher-confidence floor (proven recipe, un-primed axis); A1 adds the most lane diversity away from the Transcription concentration.
3. Hold A5 (amputation, lane 8) as the tenth if a second new lane is wanted, benched carefully for the warm-axis ceiling risk, built as embedded-wrong not decline-external.
4. Treat the five model-strong analysis lanes (Coding, Pharmacy Rejection, HEDIS, CDI, PSI) as last resorts; only pursue with an off-text or embedded engine bolted on, never as a clean analysis task.
