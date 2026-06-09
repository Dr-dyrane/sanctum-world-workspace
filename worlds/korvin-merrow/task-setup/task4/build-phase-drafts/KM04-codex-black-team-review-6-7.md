# KM04 Codex black-team review (6/7)

Status: GO for Alexander physician sign-off and platform Task AutoQC, with upload still under Alexander's direct operation. This review audits the local staged set only. It does not upload, run AutoQC, run agents, edit locked canon, or change RL Studio.

Reviewed staged set: `worlds/korvin-merrow/task-setup/platform/task4/current/`

- `prompt-task4-escalation.txt` - sha256 prefix `02289ADE`
- `interdisciplinary_consultant_synthesis_draft_05242026.docx` - sha256 prefix `020F0C8A`
- `golden-KM04-v1.docx` - sha256 prefix `882F3E4A`
- `grader-guidelines-task4.txt` - sha256 prefix `CB999E85`
- `RUN-INSTRUCTIONS.md` - sha256 prefix `217212FE`

## Verification performed

Mode A verification passed for both DOCX files.

- Mounted resident draft verified against the approved KM02 task-file base.
- Golden verified against the approved `golden-KM02-v5.docx` base.
- `styles.xml` byte-identical, fills identical, border colors identical, palette subset, no em dash, no en dash, no arrow, no synthetic token, no banner, and core metadata scrubbed.

DOCX integrity and render checks passed.

- Both files open as ZIP packages and with python-docx.
- Required Word parts are present.
- LibreOffice rendered the mounted draft to one clean page and the golden to two readable pages.
- No blank, corrupt, or visually broken rendered pages observed.

Leak and hygiene scan passed for platform-facing files.

- Mounted DOCX text has no FI IDs, trap language, friction language, source-of-truth language, architecture language, candidate-review language, AutoQC language, Codex/Claude language, python-docx metadata text, synthetic banner, or local path leakage.
- Golden DOCX text has no internal meta leakage.
- The only `FI-T04` and `friction` tokens are in `RUN-INSTRUCTIONS.md`, where they explicitly tell the writer not to mount the rendered FI-T04 request because it is not de-hinted. That is acceptable local instruction material, not a platform upload file.

## Clinical and task-mechanism review

The staged mechanism correctly applies the Claude.ai GO-with-fixes review. The mounted document is a resident draft for attending review, not a signed consultant clearance. That de-authorizes the source enough to make the failure fair: the model may use the draft, but should not ratify its over-closure as the final hospitalist plan.

The cardiorenal paragraph is now quiet enough. It no longer says sacubitril/valsartan, spironolactone, empagliflozin, metformin, or a diuretic must be restarted today. The plant is instead the more realistic consensus-wash: Cardiology and Nephrology are "essentially aligned," sequencing has been "worked through," and the cardiorenal piece is "in hand." That is rebuttable only by synthesis across consultants, MAR, trend source, and hospitalist ownership, which is the intended KM04 axis.

The golden models the correct response. It uses the resident draft as a starting point, explicitly refuses to sign the draft as written, preserves both Cardiology and Nephrology as reasonable, keeps steroid certainty unresolved and non-numeric, treats functional and care-coordination evidence as active discharge-readiness constraints, and ends with a conditional hospitalist-owned plan rather than a final discharge authorization.

The grader is platform-native enough for this stage. It uses task context, golden reference, must-be-present criteria, acceptable variation, and penalize-for sections. It does not assign point values, thresholds, bands, severity labels, or A/B labels. The phrase "scored failure" appears once; this is already present in the KM03 grader that passed Task AutoQC, so it is a watch item rather than a blocker.

## Watch item

The prompt phrase "with clear owners or follow-up for anything still unresolved" mildly primes gap-finding. It is clinically natural for an attending review request and not a trap tell. Keep it for this pilot. If the first KM04 run scores too high because models routinely identify the unresolved pieces, the lightest next lever is to trim that phrase rather than making the mounted draft louder.

## Verdict

GO, with no blocker identified.

Remaining human gate: Alexander physician sign-off on `golden-KM04-v1.docx` before final platform use.

Operational boundary: upload, Task AutoQC, Taiga trajectories, QA, and any RL Studio mutation remain Alexander-authorized platform actions only.
