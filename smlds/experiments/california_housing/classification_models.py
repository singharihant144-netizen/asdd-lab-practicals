"""
Classification Models (Logistic Regression, KNN, Naive Bayes)
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

from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()

df_housing = pd.DataFrame(housing.data, columns=housing.feature_names)
df_housing['MedHouseVal'] = housing.target

median_value = df_housing['MedHouseVal'].median()
df_housing['target'] = (df_housing['MedHouseVal'] > median_value).astype(int)

df_housing = df_housing.drop('MedHouseVal', axis=1)

display(df_housing.head())


# Preprocess California Housing Data

X_housing = df_housing.drop('target', axis=1)
y_housing = df_housing['target']

display(X_housing.head())
print("\nCalifornia Housing Data Info after Preprocessing:")
display(df_housing.info())


# Split California Housing Data

X_train_housing, X_test_housing, y_train_housing, y_test_housing = train_test_split(
    X_housing,
    y_housing,
    test_size=0.2,
    random_state=42
)


# Feature Scaling

scaler_housing = StandardScaler()

X_train_housing = scaler_housing.fit_transform(X_train_housing)
X_test_housing = scaler_housing.transform(X_test_housing)


# Logistic Regression

logistic_housing = LogisticRegression(max_iter=200)

logistic_housing.fit(X_train_housing, y_train_housing)

y_pred_log_housing = logistic_housing.predict(X_test_housing)

print("Accuracy (Logistic Regression, California Housing):", accuracy_score(y_test_housing, y_pred_log_housing))
print("Confusion Matrix (Logistic Regression, California Housing):\n", confusion_matrix(y_test_housing, y_pred_log_housing))
print("Classification Report (Logistic Regression, California Housing):\n", classification_report(y_test_housing, y_pred_log_housing))


# K-Nearest Neighbors

knn_housing = KNeighborsClassifier(n_neighbors=5)

knn_housing.fit(X_train_housing, y_train_housing)

y_pred_knn_housing = knn_housing.predict(X_test_housing)

print("Accuracy (KNN, California Housing):", accuracy_score(y_test_housing, y_pred_knn_housing))
print("Confusion Matrix (KNN, California Housing):\n", confusion_matrix(y_test_housing, y_pred_knn_housing))
print("Classification Report (KNN, California Housing):\n", classification_report(y_test_housing, y_pred_knn_housing))


# Naive Bayes

nb_housing = GaussianNB()

nb_housing.fit(X_train_housing, y_train_housing)

y_pred_nb_housing = nb_housing.predict(X_test_housing)

print("Accuracy (Naive Bayes, California Housing):", accuracy_score(y_test_housing, y_pred_nb_housing))
print("Confusion Matrix (Naive Bayes, California Housing):\n", confusion_matrix(y_test_housing, y_pred_nb_housing))
print("Classification Report (Naive Bayes, California Housing):\n", classification_report(y_test_housing, y_pred_nb_housing))


# ROC Curve

log_prob_housing = logistic_housing.predict_proba(X_test_housing)[:, 1]

fpr_housing, tpr_housing, _ = roc_curve(y_test_housing, log_prob_housing)

auc_housing = roc_auc_score(y_test_housing, log_prob_housing)

print("AUC Score (Logistic Regression, California Housing):", auc_housing)

plt.figure(figsize=(8, 5))
plt.plot(fpr_housing, tpr_housing, label=f"Logistic Regression (California Housing) - AUC: {auc_housing:.2f}")
plt.plot([0, 1], [0, 1], linestyle="--", color='grey') # Add a random guess line
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve (California Housing)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


# Compare Models

result_housing = pd.DataFrame({
    "Model": ["Logistic Regression", "KNN", "Naive Bayes"],
    "Accuracy": [
        accuracy_score(y_test_housing, y_pred_log_housing),
        accuracy_score(y_test_housing, y_pred_knn_housing),
        accuracy_score(y_test_housing, y_pred_nb_housing)
    ]
})

print(result_housing)


# Conclusion for California Housing Analysis

print("Conclusion for California Housing Dataset Analysis:")
print("1. Logistic Regression, KNN, and Naive Bayes models were applied to the California Housing dataset after converting it to a binary classification problem.")
print("2. The dataset was preprocessed and features were scaled.")
print("3. The models were evaluated using Accuracy, Confusion Matrix, Classification Report, and ROC Curve.")
print("4. The comparative analysis shows the performance of each model in predicting if a house is 'expensive'.")
