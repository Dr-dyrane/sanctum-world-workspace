STATUS 2026-06-17 (v2): OV09 = off-text image floor on the Post-Acute Care Coordination lane (fresh 6th lane). OV04/OV07 family. v1 (contrast commission) RETIRED: ceilinged all-catch (job 21e12fc3), the frozen H&P says "avoid contrast" so the catch was a one-line lookup. v2 deliverable is a transfer handoff note finalized from the prose; the decisive osteomyelitis finding lives in a transfer-day foot radiograph the handoff does not force opening. Floor = transfer on the short soft-tissue antibiotic course, miss the osteo; catcher = surface it and escalate to a prolonged IV/OPAT course and a parenteral-capable setting.

## Workflow type
Post-Acute Care Coordination Documentation (P1 on the 06/10 snapshot). Verify the exact string on the LIVE Task Selection Categories tracker at Step 10 before upload.

## Studio task setup
- Prompt: prompt-OV09.txt (plain "finish it from her chart so it is ready for my signature").
- Task files to mount: started_post_acute_coordination_note_05242026.docx, foot_radiograph_05242026.jpg (Codex render; must match the locked osteomyelitis finding), plus the full OV world chart.
- Golden: golden-OV09-v1.docx. Grader: grader-guidelines-OV09.txt (model grader; does NOT read the image).
- First-trajectory find /docs gate: exactly one started note under filesystem, the radiograph mounted, no stale v1 contrast deliverable, no .apps_data duplicate.
- Run 10 trajectories.

## Build / render
- python3 worlds/ondina-vasquell/phase-3-build-task-artifacts/build/build_ov09.py renders the deliverable and golden into platform/task9/current/.
- The image is produced by Codex from osteo-image-spec.md; the finding (cortical destruction at the second metatarsal head, consistent with osteomyelitis, 05/24/2026) is locked to the golden. QA the legible impression strip before mounting.

## Pilot read
- Expect bimodal (OV04/OV07 parity): floors miss the radiograph, catchers escalate on the osteomyelitis. Target floor 0.10-0.40 with a catcher above 0.85.
- KNOWN RISK: a bone-infection handoff may prime an imaging re-check and force the image open (ceiling). If all-catch, one re-roll moving the finding to a more peripheral axis, then retire. If all-floor, confirm reachability before banking.
- Prereg: OV09-pilot-preregistration.md. Design + the v1 retirement and the C. diff drop: OV09-DESIGN-grounding.md.
