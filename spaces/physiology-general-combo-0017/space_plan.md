# Space Plan - physiology-general-combo-0017

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-cellml-a-primer-on-modular-mass-action-modelling-with-c-modularmassactionprimer-model, physiology-cellml-a-simple-voltage-modulated-markov-chain-model-fo-d20-model

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
