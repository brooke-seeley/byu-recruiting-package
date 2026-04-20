# BYU Recruiting Prediction Project

This project predicts the probability that a football recruit will commit to BYU using machine learning models trained on recruiting data.

---

## Project Overview

The goal of this project is to understand what factors influence BYU football recruiting decisions and to build a predictive model based on those factors.

The project includes:

- Data collection via web scraping
- Feature engineering
- Machine learning models
- A Streamlit web application
- A Python package for reuse

---

## Repository Structure

```

byu_recruiting-package/
│
├── app/
│   └── 
│
├── byu_recruiting/        # Python package
│   ├── __init__.py
│   ├── data.py            # Data loading functions
│   ├── modeling.py        # Model training and prediction
│   ├── utils.py           # Helper functions
│   └── visualize.py       # Visualization functions
│
├── data/
│   └── RecruitmentPrediction.xlsx
│
├── docs/
│   └──notebooks/
│       ├── distance_calc.md
│       ├── non_top_pages.md
│       └── top_pages.md
│   ├── dataset.md
│   ├── functions.md
│   ├── index.md
│   └── tutorial.md
│
├── models/
│   ├── hs_model.pkl
│   └── transfer_jc_model.pkl
│
├── requirements.txt # Requirements for app
│
├── streamlit_app.py   # Interactive app
│
└── README.md

```

---

## Features

- Predict commitment probability
- Compare high school vs transfer recruits
- Visualize recruiting trends
- Interactive Streamlit dashboard

---

## Installation

```bash
pip install -e .
```

---

## Run the App

```bash
streamlit run app/streamlit_app.py
```

---

## Documentation

* Tutorial: how to use the package
* Function reference: API documentation
* Dataset: how data was collected

---

## Models

Two models were trained:

* High School Recruiting Model
* Transfer / Junior College Model

Both use:

* Gradient Boosting
* SMOTE for class imbalance
* Cross-validation for tuning

---

## Key Insights

* Distance from BYU plays a major role
* Higher-rated players are less likely to commit
* Transfers come from a wider geographic range

---

## Author

Brooke Seeley
