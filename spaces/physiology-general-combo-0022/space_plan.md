# Space Plan - physiology-general-combo-0022

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-cellml-ae1-bg-6b9-model, physiology-cellml-ae3-the-physics-of-physiology-c78-model

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
