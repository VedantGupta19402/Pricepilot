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


def load_model(path: Path | str = DEFAULT_MODEL_PATH) -> BaseEstimator:
    """Load a trained model from disk.

    Args:
        path: Location of the saved model artifact.

    Returns:
        The loaded scikit-learn model.

    Raises:
        NotImplementedError: Model loading is not implemented yet.
    """
    raise NotImplementedError(
        "Model loading is not implemented yet. "
        "A model must be trained and saved before predictions are possible."
    )


def predict_price(model: BaseEstimator, features: Mapping[str, float]) -> float:
    """Estimate the price of a single house.

    Args:
        model: A fitted scikit-learn regression model.
        features: Feature names mapped to their values for one house.

    Returns:
        The estimated house price.

    Raises:
        NotImplementedError: Prediction is not implemented yet.
    """
    raise NotImplementedError(
        "Prediction is not implemented yet. "
        "See README.md for the planned machine learning workflow."
    )
