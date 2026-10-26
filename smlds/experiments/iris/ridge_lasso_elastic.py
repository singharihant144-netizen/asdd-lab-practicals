"""
Ridge, Lasso & Elastic Net Regression
Dataset : Iris
Source  : seaborn load_dataset("iris") / sklearn load_iris

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


# Dataset 2:-Iris Dataset

from sklearn.datasets import load_iris

iris = load_iris()

df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)

# For regression, we'll try to predict one of the features, for example, 'petal length (cm)'
df_iris["Target"] = iris.target

display(df_iris.head())

X_iris = df_iris.drop("Target", axis=1)
y_iris = df_iris["Target"]

X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(
    X_iris,
    y_iris,
    test_size=0.2,
    random_state=42
)


# Ridge Regression
# 
# ---

ridge_iris = Ridge()

parameters_iris = {
    "alpha": [0.01, 0.1, 1, 10, 100]
}

ridge_model_iris = GridSearchCV(
    ridge_iris,
    parameters_iris,
    cv=5
)

ridge_model_iris.fit(X_train_iris, y_train_iris)
print("Best Alpha (Iris):", ridge_model_iris.best_params_)

ridge_prediction_iris = ridge_model_iris.predict(X_test_iris)

print("R2 Score (Iris):", r2_score(y_test_iris, ridge_prediction_iris))
print("MSE (Iris):", mean_squared_error(y_test_iris, ridge_prediction_iris))


# Lasso Regression

lasso_iris = Lasso(max_iter=10000)

parameters_iris_lasso = {
    "alpha": [0.001, 0.01, 0.1, 1]
}

lasso_model_iris = GridSearchCV(
    lasso_iris,
    parameters_iris_lasso,
    cv=5
)

lasso_model_iris.fit(X_train_iris, y_train_iris)
print("Best Alpha (Iris):", lasso_model_iris.best_params_)

lasso_prediction_iris = lasso_model_iris.predict(X_test_iris)

print("R2 Score (Iris):", r2_score(y_test_iris, lasso_prediction_iris))
print("MSE (Iris):", mean_squared_error(y_test_iris, lasso_prediction_iris))


# 
# ElasticNet Regression

elastic_iris = ElasticNet(max_iter=10000)

parameters_iris_elastic = {
    "alpha": [0.001, 0.01, 0.1],
    "l1_ratio": [0.2, 0.5, 0.8]
}

elastic_model_iris = GridSearchCV(
    elastic_iris,
    parameters_iris_elastic,
    cv=5
)

elastic_model_iris.fit(X_train_iris, y_train_iris)
print("Best Parameters (Iris):", elastic_model_iris.best_params_)

elastic_prediction_iris = elastic_model_iris.predict(X_test_iris)

print("R2 Score (Iris):", r2_score(y_test_iris, elastic_prediction_iris))
print("MSE (Iris):", mean_squared_error(y_test_iris, elastic_prediction_iris))

print("--- Conclusion for Iris Dataset ---")
print("\nRidge Regression (Iris):")
print(f"  Best Parameter: {ridge_model_iris.best_params_['alpha']}")
print(f"  R2 Score: {r2_score(y_test_iris, ridge_prediction_iris):.4f}")
print(f"  MSE: {mean_squared_error(y_test_iris, ridge_prediction_iris):.4f}")

print("\nLasso Regression (Iris):")
print(f"  Best Parameter: {lasso_model_iris.best_params_['alpha']}")
print(f"  R2 Score: {r2_score(y_test_iris, lasso_prediction_iris):.4f}")
print(f"  MSE: {mean_squared_error(y_test_iris, lasso_prediction_iris):.4f}")

print("\nElastic Net Regression (Iris):")
print(f"  Best Parameters: {elastic_model_iris.best_params_}")
print(f"  R2 Score: {r2_score(y_test_iris, elastic_prediction_iris):.4f}")
print(f"  MSE: {mean_squared_error(y_test_iris, elastic_prediction_iris):.4f}")
