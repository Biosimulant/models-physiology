# Space Plan - physiology-endocrine-metabolic-combo-0055

## Scientific Scope
- Domain: physiology
- Theme: endocrine_metabolic
- Base models: physiology-cellml-guyton-antidiuretic-hormone-2008-guytonantidiuretichormone2008-model, physiology-cellml-modular-version-of-glucose-uptake-including-wate-58c-model, physiology-cellml-na-glucose-transporter-436-model

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
