# Space Prompt - physiology-cardiac-electrophysiology-combo-0001

Create a scientifically coherent **physiology / cardiac_electrophysiology** comparative space using:
- Base models: physiology-cellml-a-0d-model-of-the-heart-44c-model, physiology-cellml-a-computational-human-atrial-myofibroblast-elect-785-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
