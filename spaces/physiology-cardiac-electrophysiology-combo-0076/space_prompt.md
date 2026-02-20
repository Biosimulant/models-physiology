# Space Prompt - physiology-cardiac-electrophysiology-combo-0076

Create a scientifically coherent **physiology / cardiac_electrophysiology** comparative space using:
- Base models: physiology-cellml-aslanidi-atrial-model-2009-aslanidiatrialmodel2009-model, physiology-cellml-atrial-fibroblast-model-4be-model, physiology-cellml-fcu-cardiac-ph-885-model, physiology-cellml-fcu-cardiacap-composite-839-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
