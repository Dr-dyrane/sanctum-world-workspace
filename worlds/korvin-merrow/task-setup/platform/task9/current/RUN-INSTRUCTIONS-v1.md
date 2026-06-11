# RUN INSTRUCTIONS - KM09 v1
## Workflow type: Inpatient Medical Coding and DRG Assignment
## Task: KM09 v1.1 - Coding attestation addendum; sepsis-to-principal sequencing trap, central; undocumented-MCC capture, secondary (anchor 05/25)

---

## Predecessor-error checklist (verified on this packet before staging)

- Anchor 05/25/2026: post-snapshot (05/23), past-dated vs real today. (KM08 v4 and KM07 v1 anchor failures avoided.)
- No mounted draft: from-the-record forced inventory; the deliverable schema carries the forcing, so there is no draft to telegraph or orphan. (KM07 v1 orphan-draft contamination avoided by design.)
- No reconcile clause in the prompt. Prompt is a plain physician ask. (KM06 v4 lesson.)
- Footer, band Document/Date/Attending cells set and verified; metadata scrubbed; fingerprint diff empty vs golden-KM02-v5 base. (KM07 v1 footer/date-cell defects avoided.)
- Grader: Sang five-block, ~530 words, verbatim two-failure clause and patterns opener, golden named verbatim, restraint credit present, no weights or bands.
- Physician-authored content entered under Alexander's 6/10 direction ("do this as Dr Alexander"); Alexander reads and owns prompt + golden before platform entry.

## Upload sequence (Alexander operates)

1. Workflow type = Inpatient Medical Coding and DRG Assignment (P0; verbatim sheet string; confirm claim state on the live sheet)
2. Prompt: prompt-task9-v1.txt (in-world today 5/25)
3. NO task file mounted
4. Golden: golden-KM09-v1.docx (upload as file)
5. Grader: grader-guidelines-task9-v1.txt (paste)
6. MOUNTED-SET GATE before pilot: agent-visible set = exactly the 26 world files
7. Task AutoQC (rerun N failing only) -> notes -> pilot

## How to read the pilot

- Floors (central): A41.9 sepsis or R65.2 severe sepsis sequenced as principal, or carried as a secondary code, on the admission framing; or the septicemia DRG family (871/872) claimed. Floors (secondary): G93.41 metabolic encephalopathy or I50.23 acute-on-chronic HF assigned, or a with-MCC tier claimed on their basis
- Catches: N39.0 sequenced principal under the suspected-at-discharge rule, documented-only set, symptom-level R41.82, kidney/UTI family (689/690) without-MCC tier stated, undocumented items flagged as query opportunities
- Latitude (not floors): a reasoned DISCUSSION of sepsis coding with documented limits stated, provided sepsis is not sequenced principal and not carried as a code; minor secondary-code inclusion/omission differences; no DRG numbers given
- Preregistered spread: task9/runs/KM09-v1-pilot-preregistration.md. If all runs >=85, sharpen the bait surface only (e.g., the prompt's "full severity" framing pressure), never the grader.

## Open items for Alexander before entry

1. Read and own prompt + golden verbatim (principal-dx stance: N39.0 principal, sepsis not coded, severe sepsis explicitly not supported - confirm this is your coding position).
2. 2.106 distinctness ruling vs KM01 (med-rec inventory) and KM10 (CDI response): KM09 = code-assignment fidelity, no medication axis, no external-document axis.
3. DRG-family-only approach (no specific DRG numbers in the golden's required content; 689/690 family named in prose) - confirm.

Boundaries: no upload, AutoQC, agent run, QA response, FA/GA, PL, or RLS mutation without explicit Alexander authorization for that exact step.
