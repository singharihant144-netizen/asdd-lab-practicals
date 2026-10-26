"""
Maximum Likelihood Estimation (MLE)
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

df = sns.load_dataset("iris")

df["setosa"] = (df["species"] == "setosa").astype(int)

df = df[["sepal_length", "setosa"]]

df = df.dropna()

display(df.head())


# MLE for Normal Distribution

sigma = df["sepal_length"].std(ddof=0)

print("Estimated Standard Deviation (σ):", sigma)

sigma = df["sepal_length"].std(ddof=0)

print("Estimated Standard Deviation (σ):", sigma)

mu = df["sepal_length"].mean()
print("Normal Distribution Parameters")
print("Mean (μ):", mu)
print("Standard Deviation (σ):", sigma)


# MLE for Bernoulli Distribution

p = df["setosa"].mean()

print("Estimated Probability (p):", p)

print("Probability of Setosa :", round(p, 3))

print("Probability of Not Setosa :", round(1 - p, 3))

import matplotlib.pyplot as plt

counts = df["setosa"].value_counts().sort_index()

plt.bar(["Not Setosa", "Setosa"], counts)

plt.title("Setosa Count")

plt.xlabel("Status")

plt.ylabel("Number of Flowers")

plt.show()

print("Conclusion")

print("1. MLE was used to estimate the parameters of a Normal Distribution.")
print("2. The estimated mean (μ) and standard deviation (σ) were calculated using the Sepal Length column.")
print("3. MLE was also used to estimate the probability of Setosa for the Bernoulli Distribution.")
print("4. The probability was calculated using the average value of the Setosa column.")
