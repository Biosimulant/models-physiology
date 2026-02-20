# Space Prompt - physiology-respiratory-physiology-combo-0066

Create a scientifically coherent **physiology / respiratory_physiology** comparative space using:
- Base models: physiology-cellml-guyton-pulmonary-fluid-dynamics-2008-guytonpulmonaryfluiddynamics2008-model, physiology-cellml-guyton-pulmonary-oxygen-uptake-2008-guytonpulmonaryoxygenuptake2008-model, physiology-cellml-pulmonary-acinus-pftu-d35-model, physiology-cellml-respiratory-system-3a4-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
