# COMBO_0058 - Physiology Endocrine Metabolic

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
- `physiology-sbml-fridlyand2010-glucosesensitivity-b-biomd0000000349-model`: Physiology: Fridlyand2010GlucosesensitivityBBiomd0000000349Model
- `physiology-sbml-heinze1998-gnrh-lh-model0848507209-model`: Physiology: Heinze1998GnrhLhModel0848507209Model
- `physiology-sbml-jiang2007-gsis-system-pancreatic-beta-cells-biomd0000000239-model`: Physiology: Jiang2007GsisSystemPancreaticBetaCellsBiomd0000000239Model
- `physiology-sbml-keener2001-oscillatoryinsulinsecretionmodel-model1201140001-model`: Physiology: Keener2001OscillatoryinsulinsecretionmodelModel1201140001Model

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
- physiology-sbml-fridlyand2010-glucosesensitivity-b-biomd0000000349-model :: biomodels_ebi:BIOMD0000000349 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000349
- physiology-sbml-heinze1998-gnrh-lh-model0848507209-model :: biomodels_ebi:MODEL0848507209 :: https://www.ebi.ac.uk/biomodels/MODEL0848507209
- physiology-sbml-jiang2007-gsis-system-pancreatic-beta-cells-biomd0000000239-model :: biomodels_ebi:BIOMD0000000239 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000239
- physiology-sbml-keener2001-oscillatoryinsulinsecretionmodel-model1201140001-model :: biomodels_ebi:MODEL1201140001 :: https://www.ebi.ac.uk/biomodels/MODEL1201140001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
