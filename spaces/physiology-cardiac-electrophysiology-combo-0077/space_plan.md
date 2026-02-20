# Space Plan - physiology-cardiac-electrophysiology-combo-0077

## Scientific Scope
- Domain: physiology
- Theme: cardiac_electrophysiology
- Base models: physiology-cellml-atrial-fibroblast-model-4be-model, physiology-cellml-fcu-cardiac-ph-885-model, physiology-cellml-fcu-cardiacap-composite-839-model, physiology-cellml-fcu-cardiacap-pan-81b-model

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
