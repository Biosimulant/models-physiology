# Space Plan - physiology-general-combo-0023

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-cellml-aguda-b-1999-35e-model, physiology-cellml-aguda-b-1999-agudab1999-model

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
