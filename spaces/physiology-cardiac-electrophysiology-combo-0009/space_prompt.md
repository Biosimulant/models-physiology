# Space Prompt - physiology-cardiac-electrophysiology-combo-0009

Create a scientifically coherent **physiology / cardiac_electrophysiology** comparative space using:
- Base models: physiology-cellml-heart-failure-model-with-sk-channels-included-d7b-model, physiology-cellml-human-atrial-cell-models-for-investigating-tbx5-520-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
