# Space Prompt - physiology-endocrine-metabolic-combo-0056

Create a scientifically coherent **physiology / endocrine_metabolic** comparative space using:
- Base models: physiology-sbml-alvehag2006-ivgtt-glucosemodel-a-model1112110000-model, physiology-sbml-alvehag2006-ogtt-glucosemodel-b-model1112110001-model, physiology-sbml-berzins2022-crypthecodinium-cohnii-ethanol-uptak-model2112290001-model, physiology-sbml-berzins2022-crypthecodinium-cohnii-glucose-and-g-model2112280001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
