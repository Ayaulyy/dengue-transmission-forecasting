# Reusable Python code

`data.py` contains `make_features(frame)` and `prepare_data(project_root)`.

The lag and seasonal feature function is copied from the original research notebook. Preparation validates unique joins, Iquitos row counts, historical CDC agreement, and non-overlapping later dates before exporting the three processed tables. It performs no model fitting or global imputation.

Call preparation through `python scripts/prepare_data.py`. Keep future reusable transformations or modelling utilities in this folder; use notebooks for interactive analysis.
