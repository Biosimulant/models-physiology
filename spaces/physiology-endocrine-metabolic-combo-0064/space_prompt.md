# Space Prompt - physiology-endocrine-metabolic-combo-0064

Create a scientifically coherent **physiology / endocrine_metabolic** comparative space using:
- Base models: physiology-sbml-sonntag2012-mtor-model-irs-dependent-regulation-biomd0000000580-model, physiology-sbml-sturis1991-insulinglucosemodel-ultradianoscillat-biomd0000000382-model, physiology-sbml-tolic2000-insulinglucosefeedback-biomd0000000372-model, physiology-sbml-topp200-model-of-b-cell-mass-insulin-and-glucose-model2001080002-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
