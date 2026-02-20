# COMBO_0057 - Physiology Endocrine Metabolic

## Scientific Question
How do endocrine metabolic mechanisms compare across these models?

## Biological Context
Organ or system-level physiological regulation under changing conditions.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `physiology-sbml-chay1997-calciumconcentration-biomd0000000378-model`: Physiology: Chay1997CalciumconcentrationBiomd0000000378Model
- `physiology-sbml-dallaman2007-mealmodel-glucoseinsulinsystem-biomd0000000379-model`: Physiology: Dallaman2007MealmodelGlucoseinsulinsystemBiomd0000000379Model
- `physiology-sbml-edes1-0-eindhoven-diabetes-simulator-model2403070001-model`: Physiology: Edes10EindhovenDiabetesSimulatorModel2403070001Model
- `physiology-sbml-fridlyand2010-glucosesensitivity-a-biomd0000000348-model`: Physiology: Fridlyand2010GlucosesensitivityABiomd0000000348Model

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
- physiology-sbml-chay1997-calciumconcentration-biomd0000000378-model :: biomodels_ebi:BIOMD0000000378 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000378
- physiology-sbml-dallaman2007-mealmodel-glucoseinsulinsystem-biomd0000000379-model :: biomodels_ebi:BIOMD0000000379 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000379
- physiology-sbml-edes1-0-eindhoven-diabetes-simulator-model2403070001-model :: biomodels_ebi:MODEL2403070001 :: https://www.ebi.ac.uk/biomodels/MODEL2403070001
- physiology-sbml-fridlyand2010-glucosesensitivity-a-biomd0000000348-model :: biomodels_ebi:BIOMD0000000348 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000348

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
