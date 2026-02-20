# COMBO_0065 - Physiology General

## Scientific Question
How do general mechanisms compare across these models?

## Biological Context
Organ or system-level physiological regulation under changing conditions.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `physiology-sbml-corrias2008-gastricslowwaveactivity-model0913095435-model`: Physiology: Corrias2008GastricslowwaveactivityModel0913095435Model
- `physiology-sbml-gaetano2008-diabetesprogressionmodel-model1112110003-model`: Physiology: Gaetano2008DiabetesprogressionmodelModel1112110003Model
- `physiology-sbml-nampala2013-liver-enzyme-elevation-in-hiv-mono-i-model1812040002-model`: Physiology: Nampala2013LiverEnzymeElevationInHivMonoIModel1812040002Model
- `physiology-sbml-potter2006-androgenicregulation-model8684444027-model`: Physiology: Potter2006AndrogenicregulationModel8684444027Model

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
- physiology-sbml-corrias2008-gastricslowwaveactivity-model0913095435-model :: biomodels_ebi:MODEL0913095435 :: https://www.ebi.ac.uk/biomodels/MODEL0913095435
- physiology-sbml-gaetano2008-diabetesprogressionmodel-model1112110003-model :: biomodels_ebi:MODEL1112110003 :: https://www.ebi.ac.uk/biomodels/MODEL1112110003
- physiology-sbml-nampala2013-liver-enzyme-elevation-in-hiv-mono-i-model1812040002-model :: biomodels_ebi:MODEL1812040002 :: https://www.ebi.ac.uk/biomodels/MODEL1812040002
- physiology-sbml-potter2006-androgenicregulation-model8684444027-model :: biomodels_ebi:MODEL8684444027 :: https://www.ebi.ac.uk/biomodels/MODEL8684444027

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
