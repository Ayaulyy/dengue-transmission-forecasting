"""Run from any working directory: python scripts/prepare_data.py."""
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
from src.data import prepare_data

if __name__ == "__main__":
    for name, rows in prepare_data(PROJECT_ROOT).items():
        print(f"{name}: {rows} rows")
