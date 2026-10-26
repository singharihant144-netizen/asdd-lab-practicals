"""
Bootstrap Confidence Intervals & Permutation Test
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


# California Housing Dataset Analysis: Bootstrap Confidence Interval for Median House Value

import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing(as_frame=True)

df = housing.frame

df = df[["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude", "MedHouseVal"]]

df = df.dropna()

df.head()

bootstrap_means = []

for i in range(1000):

    sample = df["MedInc"].sample(n=len(df), replace=True)

    bootstrap_means.append(sample.mean())

lower = np.percentile(bootstrap_means, 2.5)

upper = np.percentile(bootstrap_means, 97.5)

print("95% Confidence Interval")

print("Lower Limit:", lower)

print("Upper Limit:", upper)

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

plt.hist(bootstrap_means, bins=20, edgecolor="black")

plt.title("Bootstrap Distribution of Mean Median Income")

plt.xlabel("Mean Median Income")

plt.ylabel("Frequency")

plt.show()

df_with_occupancy = housing.frame

low_occupancy = df_with_occupancy[
    df_with_occupancy["AveOccup"] < df_with_occupancy["AveOccup"].median()
]["MedInc"]

high_occupancy = df_with_occupancy[
    df_with_occupancy["AveOccup"] >= df_with_occupancy["AveOccup"].median()
]["MedInc"]

original_difference = abs(low_occupancy.mean() - high_occupancy.mean())

print("\nOriginal Difference :", original_difference)

count = 0

combined = pd.concat([low_occupancy, high_occupancy]).to_numpy()

n_low_occupancy = len(low_occupancy)

for _ in range(1000):

    shuffled = np.random.permutation(combined)

    group1 = shuffled[:n_low_occupancy]

    group2 = shuffled[n_low_occupancy:]

    difference = abs(group1.mean() - group2.mean())

    if difference >= original_difference:

        count += 1

p_value = count / 1000

print("P-value :", p_value)

if p_value < 0.05:

    print("Reject the Null Hypothesis")

    print("There is a significant difference in median income between the two occupancy groups.")

else:

    print("Fail to Reject the Null Hypothesis")

    print("There is no significant difference in median income between the two occupancy groups.")

print("\nConclusion")

print("1. Bootstrap sampling was used to estimate the confidence interval of the mean median income.")

print("2. A 95% confidence interval was obtained from 1000 bootstrap samples.")

print("3. A permutation test was performed to compare the mean median income of low and high occupancy groups.")

print("4. The hypothesis was accepted or rejected based on the p-value.")
