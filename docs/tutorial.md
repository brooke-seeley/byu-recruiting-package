---
title: Tutorial: Using the BYU Commitment Predictor Package
---

This tutorial walks through how to install and use the **BYU Commitment Predictor** package.

---

## Installation

Clone the repository and install the package locally:

```bash
git clone https://github.com/brooke-seeley/byu-recruiting-package.git
cd byu-recruiting-package
pip install -e .
```

---

## Step 1: Load Data

Use the data module to load either the high school or transfer dataset:

```python
from byu_recruiting.data import load_hs_data, load_transfer_data

hs_data = load_hs_data('RecruitmentPrediction.xlsx')
transfer_data = load_transfer_data('RecruitmentPrediction.xlsx')

print(hs_data.head())
```

---

## Step 2: Prepare Features

Separate predictors and outcome:

```python
X = hs_data.drop(columns='BYU')
y = hs_data['BYU']
```

---

## Step 3: Train a Model

Train a high school model using cross-validation:

```python
from byu_recruiting.modeling import train_hs_model

model = train_hs_model(X, y)

print(model)
```

---

## Step 4: Evaluate Model Performance

Evaluate accuracy and ROC AUC:

```python
from byu_recruiting.modeling import evaluate_model

results = evaluate_model(model, X, y)

print(results)
```

Example output:

```bash
{'roc_auc': 0.91, 'accuracy': 0.86}
```

---

## Step 5: Make Predictions

Create a new player and predict their probability of committing:

```python
import pandas as pd

new_player = pd.DataFrame({
    '247Top': ['Y'],
    'Position': ['QB'],
    'Utah': ['N'],
    'Distance': [850],
    'Height': [74],
    'Weight': [210],
    'Score': [0.92],
    'LDS': ['N'],
    'Alumni': ['N'],
    'Poly': ['N']
})

prob = model.predict_proba(new_player)[0][1]

print(f'Commitment Probability: {prob:.3f}')
```

---

## Transfer / JC Model Example

The process is identical for transfer players:

```python
from byu_recruiting.modeling import train_transfer_model

X_t = transfer_data.drop(columns='BYU')
y_t = transfer_data['BYU']

transfer_model = train_transfer_model(X_t, y_t)
```

---

## Step 6: Create Visualizations

Generate simple plots to explore the data:

```python
from byu_recruiting.visualize import plot_distance_distribution

plot_distance_distribution(hs_data)
```

---

## Step 7: Save and Load Models

Save a trained model:

```python
from byu_recruiting.utils import save_model

save_model(model, 'hs_model.pkl')
```

Load it later:

```python
from byu_recruiting.utils import load_model

model = load_model('hs_model.pkl')
```

---

Explore the other pages for more details:

* [Function Documentation](functions.md) → full package reference
* [Dataset Construction](dataset.md) → how the data was created