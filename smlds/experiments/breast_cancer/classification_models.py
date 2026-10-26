"""
Classification Models (Logistic Regression, KNN, Naive Bayes)
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

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelBinarizer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, roc_auc_score
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelBinarizer
from sklearn.datasets import fetch_california_housing
from sklearn.datasets import load_breast_cancer

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

df_cancer = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df_cancer["target"] = cancer.target

display(df_cancer.head())

X_cancer = df_cancer.drop("target", axis=1)
y_cancer = df_cancer["target"]

X_train_cancer, X_test_cancer, y_train_cancer, y_test_cancer = train_test_split(
    X_cancer,
    y_cancer,
    test_size=0.2,
    random_state=42
)

scaler_cancer = StandardScaler()

X_train_cancer = scaler_cancer.fit_transform(X_train_cancer)
X_test_cancer = scaler_cancer.transform(X_test_cancer)


# Logistic Regression

logistic_cancer = LogisticRegression(max_iter=100)

logistic_cancer.fit(X_train_cancer, y_train_cancer)

y_pred_log_cancer = logistic_cancer.predict(X_test_cancer)

print("Accuracy (Logistic Regression, Breast Cancer):", accuracy_score(y_test_cancer, y_pred_log_cancer))
print("Confusion Matrix (Logistic Regression, Breast Cancer):\n", confusion_matrix(y_test_cancer, y_pred_log_cancer))
print("Classification Report (Logistic Regression, Breast Cancer):\n", classification_report(y_test_cancer, y_pred_log_cancer))


# K-Nearest Neighbors

knn_cancer = KNeighborsClassifier(n_neighbors=5)

knn_cancer.fit(X_train_cancer, y_train_cancer)

y_pred_knn_cancer = knn_cancer.predict(X_test_cancer)

print("Accuracy (KNN, Breast Cancer):", accuracy_score(y_test_cancer, y_pred_knn_cancer))
print("Confusion Matrix (KNN, Breast Cancer):\n", confusion_matrix(y_test_cancer, y_pred_knn_cancer))
print("Classification Report (KNN, Breast Cancer):\n", classification_report(y_test_cancer, y_pred_knn_cancer))


# Naive Bayes

nb_cancer = GaussianNB()

nb_cancer.fit(X_train_cancer, y_train_cancer)

y_pred_nb_cancer = nb_cancer.predict(X_test_cancer)

print("Accuracy (Naive Bayes, Breast Cancer):", accuracy_score(y_test_cancer, y_pred_nb_cancer))
print("Confusion Matrix (Naive Bayes, Breast Cancer):\n", confusion_matrix(y_test_cancer, y_pred_nb_cancer))
print("Classification Report (Naive Bayes, Breast Cancer):\n", classification_report(y_test_cancer, y_pred_nb_cancer))


# ROC Curve

log_prob_cancer = logistic_cancer.predict_proba(X_test_cancer)[:, 1]

fpr_cancer, tpr_cancer, _ = roc_curve(y_test_cancer, log_prob_cancer)

auc_cancer = roc_auc_score(y_test_cancer, log_prob_cancer)

print("AUC Score (Logistic Regression, Breast Cancer):", auc_cancer)

plt.figure(figsize=(8, 5))
plt.plot(fpr_cancer, tpr_cancer, label=f"Logistic Regression (Breast Cancer) - AUC: {auc_cancer:.2f}")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve (Breast Cancer)")
plt.legend()
plt.show()


# Compare Models

result_cancer = pd.DataFrame({
    "Model": ["Logistic Regression", "KNN", "Naive Bayes"],
    "Accuracy": [
        accuracy_score(y_test_cancer, y_pred_log_cancer),
        accuracy_score(y_test_cancer, y_pred_knn_cancer),
        accuracy_score(y_test_cancer, y_pred_nb_cancer)
    ]
})

print(result_cancer)

print("Conclusion for Breast Cancer Dataset Analysis:")
print("1. Logistic Regression, KNN, and Naive Bayes models were applied to the Breast Cancer dataset.")
print("2. The models were evaluated using Accuracy, Confusion Matrix, Classification Report, and ROC Curve.")
print("3. The comparative analysis shows the performance of each model in predicting malignancy.")
