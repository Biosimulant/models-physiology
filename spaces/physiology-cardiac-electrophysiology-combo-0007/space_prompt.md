# Space Prompt - physiology-cardiac-electrophysiology-combo-0007

Create a scientifically coherent **physiology / cardiac_electrophysiology** comparative space using:
- Base models: physiology-cellml-grandi-et-al-2011-atrial-action-potential-and-ca-595-model, physiology-cellml-guyton-atrial-natriuretic-peptide-2008-guytonatrialnatriureticpeptide2008-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
