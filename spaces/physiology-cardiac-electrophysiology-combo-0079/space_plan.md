# Space Plan - physiology-cardiac-electrophysiology-combo-0079

## Scientific Scope
- Domain: physiology
- Theme: cardiac_electrophysiology
- Base models: physiology-cellml-fcu-cardiacap-composite-839-model, physiology-cellml-fcu-cardiacap-pan-81b-model, physiology-cellml-ftu-heart-70b-model, physiology-cellml-grandi-et-al-2011-atrial-action-potential-and-ca-595-model

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
