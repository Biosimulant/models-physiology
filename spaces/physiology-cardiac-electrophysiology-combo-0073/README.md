# COMBO_0073 - Physiology Cardiac Electrophysiology

## Scientific Question
How do cardiac electrophysiology mechanisms compare across these models?

## Biological Context
Organ or system-level physiological regulation under changing conditions.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `physiology-cellml-a-computational-human-ventricular-electrophysiol-5e1-model`: Physiology: AComputationalHumanVentricularElectrophysiol5e1Model
- `physiology-cellml-a-computational-human-ventricular-electrophysiol-5e2-model`: Physiology: AComputationalHumanVentricularElectrophysiol5e2Model
- `physiology-cellml-a-model-for-the-human-fetal-ventricular-myocyte-d90-model`: Physiology: AModelForTheHumanFetalVentricularMyocyteD90Model
- `physiology-cellml-aslanidi-atrial-model-2009-aslanidiatrialmodel2009-model`: Physiology: AslanidiAtrialModel2009Aslanidiatrialmodel2009Model

## Wiring Rationale
- Comparative (non-causal) mode: no direct causal links were created.

## Visualization Strategy
- Monitor-driven visualization is required for this space.
- State streams are routed into explicit monitor ports (`state_a..state_d`) to avoid signal overwrite.
- At minimum, monitor visuals include one timeseries panel and one summary table.
- Rationale: A dedicated monitor model receives all participating model state streams (`state_a..state_d`) so trajectories can be compared in one place without claiming causal coupling when IO semantics are incomplete.

## Expected Behaviors
- Model output trajectories under shared runtime settings.
- Cross-model agreement/divergence in key state or metric signals.
- Relative behavior comparison without causal linkage claims.

## Known Limitations
- No new biology is introduced beyond what upstream models encode.
- Cross-model semantic matching is rule-based and may under-connect uncertain routes.

## Source Provenance
- physiology-cellml-a-computational-human-ventricular-electrophysiol-5e1-model :: physiome:5e1 :: https://models.physiomeproject.org/workspace/5e1
- physiology-cellml-a-computational-human-ventricular-electrophysiol-5e2-model :: physiome:5e2 :: https://models.physiomeproject.org/workspace/5e2
- physiology-cellml-a-model-for-the-human-fetal-ventricular-myocyte-d90-model :: physiome:d90 :: https://models.physiomeproject.org/workspace/d90
- physiology-cellml-aslanidi-atrial-model-2009-aslanidiatrialmodel2009-model :: physiome:aslanidi_atrial_model_2009 :: https://models.physiomeproject.org/workspace/aslanidi_atrial_model_2009

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
