# Processed analysis data

Regenerate with `python scripts/prepare_data.py` from the repository root. These tables retain missing environmental values; training-fitted imputation belongs in the model pipeline.

| File | Rows | Meaning |
| --- | ---: | --- |
| `iquitos_history.csv` | 520 | Historical features joined to labels, ordered by date, with Celsius temperature and mean NDVI |
| `iquitos_model_features.csv` | 518 | Historical rows after the two-week lag warm-up, with lagged cases, climate, NDVI, and seasonal terms |
| `iquitos_external_features.csv` | 156 | Later-period inputs, constructed on the continuous historical and later timeline |

`total_cases` is an outcome, never a contemporaneous predictor. The external table includes observed outcomes for retrospective evaluation and uses observed earlier cases for lagged inputs. Its environmental and case values from the target week must not be fed into a one-week-ahead predictor; the notebook selects the explicitly lagged feature columns.

The notebook exports the same three datasets. Keep raw inputs unchanged. See `docs/data_dictionary.md` for fields and `docs/methodology.md` for the information-timing assumption.
