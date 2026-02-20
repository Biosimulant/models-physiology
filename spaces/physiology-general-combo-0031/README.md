# COMBO_0031 - Physiology General

## Scientific Question
How do general mechanisms compare across these models?

## Biological Context
Organ or system-level physiological regulation under changing conditions.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `physiology-cellml-asthagiri-lauffenburger-2001-asthagirilauffenburger2001-model`: Physiology: AsthagiriLauffenburger2001Asthagirilauffenburger2001Model
- `physiology-cellml-bacillus-chassis-svp00000031-model`: Physiology: BacillusChassisSvp00000031Model
- `physiology-cellml-bagci-2006-bagci2006-model`: Physiology: Bagci2006Bagci2006Model

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
- physiology-cellml-asthagiri-lauffenburger-2001-asthagirilauffenburger2001-model :: physiome:asthagiri_lauffenburger_2001 :: https://models.physiomeproject.org/workspace/asthagiri_lauffenburger_2001
- physiology-cellml-bacillus-chassis-svp00000031-model :: physiome:SVP_00000031 :: https://models.physiomeproject.org/workspace/SVP_00000031
- physiology-cellml-bagci-2006-bagci2006-model :: physiome:bagci_2006 :: https://models.physiomeproject.org/workspace/bagci_2006

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
