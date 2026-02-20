# COMBO_0062 - Physiology Endocrine Metabolic

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
- `physiology-sbml-rattanakul2003-boneformationmodel-biomd0000000274-model`: Physiology: Rattanakul2003BoneformationmodelBiomd0000000274Model
- `physiology-sbml-rozendaal2018-model-integrating-glucose-and-lipi-model1803200001-model`: Physiology: Rozendaal2018ModelIntegratingGlucoseAndLipiModel1803200001Model
- `physiology-sbml-schlosser2000-glucoseinsulinfeedback-betacells-model1006230045-model`: Physiology: Schlosser2000GlucoseinsulinfeedbackBetacellsModel1006230045Model
- `physiology-sbml-shrestha2010-hypercalcemia-pthresponse-biomd0000000277-model`: Physiology: Shrestha2010HypercalcemiaPthresponseBiomd0000000277Model

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
- physiology-sbml-rattanakul2003-boneformationmodel-biomd0000000274-model :: biomodels_ebi:BIOMD0000000274 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000274
- physiology-sbml-rozendaal2018-model-integrating-glucose-and-lipi-model1803200001-model :: biomodels_ebi:MODEL1803200001 :: https://www.ebi.ac.uk/biomodels/MODEL1803200001
- physiology-sbml-schlosser2000-glucoseinsulinfeedback-betacells-model1006230045-model :: biomodels_ebi:MODEL1006230045 :: https://www.ebi.ac.uk/biomodels/MODEL1006230045
- physiology-sbml-shrestha2010-hypercalcemia-pthresponse-biomd0000000277-model :: biomodels_ebi:BIOMD0000000277 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000277

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
