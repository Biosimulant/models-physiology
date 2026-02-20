# COMBO_0060 - Physiology Endocrine Metabolic

## Scientific Question
How do endocrine metabolic mechanisms compare across these models?

## Biological Context
Organ or system-level physiological regulation under changing conditions.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `physiology-sbml-lenbury2001-insulinkineticsmodel-b-model1201140003-model`: Physiology: Lenbury2001InsulinkineticsmodelBModel1201140003Model
- `physiology-sbml-liu2009-glucosemobilization-uptakemodel-model1112050001-model`: Physiology: Liu2009GlucosemobilizationUptakemodelModel1112050001Model
- `physiology-sbml-mackenzie1996-naglucosecotransporter-kidney-model1006230076-model`: Physiology: Mackenzie1996NaglucosecotransporterKidneyModel1006230076Model
- `physiology-sbml-nad-labelling-dynamics-model2409150001-model`: Physiology: NadLabellingDynamicsModel2409150001Model

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
- physiology-sbml-lenbury2001-insulinkineticsmodel-b-model1201140003-model :: biomodels_ebi:MODEL1201140003 :: https://www.ebi.ac.uk/biomodels/MODEL1201140003
- physiology-sbml-liu2009-glucosemobilization-uptakemodel-model1112050001-model :: biomodels_ebi:MODEL1112050001 :: https://www.ebi.ac.uk/biomodels/MODEL1112050001
- physiology-sbml-mackenzie1996-naglucosecotransporter-kidney-model1006230076-model :: biomodels_ebi:MODEL1006230076 :: https://www.ebi.ac.uk/biomodels/MODEL1006230076
- physiology-sbml-nad-labelling-dynamics-model2409150001-model :: biomodels_ebi:MODEL2409150001 :: https://www.ebi.ac.uk/biomodels/MODEL2409150001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
