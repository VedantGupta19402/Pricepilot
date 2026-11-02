"""Dataset loading and validation for PricePilot."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATASET_PATH = PROJECT_ROOT / "data" / "raw" / "housing.csv"
TARGET_COLUMN = "price"


