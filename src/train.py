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


def train_model(features: pd.DataFrame, target: pd.Series) -> LinearRegression:
    """Train a multiple linear regression model.

    Args:
        features: Numeric feature columns used for prediction.
        target: House prices aligned with ``features``.

    Returns:
        The fitted scikit-learn model.

    Raises:
        NotImplementedError: Training is not implemented yet.
    """
    raise NotImplementedError(
        "Model training is not implemented yet. "
        "See README.md for the planned machine learning workflow."
    )
