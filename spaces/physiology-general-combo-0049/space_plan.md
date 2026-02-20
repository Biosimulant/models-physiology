# Space Plan - physiology-general-combo-0049

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-cellml-bg-gpcr-m2-reduced-7dd-model, physiology-cellml-bg-gsprotein-6f8-model, physiology-cellml-bg-gsprotein-sneyd-6cb-model

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
