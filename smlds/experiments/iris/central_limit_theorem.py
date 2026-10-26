"""
Central Limit Theorem
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
from sklearn.datasets import load_iris
import numpy as np
from sklearn.datasets import load_breast_cancer

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

display(df.head())

data = df["sepal length (cm)"]

print(data.head())

plt.figure(figsize=(8, 5))

plt.hist(data, bins=10, edgecolor="black")

plt.title("Original Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")

plt.show()

data = df["sepal length (cm)"]
sample_means = []
for i in range(1000):
    sample = data.sample(n=30, replace=True)
    sample_means.append(sample.mean())
    print(sample_means [:10])

print(sample_means [:10])

plt.figure(figsize = (8, 5) )
plt.hist(sample_means, bins=20, edgecolor="black")
plt.title("Distribution of Sample Means")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()

print("Population Mean:", data.mean())
print("Sample Mean:", sum(sample_means) / len(sample_means))
