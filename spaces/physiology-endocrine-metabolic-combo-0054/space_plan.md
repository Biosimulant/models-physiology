# Space Plan - physiology-endocrine-metabolic-combo-0054

## Scientific Scope
- Domain: physiology
- Theme: endocrine_metabolic
- Base models: physiology-cellml-computational-modelling-of-glucose-uptake-by-sgl-841-model, physiology-cellml-glucose-transport-model-thorsen-5b8-model, physiology-cellml-glucose-uptake-in-enterocyte-572-model

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
