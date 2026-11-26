# File provenance and organization

## Inputs

This repository uses the saved `Iquitos_DengAI_Robustness_Package.zip` and `Iquitos_DengAI_Robustness_Step_by_Step.ipynb` from 15 November 2026. The descriptive city comparison was separately saved on that date. The package is a project archive, not an upstream data-provider release.

## Changes made for the repository

- Raw CSVs are copied without byte changes to `data/raw/`.
- Seven saved result CSVs and one PNG are copied without byte changes to `reports/`.
- The city-comparison CSV is copied without changes to `reports/tables/`.
- The notebook is renamed, its folder paths and setup text are adapted, and processed-table exports are added. Modelling and evaluation specifications are preserved. Stale documentation referring to an absent Section 10 is removed.
- The preparation function reuses the notebook's feature construction; three processed tables are generated from raw inputs.
- READMEs, documentation, requirements, and `.gitignore` describe the organized project.

## Verification scope

Raw-file identity, notebook code syntax, preprocessing joins, historical label agreement, date separation, row counts, and equivalence of exported preprocessing tables are checked during organization. The complete eight-model comparison is not rerun; the displayed historical metrics come from the included archived tables. Dependencies are not version-locked, so future model runs may differ numerically.

## Raw-file SHA-256 fingerprints

| File | SHA-256 |
| --- | --- |
| `Iquitos_CDC_Observed_Cases_2000_2013.csv` | `0799348494905943a65705a8d7b5237e1a9c23906a446fa35d3b003d5eb46921` |
| `dengue_features_test.csv` | `4c1d9a4f4dbbe71292cbd31c0e5ad29220371aebabd7f1ed65e33fd027b2bea0` |
| `dengue_features_train.csv` | `2d983a71d413fadd93a763a8f5928020283cd4d4abe4ca4bd951392034fd657f` |
| `dengue_labels_train.csv` | `f70d52b747d46b58ae3778084130529bb07858d65967080ec76e31960e8f2fd2` |
