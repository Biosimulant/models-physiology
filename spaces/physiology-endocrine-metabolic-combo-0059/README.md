# COMBO_0059 - Physiology Endocrine Metabolic

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
- `physiology-sbml-kiselyov2009-insulinreceptormodel-model1112050000-model`: Physiology: Kiselyov2009InsulinreceptormodelModel1112050000Model
- `physiology-sbml-komarova2005-pthaction-osteoclastosteoblastcoupl-biomd0000000279-model`: Physiology: Komarova2005PthactionOsteoclastosteoblastcouplBiomd0000000279Model
- `physiology-sbml-kroll2000-pth-boneformationdesorption-model1006230083-model`: Physiology: Kroll2000PthBoneformationdesorptionModel1006230083Model
- `physiology-sbml-lenbury2001-insulinkineticsmodel-a-biomd0000000878-model`: Physiology: Lenbury2001InsulinkineticsmodelABiomd0000000878Model

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
- physiology-sbml-kiselyov2009-insulinreceptormodel-model1112050000-model :: biomodels_ebi:MODEL1112050000 :: https://www.ebi.ac.uk/biomodels/MODEL1112050000
- physiology-sbml-komarova2005-pthaction-osteoclastosteoblastcoupl-biomd0000000279-model :: biomodels_ebi:BIOMD0000000279 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000279
- physiology-sbml-kroll2000-pth-boneformationdesorption-model1006230083-model :: biomodels_ebi:MODEL1006230083 :: https://www.ebi.ac.uk/biomodels/MODEL1006230083
- physiology-sbml-lenbury2001-insulinkineticsmodel-a-biomd0000000878-model :: biomodels_ebi:BIOMD0000000878 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000878

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
