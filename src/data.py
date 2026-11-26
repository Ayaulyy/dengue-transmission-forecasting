"""Prepare analysis tables without fitting models or imputing future data.

The feature function preserves the specification of the 15 November notebook.
"""
from pathlib import Path
import numpy as np
import pandas as pd

ndvi_columns = ["ndvi_ne", "ndvi_nw", "ndvi_se", "ndvi_sw"]

def make_features(frame):
    d = frame.sort_values("week_start_date").reset_index(drop=True).copy()
    d["temperature_c"] = d["reanalysis_avg_temp_k"] - 273.15
    d["ndvi_mean"] = d[ndvi_columns].mean(axis=1)

    d["cases_lag1"] = d["total_cases"].shift(1)
    d["cases_lag2"] = d["total_cases"].shift(2)
    d["log_cases_lag1"] = np.log1p(d["cases_lag1"])
    d["log_cases_lag2"] = np.log1p(d["cases_lag2"])

    d["rain_lag1"] = d["precipitation_amt_mm"].shift(1)
    d["rain_lag2"] = d["precipitation_amt_mm"].shift(2)
    d["temp_lag1"] = d["temperature_c"].shift(1)
    d["humidity_lag1"] = d["reanalysis_relative_humidity_percent"].shift(1)
    d["ndvi_lag1"] = d["ndvi_mean"].shift(1)

    angle = 2 * np.pi * (d["weekofyear"] - 1) / 52.1775
    d["season_sin"] = np.sin(angle)
    d["season_cos"] = np.cos(angle)
    return d

def prepare_data(project_root):
    root = Path(project_root)
    raw = root / "data" / "raw"
    destination = root / "data" / "processed"
    destination.mkdir(parents=True, exist_ok=True)
    features = pd.read_csv(raw / "dengue_features_train.csv")
    labels = pd.read_csv(raw / "dengue_labels_train.csv")
    keys = ["city", "year", "weekofyear"]
    assert not features.duplicated(keys).any()
    assert not labels.duplicated(keys).any()
    merged = features.merge(labels, on=keys, validate="one_to_one")
    assert len(merged) == len(features) == len(labels)
    history = merged.loc[merged.city.eq("iq")].copy()
    history["week_start_date"] = pd.to_datetime(history.week_start_date)
    history = history.sort_values("week_start_date").reset_index(drop=True)
    assert len(history) == 520 and history.week_start_date.is_unique
    history["rain_mm"] = history.precipitation_amt_mm
    history["temperature_c"] = history.reanalysis_avg_temp_k - 273.15
    history["humidity_pct"] = history.reanalysis_relative_humidity_percent
    history["ndvi_mean"] = history[ndvi_columns].mean(axis=1)
    model = make_features(history).dropna(subset=["cases_lag1", "cases_lag2"])
    assert len(model) == 518

    cdc = pd.read_csv(raw / "Iquitos_CDC_Observed_Cases_2000_2013.csv",
                      parse_dates=["week_start_date"])
    assert len(cdc) == 676 and cdc.week_start_date.is_unique
    check = history.merge(cdc, on="week_start_date", validate="one_to_one")
    assert len(check) == 520
    assert (check.total_cases == check.total_cases_cdc).all()
    later = pd.read_csv(raw / "dengue_features_test.csv",
                        parse_dates=["week_start_date"])
    later = later.loc[later.city.eq("iq")].sort_values("week_start_date")
    assert len(later) == 156 and later.week_start_date.is_unique
    assert not set(later.week_start_date).intersection(history.week_start_date)
    later = later.merge(cdc, on="week_start_date", how="left", validate="one_to_one")
    assert later.total_cases_cdc.notna().all()
    later = later.rename(columns={"total_cases_cdc": "total_cases"})
    timeline = pd.concat([history, later], ignore_index=True).sort_values("week_start_date")
    external = make_features(timeline).iloc[520:].copy()
    assert len(external) == 156
    outputs = {
        "iquitos_history.csv": history,
        "iquitos_model_features.csv": model,
        "iquitos_external_features.csv": external,
    }
    for name, frame in outputs.items():
        frame.to_csv(destination / name, index=False)
    return {name: len(frame) for name, frame in outputs.items()}
