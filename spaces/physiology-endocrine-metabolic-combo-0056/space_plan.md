# Space Plan - physiology-endocrine-metabolic-combo-0056

## Scientific Scope
- Domain: physiology
- Theme: endocrine_metabolic
- Base models: physiology-sbml-alvehag2006-ivgtt-glucosemodel-a-model1112110000-model, physiology-sbml-alvehag2006-ogtt-glucosemodel-b-model1112110001-model, physiology-sbml-berzins2022-crypthecodinium-cohnii-ethanol-uptak-model2112290001-model, physiology-sbml-berzins2022-crypthecodinium-cohnii-glucose-and-g-model2112280001-model

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
