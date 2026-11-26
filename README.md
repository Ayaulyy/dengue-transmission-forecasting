# Environmental Conditions and Dengue Forecasting

**Iquitos, Peru · Projet Transversal · Aix-Marseille School of Economics**

## Research question

Do climate and vegetation measurements improve one-week-ahead predictions of reported dengue cases in Iquitos compared with recent case history and seasonality alone?

## Repository guide

| Location | Contents |
| --- | --- |
| [data/raw/](data/raw/) | Four unmodified source CSV files |
| [data/processed/](data/processed/) | Merged Iquitos history and lagged forecasting inputs |
| [notebooks/](notebooks/) | Main research notebook |
| [reports/tables/](reports/tables/) | Saved model comparisons, predictions, robustness tables, and city comparison |
| [reports/figures/](reports/figures/) | Saved and generated analysis figures |
| [src/](src/) | Reusable data preparation and feature construction |
| [scripts/](scripts/) | Command-line data preparation |
| [docs/](docs/) | Methodology, variable guide, and file provenance |
| [models/](models/) | Documentation for future fitted-model exports |

Each folder contains a README explaining its contents and use.

## Getting started

Use Python 3.10 or later. From the repository root:

```bash
python -m venv .venv
# Activate .venv in your shell, then:
python -m pip install -r requirements.txt
python scripts/prepare_data.py
jupyter lab
```

Open `notebooks/01_iquitos_dengue_forecasting.ipynb` and run the cells in order. Jupyter may start at the repository root or inside `notebooks/`; the notebook finds the root automatically. Preparation alone requires only NumPy and pandas.

## Data and evaluation

The four input files combine DrivenData DengAI environmental observations and labels with a two-column extract of the CDC Epidemic Prediction Initiative Iquitos case series. Historical analysis uses 520 Iquitos weeks (2000–2010); two lag weeks leave 518 model rows, split into 414 fitting and 104 internal-validation rows. The later evaluation covers 156 weeks (2010–2013).

Candidate models include persistence, Ridge, Poisson regression, and XGBoost, with history, seasonality, climate, and NDVI feature sets. Select the specification by internal MAE, retain the same specification for later evaluation, and also report RMSE. Robustness checks cover expanding windows, block-bootstrap uncertainty, and sensitivity to extreme weeks.

The later assessment is a retrospective rolling one-week-ahead procedure using previously observed case counts; reporting delays matter for real-time use. It does not measure a 156-week-ahead forecast or geographic transfer to another city. See [methodology](docs/methodology.md).

## Included results

The saved 15 November package selected **Ridge: history + climate** with internal MAE **3.902** and later-period MAE **3.684**. These are archived results, not a newly rerun model comparison. The small climate improvement is sensitive to validation period and extreme weeks; the saved block-bootstrap interval includes zero. See [reports](reports/README.md) for exact tables and interpretation.

## Provenance and reproducibility

This repository organizes the saved research package from **15 November 2026**. Raw CSV bytes and archived result files are preserved. The notebook changes concern paths, processed-data exports, and setup documentation. Prepared data can be regenerated with the supplied script. Full notebook execution requires XGBoost; dependencies are listed but the original environment was not version-locked. See [provenance](docs/provenance.md).

The target is weekly reported case counts, rather than population-standardized incidence. Predictive associations do not establish causal environmental effects. Dataset attribution and applicable source terms remain with the original providers.
