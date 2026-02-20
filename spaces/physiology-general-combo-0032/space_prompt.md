# Space Prompt - physiology-general-combo-0032

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-bagci-2008-363-model, physiology-cellml-bagci-2008-bagci2008-model, physiology-cellml-bakker-mensonides-teusink-vanhoek-michels-wester-bakkermensonidesteusinkvanhoekmichelswesterhoff2000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
