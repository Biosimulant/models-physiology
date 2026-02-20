# Space Plan - physiology-general-combo-0039

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-cellml-bertram-rhoads-and-cimbora-2008-bertramrhoadscimbora2008-model, physiology-cellml-bertram-satin-pedersen-luciani-sherman-2007-570-model, physiology-cellml-bertram-satin-pedersen-luciani-sherman-2007-bertramsatinpedersenlucianisherman2007-model

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
