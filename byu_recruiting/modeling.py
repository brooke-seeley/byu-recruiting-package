import joblib
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import GridSearchCV, StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score

from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

from sklearn.ensemble import HistGradientBoostingClassifier

## Create preprocessing + model pipeline

def build_pipeline(categorical_cols):

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
        ],
        remainder='passthrough'
    )

    pipeline = Pipeline(steps=[
        ('preprocess', preprocessor),
        ('smote', SMOTE(random_state=123)),
        ('model', HistGradientBoostingClassifier(random_state=123))
    ])

    return pipeline

## Train model using cross-validation and grid search

def train_model(X, y, categorical_cols):

    pipeline = build_pipeline(categorical_cols)

    param_grid = {
        'model__max_depth': [4, 6, None],
        'model__learning_rate': [0.03, 0.05],
        'model__max_iter': [200, 300]
    }

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=123)

    grid_search = GridSearchCV(
        pipeline,
        param_grid,
        cv=cv,
        scoring='roc_auc',
        n_jobs=-1
    )

    grid_search.fit(X, y)

    return grid_search

## Return accuracy and CV accuracy

def evaluate_model(model, X, y):

    probs = model.predict_proba(X)[:, 1]
    preds = (probs >= 0.5).astype(int)

    accuracy = accuracy_score(y, preds)

    cv_scores = cross_val_score(
        model, X, y,
        cv=5,
        scoring='accuracy'
    )

    return {
        "accuracy": accuracy,
        "cv_accuracy": np.mean(cv_scores)
    }

## Predict probability of BYU commitment

def predict_proba(model, input_df):

    return model.predict_proba(input_df)[:, 1]

## Save/load models

def save_model(model, path):
    joblib.dump(model, path)


def load_model(path):
    return joblib.load(path)