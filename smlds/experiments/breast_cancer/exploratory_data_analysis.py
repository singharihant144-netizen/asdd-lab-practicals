"""
Exploratory Data Analysis
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

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
breast_cancer = load_breast_cancer()
df = pd.DataFrame(breast_cancer.data , columns= breast_cancer.feature_names)
df["diagnosis"] = breast_cancer.target
df["diagnosis"] = df["diagnosis"].replace({
    0:"M",
    1:"B"})
display(df.head())

print("Shape of Dataset")
print(df.shape)

print("\n First Five Rows")
print(df.head())

print("\nInformation")
print(df.info())

print("Descriptive Statistics")

desc = df.describe().T
desc["Variance"] = df.var(numeric_only=True)
desc["Skewness"] = df.skew(numeric_only=True)
desc["Kurtosis"] = df.kurt(numeric_only=True)

print(desc)

print("Missing Value")
print(df.isnull().sum())

print(df["diagnosis"].value_counts())

df.hist(figsize=(16,16))
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(data=df.iloc[:,0:4])
plt.title("Boxplot")
plt.show()

plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="mean radius",
    y="mean texture",
    hue="diagnosis"
)

plt.show()

correlation = df.iloc[:,0:4].corr()
plt.figure(figsize=(8,6))
sns.heatmap(correlation, annot=True)
plt.title("Correlation Matrix")
plt.show()

sns.pairplot(df, hue="diagnosis")
plt.show()
