# Space Plan - physiology-general-combo-0036

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-cellml-bental-2006-366-model, physiology-cellml-bental-2006-bental2006-model, physiology-cellml-bernus-wilders-zemlin-verschelde-panfilov-2002-bernuswilderszemlinverscheldepanfilov2002-model

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
