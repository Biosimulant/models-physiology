# Space Plan - physiology-endocrine-metabolic-combo-0061

## Scientific Scope
- Domain: physiology
- Theme: endocrine_metabolic
- Base models: physiology-sbml-o-donovan2022-the-mixed-meal-model-model2212300001-model, physiology-sbml-pancreas-glucose-model-model2401110001-model, physiology-sbml-rattanakul2003-boneformation-estrogenadministrat-model1012140001-model, physiology-sbml-rattanakul2003-boneformation-pthadministration-model1012140000-model

## Wiring Plan
- Comparative mode with monitor-only routing.
- Each base model state-like output connects to monitor ports `state_a..state_d`.
- No direct causal links among base models unless explicitly upgraded later.

## Visualization Plan
- Include `StateComparisonMonitor` and `StateMetricsMonitor`.
- Require at least:
  - one timeseries visual,
  - one summary table visual.

## Validation Gates
- space schema validity
- wiring endpoint validity
- smoke run success
- repo manifest/entrypoint validators pass
