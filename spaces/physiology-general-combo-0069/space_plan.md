# Space Plan - physiology-general-combo-0069

## Scientific Scope
- Domain: physiology
- Theme: general
- Base models: physiology-sbml-gaetano2008-diabetesprogressionmodel-model1112110003-model, physiology-sbml-nampala2013-liver-enzyme-elevation-in-hiv-mono-i-model1812040002-model, physiology-sbml-potter2006-androgenicregulation-model8684444027-model, physiology-sbml-weinstein2000-omcd-model1006230037-model

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
