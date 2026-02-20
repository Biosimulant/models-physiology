# COMBO_0079 - Physiology Cardiac Electrophysiology

## Scientific Question
How do cardiac electrophysiology mechanisms compare across these models?

## Biological Context
Organ or system-level physiological regulation under changing conditions.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `physiology-cellml-fcu-cardiacap-composite-839-model`: Physiology: FcuCardiacapComposite839Model
- `physiology-cellml-fcu-cardiacap-pan-81b-model`: Physiology: FcuCardiacapPan81bModel
- `physiology-cellml-ftu-heart-70b-model`: Physiology: FtuHeart70bModel
- `physiology-cellml-grandi-et-al-2011-atrial-action-potential-and-ca-595-model`: Physiology: GrandiEtAl2011AtrialActionPotentialAndCa595Model

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
- physiology-cellml-fcu-cardiacap-composite-839-model :: physiome:839 :: https://models.physiomeproject.org/workspace/839
- physiology-cellml-fcu-cardiacap-pan-81b-model :: physiome:81b :: https://models.physiomeproject.org/workspace/81b
- physiology-cellml-ftu-heart-70b-model :: physiome:70b :: https://models.physiomeproject.org/workspace/70b
- physiology-cellml-grandi-et-al-2011-atrial-action-potential-and-ca-595-model :: physiome:595 :: https://models.physiomeproject.org/workspace/595

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
