# Space Plan - physiology-endocrine-metabolic-combo-0064

## Scientific Scope
- Domain: physiology
- Theme: endocrine_metabolic
- Base models: physiology-sbml-sonntag2012-mtor-model-irs-dependent-regulation-biomd0000000580-model, physiology-sbml-sturis1991-insulinglucosemodel-ultradianoscillat-biomd0000000382-model, physiology-sbml-tolic2000-insulinglucosefeedback-biomd0000000372-model, physiology-sbml-topp200-model-of-b-cell-mass-insulin-and-glucose-model2001080002-model

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
