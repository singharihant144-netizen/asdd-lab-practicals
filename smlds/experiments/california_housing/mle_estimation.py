"""
Maximum Likelihood Estimation (MLE)
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
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing


# CALIFORNIA HOUSING

from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing(as_frame=True)

df = housing.frame

df["high_value"] = (df["MedHouseVal"] >= df["MedHouseVal"].median()).astype(int)

df = df[["MedInc", "high_value"]]

df = df.dropna()

display(df.head())


# MLE for Normal Distribution

mu = df["MedInc"].mean()

print("Estimated Mean (μ):", mu)

sigma = df["MedInc"].std(ddof=0)

print("Estimated Standard Deviation (σ):", sigma)

print("Normal Distribution Parameters")
print("Mean (μ):", mu)
print("Standard Deviation (σ):", sigma)


# MLE for Bernoulli Distribution

p = df["high_value"].mean()

print("Estimated Probability (p):", p)

print("Probability of High Value :", round(p, 3))

print("Probability of Low Value :", round(1 - p, 3))

import matplotlib.pyplot as plt

counts = df["high_value"].value_counts().sort_index()

plt.bar(["Low Value", "High Value"], counts)

plt.title("Housing Value Count")

plt.xlabel("Status")

plt.ylabel("Number of Houses")

plt.show()

print("Conclusion")

print("1. MLE was used to estimate the parameters of a Normal Distribution.")
print("2. The estimated mean (μ) and standard deviation (σ) were calculated using the MedInc column.")
print("3. MLE was also used to estimate the probability of high-value houses for the Bernoulli Distribution.")
print("4. The probability was calculated using the average value of the High Value column.")
