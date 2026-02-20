# Space Prompt - physiology-general-combo-0034

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-bartolucci-passini-severi-2020-5fd-model, physiology-cellml-baylor-hollingworth-chandler-2002-baylorhollingworthchandler2002-model, physiology-cellml-beard-2005-beard2005-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
