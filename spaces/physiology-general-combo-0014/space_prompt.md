# Space Prompt - physiology-general-combo-0014

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-a-model-for-pacemaking-in-substantia-nigra-neuro-3e0-model, physiology-cellml-a-model-of-intracellular-ph-control-4a3-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
