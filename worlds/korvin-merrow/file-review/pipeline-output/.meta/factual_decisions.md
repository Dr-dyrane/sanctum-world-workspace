# Factual Decisions — Korvin Merrow World

This document records every invented fact (anything not stated explicitly in the spec or reference files) with brief rationale. All explicit spec facts (patient demographics, baseline med list, dates, lab values, consultant names, traps, etc.) are carried verbatim into `/structured_spec.json` and are not re-listed here.

## Facility identity

The spec and reference docs name **Mercy Vale Regional Medical Center** with an ED at **5 Harbor Crest Way** (visible in the EW1 header). Everything else about the facility was invented to give downstream documents complete, internally consistent letterhead-quality detail.

| Field | Value | Rationale |
|---|---|---|
| City / state / ZIP | Bridgehollow, PA 15211 | "Harbor Crest" suggests a riverside Mid-Atlantic town; Pittsburgh-area area code chosen for consistency. ZIPs in the 15200 range cluster around Pittsburgh, fitting "Bridgehollow." |
| Main phone | (412) 555-0143 | 412 area code matches the Pittsburgh-area town. 555-01xx is a reserved test-prefix block. |
| Fax / department phones | (412) 555-01xx series | All in reserved fictional-test range; distinct numbers per department keep documents distinguishable. |
| NPI | 1437295860 | Plausible 10-digit hospital NPI (Luhn-valid format, invented). |
| EIN | 47-3219085 | Plausible IRS EIN; invented for billing/letterhead context. |
| Unit / room | 5 West Medical, Room 5W-318 | Common general-medicine unit naming. |

## Patient PII (beyond the spec)

The spec is explicit only on name, DOB, MRN, height/weight/BMI, allergy, code status, baseline living situation, baseline function/cognition, baseline clinical anchors, and home medication list. Invented:

| Field | Value | Rationale |
|---|---|---|
| Home address | 1842 Larchmere Lane, Bridgehollow, PA 15214 | Residential ZIP near the facility ZIP; plausible street name. |
| Home / mobile phone | (412) 555-0227 / (412) 555-0228 | Same reserved test prefix. |
| SSN last 4 | 4216 | Plausible last-4 only; full SSN intentionally not stored. |
| FIN / encounter # | KM-2026-051877 | Pattern: initials + year + Julian-ish encounter slot. |
| Marital status | Married | Consistent with wife Mara Merrow named in spec. |
| Employment | Retired (former machinist) | Plausible for a 62-year-old man in a Pittsburgh-area town with multi-decade cardiometabolic disease. Does not contradict anything. |
| Religion | Not specified | Spec never references religion; left blank rather than invent. |
| Preferred language | English | Default; no indication otherwise. |
| Primary insurance | Medicare Part A & B, member ID 1ABC-DE4-F562, effective 2024-03-01 | Patient turned 62 in 2026, but Medicare eligibility before 65 is plausible via disability/ESRD-equivalent pathway given CKD stage 3 and HFrEF. Effective date placed ~2 years before admission. |
| Secondary | Keystone Senior Supplement Plan G | "Keystone" is a common PA insurer-name pattern. |
| Pharmacy benefit | Medicare Part D - Keystone Rx (BIN 017920, PCN MEDDPRIME) | BIN and PCN are realistic Part D format placeholders. |

## Family

The spec names Mara Merrow (wife / family caregiver / historian). Invented:

| Field | Value | Rationale |
|---|---|---|
| Mara phone / email | (412) 555-0229 / mara.merrow@example.org | Reserved test number + example.org domain to keep contact info fictional. |
| Lenora Merrow-Halsey (adult daughter, intermittent caregiver) | Phone (412) 555-0231 | Spec mentions "lives with family" and family-as-caregiver; adding a second named family member supports realistic caregiver-capacity reasoning without contradicting the spec, and gives Task 3 / Task 6 a textured "supervision capacity" surface. Identified as **secondary contact**, not a substitute for Mara. |

## Named clinicians (beyond the seven named in spec)

The spec names: Dr. Elian Vossmere (hospitalist), Dr. Maris Caldrane (Cardiology), Dr. Iven Solthar (Nephrology), Dr. Nerea Veylorn (Endocrinology), Dr. Talia Quenor (PCP), Dr. Soren Halvek (Rheumatology), Mara Merrow (family). It also identifies role-only contributors: hospitalist resident, bedside nursing, PT, OT, case management, social work, pharmacy/medication-reconciliation pharmacist.

For document realism I invented one named clinician per role-only contributor. None of these names are anchored in the spec, so any downstream document can use the role name only if preferred — the named version is provided as a convenience to keep cross-document consistency.

