# Space Prompt - physiology-general-combo-0035

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-beeler-reuter-1977-beelerreuter1977-model, physiology-cellml-benson-2008-2e3-model, physiology-cellml-benson-2008-benson2008-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
