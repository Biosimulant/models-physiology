# Space Prompt - physiology-endocrine-metabolic-combo-0062

Create a scientifically coherent **physiology / endocrine_metabolic** comparative space using:
- Base models: physiology-sbml-rattanakul2003-boneformationmodel-biomd0000000274-model, physiology-sbml-rozendaal2018-model-integrating-glucose-and-lipi-model1803200001-model, physiology-sbml-schlosser2000-glucoseinsulinfeedback-betacells-model1006230045-model, physiology-sbml-shrestha2010-hypercalcemia-pthresponse-biomd0000000277-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
