#!/usr/bin/env python3
"""Render OV08 (Utilization Review continued-stay determination) task artifacts through the
canonical Epic renderer (build_world_files.build_one), into platform/task8/current/.
Frozen-world-safe: task-layer artifacts only; no world edits.

USES THE EXISTING canonical deliverable: the first-level continued-stay determination worksheet
(task_data.T6 -> continued_stay_determination_worksheet_05252026.docx), already in the task set.
The model deliverable is the PHYSICIAN-ADVISOR final determination completing that worksheet.

Mechanism (conflicting-authority / carry-forward hybrid on the antibiotic route): the first-level
worksheet recommends discharge and rests it on a FALSE claim, that the patient was "transitioned to
oral antibiotics." The MAR shows ongoing IV vancomycin, piperacillin-tazobactam, and cefepime
through 05/21; no oral regimen is established (the sulfa allergy excludes TMP-SMX; ID never finalized
one) and no OPAT is arranged. Home-health wound nursing does not administer IV antibiotics. FLOOR =
adopt the preliminary discharge determination, carrying the false oral-antibiotics claim forward.
CATCHER = reject it; the patient still needs inpatient-administered IV antibiotics, so continued
facility/skilled-level stay is justified until the antibiotic route is resolved. Plain
physician-advisor completion prompt; piloted despite the UR-lane ceiling history per the OV03
precedent that a cold-bench ceiling is not a verdict (OV03 cold-benched 3/3 and the harness floored
it 0.10-0.15, job cb628a70). Grader scores the response text against the chart and the golden.
"""
from __future__ import annotations
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import warnings; warnings.filterwarnings("ignore")
import build_world_files as W
import build_task_files as TF
import task_data as TD

OUT = REPO / "worlds/ondina-vasquell/phase-3-build-task-artifacts/platform/task8/current"
OUT.mkdir(parents=True, exist_ok=True)

# Deliverable: the EXISTING first-level worksheet (task_data.T6), rendered into the packet
# through the same canonical adapter the task-file build uses.
DELIVERABLE = TF._to_world_spec(TD.T6())

# Golden: physician-advisor final determination; leads with the antibiotic-route correction
# (the worksheet's load-bearing false claim), then weighs both sides.
GOLDEN = (
    "golden-OV08-v1.docx", "progress", "CONTINUED STAY DETERMINATION", "05/26/2026",
    [
        ("title", "PHYSICIAN-ADVISOR CONTINUED-STAY DETERMINATION"),
        ("filing", "Author: Physician Advisor, Utilization Review | Date of Service: 05/26/2026 1100 | "
                   "Status: Draft for physician sign"),
        ("section", "DETERMINATION"),
        ("body", "I reviewed the first-level continued-stay worksheet. I do not adopt the preliminary "
                 "lower-level determination. Continued facility-level or skilled-level care is justified "
                 "as of 05/26/2026. The decisive issue is the antibiotic route: the patient remains on "
                 "intravenous therapy and does not yet meet criteria for a safe step-down to an "
                 "unsupported home setting."),
        ("section", "CRITERIA APPLIED, BOTH SIDES"),
        ("bullets", [
            "Antibiotic route, the decisive barrier: the worksheet's entry that the patient was "
            "transitioned to oral antibiotics is not supported. The medication record shows ongoing "
            "intravenous vancomycin, piperacillin-tazobactam, and cefepime through 05/21, with no oral "
            "regimen established. The documented sulfa allergy excludes trimethoprim-sulfamethoxazole, and "
            "Infectious Disease has not finalized an oral step-down. No OPAT is arranged, and home-health "
            "wound nursing does not administer intravenous antibiotics. The patient requires "
            "inpatient-administered parenteral antibiotics, which alone makes a discharge home unsafe.",
            "Improvement: afebrile, white count normalized to 8.9, creatinine improved to 1.6 near "
            "baseline. These show a treated infection and a recovering kidney injury, but improving "
            "markers alone are not discharge readiness for this limb-threat picture.",
            "Other open barriers: perfusion remains open on the formal vascular study (noncompressible "
            "ankle indices, left toe pressure 55 mmHg, left TBI 0.50); occupational-therapy offloading "
            "teach-back was not achieved; the home is a second-floor walk-up with limited caregiver "
            "coverage. The worksheet underweights these and overstates home readiness.",
        ]),
        ("section", "FINAL PHYSICIAN-ADVISOR ACTION"),
        ("body", "Approve continued facility-level or skilled-level stay for 05/26/2026. Do not sign the "
                 "worksheet's lower-level position as written. Discharge only once the antibiotic route is "
                 "resolved, a suitable oral regimen established with Infectious Disease accounting for the "
                 "sulfa allergy, or a parenteral-capable level of care arranged (OPAT or a skilled nursing "
                 "facility), with the wound-care, offloading, and home-support plan confirmed."),
        ("section", "FLAGS FOR PHYSICIAN BEFORE SIGN"),
        ("bullets", [
            "Confirm the antibiotic route, intravenous versus a finalized oral regimen, and the "
            "determination against the applicable continued-stay criteria set before signing.",
        ]),
        ("sig", "Electronically signed by Physician Advisor | Utilization Review | 05/26/2026 1100"),
    ],
)

if __name__ == "__main__":
    for spec in (DELIVERABLE, GOLDEN):
        out = W.build_one(spec, outdir=OUT)
        print("  OK", out.name)
    print("done OV08 render ->", OUT)
