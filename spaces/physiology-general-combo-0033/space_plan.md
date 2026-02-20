# Space Plan - physiology-general-combo-0033

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-cellml-bakker-michels-opperdoes-westerhoff-1997-bakkermichelsopperdoeswesterhoff1997-model, physiology-cellml-barberis-klipp-vanoni-alberghina-2007-364-model, physiology-cellml-barberis-klipp-vanoni-alberghina-2007-barberisklippvanonialberghina2007-model

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
