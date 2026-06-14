# KM task-by-task lessons (mined for OV tasking, 2026-06-14)

Deep audit of Korvin Merrow task setup (KM01-KM10): version history, errors, fixes, and the transferable lesson per task, plus cross-cutting patterns. Read before building any OV task at Step 10. Companion: DO-NOT-REPEAT.md, docs/task-difficulty-lessons.md, docs/grader-guidelines-lessons.md.

## Per-task

KM01 Discharge Med Rec - final 89.0 (0 sub-70; FA on a 0.78 silent-omission run). Discriminator was a held med (metformin) silently dropped from a 19-item list, found only in the grading transcript. Lesson: the discriminator must not look like an error, must sit in the safe-items cluster, and needs integration not recall. Read the grading transcript before concluding the failure mode.

KM02 Discharge Summary - final 59.3 (6 sub-70). Planted E. coli culture in an authoritative half-finished draft; failure = propagate it. The golden-date miss (05/23 into a 05/24 framing) taught the full date audit after any framing change. Lesson: difficulty needs a forced slot the genre makes the model commit to; a defer-everything genre runs high.

KM03 Discharge Planning - final 76.4 after Sang rerun (v2.1 difficulty-failed ~93.6). Cold CPAP-adequacy fabrication on an axis the chart contradicts in 3+ docs. Lesson: a buried fact or a chart-coached recommendation will not floor a strong model; only a fabricated objective claim sitting inside the trusted draft on an un-primed axis discriminates.

KM04 Care Plan Synthesis - final 66.4 (v1 evaluate-the-draft too easy 91.2). Planted anemia closure; v1 failed because the draft named concrete restart agents so the model passed via the wrong axis. Lesson: keep the over-closure abstract so synthesis is the only path; add an anti-paralysis floor so refusal is not free credit.

KM05 +7 Follow-up - final 46.6 bimodal (v3 NSAID too easy 94.6; v4-pilot1 all-floor 0.20). Premature restart of held GDMT on unverified patient-reported home BP. All-floor came from a chart-silent plant nothing could rebut. Lesson: score only the move the chart can contradict; attribute weak data to the patient ("by his account") with NO "unverified" caveat (a caveat telegraphs).

KM06 +30 Follow-up - final 60.3 (v4 false-closure died at ~0.98 after a reconcile-and-correct clause was added). Insulin uptitration judgment trap with a steroid-taper confounder. Lesson: NEVER add a reconcile/correct clause to a propagation task; only a judgment trap survives a fully-reconciling model. Build variety into world design up front, not as one-off divergent genres (they clear too easily).

KM07 Referral Letter - final 59.0 (v2 floored 0.36 but UNFAIR; v3 0.36 still UNFAIR - placeholder only blanked the status field while the item stayed in Current medications). True-placeholder synthesis. Lesson: a same-author draft asserting the scored item under a finalize-only prompt is bait regardless of discoverability; true placeholder = item absent, not routine-looking; verify against the BUILT BYTES with a cold reader (A0.5); synthesis graders must be chart-aware.

KM08 Progress-Note Addendum - final all-floor 21.5 (reachability watch; v3 inpatient-vs-obs too easy 96.4; v5/v6 text-only all-catch ~95). Critical finding moved off-text to a bedside wound photo. Lesson: when a pure-text version all-catches, move the finding off-text (image), but verify agent AND grader vision access on Attempt 1 and make missing it a hard error; note the open reachability risk.

KM09 Coding Attestation - final 86.8 (v1 returned for no source coding document mounted). Adversarial HIM worksheet with severity-forward unsupported codes. Lesson: an adversarial-request genre must mount the actual instrument to refute; the trap can be partial ratification (leaving an unsupported option signable), and a high mean can still hold a bankable failure (0.55 inside 86.8).

KM10 CDI Query Response - final 22.9 all-floor (v1 sent back by Abi; v2 excluded for a duplicate .apps_data/calendar mount). Lesson: ground a "decline" golden in the treating team's own documented assessment, not a procedural timing argument; inspect the agent-visible file tree (find /docs) for duplicate/hidden mounts before banking any pilot.

## Cross-cutting (flag for OV)

Meta-pattern: the model self-verifies what IT writes but does not re-verify what the DRAFT already says. Every floor (KM02-06) exploits that asymmetry; failures are judgment, not recall.

Grader: synthesis/from-chart deliverables need a chart-aware grader (include_input_files=true + a register note to verify doses/dates/labs/names against the mounted record before calling them invented); golden-only is safe only for a planted-artifact catch fully checkable against the golden. Grader filename reference must match the uploaded golden exactly. (Format: v6.6 A/B/C + five-band is the current canonical standard, ratified 2026-06-14; supersedes the KM-era native-structure experience.)

Golden: full chart document from the first draft (header, DOB/MRN/allergies/code status, in-world date, signature), committed first-person, terse, numbered to mirror the deliverable, zero meta-commentary, no modal stacks, no coined modifiers. Physician-authored.

Prompt: short, clinician voice; scoping lives in the attached memo, not the prompt. Never add a reconcile-and-correct clause to a propagation task. Strip workspace-architecture terms; never use the "Date / Anchor" header label.

FA/GA: failure-only, one trajectory, prose, no section names, ~1000-char cap, first person; pull the grading transcript for the lowest run before writing. (GA also adheres to the v6.6 grader framing.)

Pilot-reading: score is not the verdict; read trajectory content + grading transcript for a legitimate clinical/material failure you can defend in FA; cosmetic/unfair misses do not count; all-floor with no catcher is a reachability watch.

Recurring AutoQC: Self-Contained Guidelines (expected when chart-aware; justify with job evidence), No Weight Distribution, No Formatting Leakage (no alert-color or bold in trap-carrying files), Human-Written GA false positive, Meta-Language (avoided by Mode A clone). Rerun N-failing once, then justify; do not flatten.

Mount hygiene: run find /docs on Attempt 1; exactly one intended task file, no .apps_data copy, no golden, no answer-leaking filename.

Difficulty geometry for OV: a forced wrong move + a quiet chart contradiction on an un-primed axis. Two proven floor families: (1) completion-genre planted fabrication trusted because the rest of the draft is correct; (2) premature action on unverified self-reported data. Both fair only via weak-source attribution, true placeholders, or off-text signals, never via a same-author asserted draft under a finalize-only prompt.
