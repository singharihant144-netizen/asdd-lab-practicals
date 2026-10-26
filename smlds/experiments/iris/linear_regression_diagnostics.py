"""
Linear Regression & Diagnostics
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
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import seaborn as sns


# IRIS DATASET

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = sns.load_dataset("iris")
df = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
df = df.dropna()
print(df.head())

print("\nShape :", df.shape)
print("\nMissing Values")
print(df.isnull().sum())

X = df.drop("sepal_length", axis=1)
y = df["sepal_length"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel Trained Successfully")
y_pred = model.predict(X_test)

print("\nPredicted Values")
print(y_pred[:10])

residuals = y_test - y_pred

plt.figure(figsize=(8,5))
plt.scatter(y_pred, residuals)
plt.axhline(y=0, color="red")
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot - Iris Dataset")
plt.show()

X_vif = sm.add_constant(X)

vif = pd.DataFrame()

vif["Feature"] = X_vif.columns

vif["VIF"] = [
    variance_inflation_factor(X_vif.values, i)
    for i in range(X_vif.shape[1])
]

print("\nVariance Inflation Factor (VIF)")
print(vif)
X_constant = sm.add_constant(X)

ols_model = sm.OLS(y, X_constant).fit()
influence = ols_model.get_influence()

cooks = influence.cooks_distance[0]

print("\nCook's Distance")
print(cooks[:10])

plt.figure(figsize=(10,5))
plt.stem(cooks)
plt.title("Cook's Distance - Iris Dataset")
plt.xlabel("Observation")
plt.ylabel("Cook's Distance")

plt.show()

print("\nOLS Regression Summary")
print(ols_model.summary())

print("\nConclusion")
print("1. A Linear Regression model was built using the Iris dataset.")
print("2. Residuals were plotted to check model errors.")
print("3. VIF was calculated to detect multicollinearity.")
print("4. Cook's Distance was used to identify influential observations.")
