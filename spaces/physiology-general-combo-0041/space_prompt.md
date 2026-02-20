# Space Prompt - physiology-general-combo-0041

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-bg-abc-c2a-model, physiology-cellml-bg-ae-882-model, physiology-cellml-bg-ae1-weinstein-877-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
