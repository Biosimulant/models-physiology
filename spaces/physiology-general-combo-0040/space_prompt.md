# Space Prompt - physiology-general-combo-0040

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-bertram-satin-zhang-smolen-sherman-2004-bertramsatinzhangsmolensherman2004-model, physiology-cellml-bertram-sherman-2004-bertramsherman2004-model, physiology-cellml-bertram-smolen-sherman-mears-atwater-martin-sori-bertramsmolenshermanmearsatwatermartinsoria1995-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
