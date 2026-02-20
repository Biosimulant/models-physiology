# Space Plan - physiology-general-combo-0037

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-cellml-bertram-arnot-zamponi-2002-bertramarnotzamponi2002-model, physiology-cellml-bertram-et-al-2011-lymphangion-model-b44-model, physiology-cellml-bertram-pedersen-luciani-and-sherman-2006-bertrampedersenlucianisherman-model

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
