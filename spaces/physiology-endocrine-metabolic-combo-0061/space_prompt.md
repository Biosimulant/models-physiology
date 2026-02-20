# Space Prompt - physiology-endocrine-metabolic-combo-0061

Create a scientifically coherent **physiology / endocrine_metabolic** comparative space using:
- Base models: physiology-sbml-o-donovan2022-the-mixed-meal-model-model2212300001-model, physiology-sbml-pancreas-glucose-model-model2401110001-model, physiology-sbml-rattanakul2003-boneformation-estrogenadministrat-model1012140001-model, physiology-sbml-rattanakul2003-boneformation-pthadministration-model1012140000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
