"""
Maximum Likelihood Estimation (MLE)
Dataset : Titanic
Source  : seaborn load_dataset("titanic") (needs internet)

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


# TITANIC DATASET

import pandas as pd
import seaborn as sns
import numpy as np

df_titanic = sns.load_dataset("titanic")

# For normal distribution, let's use 'age'
# For bernoulli distribution, 'survived' is already binary (0 or 1)

# Drop rows with missing 'age' values for normal distribution calculation
df_titanic_age = df_titanic.dropna(subset=["age"])

print("Titanic Dataset Head (Age for Normal Dist.):")
display(df_titanic_age[["age"]].head())

print("\nTitanic Dataset Head (Survived for Bernoulli Dist.):")
display(df_titanic[["survived"]].head())


# MLE for Normal Distribution (Age)

mu_age = df_titanic_age["age"].mean()

print("Estimated Mean (μ) for Age:", mu_age)

sigma_age = df_titanic_age["age"].std(ddof=0)

print("Estimated Standard Deviation (σ) for Age:", sigma_age)

print("Normal Distribution Parameters for Age")
print("Mean (μ):", mu_age)
print("Standard Deviation (σ):", sigma_age)


# MLE for Bernoulli Distribution (Survived)

p_survived = df_titanic["survived"].mean()

print("Estimated Probability (p) of Survival:", p_survived)

print("Probability of Survival :", round(p_survived, 3))

print("Probability of Not Surviving :", round(1 - p_survived, 3))

import matplotlib.pyplot as plt

counts_survived = df_titanic["survived"].value_counts().sort_index()

plt.bar(["Not Survived", "Survived"], counts_survived)

plt.title("Survival Count on Titanic")

plt.xlabel("Status")

plt.ylabel("Number of Passengers")

plt.show()


# Conclusion (Titanic Dataset)
# 
# 1. MLE was used to estimate the parameters of a Normal Distribution.
# 2. The estimated mean (μ) and standard deviation (σ) were calculated using the 'age' column, after handling missing values.
# 3. MLE was also used to estimate the probability of survival for the Bernoulli Distribution.
# 4. The probability was calculated using the average value of the 'survived' column.
