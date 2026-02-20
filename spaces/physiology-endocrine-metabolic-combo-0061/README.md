# COMBO_0061 - Physiology Endocrine Metabolic

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
- `physiology-sbml-o-donovan2022-the-mixed-meal-model-model2212300001-model`: Physiology: ODonovan2022TheMixedMealModelModel2212300001Model
- `physiology-sbml-pancreas-glucose-model-model2401110001-model`: Physiology: PancreasGlucoseModelModel2401110001Model
- `physiology-sbml-rattanakul2003-boneformation-estrogenadministrat-model1012140001-model`: Physiology: Rattanakul2003BoneformationEstrogenadministratModel1012140001Model
- `physiology-sbml-rattanakul2003-boneformation-pthadministration-model1012140000-model`: Physiology: Rattanakul2003BoneformationPthadministrationModel1012140000Model

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
- physiology-sbml-o-donovan2022-the-mixed-meal-model-model2212300001-model :: biomodels_ebi:MODEL2212300001 :: https://www.ebi.ac.uk/biomodels/MODEL2212300001
- physiology-sbml-pancreas-glucose-model-model2401110001-model :: biomodels_ebi:MODEL2401110001 :: https://www.ebi.ac.uk/biomodels/MODEL2401110001
- physiology-sbml-rattanakul2003-boneformation-estrogenadministrat-model1012140001-model :: biomodels_ebi:MODEL1012140001 :: https://www.ebi.ac.uk/biomodels/MODEL1012140001
- physiology-sbml-rattanakul2003-boneformation-pthadministration-model1012140000-model :: biomodels_ebi:MODEL1012140000 :: https://www.ebi.ac.uk/biomodels/MODEL1012140000

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
