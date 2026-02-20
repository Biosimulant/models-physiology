# COMBO_0064 - Physiology Endocrine Metabolic

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
- `physiology-sbml-sonntag2012-mtor-model-irs-dependent-regulation-biomd0000000580-model`: Physiology: Sonntag2012MtorModelIrsDependentRegulationBiomd0000000580Model
- `physiology-sbml-sturis1991-insulinglucosemodel-ultradianoscillat-biomd0000000382-model`: Physiology: Sturis1991InsulinglucosemodelUltradianoscillatBiomd0000000382Model
- `physiology-sbml-tolic2000-insulinglucosefeedback-biomd0000000372-model`: Physiology: Tolic2000InsulinglucosefeedbackBiomd0000000372Model
- `physiology-sbml-topp200-model-of-b-cell-mass-insulin-and-glucose-model2001080002-model`: Physiology: Topp200ModelOfBCellMassInsulinAndGlucoseModel2001080002Model

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
- physiology-sbml-sonntag2012-mtor-model-irs-dependent-regulation-biomd0000000580-model :: biomodels_ebi:BIOMD0000000580 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000580
- physiology-sbml-sturis1991-insulinglucosemodel-ultradianoscillat-biomd0000000382-model :: biomodels_ebi:BIOMD0000000382 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000382
- physiology-sbml-tolic2000-insulinglucosefeedback-biomd0000000372-model :: biomodels_ebi:BIOMD0000000372 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000372
- physiology-sbml-topp200-model-of-b-cell-mass-insulin-and-glucose-model2001080002-model :: biomodels_ebi:MODEL2001080002 :: https://www.ebi.ac.uk/biomodels/MODEL2001080002

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
