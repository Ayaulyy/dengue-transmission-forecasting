# Model artifacts

No fitted model binaries are included. The notebook fits models in memory and exports evaluation tables and predictions to `reports/`.

If fitted models are added later, record the model specification, training cutoff, feature order, dependency versions, and evaluation provenance beside each artifact. Do not select a model by inspecting the later evaluation results. Local pickle/joblib artifacts are ignored by default in `.gitignore`.
