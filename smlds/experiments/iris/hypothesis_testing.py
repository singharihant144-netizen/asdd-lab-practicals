"""
Hypothesis Testing (t-test, Chi-square, ANOVA)
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
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
from scipy.stats import f_oneway
from sklearn.datasets import load_breast_cancer


# Iris

import pandas as pd
import seaborn as sns
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
from scipy.stats import f_oneway

df = sns.load_dataset("iris")

display(df.head())

print(df.isnull().sum())

df = df[["sepal_width", "species", "sepal_length"]]

df = df.dropna()

display(df.head())


# INDEPENDENT t-test

setosa_length = df[df["species"] == "setosa"]["sepal_length"]

versicolor_length = df[df["species"] == "versicolor"]["sepal_length"]

t_stat, p_value = ttest_ind(setosa_length, versicolor_length)

print("T-Statistic :", t_stat)

print("P-Value :", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
    print("There is a significant difference in sepal length.")
else:
    print("Fail to Reject the Null Hypothesis")
    print("There is no significant difference in sepal length.")


# Chi Square Test

df["sepal_width_category"] = pd.cut(
    df["sepal_width"],
    bins=[0, 3, 3.5, 10],
    labels=["Low", "Medium", "High"]
)

table = pd.crosstab(df["species"], df["sepal_width_category"])

print(table)

chi2, p_value, dof, expected = chi2_contingency(table)

print("Chi-Square Statistic :", chi2)

print("P-Value :", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
    print("Species and Sepal Width Category are associated.")
else:
    print("Fail to Reject the Null Hypothesis")
    print("Species and Sepal Width Category are independent.")


# One Way ANOVA

setosa = df[df["species"] == "setosa"]["sepal_length"]

versicolor = df[df["species"] == "versicolor"]["sepal_length"]

virginica = df[df["species"] == "virginica"]["sepal_length"]

f_stat, p_value = f_oneway(setosa, versicolor, virginica)

print("F Statistic :", f_stat)

print("P Value :", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
    print("Average sepal length differs among Iris species.")
else:
    print("Fail to Reject the Null Hypothesis")
    print("Average sepal length is the same among Iris species.")

print("Conclusion")

print("1. Independent t-test compared the average sepal length of Setosa and Versicolor.")

print("2. Chi-square test checked the relationship between species and sepal width category.")

print("3. One-Way ANOVA compared the average sepal length across the three Iris species.")

print("4. Decisions were made based on the p-value (0.05 significance level).")
