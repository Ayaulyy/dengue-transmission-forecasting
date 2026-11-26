# Research tables

Archived CSV outputs copied unchanged from the saved project package:

| File | Contents |
| --- | --- |
| `internal_model_comparison.csv` | Eight candidate models evaluated on internal validation |
| `external_model_comparison.csv` | Frozen selected model and predeclared references on later weeks |
| `external_predictions.csv` | Later dates, observed cases, predictions, and selected-model absolute errors |
| `research_results_summary.csv` | Internal and later-period headline metrics |
| `robustness_expanding_windows.csv` | Model errors across historical validation windows |
| `robustness_block_bootstrap.csv` | Approximate uncertainty interval for the internal climate MAE gain |
| `robustness_extreme_week_sensitivity.csv` | Climate gain after omitting the largest observed weeks from scoring |
| `City_Comparison_Iquitos_vs_SanJuan.csv` | Separately saved descriptive comparison of the two cities |

The notebook writes its seven result CSVs here. The city-comparison CSV is an existing separate descriptive artifact, not an output of the preparation script. Prediction tables belong here; model input tables belong in `data/processed/`.
