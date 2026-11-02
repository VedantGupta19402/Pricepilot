"""Model evaluation responsibilities for PricePilot.

Evaluation will report standard regression metrics on held-out data once
training is implemented. No performance figures are available yet.
"""

from __future__ import annotations

import pandas as pd
from sklearn.base import BaseEstimator

METRIC_NAMES = ("mae", "rmse", "r2")


