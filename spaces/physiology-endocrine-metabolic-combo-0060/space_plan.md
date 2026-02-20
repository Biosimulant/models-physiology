# Space Plan - physiology-endocrine-metabolic-combo-0060

## Scientific Scope
- Domain: physiology
- Theme: endocrine_metabolic
- Base models: physiology-sbml-lenbury2001-insulinkineticsmodel-b-model1201140003-model, physiology-sbml-liu2009-glucosemobilization-uptakemodel-model1112050001-model, physiology-sbml-mackenzie1996-naglucosecotransporter-kidney-model1006230076-model, physiology-sbml-nad-labelling-dynamics-model2409150001-model

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
