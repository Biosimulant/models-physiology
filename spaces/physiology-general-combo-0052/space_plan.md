# Space Plan - physiology-general-combo-0052

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-cellml-bg-k1-uterine-d57-model, physiology-cellml-bg-kach-bbf-model, physiology-cellml-bg-kp-825-model

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
