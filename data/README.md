# Data

- [raw/](raw/): original inputs; preserve their bytes.
- [processed/](processed/): reproducible derived tables used for inspection and modelling.

Run `python scripts/prepare_data.py` from the repository root to regenerate processed tables. Transformations do not fill missing environmental values; model pipelines fit their imputation on training data only. Descriptive city comparisons belong in `reports/tables/`.

See [the variable guide](../docs/data_dictionary.md) and each subfolder README.
