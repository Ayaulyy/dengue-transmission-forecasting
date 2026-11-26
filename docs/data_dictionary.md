# Variable guide

| Variable | Meaning or construction |
| --- | --- |
| `city` | City code: `iq` for Iquitos, `sj` for San Juan |
| `year`, `weekofyear` | Calendar keys supplied in DengAI |
| `week_start_date` | Source weekly date; preserve original date conventions |
| `total_cases` | Reported dengue case count for the target week |
| `total_cases_cdc` | CDC-extract reported count; renamed to `total_cases` for later feature construction |
| `precipitation_amt_mm`, `rain_mm` | Source weekly precipitation estimate, in millimetres |
| `reanalysis_avg_temp_k` | Source mean reanalysis temperature in kelvin |
| `temperature_c` | `reanalysis_avg_temp_k - 273.15` |
| `reanalysis_relative_humidity_percent`, `humidity_pct` | Source relative humidity, percent |
| `ndvi_ne`, `ndvi_nw`, `ndvi_se`, `ndvi_sw` | NDVI measurements for four satellite cells |
| `ndvi_mean` | Row mean over the four NDVI cells, ignoring missing cells |
| `cases_lag1`, `cases_lag2` | Reported cases one and two earlier rows/weeks |
| `log_cases_lag1`, `log_cases_lag2` | Natural log of one plus the corresponding case lag |
| `rain_lag1`, `rain_lag2` | Precipitation one and two earlier weeks |
| `temp_lag1` | Celsius temperature one earlier week |
| `humidity_lag1` | Relative humidity one earlier week |
| `ndvi_lag1` | Mean NDVI one earlier week |
| `season_sin`, `season_cos` | Sine/cosine of `2*pi*(weekofyear-1)/52.1775` |

Source files also retain other DengAI measurements that are not all used by the selected feature sets. Consult the upstream data documentation for their full definitions. Missing values are preserved during preparation; model pipelines fit imputers on training data. Do not use contemporaneous target-week measurements as forecast predictors.
