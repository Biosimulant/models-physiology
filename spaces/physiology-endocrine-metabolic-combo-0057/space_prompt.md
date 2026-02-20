# Space Prompt - physiology-endocrine-metabolic-combo-0057

Create a scientifically coherent **physiology / endocrine_metabolic** comparative space using:
- Base models: physiology-sbml-chay1997-calciumconcentration-biomd0000000378-model, physiology-sbml-dallaman2007-mealmodel-glucoseinsulinsystem-biomd0000000379-model, physiology-sbml-edes1-0-eindhoven-diabetes-simulator-model2403070001-model, physiology-sbml-fridlyand2010-glucosesensitivity-a-biomd0000000348-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
