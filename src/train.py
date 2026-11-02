"""Model training responsibilities for PricePilot.

Training will fit a multiple linear regression model on prepared features
and house prices. The implementation is intentionally deferred until the
dataset and feature set are finalized.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL_PATH = PROJECT_ROOT / "models" / "pricepilot_linear_regression.joblib"


