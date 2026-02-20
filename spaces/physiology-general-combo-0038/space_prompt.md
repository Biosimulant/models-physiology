# Space Prompt - physiology-general-combo-0038

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-bertram-previte-sherman-kinard-satin-2000-2e0-model, physiology-cellml-bertram-previte-sherman-kinard-satin-2000-bertrampreviteshermankinardsatin2000-model, physiology-cellml-bertram-rhoads-and-cimbora-2008-2e7-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
