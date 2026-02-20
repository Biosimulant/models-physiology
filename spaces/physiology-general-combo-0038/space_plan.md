# Space Plan - physiology-general-combo-0038

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-cellml-bertram-previte-sherman-kinard-satin-2000-2e0-model, physiology-cellml-bertram-previte-sherman-kinard-satin-2000-bertrampreviteshermankinardsatin2000-model, physiology-cellml-bertram-rhoads-and-cimbora-2008-2e7-model

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
