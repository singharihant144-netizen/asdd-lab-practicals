"""
Bootstrap Confidence Intervals & Permutation Test
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

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic_df = sns.load_dataset("titanic")

# Select the 'age' column and drop NaN values for bootstrap analysis
titanic_age = titanic_df["age"].dropna()
print("Titanic Age data info:")
titanic_age.info()
print("\nFirst 5 rows of Titanic Age data:")
display(titanic_age.head())


# Bootstrap Confidence Interval for Mean Age

bootstrap_means_age = []

for i in range(1000):
    sample = titanic_age.sample(n=len(titanic_age), replace=True)
    bootstrap_means_age.append(sample.mean())

lower_age = np.percentile(bootstrap_means_age, 2.5)
upper_age = np.percentile(bootstrap_means_age, 97.5)

print("95% Confidence Interval for Mean Age")
print("Lower Limit:", lower_age)
print("Upper Limit:", upper_age)

plt.figure(figsize=(8,5))
plt.hist(bootstrap_means_age, bins=20, edgecolor="black")
plt.title("Bootstrap Distribution of Mean Age on Titanic")
plt.xlabel("Mean Age")
plt.ylabel("Frequency")
plt.show()


# Titanic Dataset Analysis: Permutation Test for Fare based on Survival

survived_fare = titanic_df[titanic_df["survived"] == 1]["fare"]
not_survived_fare = titanic_df[titanic_df["survived"] == 0]["fare"]
original_difference_fare = abs(survived_fare.mean() - not_survived_fare.mean())
print("\nOriginal Difference in Fare (Survived vs Not Survived) :", original_difference_fare)

count_fare = 0
combined_fares = pd.concat([survived_fare, not_survived_fare]).to_numpy()
n_survived = len(survived_fare)
for _ in range(1000):
    shuffled = np.random.permutation(combined_fares)
    group1_perm = shuffled[:n_survived]
    group2_perm = shuffled[n_survived:]

    difference_perm = abs(group1_perm.mean() - group2_perm.mean())

    if difference_perm >= original_difference_fare:
        count_fare += 1

p_value_fare = count_fare / 1000

print("P-value (Fare difference) :", p_value_fare)

if p_value_fare < 0.05:
    print("Reject the Null Hypothesis")
    print("There is a significant difference in fare between survived and not survived passengers.")
else:
    print("Fail to Reject the Null Hypothesis")
    print("There is no significant difference in fare between survived and not survived passengers.")
