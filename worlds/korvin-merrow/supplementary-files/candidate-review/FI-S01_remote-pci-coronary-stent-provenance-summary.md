# FI-S01 - Remote PCI / Coronary Stent Provenance Summary

File ID: FI-S01

File Type: Remote PCI / coronary stent provenance summary

Level: Supplementary

Approximate Date / Anchor: Pre-admission provenance

Author / Source: Cardiology or PCP history source

Tool / Origin: Writer-created supplementary provenance file

Purpose: Support CAD/procedure background and chronic cardiovascular prevention without creating an acute procedure arc.

Supported Workflow(s) / Trap(s) / Friction(s): Hospital Discharge Summary Generation; Discharge Medication Reconciliation; Trap #2 indirect support

World Boundary: contains only remote pre-admission cardiovascular provenance. It contains no inpatient procedure, acute coronary event, final GDMT restart decision, final medication list, discharge medication reconciliation, task framing, expected output, golden response, grader guidance, AutoQC response, DOCX artifact, or submission material.

## Remote Cardiovascular Procedure Provenance

Patient: Korvin Merrow

Source type: historical cardiology / primary care provenance summary

Korvin has a remote history of percutaneous coronary intervention with coronary stent placement. The available chart provenance supports chronic CAD history and the reason chronic cardiovascular prevention appears throughout the record.

This supplementary file is background texture. It is not an active cardiology consultation, inpatient procedure note, discharge summary, or final medication decision.

## Background Context

The remote stent history helps explain why CAD prevention remains clinically relevant in the world.

Background implications:

- chronic CAD remains part of Korvin's baseline condition burden;
- aspirin and statin continuity appear in stronger medication and consultant sources;
- HFrEF/CAD medication discussions should be interpreted in the context of long-term cardiovascular risk;
- remote procedure history does not by itself determine acute medication restart timing.

The provenance does not describe new chest pain, new ischemia, new catheterization, or any inpatient coronary intervention during this hospitalization.

## Relationship To Current Hospitalization

This background may help a reviewer understand why Cardiology is attentive to chronic cardiovascular protection.

It does not resolve the Cardiology vs Nephrology disagreement.

The medication-restart problem still requires synthesis of:

- objective renal, potassium, hemodynamic, and intake trends;
- MAR and inpatient medication action evidence;
- nephrology recommendations;
- cardiology recommendations;
- hospitalist synthesis;
- discharge support and medication-management safety.

FI-S01 does not decide whether sacubitril/valsartan, carvedilol, diuretic therapy, spironolactone, empagliflozin, metformin, or other renal/hemodynamic-sensitive medications should be continued, restarted, held, or deferred.

## Supplementary Interpretation

This file may support Hospital Discharge Summary Generation by giving remote procedural context.

This file may support Discharge Medication Reconciliation only as background for chronic CAD/HFrEF prevention.

It is not a medication source and does not outrank:

1. attending documentation;
2. verified medication reconciliation;
3. pharmacy history;
4. consultant documentation;
5. primary care documentation;
6. family report;
7. patient recollection.

## Guardrails

FI-S01 must not become Trap #2 answer support.

It must not:

- resolve Cardiology vs Nephrology;
- decide GDMT restart timing;
- override FI-W12 objective trends;
- convert FI-W13 inpatient medication actions into a final plan;
- create a final medication list;
- create a discharge medication reconciliation;
- create an acute cardiac diagnosis or procedure.

No post-world information, discharge outcome, +7 follow-up information, +30 follow-up information, task prompt, expected output, golden response, grader guidance, AutoQC response, DOCX artifact, or submission material is present.
