# Space Plan - physiology-general-combo-0040

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-cellml-bertram-satin-zhang-smolen-sherman-2004-bertramsatinzhangsmolensherman2004-model, physiology-cellml-bertram-sherman-2004-bertramsherman2004-model, physiology-cellml-bertram-smolen-sherman-mears-atwater-martin-sori-bertramsmolenshermanmearsatwatermartinsoria1995-model

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
