"""
PCA + Clustering
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
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage

# Load data
iris = load_iris()
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)
print(df.head())

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(df)

pca_df = pd.DataFrame(
    X_pca,
    columns=["PC1", "PC2"]
)
print(pca_df.head())

# PCA scatter plot
plt.figure(figsize=(8,6))
plt.scatter(
    pca_df["PC1"],
    pca_df["PC2"]
)
plt.title("PCA of Iris Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()

# K-Means Clustering
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)
clusters = kmeans.fit_predict(pca_df)
pca_df["Cluster"] = clusters
print(pca_df.head())

# K-Means plot
plt.figure(figsize=(8,6))
plt.scatter(
    pca_df["PC1"],
    pca_df["PC2"],
    c=pca_df["Cluster"]
)
plt.title("K-Means Clustering")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()

# Hierarchical Clustering
linked = linkage(
    pca_df[["PC1", "PC2"]],
    method="ward"
)

plt.figure(figsize=(10,5))
dendrogram(linked)
plt.title("Hierarchical Clustering")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()

# Explained Variance
print("Explained Variance Ratio")
print(pca.explained_variance_ratio_)

print("Conclusion")
print("1. PCA reduced the dataset from 4 features to 2 principal components.")
print("2. K-Means grouped the data into 3 clusters.")
print("3. Hierarchical Clustering was visualized using a dendrogram.")
print("4. PCA helps simplify high-dimensional data while preserving important information.")
