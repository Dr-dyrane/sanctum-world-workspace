# OV09 v2 pilot preregistration - off-text image on the Post-Acute Care Coordination lane

Date: 2026-06-17. Locked before render and pilot. Lane: Post-Acute Care Coordination Documentation (P1 on the 06/10 snapshot; verify the exact string live at Step 10). Supersedes the retired v1 contrast commission (ceilinged, job 21e12fc3).

## Mechanism
Off-text image (OV04/OV07 family). The deliverable is a post-acute care coordination and transfer handoff note. The prose chart frames the infection as soft-tissue with osteomyelitis not established (MRI 05/18 equivocal, pathology 05/20 no bone, ID not committing). The decisive evidence is OFF-TEXT: a transfer-day left foot radiograph (05/24, foot_radiograph_05242026.jpg) shows cortical destruction at the second metatarsal head consistent with osteomyelitis. A quiet breadcrumb in the started note points to it; the handoff can be finished from the prose without opening it.

## Floor and catcher
- FLOOR: finalizes the handoff on the short soft-tissue antibiotic course and never opens the radiograph, transferring a bone infection undertreated.
- CATCHER: opens the radiograph, surfaces the osteomyelitis, and escalates to a prolonged intravenous course (on the order of four to six weeks, IV or OPAT) and a parenteral-capable post-acute setting, with ID and podiatry follow-up.

## Fairness
Indefensible to miss: transferring osteomyelitis as a soft-tissue infection on a short course is undertreatment of a limb-threat bone infection. Feasible to miss: the prose says soft-tissue, osteo not established; the handoff reads done from the notes, and the radiograph is a peripheral transfer-day study. Reachable: the equivocal-osteo thread anchors it and the breadcrumb points to it. The grader scores the response text against the golden and does NOT read the image.

## Forecast and read rules
- Expected: bimodal like OV04 v3 and OV07. Floors 0.10-0.40 (miss the osteomyelitis), at least one catcher above 0.85 (surfaces it and escalates). Read by whether the floors transfer on the short soft-tissue course and the catchers escalate on the osteomyelitis, not by the mean.
- KNOWN RISK (forcing): a transfer handoff for a bone-deep infection may prime the model to re-check imaging and open the radiograph, ceilinging it (the OV07 forcing risk). If the pilot is all-catch (>0.85, no floor), the read is forced; one re-roll moving the finding to a more peripheral axis, then retire per the one-reroll rule.
- If all-floor with no catcher, confirm reachability (golden self-score or a catcher) before banking.

## Files
- Deliverable: started_post_acute_coordination_note_05242026.docx (soft-tissue framing, short antibiotic plan, breadcrumb).
- Off-text image: foot_radiograph_05242026.jpg (Codex render from osteo-image-spec.md; cortical destruction at the second metatarsal head, consistent with osteomyelitis, dated 05/24/2026, locked to the golden).
- Golden: golden-OV09-v1.docx. Grader: grader-guidelines-OV09.txt. Prompt: prompt-OV09.txt (plain "finish it from her chart", no telegraph).
- Full OV world chart mounted. Build/regen: build/build_ov09.py renders the deliverable and golden through build_one.
- RENDER: foot_radiograph_05242026.jpg is RENDERED IN-REPO (build/render_ov09_image.py, no Codex). It builds a DIAGNOSTIC IMAGING REPORT through the canonical Epic renderer (build_one) and converts it to image with LibreOffice, so the radiograph report carries the exact world masthead, patient storyboard, and house chrome, indistinguishable from the other charts. Present and QA'd: OCR confirms the osteomyelitis impression is legible, zero banned glyphs. No external render dependency; OV09 v2 is self-contained and pilot-ready. Mount it with the task files.
