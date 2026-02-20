# Space Prompt - physiology-general-combo-0065

Create a scientifically coherent **physiology / general** comparative space using:
- Base models: physiology-sbml-corrias2008-gastricslowwaveactivity-model0913095435-model, physiology-sbml-gaetano2008-diabetesprogressionmodel-model1112110003-model, physiology-sbml-nampala2013-liver-enzyme-elevation-in-hiv-mono-i-model1812040002-model, physiology-sbml-potter2006-androgenicregulation-model8684444027-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
