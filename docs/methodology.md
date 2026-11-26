# Methodology

## Target and scope

Forecast weekly reported dengue counts for Iquitos, Peru, one week ahead. The scientific comparison asks whether lagged climate and NDVI improve prediction relative to case history and seasonality. San Juan appears in source data and a descriptive city comparison; it is not the external evaluation site.

## Chronological evaluation

There are 520 historical Iquitos weeks. Construct lagged predictors without random shuffling; dropping two initial lag-warm-up rows leaves 518 usable rows. Fit candidates on the first 414 usable rows and validate on the final 104 historical weeks. Candidate specifications include persistence, Ridge, Poisson regression, and XGBoost.

Select the model specification by internal MAE, then refit that specification on all available historical model rows. Evaluate it once on 156 later Iquitos weeks, using CDC observations as outcomes. MAE and RMSE answer different error questions; report both. Later-period data must not drive model reselection.

## Forecast timing

For target week t, predictor columns use case counts and environmental measurements from earlier weeks, plus known seasonal terms. Although exported tables retain contemporaneous columns for inspection, the model must use only its named lagged feature list.

The later assessment constructs lagged inputs on the combined timeline and can use previously observed later-period cases. This assumes those past counts are available when each forecast is made. It is a retrospective rolling one-week-ahead exercise, not a single 156-week-ahead forecast or a prospective operational trial. Reporting delays can reduce real-time usefulness.

## Robustness and interpretation

Historical expanding windows, an approximate paired block bootstrap, and extreme-week sensitivity checks examine stability. The saved climate-gain interval spans zero and results vary with large fluctuations. These checks do not turn observational predictive relationships into causal effects.

The later period is a temporal holdout for the same city, rather than independent geographic validation. Reported cases can reflect surveillance and reporting changes; they are not population-standardized incidence rates.
