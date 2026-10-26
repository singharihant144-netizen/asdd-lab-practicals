"""
Central Limit Theorem
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
from sklearn.datasets import load_iris
import numpy as np
from sklearn.datasets import load_breast_cancer


# Breast Cancer

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

df = pd.DataFrame(cancer.data, columns=cancer.feature_names)

print(df.head())

data = df["mean radius"]

plt.figure(figsize=(8,5))
plt.hist(data, bins=10, edgecolor="black")
plt.title("Original Distribution of Mean Radius")
plt.xlabel("Mean Radius")
plt.ylabel("Frequency")
plt.show()

sample_means = []

for i in range(1000):
    sample = np.random.choice(data, size=30, replace=True)
    sample_means.append(np.mean(sample))

plt.figure(figsize=(8,5))
plt.hist(sample_means, bins=20, edgecolor="black")
plt.title("Distribution of Sample Means (n=30)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()

print("Original Mean:", np.mean(data))
print("Mean of Sample Means:", np.mean(sample_means))

print("Original Standard Deviation:", np.std(data))
print("Standard Deviation of Sample Means:", np.std(sample_means))
