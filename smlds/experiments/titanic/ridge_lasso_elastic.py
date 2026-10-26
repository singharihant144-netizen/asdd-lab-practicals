"""
Ridge, Lasso & Elastic Net Regression
Dataset : Titanic
Source  : seaborn load_dataset("titanic") (needs internet)

Run in VS Code: open this file and press "Run Python File" (or: python <file>.py)
Requires: pip install numpy pandas matplotlib seaborn scikit-learn scipy statsmodels
"""

import warnings
warnings.filterwarnings("ignore")

def display(obj):
    """Stand-in for Jupyter's display() so the script runs in plain VS Code."""
    print(obj)

import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_iris
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import Ridge, Lasso, ElasticNet


# Dataset 3:- Titanic Dataset

df = sns.load_dataset("titanic")

display(df.head())

df = df[["survived", "pclass", "age", "sibsp", "parch", "fare"]]

df = df.dropna()

display(df.head())

X = df.drop("survived", axis=1)

y = df["survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Ridge Regretion

ridge = Ridge()

parameters = {
    "alpha": [0.01, 0.1, 1, 10, 100]
}

ridge_model = GridSearchCV(
    ridge,
    parameters,
    cv=5
)

ridge_model.fit(X_train, y_train)

print("Ridge Best Alpha:", ridge_model.best_params_)

ridge_prediction = ridge_model.predict(X_test)

print("Ridge R2 Score:", r2_score(y_test, ridge_prediction))

print("Ridge MSE:", mean_squared_error(y_test, ridge_prediction))


# Lasso Regression

lasso = Lasso(max_iter=10000)

parameters = {
    "alpha": [0.01, 0.1, 1, 10]
}

lasso_model = GridSearchCV(
    lasso,
    parameters,
    cv=5
)

lasso_model.fit(X_train, y_train)

print("Lasso Best Alpha:", lasso_model.best_params_)

lasso_prediction = lasso_model.predict(X_test)

print("Lasso R2 Score:", r2_score(y_test, lasso_prediction))

print("Lasso MSE:", mean_squared_error(y_test, lasso_prediction))


# Elastic Regression

elastic = ElasticNet(max_iter=10000)

parameters = {
    "alpha": [0.01, 0.1, 1],
    "l1_ratio": [0.2, 0.5, 0.8]
}

elastic_model = GridSearchCV(
    elastic,
    parameters,
    cv=5
)

elastic_model.fit(X_train, y_train)

print("Elastic Net Best Parameters:", elastic_model.best_params_)

elastic_prediction = elastic_model.predict(X_test)

print("Elastic Net R2 Score:", r2_score(y_test, elastic_prediction))

print("Elastic Net MSE:", mean_squared_error(y_test, elastic_prediction))

print("Conclusion")

print("1. The Titanic dataset was loaded and preprocessed.")

print("2. Missing values were removed from the selected features.")

print("3. Ridge Regression was applied with different alpha values.")

print("4. Lasso Regression was applied with different alpha values.")

print("5. Elastic Net Regression was applied using different alpha and l1_ratio values.")

print("6. GridSearchCV was used to find the best parameters for each model.")

print("7. R2 Score and Mean Squared Error were used to evaluate the models.")
