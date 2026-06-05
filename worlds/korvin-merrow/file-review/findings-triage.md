# Findings Triage - Pipeline Run #1 (B2 Review Packet)

Date: 2026-06-04. Source: `.meta/needs_action.json` (95), red-team (13), cross-doc (71; merged). Integrity: 33/33 generated docx pass the gate; filenames = spec file plan exactly. Items marked **[A]** need Alexander's ruling.

## VERDICT SNAPSHOT

- **Trap fidelity: SURVIVED.** Prednisone has zero numeric current-dose assertions anywhere (refill table shows dispensed strengths with taper-style directions - designed substrate). EW22 ends reassuring and omits functional specifics. Canon doses: 0 drift across all 33 files. Consultant dates all 05/21. MAR dose-less steroid rows intact.
- **Main disease: authoring meta-language leaked into files** ("world close" x13, EW-ID references, guardrails sections, coaching commentary). Cure is a scrub pass, mostly mechanical.
- **Two traps were WEAKENED by generation** (nephrology hands over the restart framework; HD3 un-buries PT/OT). Needs surgical edits.
- ~50 of the 66 cross-doc "mismatches" are noise (identical values, format variance). No action.

## GROUP 1 - FIX: meta-language scrub in WORLD files (mechanical)

| File | What | Edit |
|---|---|---|
| EW11 hospitalist_discharge_planning_hd5_hd6 | "world close" x5 incl. "before 18:00 world close", "world-close snapshot" | -> "as of 05/23/2026 18:00", "end of this documentation period", natural phrasing |
| EW21 case_management note | "at world close" x4 | -> "as of this note (05/23/2026 18:00)" |
| WS3 home_support_equipment | header chrome "Date / Anchor: ... World close 05/23/2026 18:00" + "at world close" | -> "Compiled through 05/22/2026"; drop Anchor vocabulary |
| EW12 renal_trend_summary | "World-close day / discharge planning" row label | -> "HD6 / discharge planning" |
| EW13 MAR | "Source reconstruction ongoing at world close" | -> "ongoing as of 05/23/2026 18:00" |
| EW14 nephrology | "(per EW4 reconciliation)" | -> "(per inpatient pharmacy medication reconciliation note, 05/18/2026)" |
| WS2 sleep_study | "This summary must not: explain the near-fall..." + "This file does not add:" guardrails lists | DELETE; replace with one natural line: "No interval sleep testing since 04/22/2019; this summary reflects historical outpatient management only." |
| WS4 problem_list | "No post-world information, discharge outcome, follow-up findings, task prompt, expected output, or grading material..." | DELETE; replace: "Snapshot reflects the record as of admission 05/18/2026." |
| EW6 rheum provenance | guardrails-flavored passages (red-team #5 grouping) | Soften to natural consultant scope language; KEEP the source-hierarchy/intent-vs-verification content (that IS the trap substrate) |
| EW19 OT assessment | "subtle rather than dramatic and are easy to overlook... likely to understate the supervision need" | DELETE the coaching sentences; the findings themselves stay buried in detail |

## GROUP 2 - FIX: trap restoration (surgical, physician-reviewed) **[A]**

1. **EW9 HD3 note un-buries PT/OT (certifier #94).** "PT and OT findings are being treated as central rather than supplementary... medication-management gap on OT testing is directly relevant to home safety." This defeats the T3 buried-evidence trap from a single physician summary. Proposed replacement: "Continue PT and OT daily. Falls precautions, bed alarm, transfer assistance, and evening orientation continue." (No editorial weighting.) **[A approve]**
2. **EW14 nephrology hands over the restart framework (certifier #92/#93).** HD4 addendum enumerates the exact gating parameters; HD5 addendum names sacubitril/valsartan first, below-home dose, 24-48h recheck - that is most of the T1/T4 golden synthesis. Proposed: keep nephrology's *position* (protect renal recovery; restart when stable) but remove the enumerated parameter list and the specific sequencing prescription; leave cardiology's counter-position untouched so the friction stays live and the synthesis stays the solver's job. **[A approve language]**
3. **EW16 endocrinology consult has no physical exam (certifier #89).** Peer consults have PE sections; absence is an authenticity flag. Needs a brief PE consistent with canon vitals (no new diagnostic findings). Draft will be presented for sign-off before insertion - guardrail 5. **[A approve drafted PE]**

## GROUP 3 - FIX: mechanical consistency

- **MAR ferrous sulfate QOD pattern breaks at HD5 -> HD6** (#19): HD5 "HELD (intake variable)" / HD6 "GIVEN" violates the established alternating pattern. Align HD5/HD6 to the on/off cadence (or document the hold reason on the correct day). **[A: confirm intended on-days]**
- **Letterhead chrome inconsistent across hospitalist notes** (certifier #86-88): HD1-HD2 plain text with "|", HD5-HD6 with "bullet", nursing flowsheet "bullet", while HD3/HD4 use the 2-column table. Normalize all Mercy Vale documents to the table letterhead.
- **Daughter name** (#85): "Lenora Merrow" in one extraction vs "Lenora Merrow-Halsey" x5. Align to canon full name where she's formally listed; bare "Lenora" in narrative prose is fine.
- **Wrong EW reference** (#1): readmission request cites "trend substrate EW16" where the trend summary is EW12 - task file (holdback), fix during Step 10 de-hinting.

## GROUP 4 - PROTECT: do not touch (note-ready for Final Files AutoQC)

- **MAR prednisone rows dose-less** (certifier #90/#91): "GIVEN - interim inpatient steroid coverage per attending plan", no mg anywhere HD1-HD6. This is the central trap working. Note text: quote flag, then: "By design per approved spec section 1.2/2.5: the prednisone dose is deliberately unverifiable; the MAR chains to the attending plan, which likewise preserves source-reconstruction. The reviewer-approved spec carries the same note at 2.5."
- **Refill history multi-strength table** (EW5): dispensing facts does not equal current dose; designed substrate.
- **EW22 reassuring-but-incomplete**: verified intact; omits PT/OT/nursing specifics, ends with routine follow-up tables.
- **Triage vs ED-provider vital variances** (#67-71: temp 100.3 F/38.0 C, HR 104/102, RR 20/18): realistic re-measurement variance, supports "Realistic Imperfections Present" dimension. No edit.
- **Code status "not yet confirmed in triage" -> "Full Code" later** (#40): realistic sequence.

## GROUP 5 - NOTE: noise, no action (~50 items)

Identical-value cross-packet "mismatches" (creatinine 2.62 everywhere, K 5.1, WBC 15.6, all med doses matching with/without "PO"/units), date-format variance (MM/DD/YYYY vs ISO - in-document realism, not the spec filename rule), address with/without ZIP, height/weight unit duals, "mid-LAD" vs "mid-LAD DES". One genuine decision: **Medicare at age 62** (#qualifier) - eligibility needs disability/ESRD. Options: (a) add "(disability)" to the payer line in EW21, (b) switch payer to commercial/marketplace. **[A choose]**

## GROUP 6 - HOLDBACK: 7 task-level files out of the world

The worst red-team findings (EW source maps, F1/F2/F3 enumeration, output-structure dictation - breaking #2,3,4,8,9,10,12) live in the 7 E#-T# request files. Platform rule removes them from the world entirely, so leakage is resolved at world level. They go to `task-files-holdback/` and get the full de-hinting pass at Step 10 before task setup (tracked: preflight prompt rules apply; fix EW16 -> EW12 there).

## OPEN QUESTION (low risk)

Generated files use "PO" route tokens (MAR x18, H&P x2, others) - realistic EHR register; World Files AutoQC did not flag it. The "Oral" rule was a spec-document regex collision. Leave unless Final Files AutoQC flags. **[A confirm leave]**

## EXECUTION ORDER AFTER RULINGS

1. Apply Group 1 + 3 scrubs (object model, content locators, integrity gate per save, last-valid copies).
2. Apply approved Group 2 edits.
3. Move 7 task files to holdback; final filesystem = 26 files.
4. Self-check: re-grep scrub targets = 0; canon-dose sweep; render-check edited pages.
5. Upload folder named exactly `filesystem` in Revisions card -> Apply to Task -> verify 4.1 -> run Final Files AutoQC -> notes from Group 4 as needed.
