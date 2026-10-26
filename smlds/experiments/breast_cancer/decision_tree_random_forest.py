"""
Decision Tree & Random Forest
Dataset : Breast Cancer
Source  : sklearn built-in (load_breast_cancer)

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

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
cancer = load_breast_cancer()
df_cancer = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df_cancer["Target"] = cancer.target

display(df_cancer.head())

X_cancer = df_cancer.drop("Target", axis=1)
y_cancer = df_cancer["Target"]

X_train_cancer, X_test_cancer, y_train_cancer, y_test_cancer = train_test_split(
    X_cancer,
    y_cancer,
    test_size=0.2,
    random_state=42
)


# Decision Tree Classifier

dt_cancer = DecisionTreeClassifier(random_state=42)
dt_cancer.fit(X_train_cancer, y_train_cancer)
y_pred_dt_cancer = dt_cancer.predict(X_test_cancer)

print("Decision Tree Accuracy (Breast Cancer):", accuracy_score(y_test_cancer, y_pred_dt_cancer))


# Evaluate Decision Tree

print("Confusion Matrix (Breast Cancer - Decision Tree):")
print(confusion_matrix(y_test_cancer, y_pred_dt_cancer))
print("\nClassification Report (Breast Cancer - Decision Tree):")
print(classification_report(y_test_cancer, y_pred_dt_cancer))


# Random Forest Classifier

rf_cancer = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
rf_cancer.fit(X_train_cancer, y_train_cancer)
y_pred_rf_cancer = rf_cancer.predict(X_test_cancer)

print("Random Forest Accuracy (Breast Cancer):", accuracy_score(y_test_cancer, y_pred_rf_cancer))


# Evaluate Random Forest

print("Confusion Matrix (Breast Cancer - Random Forest):")
print(confusion_matrix(y_test_cancer, y_pred_rf_cancer))
print("\nClassification Report (Breast Cancer - Random Forest):")
print(classification_report(y_test_cancer, y_pred_rf_cancer))


# Breast Cancer Feature Importance

importance_cancer = pd.DataFrame({
    "Feature": X_cancer.columns,
    "Importance": rf_cancer.feature_importances_
})
importance_cancer = importance_cancer.sort_values(
    by="Importance",
    ascending=False
)
print("Breast Cancer Feature Importance:")
print(importance_cancer)

plt.figure(figsize=(10, 8))
plt.barh(
    importance_cancer["Feature"],
    importance_cancer["Importance"]
)
plt.title("Breast Cancer Feature Importance")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.gca().invert_yaxis()
plt.show()

result_cancer = pd.DataFrame({
    "Model": ["Decision Tree", "Random Forest"],
    "Accuracy": [
        accuracy_score(y_test_cancer, y_pred_dt_cancer),
        accuracy_score(y_test_cancer, y_pred_rf_cancer)
    ]
})
print("Breast Cancer Model Comparison:")
display(result_cancer)


# Conclusion (Breast Cancer Dataset)
# 
# *   The Random Forest model generally performed slightly better than the Decision Tree model on the Breast Cancer dataset.
# *   Both models achieved high accuracy, precision, recall, and F1-scores, indicating good performance in classifying benign and malignant tumors.
# *   Key features like 'worst area', 'worst concave points', and 'mean concave points' were identified as highly important for classification.
