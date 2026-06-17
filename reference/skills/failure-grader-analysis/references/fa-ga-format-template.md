# FA/GA format template (KM7-10 house style)

Copy the skeleton, fill every field, then run the gates. The Status line carries
the metadata so the prose can stay clinical. The FA and GA are each two paragraphs,
no bullets, about 1000 characters.

## Skeleton

```
# <TASK> FA/GA - failure-only (<lever, e.g. discharge insulin / hypoglycemia>)

Status <date>: paste-ready draft for <job id>. Scored <s1, s2, ... s10>. Mean ~<m>,
<all low / bimodal>, <no catcher / N catchers>. FA subject: Attempt <n>, run <run
id>, <traj id>, score <x> (<note if not the strict second-lowest distinct; offer to
rebind>). Guidance applied: KM7-10 house style, one trajectory, failure-only prose,
no grader-section names, no bullets, each field about 1000 characters.

## Failure Analysis

<Paragraph 1: open by naming the bound run by number ("On trajectory N..." or "On
Attempt N..."), never a numberless opener. FAILURE-ONLY (pod lead Ahmad): lead with
the failure itself, named specifically and tied to the golden. No competent-baseline
paragraph. You may note the model had the evidence and failed anyway, framed as
failure not praise. One connected argument about this ONE trajectory, not a list of
"It did X. It did Y." sentences.>

<Paragraph 2: spell out the mechanism and the consequences in several sentences (the
harm to the patient), add any secondary failures, and name the central failure. Keep
the run distribution OUT of the FA; it belongs in the GA. Err toward more detail when
the pod lead asks.>

## Grader Analysis

<Paragraph 1: the score is appropriate for an otherwise usable deliverable that
misses the central item; then how the grader got there (compared to golden, found
the failure, applied the cap rule, gave appropriate credit, flagged secondaries).>

<Paragraph 2: the calibration holds across the run set; then the close - a deep
floor would overstate, a high score would ignore the hazard, so the band is well
placed. End: the score is justified.>
```

## The across-trajectory line (when a reviewer asks the FA to justify the low average)

Put one sentence at the end of FA paragraph two that names the pattern and ties it
to the whole distribution. It does not need a third paragraph:

> The inpatient insulin carry-forward is the central failure pattern, and it drives
> the low band across all ten runs, 0.05 to 0.20.

## The GA calibration close (the KM move)

> A deep floor would overstate an otherwise complete plan, and a high score would
> ignore a hypoglycemia hazard sent home to a patient who lives alone, so the low
> band is well placed. The score is justified.

## Phrases that trip the gate (use the right column)

| Do not write (gate rejects) | Write instead |
|---|---|
| the grader credited the accurate parts | gave appropriate credit for the accurate parts |
| it credited the correct renal course | credited correctly the renal course -> reword: noted the correct renal course |
| credited the correct / useful / complete / model ... | gave appropriate credit for ... |
| what the model did well | (lead the FA with the specific competent items instead) |
| Section A / Section B / Section C | (state the content, not the section name) |
| Recommended grader rating: Great | (omit; the rating lives in the Studio field) |
| em dash or en dash | plain hyphen or comma |
| Furthermore / Moreover / Consequently / Notably / In addition | (drop it; start the sentence plainly) |

## Length check

KM7 fields run about 1035 and 1081 characters, so "about 1000" is the target. Aim
at or just under 1000 so the gate stays clean. If the gate flags a field a little
over 1000 and trimming would cost real clinical content, matching KM at ~1050 is
acceptable; say so in the Status line.