| Role | Invented name | Notes |
|---|---|---|
| Hospitalist resident | Ines Travyn, MD (PGY-2) | Consistent with Vossmere as attending. |
| ED attending | Calder Brensmuth, MD (NPI 1184930526) | EW2 source = "Emergency Medicine provider" (unnamed in spec). |
| Day-shift charge nurse, 5W | Aila Rensby, RN | EW17 attribution. |
| Night-shift charge nurse, 5W | Toren Pelvik, RN | EW17 attribution. |
| Physical Therapist | Renna Volkos, DPT | EW18 author. |
| Occupational Therapist | Brennan Sayre, OTR/L | EW19 author. |
| Case Manager | Priya Ostroff, RN, BSN, CCM | EW21 author. |
| Social Worker | Devra Aimes, LCSW | EW21 author. |
| Pharmacist (med rec) | Ezekiel Marlott, PharmD, BCPS | EW4 / EW13 author. |

NPIs / pagers / office phones for the named MDs (Vossmere, Caldrane, Solthar, Veylorn, Quenor, Halvek, Brensmuth) are all invented placeholders in plausible NPI format and the (412) 555-03xx series.

## Outpatient sites

| Entity | Value | Rationale |
|---|---|---|
| Talia Quenor clinic | Mercy Vale Primary Care - Harbor Crest Clinic, 215 Harbor Crest Way Suite 220, Bridgehollow PA 15211 | Same Harbor Crest corridor as the hospital — keeps PCP within the system, consistent with primary care baseline summary being available to the inpatient team. |
| Soren Halvek clinic | Riverbend Rheumatology Associates, 402 Mill Ridge Road Suite 105, Bridgehollow PA 15213 | Independent outpatient practice (matches "outpatient rheumatology" framing); separate building so refill history and provenance records flow through Mercy Vale's chart but originate externally. |
| Primary outpatient pharmacy | Harbor Crest Community Pharmacy, 318 Mill Ridge Road, NCPDP 3947182 | Consistent with EW5 referencing "external pharmacy fill-history query." |
| Home health referral candidate | Keystone HomeCare Services | EW21 / WS3 mention home health options under discussion; named the candidate agency for document continuity. |
| Outpatient lab | Mercy Vale Outpatient Laboratory - Harbor Crest, Suite 110 | Same building as PCP clinic — Task 5 follow-up labs realistic. |

## Procedural history dates

The spec says "remote PCI with coronary stent placement" and "remote diagnostic sleep study confirming OSA" with no dates. Invented:

| Procedure | Date | Rationale |
|---|---|---|
| PCI with drug-eluting stent (single vessel, mid-LAD) | 2018-09-12 | "Remote" = several years before admission. ~8 years pre-admission is consistent with chronic CAD secondary prevention on aspirin monotherapy. DES is the standard-of-care stent type for elective single-vessel LAD PCI by the late 2010s, so a 2018 placement reads naturally as DES. Specifying mid-LAD is plausible but not load-bearing for any task; WS1 is supplementary background only. |
| Diagnostic polysomnography | 2019-04-22 | Also "remote." Sleep study and CPAP prescription pattern consistent with chronic OSA reserve burden; CPAP adherence "variable" leaves room for the trap design (OSA does not explain acute presentation). |

## Daily numeric trend values

The spec provides full daily lab values for the trend flowsheet (creatinine, BUN, potassium, WBC, glucose ranges, temperature pattern, intake) via the EW12 reference doc. **No invention needed for labs.** The only daily fields I added are BP ranges:

| HD | Date | BP range invented | Rationale |
|---|---|---|---|
| 1 | 05-18 | systolic 96-110, diastolic 56-68 | EW12 says "borderline low-normal pressures with lightheadedness history" — translated to a numeric range consistent with that phrase. |
| 2 | 05-19 | systolic 100-118 | EW12 says "still low-normal, improved." |
| 3 | 05-20 | systolic 106-124 | "Less symptomatic but not clearly at baseline reserve." |
| 4 | 05-21 | systolic 110-128 | "More stable but still vulnerable." |
| 5 | 05-22 | systolic 112-128 | "Stable enough for reassessment." |
| 6 | 05-23 | systolic 114-130 | "Stable on floor checks." |

These ranges trend upward with renal recovery and decreasing volume vulnerability, consistent with EW12's narrative. Numbers are bracket ranges (not single values) to preserve the "orthostatic reserve not fully captured by this table" caveat.

## Functional assessment detail (PT/OT)

The spec describes PT and OT findings qualitatively. I added specific but spec-consistent numeric/scale detail to make the functional evidence concrete enough to drive Tasks 3, 5, and 6 while staying inside the spec's framing ("not back to baseline").

