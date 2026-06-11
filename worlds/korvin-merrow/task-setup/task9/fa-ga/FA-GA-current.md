# KM09 v1 FA/GA - current draft (6/10)
Job df5ba05c. Bimodal spread: 20, 15, 15, 15, 85, 15, 93, 20, 15, 20; mean about 0.31; eight floors in the 0.15 to 0.20 band and two catchers (Att5 ff87c004 0.85, Att7 80be5747 0.93). FA subject = single lowest run, Attempt 4 (962ea7f6, 0.15); the 0.15 floor is shared by Att2, Att3, Att4, Att6, Att9, and Att4 is the run read in full here. Format = Abi 6/9 failure-only, no grader section names, two short paragraphs each. Physician voice, no em dashes. Alexander owns final wording; enter on platform only after clicking Start Failure Analysis and Grader Analysis.

---

## Failure Analysis (Attempt 4, run 962ea7f6, 0.15)

The model sequenced A41.9 sepsis as the principal diagnosis and set the working DRG to the septicemia family. The record documents only suspected urinary-source infection and sepsis physiology, never a confirmed diagnosis, with no organ dysfunction linked to it; the attending's discharge snapshot ranks the suspected infection as primary. The correct attestation sequences the urinary-source infection N39.0 as principal, with the DRG in the kidney and urinary tract family without MCC.

This was not a missed read. The model saw that sepsis was still only suspected at discharge, then used the rule that codes a suspected inpatient diagnosis as established to justify the severe framing, when that rule supports coding the documented infection as principal, not escalating to sepsis. It carried the escalation into the DRG, claiming a septicemia family the record never establishes. A correct attestation routes the sepsis question to a physician query and leaves it out of the assigned code set.

---

## Grader Analysis (failure-only)

The guidance names the central failure as sepsis sequenced to principal or carried as a secondary code, and separately allows a reasoned discussion of the suspected-at-discharge rule. It does not say how to score the case in between, where a response prepares the infection as principal but also offers sepsis-to-principal as a co-equal attestation option with its higher septicemia DRG. One catcher presented that option and scored 0.85, while the catcher that kept the infection principal and routed sepsis only to a query scored 0.93.

The eight-point gap between those two is the grader's own judgment of how much the offered option should cost, not a rule the guidance sets. Stating that presenting sepsis-to-principal as a selectable attestation path carries the central failure forward at reduced weight, even when the prepared default is the infection, would anchor that boundary without changing how a clean catch or an outright sepsis-principal floor is scored.
