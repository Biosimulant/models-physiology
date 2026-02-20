# Space Prompt - physiology-cardiac-electrophysiology-combo-0010

Create a scientifically coherent **physiology / cardiac_electrophysiology** comparative space using:
- Base models: physiology-cellml-koivum-ki-korhonen-tavi-2011-atrial-ap-model-630-model, physiology-cellml-michaelpancardiacapmodel-b16-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
