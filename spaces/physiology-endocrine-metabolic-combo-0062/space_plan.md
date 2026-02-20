# Space Plan - physiology-endocrine-metabolic-combo-0062

## Scientific Scope
- Domain: physiology
- Theme: endocrine_metabolic
- Base models: physiology-sbml-rattanakul2003-boneformationmodel-biomd0000000274-model, physiology-sbml-rozendaal2018-model-integrating-glucose-and-lipi-model1803200001-model, physiology-sbml-schlosser2000-glucoseinsulinfeedback-betacells-model1006230045-model, physiology-sbml-shrestha2010-hypercalcemia-pthresponse-biomd0000000277-model

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
