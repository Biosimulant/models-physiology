# Space Prompt - physiology-endocrine-metabolic-combo-0059

Create a scientifically coherent **physiology / endocrine_metabolic** comparative space using:
- Base models: physiology-sbml-kiselyov2009-insulinreceptormodel-model1112050000-model, physiology-sbml-komarova2005-pthaction-osteoclastosteoblastcoupl-biomd0000000279-model, physiology-sbml-kroll2000-pth-boneformationdesorption-model1006230083-model, physiology-sbml-lenbury2001-insulinkineticsmodel-a-biomd0000000878-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
