# Space Prompt - physiology-cardiac-electrophysiology-combo-0067

Create a scientifically coherent **physiology / cardiac_electrophysiology** comparative space using:
- Base models: physiology-cellml-shelleycardiacapmodel-b15-model, physiology-cellml-toward-a-comprehensive-cardiomyocyte-model-d59-model, physiology-cellml-varela-canine-atrial-cell-models-47c-model, physiology-cellml-voigt-heijman-et-al-2013-human-atrial-ap-model-633-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
