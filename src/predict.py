"""Prediction responsibilities for PricePilot.

Prediction will load a trained model and estimate a house price from a
single set of feature values. No model or predictions are available yet.
"""

from __future__ import annotations

from pathlib import Path
from typing import Mapping

from sklearn.base import BaseEstimator

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL_PATH = PROJECT_ROOT / "models" / "pricepilot_linear_regression.joblib"


