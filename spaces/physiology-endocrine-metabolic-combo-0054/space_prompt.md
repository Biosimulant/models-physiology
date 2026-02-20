# Space Prompt - physiology-endocrine-metabolic-combo-0054

Create a scientifically coherent **physiology / endocrine_metabolic** comparative space using:
- Base models: physiology-cellml-computational-modelling-of-glucose-uptake-by-sgl-841-model, physiology-cellml-glucose-transport-model-thorsen-5b8-model, physiology-cellml-glucose-uptake-in-enterocyte-572-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
