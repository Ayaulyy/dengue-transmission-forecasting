# Raw input data

These four CSV files are copied byte-for-byte from the saved 15 November 2026 project package. Do not edit them; save transformations in `data/processed/`.

| File | Rows | Columns |
| --- | ---: | ---: |
| `Iquitos_CDC_Observed_Cases_2000_2013.csv` | 676 | 2 |
| `dengue_features_test.csv` | 416 | 24 |
| `dengue_features_train.csv` | 1456 | 24 |
| `dengue_labels_train.csv` | 1456 | 4 |

## Sources and scope

- `dengue_features_train.csv`: DrivenData DengAI environmental and calendar measurements for labeled weeks, including Iquitos (`iq`) and San Juan (`sj`).
- `dengue_labels_train.csv`: reported weekly case counts. Join by `city`, `year`, and `weekofyear` with a one-to-one check.
- `dengue_features_test.csv`: environmental observations for later weeks, without outcome labels. The Iquitos subset contains 156 later weeks.
- `Iquitos_CDC_Observed_Cases_2000_2013.csv`: two-column case-series extract (`week_start_date`, `total_cases_cdc`) covering 676 Iquitos weeks. The first 520 counts are checked against DengAI labels before later-period evaluation.

Upstream sources: DrivenData **DengAI: Predicting Disease Spread** and [CDC Epidemic Prediction Initiative dengue data](https://cdcepi.github.io/dengue/data.html). Files were supplied in the project archive; they were not newly downloaded from upstream. Observe the providers' attribution and reuse terms before redistributing the data.
