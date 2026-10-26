"""
Bootstrap Confidence Intervals & Permutation Test
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
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

import pandas as pd
import seaborn as sns
import numpy as np

df = sns.load_dataset("iris")

df = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]

df = df.dropna()

display(df.head())


# Bootstrap Confidence Interval

bootstrap_means = []

for i in range(1000):
    sample = df["sepal_length"].sample(n=len(df), replace=True)
    bootstrap_means.append(sample.mean())

lower = np.percentile(bootstrap_means, 2.5)
upper = np.percentile(bootstrap_means, 97.5)

print("95% Confidence Interval")
print("Lower Limit:", lower)
print("Upper Limit:", upper)

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.hist(bootstrap_means, bins=20, edgecolor="black")
plt.title("Bootstrap Distribution of Mean Sepal Length")
plt.xlabel("Mean Sepal Length")
plt.ylabel("Frequency")
plt.show()


# Permutation Test

import seaborn as sns
df_with_species = sns.load_dataset("iris")
setosa = df_with_species[df_with_species["species"] == "setosa"]["sepal_length"]
versicolor = df_with_species[df_with_species["species"] == "versicolor"]["sepal_length"]

original_difference = abs(setosa.mean() - versicolor.mean())
print("\nOriginal Difference :", original_difference)

count = 0
combined = df_with_species[
    df_with_species["species"].isin(["setosa", "versicolor"])
]["sepal_length"].to_numpy()
n_setosa = len(setosa)
for _ in range(1000):
    shuffled = np.random.permutation(combined)
    group1 = shuffled[:n_setosa]
    group2 = shuffled[n_setosa:]

    difference = abs(group1.mean() - group2.mean())

    if difference >= original_difference:
        count += 1

p_value = count / 1000

print("P-value :", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
    print("There is a significant difference in sepal length.")
else:
    print("Fail to Reject the Null Hypothesis")
    print("There is no significant difference in sepal length.")
