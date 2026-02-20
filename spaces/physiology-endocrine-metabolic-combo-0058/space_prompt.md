# Space Prompt - physiology-endocrine-metabolic-combo-0058

Create a scientifically coherent **physiology / endocrine_metabolic** comparative space using:
- Base models: physiology-sbml-fridlyand2010-glucosesensitivity-b-biomd0000000349-model, physiology-sbml-heinze1998-gnrh-lh-model0848507209-model, physiology-sbml-jiang2007-gsis-system-pancreatic-beta-cells-biomd0000000239-model, physiology-sbml-keener2001-oscillatoryinsulinsecretionmodel-model1201140001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
