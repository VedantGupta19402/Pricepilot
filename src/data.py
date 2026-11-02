"""Dataset loading and validation for PricePilot."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATASET_PATH = PROJECT_ROOT / "data" / "raw" / "housing.csv"
TARGET_COLUMN = "price"


def load_dataset(path: Path | str = DEFAULT_DATASET_PATH) -> pd.DataFrame:
    """Load a house price dataset from a CSV file.

    Args:
        path: Location of the CSV file. Defaults to the raw dataset path.

    Returns:
        The dataset as a pandas DataFrame.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        ValueError: If the file is empty or contains no rows.
    """
    csv_path = Path(path)

    if not csv_path.is_file():
        raise FileNotFoundError(f"Dataset not found: {csv_path}")

    try:
        dataset = pd.read_csv(csv_path)
    except pd.errors.EmptyDataError as error:
        raise ValueError(f"Dataset is empty: {csv_path}") from error

    if dataset.empty:
        raise ValueError(f"Dataset contains no rows: {csv_path}")

    return dataset


def validate_dataset(
    dataset: pd.DataFrame,
    required_columns: Iterable[str] | None = None,
    target_column: str = TARGET_COLUMN,
) -> pd.DataFrame:
    """Validate the structure and basic quality of a house price dataset.

    The dataset must contain rows, include the target column and any
    required feature columns, and have a numeric target without missing
    values.

    Args:
        dataset: Dataset to validate.
        required_columns: Additional columns expected in the dataset.
        target_column: Name of the house price target column.

    Returns:
        A validated copy of the dataset.

    Raises:
        ValueError: If any validation check fails.
    """
    if dataset.empty:
        raise ValueError("Dataset contains no rows.")

    expected_columns = {target_column, *(required_columns or ())}
    missing_columns = sorted(expected_columns - set(dataset.columns))
    if missing_columns:
        raise ValueError(
            "Dataset is missing required columns: " + ", ".join(missing_columns)
        )

    target = dataset[target_column]
    if not pd.api.types.is_numeric_dtype(target):
        raise ValueError(f"Target column '{target_column}' must be numeric.")
    if target.isna().any():
        raise ValueError(f"Target column '{target_column}' contains missing values.")

    return dataset.copy()
