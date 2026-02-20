# Space Plan - physiology-general-combo-0021

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-cellml-adjusted-coupled-model-exp5-kcl-cf9-model, physiology-cellml-adrian-chandler-hodgkin-1970-adrianchandlerhodgkin1970-model

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
