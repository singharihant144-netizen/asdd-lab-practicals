"""
Decision Tree & Random Forest
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

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

import seaborn as sns

# Load Dataset
df_titanic = sns.load_dataset('titanic')
display(df_titanic.head())


# Preprocess Titanic Dataset

from sklearn.preprocessing import LabelEncoder


df_titanic = df_titanic.drop(['pclass', 'name', 'ticket', 'cabin', 'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone'], axis=1, errors='ignore')

df_titanic['age'].fillna(df_titanic['age'].median(), inplace=True)

le = LabelEncoder()
df_titanic['sex'] = le.fit_transform(df_titanic['sex'])

X_titanic = df_titanic.drop('survived', axis=1)
y_titanic = df_titanic['survived']

print("Processed Features (first 5 rows):")
display(X_titanic.head())
print("Target (first 5 rows):")
display(y_titanic.head())

X_train_titanic, X_test_titanic, y_train_titanic, y_test_titanic = train_test_split(
    X_titanic,
    y_titanic,
    test_size=0.2,
    random_state=42
)


# Decision Tree Classifier

dt_titanic = DecisionTreeClassifier(random_state=42)
dt_titanic.fit(X_train_titanic, y_train_titanic)
y_pred_dt_titanic = dt_titanic.predict(X_test_titanic)

print("Decision Tree Accuracy (Titanic):", accuracy_score(y_test_titanic, y_pred_dt_titanic))


# Evaluate Decision Tree

print("Confusion Matrix (Titanic - Decision Tree):")
print(confusion_matrix(y_test_titanic, y_pred_dt_titanic))
print("\nClassification Report (Titanic - Decision Tree):")
print(classification_report(y_test_titanic, y_pred_dt_titanic))


# Random Forest Classifier

rf_titanic = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
rf_titanic.fit(X_train_titanic, y_train_titanic)
y_pred_rf_titanic = rf_titanic.predict(X_test_titanic)

print("Random Forest Accuracy (Titanic):", accuracy_score(y_test_titanic, y_pred_rf_titanic))


# Evaluate Random Forest

print("Confusion Matrix (Titanic - Random Forest):")
print(confusion_matrix(y_test_titanic, y_pred_rf_titanic))
print("\nClassification Report (Titanic - Random Forest):")
print(classification_report(y_test_titanic, y_pred_rf_titanic))


# Titanic Feature Importance

importance_titanic = pd.DataFrame({
    "Feature": X_titanic.columns,
    "Importance": rf_titanic.feature_importances_
})
importance_titanic = importance_titanic.sort_values(
    by="Importance",
    ascending=False
)
print("Titanic Feature Importance:")
print(importance_titanic)


# Plot Titanic Feature Importance

plt.figure(figsize=(10, 6))
plt.barh(
    importance_titanic["Feature"],
    importance_titanic["Importance"]
)
plt.title("Titanic Feature Importance")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.gca().invert_yaxis()
plt.show()


# Compare Models

result_titanic = pd.DataFrame({
    "Model": ["Decision Tree", "Random Forest"],
    "Accuracy": [
        accuracy_score(y_test_titanic, y_pred_dt_titanic),
        accuracy_score(y_test_titanic, y_pred_rf_titanic)
    ],
})
print("Titanic Model Comparison:")
display(result_titanic)


# Conclusion (Titanic Dataset)
# 
# *   The Random Forest classifier showed slightly better accuracy (approx. 79.33%) compared to the Decision Tree (approx. 77.10%) for predicting survival on the Titanic dataset.
# *   Feature importance analysis indicated that 'fare', 'sex', and 'age' were the most influential factors in predicting survival.
# *   Preprocessing steps included handling missing age values and encoding the 'sex' column.
