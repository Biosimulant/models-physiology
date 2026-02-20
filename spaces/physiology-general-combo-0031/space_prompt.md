# Space Prompt - physiology-general-combo-0031

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-asthagiri-lauffenburger-2001-asthagirilauffenburger2001-model, physiology-cellml-bacillus-chassis-svp00000031-model, physiology-cellml-bagci-2006-bagci2006-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
