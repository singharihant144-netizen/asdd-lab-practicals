"""
Sampling Methods
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
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["Species"] = iris.target
df["Species"] = df["Species"].replace({
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
})
display(df.head())

print("Shape of Dataset:", df.shape)
print("\nSpecies Count")
print(df["Species"].value_counts())

random_sample = df.sample(n=30, random_state=42)
display(random_sample)

print("Random Sample Shape:", random_sample.shape)
print(random_sample["Species"].value_counts())

sample, _ = train_test_split(
    df,
    test_size=0.80,
    stratify=df["Species"],
    random_state=42
)

display(sample)

print("Stratified Sample Shape:", sample.shape)
print(sample["Species"].value_counts())

cluster = df[df["Species"] == "Setosa"]
display(cluster)

print("Cluster Sample Shape:", cluster.shape)
print(cluster["Species"].value_counts())

print("Original Dataset :", len(df))
print("Simple Random Sample :", len(random_sample))
print("Stratified Sample :", len(sample))
print("Cluster Sample :", len(cluster))
