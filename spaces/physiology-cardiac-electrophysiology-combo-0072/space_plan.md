# Space Plan - physiology-cardiac-electrophysiology-combo-0072

## Scientific Scope
- Domain: physiology
- Theme: cardiac_electrophysiology
- Base models: physiology-cellml-a-computational-human-cardiac-purkinje-electroph-5d7-model, physiology-cellml-a-computational-human-ventricular-electrophysiol-5e1-model, physiology-cellml-a-computational-human-ventricular-electrophysiol-5e2-model, physiology-cellml-a-model-for-the-human-fetal-ventricular-myocyte-d90-model

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
