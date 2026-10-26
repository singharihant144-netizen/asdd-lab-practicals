"""
Data Preprocessing
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
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Load Breast Cancer dataset
breast_cancer = load_breast_cancer()

# Create DataFrame
df = pd.DataFrame(
    breast_cancer.data,
    columns=breast_cancer.feature_names
)

# Add target column
df['target'] = breast_cancer.target

# Convert target values to class names
df['target'] = df['target'].map({
    0: 'malignant',
    1: 'benign'
})

# Display first 5 rows
print(df.head())

# Introduce missing values
df.loc[5, "mean radius"] = None
df.loc[20, "mean texture"] = None
df.loc[100, "mean smoothness"] = None

# Display first 25 rows
display(df.head(25))

print(df.isnull().sum())

df.fillna(df.median(numeric_only=True), inplace=True)
print(df.isnull().sum())

encoder = LabelEncoder()
df["target"] = encoder.fit_transform(df["target"])
display(df.head())

scaler = StandardScaler()
columns = df.columns[:-1]
df[columns] = scaler.fit_transform(df[columns])
display(df.head())

plt.figure(figsize=(10, 6))
sns.boxplot(data=df.iloc[:, :4])

plt.title("Boxplot for Outlier Detection (Breast Cancer Dataset)")
plt.xlabel("Features")
plt.ylabel("Standardized Values")

plt.show()

Q1 = df.iloc[:, :4].quantile(0.25)
Q3 = df.iloc[:, :4].quantile(0.75)
IQR = Q3 - Q1
outliers = ((df.iloc[:, :4] < (Q1 - 1.5 * IQR)) |
            (df.iloc[:, :4] > (Q3 + 1.5 * IQR)))
print(outliers.sum())

display(df.head())
