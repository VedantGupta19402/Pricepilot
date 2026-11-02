# PricePilot

**Status: under active development.** PricePilot is being built incrementally as a
learning-focused machine learning project. The dataset, training, evaluation, and
prediction steps are not implemented yet, and no results are reported at this stage.

## Project Overview

PricePilot is a house price prediction system built with multiple linear regression.
It is designed as a beginner-to-intermediate machine learning project that emphasizes
clear thinking, reproducible workflows, and well-structured code rather than
unnecessary complexity.

The project follows a small, conventional layout: raw and processed data are kept
separate, exploration happens in notebooks, reusable logic lives in `src/`, and
trained artifacts are stored under `models/`.

## Problem Statement

Estimating a house price from its characteristics is a classic regression problem.
Given property features such as living area, number of bedrooms, location, and age,
the goal is to predict a continuous sale price.

A linear regression model is a strong first approach because it is interpretable,
fast to train, and provides a useful baseline for understanding which features are
associated with house prices.

## Project Objectives

- Build a clean and reproducible multiple linear regression workflow.
- Practice the full machine learning lifecycle: data loading, validation, feature
  preparation, training, evaluation, and prediction.
- Use interpretable metrics and visualizations to understand model behavior.
- Keep the codebase beginner-friendly while leaving room to grow.
- Document decisions and results honestly, without fabricated numbers.

## Technology Stack

| Category | Tools |
| --- | --- |
| Language | Python 3.10+ |
| Data handling | NumPy, Pandas |
| Visualization | Matplotlib, Seaborn |
| Machine learning | Scikit-learn |
| Exploration | Jupyter Notebook |
| Testing | Pytest |
| Version control | Git |

## Project Architecture

```text
pricepilot/
├── data/
│   ├── raw/              # Original, immutable dataset
│   └── processed/        # Cleaned and transformed data
├── notebooks/            # Exploration and analysis notebooks
├── src/
│   ├── __init__.py
│   ├── data.py           # Dataset loading and validation
│   ├── train.py          # Model training
│   ├── evaluate.py       # Model evaluation
│   └── predict.py        # Model loading and prediction
├── models/               # Saved model artifacts (not committed)
├── tests/                # Automated tests
├── requirements.txt
├── README.md
├── .gitignore
└── .python-version
```

### Module Responsibilities

- **`src/data.py`** — loads the raw CSV dataset and validates its schema and target column.
- **`src/train.py`** — will fit a multiple linear regression model on prepared features.
- **`src/evaluate.py`** — will compute regression metrics on held-out data.
- **`src/predict.py`** — will load a trained model and estimate prices for new houses.

Data flows from `data/raw/` through validation and preparation into `data/processed/`,
then into training and evaluation, with fitted models saved under `models/`.

## Planned ML Workflow

1. **Data collection** — place the raw house price dataset in `data/raw/`.
2. **Data exploration** — inspect distributions, missing values, and relationships in
   `notebooks/`.
3. **Data validation and cleaning** — check schema, handle missing values and duplicates,
   and verify sensible value ranges.
4. **Feature preparation** — select relevant features, encode categorical variables, and
   split the data into training and test sets.
5. **Model training** — fit a multiple linear regression model with Scikit-learn.
6. **Evaluation** — assess performance on the held-out test set and inspect residuals.
7. **Prediction** — use the trained model to estimate prices for new property records.

## Evaluation Metrics

The planned evaluation metrics are:

| Metric | What it measures |
| --- | --- |
| MAE | Average absolute difference between predicted and actual prices |
| RMSE | Square root of the average squared error; penalizes large errors |
| R² | Proportion of price variance explained by the model |

These metrics will be reported only after the model is trained and evaluated. No
performance values are claimed in this README.

## Installation

Prerequisites: Python 3.10 or newer and Git.

```bash
git clone <repository-url>
cd pricepilot
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS and Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## How to Run the Project

Start Jupyter from the project root to explore the notebooks:

```bash
jupyter lab
```

The data loading and validation helpers can be used directly:

```python
from src.data import load_dataset, validate_dataset

dataset = load_dataset()
dataset = validate_dataset(dataset, required_columns=["area", "bedrooms"])
```

Training, evaluation, and prediction modules currently contain documented function
signatures that raise `NotImplementedError`. They will be implemented as the project
progresses.

Run the test suite (once tests are added):

```bash
pytest
```

## Future Improvements

- Add unit tests for dataset loading, validation, and model behavior.
- Perform exploratory data analysis with clear visualizations.
- Engineer and compare additional features.
- Add cross-validation and compare with regularized models such as Ridge and Lasso.
- Save and load trained models for reproducible predictions.
- Add a small command-line interface for training and prediction.
- Expose the trained model through a lightweight inference API.
- Add CI checks for tests, formatting, and linting.
- Deploy a demo with documented, real evaluation results.
