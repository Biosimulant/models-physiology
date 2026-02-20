# Space Prompt - physiology-general-combo-0037

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-bertram-arnot-zamponi-2002-bertramarnotzamponi2002-model, physiology-cellml-bertram-et-al-2011-lymphangion-model-b44-model, physiology-cellml-bertram-pedersen-luciani-and-sherman-2006-bertrampedersenlucianisherman-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
