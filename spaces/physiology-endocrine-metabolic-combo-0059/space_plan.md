# Space Plan - physiology-endocrine-metabolic-combo-0059

## Scientific Scope
- Domain: physiology
- Theme: endocrine_metabolic
- Base models: physiology-sbml-kiselyov2009-insulinreceptormodel-model1112050000-model, physiology-sbml-komarova2005-pthaction-osteoclastosteoblastcoupl-biomd0000000279-model, physiology-sbml-kroll2000-pth-boneformationdesorption-model1006230083-model, physiology-sbml-lenbury2001-insulinkineticsmodel-a-biomd0000000878-model

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
