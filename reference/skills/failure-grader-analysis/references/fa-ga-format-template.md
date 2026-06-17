# FA/GA format template

Copy the skeleton, fill every field, then run the gates. The Status line carries the metadata so the prose stays clinical. The FA and GA are each two paragraphs, no bullets, about 1000 characters, no em dashes.

## Skeleton

```
# <TASK> FA/GA - failure-only (<lever in plain clinical terms>)

Status <date>: paste-ready for <job id>. Scored <s1, s2, ... s10>. Mean ~<m>. FA subject: Attempt <n>, run <run id>, <traj id>, score <x> (second-lowest distinct; if not, say so and offer to rebind). Failure-only, two paragraphs each, no bullets, about 1000 characters, no em dashes.

## Failure Analysis

<Paragraph 1: open by naming the bound run by number ("On trajectory N..." or "On Attempt N..."). Lead with the failure: what the response did and why it was wrong, tied to the chart. No competent-baseline or praise paragraph. You may note the response had the evidence and failed anyway, framed as failure.>

<Paragraph 2: why it matters clinically, the consequence stated at the level the chart supports (do not escalate it), any secondary errors, then the central failure restated.>

## Grader Analysis

<Paragraph 1: why the score is appropriate and the requirement that was missed, in clinical terms. A brief plain acknowledgment of the competent remainder is fine to set up the cap; do not write "the grader credited".>

<Paragraph 2: why the miss remains decisive and why the correct secondary work does not overcome it, in clinical terms (the deliverable is unsafe or incomplete for its purpose). Close on the clinical point. Do not argue the scoring framework ("a deep floor would overstate", "the band is well placed").>
```

## What to keep out of the prose

| Do not write | Why | Write instead |
|---|---|---|
| the grader credited / it credited the / credited the correct | both-sides crediting (gate fails) | gave appropriate credit for; or just name the competent items |
| Section A / B / C | self-containment | state the requirement itself |
| Recommended grader rating: ... | the rating lives in the Studio field | omit it |
| em dash or en dash | house rule | plain hyphen or comma |
| Furthermore / Moreover / Consequently / Notably / In addition | AI transition (gate fails) | start the sentence plainly |
| golden, grader, rubric, additive checklist, scored 0.NN | eval register in reviewer-facing prose | the chart, the requirement, the score |
| floor, catcher, bimodal, mechanism, bankable, score cap | builder language | describe the clinical failure and the score plainly |
| a higher score would imply..., the rubric is not additive | defending the score | state the clinical reason the miss is decisive |

The builder and reviewer-register terms are legitimate in internal docs (task state, preregs, runbooks, design notes); they are flagged only in reviewer-facing FA/GA, PL, and reviews, at warn level for now (`verify_voice`).

## Length check

Aim at or just under 1000 characters per field so the gate stays clean. If a field runs a little over and trimming would cost real clinical content, matching the KM range of about 1050 is acceptable; note it in the Status line.
