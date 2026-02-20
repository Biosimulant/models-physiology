# Space Plan - physiology-general-combo-0050

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-cellml-bg-haimurphy-818-model, physiology-cellml-bg-inhib1-6d6-model, physiology-cellml-bg-ipr-8ab-model

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
