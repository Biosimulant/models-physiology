# Space Plan - physiology-general-combo-0035

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-cellml-beeler-reuter-1977-beelerreuter1977-model, physiology-cellml-benson-2008-2e3-model, physiology-cellml-benson-2008-benson2008-model

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
