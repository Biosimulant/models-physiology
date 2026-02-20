# Space Plan - physiology-endocrine-metabolic-combo-0057

## Scientific Scope
- Domain: physiology
- Theme: endocrine_metabolic
- Base models: physiology-sbml-chay1997-calciumconcentration-biomd0000000378-model, physiology-sbml-dallaman2007-mealmodel-glucoseinsulinsystem-biomd0000000379-model, physiology-sbml-edes1-0-eindhoven-diabetes-simulator-model2403070001-model, physiology-sbml-fridlyand2010-glucosesensitivity-a-biomd0000000348-model

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
