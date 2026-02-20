# Space Plan - physiology-cardiac-electrophysiology-combo-0067

## Scientific Scope
- Domain: physiology
- Theme: cardiac_electrophysiology
- Base models: physiology-cellml-shelleycardiacapmodel-b15-model, physiology-cellml-toward-a-comprehensive-cardiomyocyte-model-d59-model, physiology-cellml-varela-canine-atrial-cell-models-47c-model, physiology-cellml-voigt-heijman-et-al-2013-human-atrial-ap-model-633-model

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
