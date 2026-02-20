# Space Prompt - physiology-general-combo-0048

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-bg-funny-838-model, physiology-cellml-bg-giprotein-6f9-model, physiology-cellml-bg-gpcr-b1ar-reduced-7dc-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
