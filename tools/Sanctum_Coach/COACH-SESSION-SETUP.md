# Sanctum Coach session setup (the mirror runbook)

The Coach runs as a Claude Project in claude.ai. This repo holds the governing copy of the package (the files below) plus our inputs and working log. The Project is a MIRROR: it produces the platform transcript, but nothing it makes is canonical until it is checked back into this repo and passes our gates. Governance stays here. See `docs/sanctum-coach-merge.md` for the why.

## One-time Project setup (about 3 minutes)

1. claude.ai, sign in with the Mercor expert email, click Projects.
2. Create Project, name it "Sanctum Coach", set the model to Opus (4.8 High if offered).
3. Open the Instructions box and paste the ENTIRE contents of `01_Custom_Instructions_PASTE_INTO_INSTRUCTIONS.txt`. Save. Do not upload this one as a file; it must be pasted.
4. Open Files / project knowledge and upload the six files from `Upload_to_Claude/` (the four curricula 02, 03, 04, 05 and the two templates). That is all the project knowledge it needs.
5. Do NOT add `Template_DataBank.docx` to project files. It is attached to the CHAT later, only when you reach Template Curation.

No Projects on the plan: start a normal chat, paste the full `01_Custom_Instructions...txt` as the first message, and attach the phase's files to that chat.

## Upload manifest (what goes where)

| File (in this package) | Destination | When |
|---|---|---|
| 01_Custom_Instructions_PASTE_INTO_INSTRUCTIONS.txt | Project Instructions box (paste, not upload) | Setup |
| Upload_to_Claude/02_Brainstorm_Curriculum.md | Project knowledge | Setup |
| Upload_to_Claude/03_Workflow_Database.md | Project knowledge | Setup |
| Upload_to_Claude/04_World_Spec_Curriculum.md | Project knowledge | Setup |
| Upload_to_Claude/05_Template_Curation_Curriculum.md | Project knowledge | Setup |
| Upload_to_Claude/Brainstorm_Template.docx | Project knowledge | Setup |
| Upload_to_Claude/World_Spec_Template.docx | Project knowledge | Setup |
| Attach_to_Chat_at_Template_Curation/Template_DataBank.docx | Chat attachment (NOT project files) | Template Curation only |

## How we run it (governed from here)

- Veteran path: open the session with the veteran activation phrase from `01_Custom_Instructions_PASTE_INTO_INSTRUCTIONS.txt` (it is in that file; we do not transcribe it into other repo docs). In that mode the Coach stops teaching, takes our inputs directly, assembles to the template, and audits. All its hard rules still hold.
- Substance is settled here. Let the Coach format to the template and run its audit. Accept format and audit fixes. Reject any new substance it tries to introduce.
- Workflow lanes: OUR locks govern. The Coach's own workflow endpoint is behind Larry's cut. If it pushes back on a lane (old tier, or it lacks Task 6's Specialist Referral lane), that is the stale endpoint; hold our locks (canonical 06/19 doc + Larry). See the reconciliation, section 1.
- Date policy: ignore the Coach's "everything before July 2025" line as Coach-stale (OV shipped on 2026 dates) unless Larry says otherwise.
- Reconcile back: paste the Coach's output into the repo, run the gates, log it in `docs/W3-WORKING-LOG.md`. Only then is it canonical.

## W3 launch sequence (Marva Lydell)

1. Open a new chat in the Project. Activate the veteran path. State the phase: World Spec.
2. Paste `worlds/marva-lydell/coach/W3-Coach-ChatRef.md` (the world essentials, the locked task table, the fairness rules, the file-plan note). That is the approved-brainstorm input plus our locks in one block.
3. Let the Coach assemble the spec into `World_Spec_Template.docx` and walk its pre-submission audit. Take format and audit fixes; keep our substance and lanes.
4. Pull the drafted spec back here, run our gates, log it. Author the Section 3 file plan here if the Coach leaves gaps (30+ world-level rows, origins, filenames per the four-origin rule).
5. Template Curation: open a NEW chat, say Template Curation, paste the Section 3 file plan, and attach `Template_DataBank.docx` to that chat. Walk the files: download each DataBank or custom template; note public-domain sources; for writer-produced rows (any rhythm strip or device printout), produce them HERE with our renderers and name them with the final datestamp.
6. Assemble the Reference Templates folder and upload it WITH the spec to RL Studio as separate files, not zipped. That upload is the handoff.

## Package contents (governing copy)

- `01_Custom_Instructions_PASTE_INTO_INSTRUCTIONS.txt` - the teaching engine + phase router (paste into Instructions).
- `Upload_to_Claude/` - the four curricula and the two output templates (project knowledge).
- `Attach_to_Chat_at_Template_Curation/Template_DataBank.docx` - the template DataBank (chat attachment at Template Curation).
- `Sanctum_Coach_Setup_and_Use.docx` - the Coach's own setup-and-use doc (reference).
- `COACH-SESSION-SETUP.md` - this runbook.
