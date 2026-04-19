---
title: "Function Reference"
---

# Function Reference

This page documents the core functions available in the `byu_recruiting` package.

---

## Data Functions

### `load_hs_data(filepath)`

Loads and preprocesses high school recruiting data.

**Arguments:**
- `filepath` (str): Path to Excel file

**Returns:**
- `X` (DataFrame): Features
- `y` (Series): Target variable
- `categorical_cols` (list): Categorical columns

---

### `load_transfer_data(filepath)`

Loads and preprocesses transfer/junior college data.

**Arguments:**
- `filepath` (str)

**Returns:**
- `X`, `y`, `categorical_cols`

---

## Modeling Functions

### `load_model(path)`

Loads a trained model from disk.

**Arguments:**
- `path` (str): File path to `.pkl`

**Returns:**
- Trained model pipeline

---

### `predict_proba(model, df)`

Generates commitment probability predictions.

**Arguments:**
- `model`: trained pipeline
- `df` (DataFrame): input data

**Returns:**
- Probability of commitment (float array)

---

## Visualization Functions

### `plot_distance_distribution(df)`

Plots distance from BYU for committed vs non-committed players.

---

### `plot_score_distribution(df)`

Plots composite score distribution.

---

### `plot_height_weight(df)`

Scatter plot of height vs weight.

---

### `plot_distance_comparison(hs_df, transfer_df)`

Compares distance distributions across datasets.

---

## Utilities

(Include anything from `utils.py` if you added it)

---

## Notes

- All models expect categorical variables as strings (e.g., `'Y'`, `'N'`)
- Input data must match training structure

---