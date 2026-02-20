# COMBO_0067 - Physiology Cardiac Electrophysiology

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
- `physiology-cellml-shelleycardiacapmodel-b15-model`: Physiology: ShelleycardiacapmodelB15Model
- `physiology-cellml-toward-a-comprehensive-cardiomyocyte-model-d59-model`: Physiology: TowardAComprehensiveCardiomyocyteModelD59Model
- `physiology-cellml-varela-canine-atrial-cell-models-47c-model`: Physiology: VarelaCanineAtrialCellModels47cModel
- `physiology-cellml-voigt-heijman-et-al-2013-human-atrial-ap-model-633-model`: Physiology: VoigtHeijmanEtAl2013HumanAtrialApModel633Model

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
- physiology-cellml-shelleycardiacapmodel-b15-model :: physiome:b15 :: https://models.physiomeproject.org/workspace/b15
- physiology-cellml-toward-a-comprehensive-cardiomyocyte-model-d59-model :: physiome:d59 :: https://models.physiomeproject.org/workspace/d59
- physiology-cellml-varela-canine-atrial-cell-models-47c-model :: physiome:47c :: https://models.physiomeproject.org/workspace/47c
- physiology-cellml-voigt-heijman-et-al-2013-human-atrial-ap-model-633-model :: physiome:633 :: https://models.physiomeproject.org/workspace/633

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
