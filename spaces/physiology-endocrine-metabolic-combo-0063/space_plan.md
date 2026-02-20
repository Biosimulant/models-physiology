# Space Plan - physiology-endocrine-metabolic-combo-0063

## Scientific Scope
- Domain: physiology
- Theme: endocrine_metabolic
- Base models: physiology-sbml-shrestha2010-hypocalcemia-pthresponse-biomd0000000276-model, physiology-sbml-silber2007-intravenousglucose-integratedglucosei-model1112110004-model, physiology-sbml-smith1980-hypothalamic-regulation-biomd0000000831-model, physiology-sbml-somogyi1990-caoscillations-biomd0000000114-model

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
