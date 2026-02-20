# Space Prompt - physiology-general-combo-0050

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-bg-haimurphy-818-model, physiology-cellml-bg-inhib1-6d6-model, physiology-cellml-bg-ipr-8ab-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
