# COMBO_0066 - Physiology Respiratory Physiology

## Scientific Question
How do respiratory physiology mechanisms compare across these models?

## Biological Context
Organ or system-level physiological regulation under changing conditions.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `physiology-cellml-guyton-pulmonary-fluid-dynamics-2008-guytonpulmonaryfluiddynamics2008-model`: Physiology: GuytonPulmonaryFluidDynamics2008Guytonpulmonaryfluiddynamics2008Model
- `physiology-cellml-guyton-pulmonary-oxygen-uptake-2008-guytonpulmonaryoxygenuptake2008-model`: Physiology: GuytonPulmonaryOxygenUptake2008Guytonpulmonaryoxygenuptake2008Model
- `physiology-cellml-pulmonary-acinus-pftu-d35-model`: Physiology: PulmonaryAcinusPftuD35Model
- `physiology-cellml-respiratory-system-3a4-model`: Physiology: RespiratorySystem3a4Model

## Wiring Rationale
- Comparative (non-causal) mode: no direct causal links were created.

## Visualization Strategy
- Monitor-driven visualization is required for this space.
- State streams are routed into explicit monitor ports (`state_a..state_d`) to avoid signal overwrite.
- At minimum, monitor visuals include one timeseries panel and one summary table.
- Rationale: A dedicated monitor model receives all participating model state streams (`state_a..state_d`) so trajectories can be compared in one place without claiming causal coupling when IO semantics are incomplete.

## Expected Behaviors
- Model output trajectories under shared runtime settings.
- Cross-model agreement/divergence in key state or metric signals.
- Relative behavior comparison without causal linkage claims.

## Known Limitations
- No new biology is introduced beyond what upstream models encode.
- Cross-model semantic matching is rule-based and may under-connect uncertain routes.

## Source Provenance
- physiology-cellml-guyton-pulmonary-fluid-dynamics-2008-guytonpulmonaryfluiddynamics2008-model :: physiome:guyton_pulmonary_fluid_dynamics_2008 :: https://models.physiomeproject.org/workspace/guyton_pulmonary_fluid_dynamics_2008
- physiology-cellml-guyton-pulmonary-oxygen-uptake-2008-guytonpulmonaryoxygenuptake2008-model :: physiome:guyton_pulmonary_oxygen_uptake_2008 :: https://models.physiomeproject.org/workspace/guyton_pulmonary_oxygen_uptake_2008
- physiology-cellml-pulmonary-acinus-pftu-d35-model :: physiome:d35 :: https://models.physiomeproject.org/workspace/d35
- physiology-cellml-respiratory-system-3a4-model :: physiome:3a4 :: https://models.physiomeproject.org/workspace/3a4

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
