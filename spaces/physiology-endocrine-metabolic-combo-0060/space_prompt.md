# Space Prompt - physiology-endocrine-metabolic-combo-0060

Create a scientifically coherent **physiology / endocrine_metabolic** comparative space using:
- Base models: physiology-sbml-lenbury2001-insulinkineticsmodel-b-model1201140003-model, physiology-sbml-liu2009-glucosemobilization-uptakemodel-model1112050001-model, physiology-sbml-mackenzie1996-naglucosecotransporter-kidney-model1006230076-model, physiology-sbml-nad-labelling-dynamics-model2409150001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
