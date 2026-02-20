# Space Prompt - physiology-general-combo-0039

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-bertram-rhoads-and-cimbora-2008-bertramrhoadscimbora2008-model, physiology-cellml-bertram-satin-pedersen-luciani-sherman-2007-570-model, physiology-cellml-bertram-satin-pedersen-luciani-sherman-2007-bertramsatinpedersenlucianisherman2007-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
