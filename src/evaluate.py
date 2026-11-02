"""Model evaluation responsibilities for PricePilot.

Evaluation will report standard regression metrics on held-out data once
training is implemented. No performance figures are available yet.
"""

from __future__ import annotations

import pandas as pd
from sklearn.base import BaseEstimator

METRIC_NAMES = ("mae", "rmse", "r2")


def evaluate_model(
    model: BaseEstimator,
    features: pd.DataFrame,
    target: pd.Series,
) -> dict[str, float]:
    """Evaluate a fitted regression model on held-out data.

    The planned metrics are mean absolute error (MAE), root mean squared
    error (RMSE), and the coefficient of determination (R²).

    Args:
        model: A fitted scikit-learn regression model.
        features: Feature columns used for prediction.
        target: True house prices aligned with ``features``.

    Returns:
        A mapping of metric names to their computed values.

    Raises:
        NotImplementedError: Evaluation is not implemented yet.
    """
    raise NotImplementedError(
        "Model evaluation is not implemented yet. "
        "No performance metrics are reported for this project."
    )
