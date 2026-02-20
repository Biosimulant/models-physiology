# Space Plan - physiology-respiratory-physiology-combo-0066

## Scientific Scope
- Domain: physiology
- Theme: respiratory_physiology
- Base models: physiology-cellml-guyton-pulmonary-fluid-dynamics-2008-guytonpulmonaryfluiddynamics2008-model, physiology-cellml-guyton-pulmonary-oxygen-uptake-2008-guytonpulmonaryoxygenuptake2008-model, physiology-cellml-pulmonary-acinus-pftu-d35-model, physiology-cellml-respiratory-system-3a4-model

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
