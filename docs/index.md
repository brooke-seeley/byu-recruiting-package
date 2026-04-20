---
title: 'Home'
---

Welcome! This project explores the factors that influence whether a football recruit commits to BYU. Using a custom-built dataset and machine learning models, the goal is to estimate the probability of commitment based on player characteristics.

---

## Project Overview

Recruiting decisions are complex and influenced by many factors, including player rankings, geography, and background. In this project, I:

- Built a custom dataset of high school, transfer, and junior college recruits  
- Engineered features such as distance from BYU and recruiting rank
- Trained machine learning models to predict commitment probability  
- Developed an interactive app to explore predictions  

This project combines data collection, feature engineering, and modeling into a single end-to-end workflow.

---

## Project Components

You can explore each part of the project below:

### [Tutorial](tutorial.md)
Learn how to install the package and generate predictions using the trained models.

### [Function Documentation](functions.md)
Detailed reference for the package functions, including inputs, outputs, and examples.

### [Dataset Construction](dataset.md)
See how the dataset was built from scratch, including web scraping and feature engineering.

---

## Tools & Methods

This project uses:

- **Python**: `pandas`, `scikit-learn`, `BeautifulSoup`, `geopy`  
- **Modeling**: Random Forest, XGBoost, cross-validation, SMOTE  
- **Visualization**: Matplotlib and Seaborn
- **Deployment**: Streamlit app for interactive predictions  

---

## Key Takeaways

- Recruiting rank and player characteristics are strong predictors of commitment  
- Transfer and high school recruits exhibit different patterns  
- Building a custom dataset enabled more targeted and meaningful analysis

---

### Live App
Try the model app: [Streamlit App](https://byu-recruiting-model.streamlit.app)

### Source Code
- View the repository for creating the transfer dataset and models: [Final Project](https://github.com/brooke-seeley/final-project)
- View the repository for this website and app: [BYU Recruiting Package](https://github.com/brooke-seeley/byu-recruiting-package)
- View the repository for my work on this project last semester: [Football](https://github.com/brooke-seeley/Football)