# Space Prompt - physiology-general-combo-0033

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-bakker-michels-opperdoes-westerhoff-1997-bakkermichelsopperdoeswesterhoff1997-model, physiology-cellml-barberis-klipp-vanoni-alberghina-2007-364-model, physiology-cellml-barberis-klipp-vanoni-alberghina-2007-barberisklippvanonialberghina2007-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
