# EO-KM01 - Discharge Medication Reconciliation / Medication Safety Recommendation

Expected Output ID: EO-KM01

Mapped Prompt: TP-KM01

Mapped Workflow: Discharge Medication Reconciliation

Primary Task Context: FI-T01, with FI-T07 as medication-safety addendum support

Status: CANDIDATE REVIEW

Boundary: this is an expected-output draft. It is not a golden response, scoring key, grader guideline, grading document, AutoQC response, discharge prescription set, or final medication list.

## Expected Senior-Clinician Output

The discharge medication reconciliation should frame Korvin Merrow's medication plan as a risk-balanced reconciliation problem, not a copied medication list. The clinician should state that the final discharge medication actions require synthesis of the verified medication reconciliation, pharmacy/refill history, rheumatology prednisone provenance, inpatient medication actions, objective trends, consultant recommendations, functional medication-management evidence, and the visible but incomplete discharge-planning snapshot.

The recommendation should separate medication categories rather than treating the home regimen as a single restart bundle. Chronic CAD protection such as aspirin and atorvastatin can generally remain important unless a contraindication is present, while HFrEF and cardiorenal therapies require individualized timing. Sacubitril/valsartan, carvedilol, furosemide, spironolactone, empagliflozin, and metformin should be discussed in relation to renal recovery, potassium, blood pressure reserve, intake, volume status, and follow-up monitoring rather than reflexively resumed or permanently stopped. The output should recognize that early inpatient holds were reasonable during acute illness and AKI risk, but those holds should not persist by inertia once objective trends improve.

The response should preserve the Cardiology and Nephrology tension. Cardiology's concern is valid because Korvin has established HFrEF and CAD with chronic protective therapy and a remote PCI/stent history. Nephrology's concern is also valid because renal recovery is recent, potassium risk remains relevant, floor blood pressures do not fully prove home physiologic reserve, and intake/volume status remain part of the discharge context. A strong recommendation should propose sequencing, monitoring, and explicit rationale rather than selecting one consultant as the winner.

Prednisone should be handled as a source-reconstruction and safety issue. The output should recognize rheumatology documentation as the highest-authority outpatient taper source, while also integrating verified medication reconciliation, pharmacy/refill history, family report, and patient recollection. The expected recommendation should avoid abrupt discontinuation language when recent exposure and adherence remain uncertain, but it should not claim that adrenal insufficiency is proven or that steroid physiology explains the admission. It should call for a clear discharge steroid instruction aligned with rheumatology intent, inpatient status, and endocrine risk interpretation.

The diabetes plan should distinguish baseline outpatient therapy from inpatient-only actions. Metformin ER and empagliflozin require renal and acute-illness review. Insulin glargine is part of the baseline architecture but should be reconciled against intake, glucose pattern, and home capacity. Inpatient correctional insulin lispro should not be converted into a home medication without independent outpatient justification.

Medication-management safety should be explicitly addressed. OT and nursing describe improved but still vulnerable cognition, sequencing, fatigue, and medication-management ability. Family reported medication mistakes during the decline and asked who would review the final medication list with them. The expected output should therefore include family-present medication education, clear written changes, and accountable follow-up for renal function, potassium, blood pressure symptoms, glucose, steroid instructions, and HF/CAD medication sequencing.

FI-W22 may be used as an organizing source, but the output should say it is not a final medication reconciliation. The final recommendation should reconcile FI-W22 against MAR/action evidence, objective trends, consultant notes, rheumatology provenance, and functional medication-management sources.

## Reasoning Domains To Cover

- Home medication provenance and admission uncertainty from FI-W03, FI-W04, FI-W05, FI-W06, and FI-S04.
- Inpatient medication actions from FI-W13 without converting MAR actions into discharge orders.
- Objective renal, potassium, hemodynamic, glucose, and intake trends from FI-W12.
- Cardiology and Nephrology recommendations from FI-W14 and FI-W15.
- Endocrinology and rheumatology-source interpretation from FI-W06 and FI-W16.
- OT/nursing/family medication-management safety from FI-W17, FI-W19, and FI-W20.
- FI-W22 as visible discharge-planning context only.

## Prohibited Drift

The output should not create a fixed restart algorithm, outpatient insulin lispro addition, final discharge prescription set, hidden diagnosis reveal, consultant winner, or answer-file shortcut. It should not expose grading logic or internal implementation labels.
