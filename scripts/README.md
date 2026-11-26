# Command-line scripts

Run from the repository root:

```bash
python scripts/prepare_data.py
```

The script also works from other directories because it resolves the repository root from its own location. It reads `data/raw/`, uses `src/data.py`, checks row counts and historical label agreement, then regenerates the three tables in `data/processed/`. It does not train models or overwrite archived research results.

Use the notebook for the full forecasting and robustness workflow.
