# COMBO_0063 - Physiology Endocrine Metabolic

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
- `physiology-sbml-shrestha2010-hypocalcemia-pthresponse-biomd0000000276-model`: Physiology: Shrestha2010HypocalcemiaPthresponseBiomd0000000276Model
- `physiology-sbml-silber2007-intravenousglucose-integratedglucosei-model1112110004-model`: Physiology: Silber2007IntravenousglucoseIntegratedglucoseiModel1112110004Model
- `physiology-sbml-smith1980-hypothalamic-regulation-biomd0000000831-model`: Physiology: Smith1980HypothalamicRegulationBiomd0000000831Model
- `physiology-sbml-somogyi1990-caoscillations-biomd0000000114-model`: Physiology: Somogyi1990CaoscillationsBiomd0000000114Model

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
- physiology-sbml-shrestha2010-hypocalcemia-pthresponse-biomd0000000276-model :: biomodels_ebi:BIOMD0000000276 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000276
- physiology-sbml-silber2007-intravenousglucose-integratedglucosei-model1112110004-model :: biomodels_ebi:MODEL1112110004 :: https://www.ebi.ac.uk/biomodels/MODEL1112110004
- physiology-sbml-smith1980-hypothalamic-regulation-biomd0000000831-model :: biomodels_ebi:BIOMD0000000831 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000831
- physiology-sbml-somogyi1990-caoscillations-biomd0000000114-model :: biomodels_ebi:BIOMD0000000114 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000114

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
