"""
Hypothesis Testing (t-test, Chi-square, ANOVA)
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
import seaborn as sns
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
from scipy.stats import f_oneway
from sklearn.datasets import load_breast_cancer


# BREAST CANCER

data = load_breast_cancer()

df = pd.DataFrame(data.data, columns=data.feature_names)

df["target"] = data.target

display(df.head())

print(df.isnull().sum())

df = df[["mean radius", "mean texture", "target"]]

df = df.dropna()

display(df.head())


# INDEPENDENT t-test

malignant_radius = df[df["target"] == 0]["mean radius"]

benign_radius = df[df["target"] == 1]["mean radius"]

t_stat, p_value = ttest_ind(malignant_radius, benign_radius)

print("T-Statistic :", t_stat)

print("P-Value :", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
    print("There is a significant difference in mean radius.")
else:
    print("Fail to Reject the Null Hypothesis")
    print("There is no significant difference in mean radius.")


# Chi Square Test

df["texture_category"] = pd.cut(
    df["mean texture"],
    bins=[0, 15, 20, 50],
    labels=["Low", "Medium", "High"]
)

table = pd.crosstab(df["target"], df["texture_category"])

print(table)

chi2, p_value, dof, expected = chi2_contingency(table)

print("Chi-Square Statistic :", chi2)

print("P-Value :", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
    print("Diagnosis and Texture Category are associated.")
else:
    print("Fail to Reject the Null Hypothesis")
    print("Diagnosis and Texture Category are independent.")


# One Way ANOVA

low_radius = df[df["mean radius"] < 12]["mean texture"]

medium_radius = df[
    (df["mean radius"] >= 12) &
    (df["mean radius"] < 18)
]["mean texture"]

high_radius = df[df["mean radius"] >= 18]["mean texture"]

f_stat, p_value = f_oneway(
    low_radius,
    medium_radius,
    high_radius
)

print("F Statistic :", f_stat)

print("P Value :", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
    print("Average mean texture differs among radius groups.")
else:
    print("Fail to Reject the Null Hypothesis")
    print("Average mean texture is the same among radius groups.")

print("Conclusion")

print("1. Independent t-test compared the average mean radius of malignant and benign cases.")

print("2. Chi-square test checked the relationship between diagnosis and texture category.")

print("3. One-Way ANOVA compared the average mean texture across different radius groups.")

print("4. Decisions were made based on the p-value (0.05 significance level).")
