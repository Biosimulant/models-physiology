# Space Prompt - physiology-endocrine-metabolic-combo-0063

Create a scientifically coherent **physiology / endocrine_metabolic** comparative space using:
- Base models: physiology-sbml-shrestha2010-hypocalcemia-pthresponse-biomd0000000276-model, physiology-sbml-silber2007-intravenousglucose-integratedglucosei-model1112110004-model, physiology-sbml-smith1980-hypothalamic-regulation-biomd0000000831-model, physiology-sbml-somogyi1990-caoscillations-biomd0000000114-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
