# Space Prompt - physiology-general-combo-0036

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-cellml-bental-2006-366-model, physiology-cellml-bental-2006-bental2006-model, physiology-cellml-bernus-wilders-zemlin-verschelde-panfilov-2002-bernuswilderszemlinverscheldepanfilov2002-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
