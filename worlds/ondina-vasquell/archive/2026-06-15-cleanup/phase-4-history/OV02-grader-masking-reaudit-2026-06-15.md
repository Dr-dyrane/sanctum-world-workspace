# OV02 grader-masking re-audit + coding-floor relocation - 2026-06-15

Trigger: Alexander's hypothesis that the grader (not only the model) has been wrong - prompted by Larry E's OV01 return (grader wording overstated the failure; FA/GA on the wrong run). Question: were OV02's five "ceilings" (v1-v5) partly the grader failing to floor a committed coding failure, rather than the model genuinely catching every trap?

## Method
Structural comparison of three graders that all use the KM five-block format:
- OV01 grader (banked; just produced a real 0.50 floor on a genuine miss).
- OV02 v5 grader (retired; never scored below 0.92 across v4/v5).
- KM09 v2 grader (the option-carrying coding shape OV02 v5 explicitly copied; floored deep bimodal).

## Finding 1 - grader-masking does NOT explain the OV02 ceiling
The KM09 v2 grader is structurally identical to OV02's: same Preamble/Register/Section A-B-C, same "patterns to reason about, not items to tick off," same Section B "two failure modes" (fabrication only), NO scoring bands, NO explicit hard-floor clause. With that grader, KM09 scored 20, 20, 15, 15, 92, 15, 20, 15, 85, 25 - eight floors at 0.15-0.25. The run that recommended the correct principal but LEFT THE WRONG ONE AS A FALLBACK (the option-carrying hedge - the same move as "leaving Pathway A signable") scored 0.25, not masked to 0.90. The identical grader machinery floored the exact failure OV02 was built around. The grader can floor this shape; OV02's 0.92-0.98 most likely reflects genuine catches, not masking.

## Finding 2 - the kernel of truth in the hypothesis (process gap)
The OV02 v4/v5 results docs each assert "every run caught it" / "in all 10 runs the model..." with NO transcript cited - the failure mode was inferred from the high score. That is exactly the KM01 error the tasking playbook warns against (line 23: pull the transcript; inferring from output/score produced wrong failure modes). KM09's record, by contrast, read representative floors in full and labeled which were inferred. So OV02 was retired on score-inference, not transcript evidence. 100% rigor still wants the three lowest OV02 runs read (v4's 0.92 runs job be4edca2; v5's 0.95 run job e8b55f48) - needs a Studio export. The structural evidence already makes masking unlikely, but this is the one open confirmation.

## Finding 3 - the real driver: coding floors need a SEDUCTIVE documented pull
KM09 floors because the chart documents sepsis physiology (SIRS) that pulls toward sepsis-principal, and resisting needs a subtle rule (SIRS from a localized infection is not documented sepsis; sequence the documented infection). OV02 v4/v5 wrong answers (AKI-principal, option-carry) were un-seductive: the chart names the limb-threat foot infection as the reason for admission / problem #1 in every note, so UHDDS principal is textbook-obvious and the model catches it every time. An EMBEDDED wrong-principal is not enough; the wrong code must be one the chart genuinely tempts.

## Finding 4 - the frozen chart's seductive coding pulls are already claimed
Seductive coding pulls present in this chart:
- Sepsis physiology (HD1: T 38.2, HR 104, WBC 14.2 with left shift, blood cultures drawn, lactate 1.6) -> tempts A41.9 sepsis-principal. This is the KM09 lever; reusing it in OV is a cross-world near-duplicate (same diagnosis, same rule, different source). DO NOT reuse.
- MRI marrow edema with no bone in path and ID not signing osteomyelitis -> tempts coding acute osteomyelitis. This is OV03's lever (KM10-lineage embedded over-affirmation).
No third, non-colliding seductive coding pull exists, and the world is FROZEN (cannot add a hospital-acquired condition with POA=No, an off-text stage recompute, or new sepsis/osteo substrate).

## Verdict
OV02 stays retired - but the reason is corrected and now rigorous. NOT "coding is model-strong in general" (false: KM09 proves coding floors hard, 0.15-0.25). The reason is: OV02's only available coding substrate is un-seductive, and the chart's two seductive coding pulls are claimed by KM09 (sepsis) and OV03 (osteo). The grader is exonerated.

The coding-floor difficulty budget belongs to OV03, built as the KM10/KM09-proven SEDUCTIVE embedded over-affirmation (a started CDI response that already agrees to add acute osteomyelitis off the marrow edema; the physician must catch and reverse it - equivocal MRI, no bone in path, ID not signing). That is the seductive-pull coding floor; OV02's id has none left.

## Grader hygiene (applies to OV03 and every future grader)
Independently of the above, fold in Larry's OV01 correction: state the central failure precisely (the actual committed move, not an overstated version) and make its materiality explicit, so a genuinely committed failure cannot sit high. This is correct calibration, not tuning to fake depth (it only floors a real committed failure).
