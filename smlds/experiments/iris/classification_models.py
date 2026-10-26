"""
Classification Models (Logistic Regression, KNN, Naive Bayes)
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

from sklearn.datasets import load_iris

iris = load_iris()
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
df_iris["target"] = iris.target

display(df_iris.head())

X_iris = df_iris.drop("target", axis=1)
y_iris = df_iris["target"]

X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(
    X_iris,
    y_iris,
    test_size=0.2,
    random_state=42
)


# Feature Scaling

scaler_iris = StandardScaler()

X_train_iris = scaler_iris.fit_transform(X_train_iris)
X_test_iris = scaler_iris.transform(X_test_iris)


# Logistic Regression

logistic_iris = LogisticRegression(max_iter=100)

logistic_iris.fit(X_train_iris, y_train_iris)

y_pred_log_iris = logistic_iris.predict(X_test_iris)

print("Accuracy (Logistic Regression, Iris):", accuracy_score(y_test_iris, y_pred_log_iris))
print("Confusion Matrix (Logistic Regression, Iris):\n", confusion_matrix(y_test_iris, y_pred_log_iris))
print("Classification Report (Logistic Regression, Iris):\n", classification_report(y_test_iris, y_pred_log_iris))


# K-Nearest Neighbors

knn_iris = KNeighborsClassifier(n_neighbors=5)

knn_iris.fit(X_train_iris, y_train_iris)

y_pred_knn_iris = knn_iris.predict(X_test_iris)

print("Accuracy (KNN, Iris):", accuracy_score(y_test_iris, y_pred_knn_iris))
print("Confusion Matrix (KNN, Iris):\n", confusion_matrix(y_test_iris, y_pred_knn_iris))
print("Classification Report (KNN, Iris):\n", classification_report(y_test_iris, y_pred_knn_iris))


# Naive Bayes

nb_iris = GaussianNB()

nb_iris.fit(X_train_iris, y_train_iris)

y_pred_nb_iris = nb_iris.predict(X_test_iris)

print("Accuracy (Naive Bayes, Iris):", accuracy_score(y_test_iris, y_pred_nb_iris))
print("Confusion Matrix (Naive Bayes, Iris):\n", confusion_matrix(y_test_iris, y_pred_nb_iris))
print("Classification Report (Naive Bayes, Iris):\n", classification_report(y_test_iris, y_pred_nb_iris))


# ROC Curve

from sklearn.preprocessing import LabelBinarizer

label_binarizer = LabelBinarizer().fit(y_train_iris)
y_test_binarized = label_binarizer.transform(y_test_iris)

log_prob_iris = logistic_iris.predict_proba(X_test_iris)

fpr_iris, tpr_iris, _ = roc_curve(y_test_binarized[:, 0], log_prob_iris[:, 0])
auc_iris = roc_auc_score(y_test_binarized[:, 0], log_prob_iris[:, 0])

print("AUC Score (Logistic Regression, Iris - Class 0 vs Rest):", auc_iris)

plt.figure(figsize=(8, 5))
plt.plot(fpr_iris, tpr_iris, label=f"Logistic Regression (Class 0) - AUC: {auc_iris:.2f}")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve (Iris - Class 0 vs Rest)")
plt.legend()
plt.show()


# Compare Models

result_iris = pd.DataFrame({
    "Model": ["Logistic Regression", "KNN", "Naive Bayes"],
    "Accuracy": [
        accuracy_score(y_test_iris, y_pred_log_iris),
        accuracy_score(y_test_iris, y_pred_knn_iris),
        accuracy_score(y_test_iris, y_pred_nb_iris)
    ]
})

print(result_iris)

print("Conclusion for Iris Dataset Analysis:")
print("1. Logistic Regression, KNN, and Naive Bayes models were applied to the Iris dataset.")
print("2. The models were evaluated using Accuracy, Confusion Matrix, and Classification Report.")
print("3. For the multi-class Iris dataset, a one-vs-rest ROC curve was plotted for Class 0 using Logistic Regression.")
print("4. The comparison of models showed their respective accuracies on the Iris dataset.")
