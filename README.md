# Environmental Conditions and Dengue Forecasting
**Iquitos, Peru | Projet Transversal | Aix-Marseille School of Economics**
## Research question
Do climate and vegetation measurements improve one-week-ahead predictions of reported dengue cases in Iquitos compared with recent case history and seasonality alone?
## Project scope
The project studies weekly reported dengue case counts alongside temperature, precipitation, humidity, and vegetation measurements (NDVI). It examines forecasting performance and sensitivity to large fluctuations in cases.
## Data
- **DengAI / DrivenData:** environmental features and dengue labels for the historical period.
- **CDC Epidemic Prediction Initiative:** observed Iquitos case counts for later-period evaluation.
The existing research workflow uses 520 historical Iquitos weeks (2000–2010), followed by 156 later weeks (2010–2013).
## Evaluation approach
1. Use chronological internal validation without random shuffling.
2. Compare forecasts using mean absolute error (MAE) and root mean squared error (RMSE).
3. Select and freeze the model specification using internal validation only.
4. Evaluate the selected specification on the later Iquitos period.
5. Assess stability and sensitivity to extreme weeks.
The later-period assessment is a retrospective rolling one-week-ahead evaluation that can use previously observed case counts. It is not a single forecast of the entire later period.
## Repository status
This repository currently contains the project overview. The research notebook, data instructions, and validated results will be added as the analysis files are organized.
## Interpretation
The target is reported case counts rather than population-standardized incidence. Predictive associations do not establish causal effects of environmental conditions.
