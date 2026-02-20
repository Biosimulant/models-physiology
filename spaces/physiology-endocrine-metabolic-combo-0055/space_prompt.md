# Space Prompt - physiology-endocrine-metabolic-combo-0055

Create a scientifically coherent **physiology / endocrine_metabolic** comparative space using:
- Base models: physiology-cellml-guyton-antidiuretic-hormone-2008-guytonantidiuretichormone2008-model, physiology-cellml-modular-version-of-glucose-uptake-including-wate-58c-model, physiology-cellml-na-glucose-transporter-436-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