| Item | Invented detail | Rationale |
|---|---|---|
| PT ambulation HD3 | 10-15 feet with rolling walker and standby assist | Consistent with "short-distance ambulation with staff supervision." |
| PT ambulation HD5-HD6 | 100-150 feet with rolling walker and supervision | Improvement without baseline return. |
| Morse Fall Scale | 65 (high risk) | Standard inpatient fall-risk scale; "65" puts him solidly in high-risk bracket consistent with multifactorial near-fall, neuropathy, deconditioning. |
| Assistive device recommendation | Transition from cane → rolling walker post-discharge | Consistent with PT/OT functional gaps and EW18 trap setup ("equipment recommendations"). Adds a concrete discharge-readiness item that EW22 omits. |
| Home safety items | Walker, bedside commode optional, grab bars, rugs removed, supervised mobility first 5-7 days | Standard discharge PT/OT recommendations; supports "service-plan overconfidence" trap (these are *recommendations*, not confirmed deliveries). |
| OT IADL medication finding | 19-item regimen organization fails under fatigue; BID/PRN timing errors | Directly grounded in EW19's "medication-management capacity under fatigue and complexity" with "cognition-in-function" findings; ties to the buried-evidence trap. |
| OT recommendations | Pre-filled weekly pill organizer, teach-back with family, daily family check-in first 5-7 days, outpatient OT for IADL if no progress by +30 | Concrete teach-back / supervision items that EW22's "simplified medication framing" omits. |

## Nursing observation specifics

EW17 describes intake percentages and ambulation qualitatively. I added day-by-day intake bands (e.g., HD1 25-40%, HD6 75-90%) that trend upward consistent with the EW12 "intake improving" narrative, and confirmed the "intermittent evening confusion" was prominent HD1-HD4 and less prominent (but still present for complex questions) HD5-HD6. None of this contradicts the spec; it operationalizes EW17's qualitative narrative for document drafting.

## Insurance / NDC / billing identifiers

NPIs, NDCs, BINs, PCNs, EINs, and member IDs are all invented placeholders in plausible format. None of them are used as canonical answers to any task — they are letterhead/realism detail for the downstream documents.

## What I deliberately did NOT invent

- **Prednisone dose / taper** — the spec is emphatic that prednisone has NO FIXED DOSE; spine carries `"NO FIXED DOSE ASSIGNED"` and `"intentional_non_fixed": true`, and the trap-design requires unresolved uncertainty.
- **Post-discharge clinical findings** at +7 (Task 5) or +30 (Task 6) — the world record ends 2026-05-23 18:00. No post-discharge symptoms, labs, vitals, visits, recoveries, deteriorations, readmissions, non-readmissions, adverse events, or outcomes have been invented. The +7 and +30 anchors are review-only.
- **A final discharge order, final medication reconciliation list, final consultant synthesis, or final disposition decision** — EW11 and EW22 explicitly leave these unfinalized at world close.
- **A definitive infection source** (e.g., specific organism, urine culture result) — EW12 explicitly does not summarize culture/source as a single-cause answer.
- **An adrenal-insufficiency diagnosis** — Endocrinology consult (EW16) explicitly avoids declaring this established; spine preserves the ambiguity.
- **A "winner" among Cardiology, Nephrology, Endocrinology, family, or primary team** — friction is the design.

## Temporal consistency check

- All world-level documents are dated on or before 2026-05-23 18:00. ✓
- Task-level documents are dated on their task anchors (05-24, 05-31, 06-23). ✓
- Procedural history (2018, 2019) precedes admission. ✓
- 3-week decline starts 2026-04-27, near-fall 2026-05-17, ED arrival 2026-05-18 — sequence is consistent. ✓
- Consultant initial notes (Cardio/Nephro 05-19, Endo 05-21) follow admission (05-18). ✓
- Rheumatology provenance is pre-admission but reviewed/available by HD4 (05-21) — internally consistent with EW6's framing. ✓

## Numeric consistency check

- Daily creatinine trend (2.62 → 2.38 → 2.12 → 1.98 → 1.86 → 1.80) approaches but does not return to baseline range (1.6-1.8). ✓
- Daily potassium trend (5.1 → 4.4) normalizes consistent with renal recovery. ✓
- Daily WBC trend (15.6 → 9.4) normalizes consistent with infection improvement. ✓
- BMI 30.6 = 97 kg / (1.78 m)² = 30.6 — math checks. ✓
- Glucose ranges across days remain in a wide 140-270 mg/dL band consistent with diabetes, acute illness, and steroid exposure. ✓
- Intake percentage trend (25-40% → 75-90%) matches EW12's "poor → improved" narrative. ✓
