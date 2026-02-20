# Space Prompt - physiology-general-combo-0024

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-aguda-tang-1999-agudatang1999-model, physiology-cellml-albert-haanstra-hannaert-van-roy-opperdoes-bakke-alberthaanstrahannaertvanroyopperdoesbakkermichels2005-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
