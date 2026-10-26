"""
Decision Tree & Random Forest
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

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
iris = load_iris()
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
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


# Decision Tree Classifier

dt_iris = DecisionTreeClassifier(random_state=42)
dt_iris.fit(X_train_iris, y_train_iris)
y_pred_dt_iris = dt_iris.predict(X_test_iris)

print("Decision Tree Accuracy (Iris):", accuracy_score(y_test_iris, y_pred_dt_iris))


# Evaluate Decision Tree

print("Confusion Matrix (Iris - Decision Tree):")
print(confusion_matrix(y_test_iris, y_pred_dt_iris))
print("\nClassification Report (Iris - Decision Tree):")
print(classification_report(y_test_iris, y_pred_dt_iris))


# Random Forest Classifier

rf_iris = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
rf_iris.fit(X_train_iris, y_train_iris)
y_pred_rf_iris = rf_iris.predict(X_test_iris)

print("Random Forest Accuracy (Iris):", accuracy_score(y_test_iris, y_pred_rf_iris))


# Evaluate Random Forest

print("Confusion Matrix (Iris - Random Forest):")
print(confusion_matrix(y_test_iris, y_pred_rf_iris))
print("\nClassification Report (Iris - Random Forest):")
print(classification_report(y_test_iris, y_pred_rf_iris))


# Iris Feature Importance

importance_iris = pd.DataFrame({
    "Feature": X_iris.columns,
    "Importance": rf_iris.feature_importances_
})
importance_iris = importance_iris.sort_values(
    by="Importance",
    ascending=False
)
print("Iris Feature Importance:")
print(importance_iris)


# Plot Iris Feature Importance

plt.figure(figsize=(10, 6))
plt.barh(
    importance_iris["Feature"],
    importance_iris["Importance"]
)
plt.title("Iris Feature Importance")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.gca().invert_yaxis()
plt.show()


# Compare Models

result_iris = pd.DataFrame({
    "Model": ["Decision Tree", "Random Forest"],
    "Accuracy": [
        accuracy_score(y_test_iris, y_pred_dt_iris),
        accuracy_score(y_test_iris, y_pred_rf_iris)
    ]
})
print("Iris Model Comparison:")
display(result_iris)


# Conclusion (Iris Dataset)
# 
# *   Both Decision Tree and Random Forest models achieved perfect accuracy on the Iris dataset, suggesting it's a relatively separable dataset.
# *   Petal length and petal width were identified as the most important features for classifying Iris species.
