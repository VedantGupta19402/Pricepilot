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


