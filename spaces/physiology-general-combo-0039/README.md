# COMBO_0039 - Physiology General

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
- `physiology-cellml-bertram-rhoads-and-cimbora-2008-bertramrhoadscimbora2008-model`: Physiology: BertramRhoadsAndCimbora2008Bertramrhoadscimbora2008Model
- `physiology-cellml-bertram-satin-pedersen-luciani-sherman-2007-570-model`: Physiology: BertramSatinPedersenLucianiSherman2007570Model
- `physiology-cellml-bertram-satin-pedersen-luciani-sherman-2007-bertramsatinpedersenlucianisherman2007-model`: Physiology: BertramSatinPedersenLucianiSherman2007Bertramsatinpedersenlucianisherman2007Model

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
- physiology-cellml-bertram-rhoads-and-cimbora-2008-bertramrhoadscimbora2008-model :: physiome:bertram_rhoads_cimbora_2008 :: https://models.physiomeproject.org/workspace/bertram_rhoads_cimbora_2008
- physiology-cellml-bertram-satin-pedersen-luciani-sherman-2007-570-model :: physiome:570 :: https://models.physiomeproject.org/workspace/570
- physiology-cellml-bertram-satin-pedersen-luciani-sherman-2007-bertramsatinpedersenlucianisherman2007-model :: physiome:bertram_satin_pedersen_luciani_sherman_2007 :: https://models.physiomeproject.org/workspace/bertram_satin_pedersen_luciani_sherman_2007

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
