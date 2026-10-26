"""
Ridge, Lasso & Elastic Net Regression
Dataset : California Housing
Source  : sklearn fetch_california_housing (downloads once, needs internet)

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


# Dataset 1:- California Housing Dataset

housing = fetch_california_housing()

df = pd.DataFrame(housing.data, columns=housing.feature_names)

df["Price"] = housing.target

display(df.head())

X = df.drop("Price", axis=1)

y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Ridge Regression

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

print("Best Alpha:", ridge_model.best_params_)

ridge_prediction = ridge_model.predict(X_test)

print("R2 Score:", r2_score(y_test, ridge_prediction))

print("MSE:", mean_squared_error(y_test, ridge_prediction))


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

print("Best Alpha:", lasso_model.best_params_)

lasso_prediction = lasso_model.predict(X_test)

print("R2 Score:", r2_score(y_test, lasso_prediction))

print("MSE:", mean_squared_error(y_test, lasso_prediction))


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

print("Best Parameters:", elastic_model.best_params_)

elastic_prediction = elastic_model.predict(X_test)

print("R2 Score:", r2_score(y_test, elastic_prediction))

print("MSE:", mean_squared_error(y_test, elastic_prediction))

print("--- Conclusion for California Housing Dataset ---")
print("\nRidge Regression:")
print(f"  Best Parameter: {ridge_model.best_params_['alpha']}")
print(f"  R2 Score: {r2_score(y_test, ridge_prediction):.4f}")
print(f"  MSE: {mean_squared_error(y_test, ridge_prediction):.4f}")

print("\nLasso Regression:")
print(f"  Best Parameter: {lasso_model.best_params_['alpha']}")
print(f"  R2 Score: {r2_score(y_test, lasso_prediction):.4f}")
print(f"  MSE: {mean_squared_error(y_test, lasso_prediction):.4f}")

print("\nElastic Net Regression:")
print(f"  Best Parameters: {elastic_model.best_params_}")
print(f"  R2 Score: {r2_score(y_test, elastic_prediction):.4f}")
print(f"  MSE: {mean_squared_error(y_test, elastic_prediction):.4f}")
