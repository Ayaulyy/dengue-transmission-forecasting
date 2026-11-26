# Reports and research outputs

- [tables/](tables/): archived CSV results and predictions from the saved 15 November package, plus the saved city-comparison table.
- [figures/](figures/): the archived robustness figure; further notebook plots are saved here when executed.

The complete model comparison has not been rerun during repository organization. Existing archived files retain their original bytes; running the notebook can regenerate and overwrite its corresponding outputs.

## Saved numerical results

| Evaluation | Model | MAE | RMSE |
| --- | --- | ---: | ---: |
| Internal, 104 weeks | Ridge: history + climate | 3.902 | 6.529 |
| Later period, 156 weeks | Ridge: history + climate | 3.684 | 8.195 |
| Later period | History-only Ridge reference | 3.729 | 8.409 |
| Later period | Persistence reference | 3.821 | 7.563 |

The selected model has the lowest saved later-period MAE among these references, while persistence has the lowest RMSE. The saved internal climate MAE gain over history-only Ridge is approximately 0.052 cases/week; the approximate block-bootstrap interval is [-0.113, 0.185]. Improvements depend on the validation window and extreme weeks. Do not interpret these results as causal estimates or robust evidence that climate always improves prediction.

Place final written reports here and presentation files in this folder when available. No final report or slides have been added yet.
