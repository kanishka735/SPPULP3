
# Experiment 5: K-Means and Agglomerative Hierarchical Clustering
#
# Problem Statement:
# Apply K-Means and Agglomerative Hierarchical Clustering
# on sales_data_sample.csv to group similar data points.
#
# If CSV is unavailable, generate a sample dataset.
#
# Tasks:
# 1. Load or generate dataset.
# 2. Perform data preprocessing.
# 3. Apply feature scaling.
# 4. Find optimal number of clusters using Silhouette Score.
# 5. Implement K-Means clustering.
# 6. Implement Agglomerative Hierarchical Clustering.
# 7. Visualize and compare both algorithms.


# --------------------------------------------------
# Step 1: Import Required Libraries
# --------------------------------------------------

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Used to standardize numerical features
from sklearn.preprocessing import StandardScaler

# Import clustering algorithms
from sklearn.cluster import KMeans, AgglomerativeClustering

# Used to evaluate clustering performance
from sklearn.metrics import silhouette_score

# Used to reduce dimensions for visualization
from sklearn.decomposition import PCA


# --------------------------------------------------
# Step 2: Load or Generate Dataset
# --------------------------------------------------

# Theory:
# A dataset contains numerical information about sales.
# We use numerical features to identify similar groups.
#
# If CSV file exists, load it.
# Otherwise, generate a synthetic dataset.

if os.path.exists("sales_data_sample.csv"):

    # Load sales dataset
    df = pd.read_csv("sales_data_sample.csv")

    # Select only numerical columns
    numeric = df.select_dtypes(
        include=np.number
    )

    # Remove columns containing only missing values
    numeric = numeric.dropna(axis=1, how="all")

    # Fill remaining missing values with 0
    numeric = numeric.fillna(0)

    print("Sales dataset loaded successfully!")

else:

    # Generate synthetic sales dataset
    rng = np.random.default_rng(12)

    # Generate three different customer groups
    # Each group has different spending and order patterns.

    data = np.vstack([
        rng.normal([20, 30], [4, 5], (80, 2)),
        rng.normal([60, 70], [5, 4], (80, 2)),
        rng.normal([90, 20], [4, 5], (80, 2))
    ])

    # Create DataFrame
    numeric = pd.DataFrame(
        data,
        columns=["Annual_Spend", "Orders"]
    )

    print("Synthetic sales dataset generated!")


# Display dataset
print("\nDataset Preview:")
print(numeric.head())

print("\nDataset Shape:", numeric.shape)


# --------------------------------------------------
# Step 3: Data Preprocessing
# --------------------------------------------------

# Theory:
# Data preprocessing prepares the dataset
# before applying clustering algorithms.
#
# Steps:
# 1. Select numerical features.
# 2. Remove invalid values.
# 3. Handle missing values.
#
# Clustering algorithms work with numerical data.

# Replace infinite values with missing values
numeric = numeric.replace(
    [np.inf, -np.inf], np.nan
)

# Fill missing values using column median
numeric = numeric.fillna(numeric.median())

# Remove columns with zero variance
numeric = numeric.loc[:, numeric.nunique() > 1]

# Check whether at least two features are available
if numeric.shape[1] < 2:
    raise ValueError(
        "Dataset must contain at least two numeric columns."
    )

# Remove rows with invalid values
numeric = numeric.dropna()

print("\nPreprocessed Dataset:")
print(numeric.head())


# --------------------------------------------------
# Step 4: Feature Scaling using StandardScaler
# --------------------------------------------------

# Theory:
# StandardScaler converts features into a common scale.
#
# Formula:
#
# Z = (X - Mean) / Standard Deviation
#
# Where:
# X = Original value
# Mean = Average of feature values
# Standard Deviation = Spread of values
#
# Scaling is important because clustering algorithms
# use distance calculations.
#
# Without scaling, features with larger values
# may dominate the clustering process.

scaler = StandardScaler()

# Transform numerical data
X = scaler.fit_transform(numeric)

print("\nFeature scaling completed!")


# --------------------------------------------------
# Step 5: Find Optimal Number of Clusters
# --------------------------------------------------

# Theory:
# A cluster is a group of similar data points.
#
# Silhouette Score measures how well data points
# are grouped into clusters.
#
# Formula:
#
# S = (b - a) / max(a, b)
#
# Where:
# a = Average distance within the same cluster
# b = Average distance to the nearest other cluster
#
# Range:
# +1 = Good clustering
#  0 = Overlapping clusters
# -1 = Incorrect clustering
#
# Higher Silhouette Score indicates better clustering.

scores = []

# Test different values of K from 2 to 7
for k in range(2, 8):

    # Apply K-Means for each K
    labels = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    ).fit_predict(X)

    # Calculate Silhouette Score
    score = silhouette_score(X, labels)

    # Store K and its score
    scores.append((k, score))

# Select K having the highest Silhouette Score
best_k = max(scores, key=lambda z: z[1])[0]

print("\nSilhouette Scores:", scores)

print("\nSelected Number of Clusters:", best_k)


# --------------------------------------------------
# Step 6: K-Means Clustering
# --------------------------------------------------

# THEORY: K-MEANS CLUSTERING
#
# K-Means is an unsupervised machine learning algorithm.
# It divides data points into K different clusters.
#
# Working:
# 1. Select K initial centroids.
# 2. Assign each point to the nearest centroid.
# 3. Calculate new cluster centroids.
# 4. Repeat until centroids stop changing significantly.
#
# Euclidean Distance Formula:
#
# d = sqrt((x1-y1)^2 + (x2-y2)^2)
#
# Centroid Formula:
#
# C = (1/n) * Sum(Xi)
#
# Where:
# C = Cluster centroid
# Xi = Data points in the cluster
# n = Number of data points
#
# K-Means minimizes the Within-Cluster Sum of Squares
# (WCSS), also called inertia.

# Create and train K-Means model
kmeans = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=10
)

# Assign cluster labels
km = kmeans.fit_predict(X)

print("\nK-Means Clustering Completed!")

print("K-Means Silhouette Score:",
      round(silhouette_score(X, km), 3))


# --------------------------------------------------
# Step 7: Agglomerative Hierarchical Clustering
# --------------------------------------------------

# THEORY: HIERARCHICAL CLUSTERING
#
# Hierarchical clustering groups similar data points
# into a hierarchy of clusters.
#
# Agglomerative clustering follows a bottom-up approach.
#
# Working:
# 1. Initially, every data point is a separate cluster.
# 2. Find the two nearest clusters.
# 3. Merge them into one cluster.
# 4. Repeat until the required number of clusters
#    is obtained.
#
# Distance Formula:
#
# d = sqrt((x1-y1)^2 + (x2-y2)^2)
#
# It uses a linkage method to calculate distance
# between clusters.
#
# Here, Ward linkage is used.
# It merges clusters while minimizing the increase
# in within-cluster variance.

# Create Agglomerative model
hc_model = AgglomerativeClustering(
    n_clusters=best_k,
    linkage="ward"
)

# Assign hierarchical cluster labels
hc = hc_model.fit_predict(X)

print("\nHierarchical Clustering Completed!")

print("Hierarchical Silhouette Score:",
      round(silhouette_score(X, hc), 3))


# --------------------------------------------------
# Step 8: Dimensionality Reduction using PCA
# --------------------------------------------------

# Theory:
# PCA stands for Principal Component Analysis.
#
# It is a dimensionality reduction technique.
# It converts high-dimensional data into fewer
# dimensions while preserving as much variance as possible.
#
# In this project, PCA converts the dataset into
# two dimensions for visualization.
#
# These two components are called:
# PC1 = First Principal Component
# PC2 = Second Principal Component

pca = PCA(n_components=2)

# Convert data into two dimensions
coords = pca.fit_transform(X)


# --------------------------------------------------
# Step 9: Visualize Clustering Results
# --------------------------------------------------

# Create two plots side by side
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Plot K-Means clusters
axes[0].scatter(
    coords[:, 0],
    coords[:, 1],
    c=km
)

axes[0].set_title("K-Means Clustering")
axes[0].set_xlabel("Principal Component 1")
axes[0].set_ylabel("Principal Component 2")


# Plot Hierarchical clusters
axes[1].scatter(
    coords[:, 0],
    coords[:, 1],
    c=hc
)

axes[1].set_title("Hierarchical Clustering")
axes[1].set_xlabel("Principal Component 1")
axes[1].set_ylabel("Principal Component 2")


# Adjust spacing between plots
plt.tight_layout()

# Save clustering visualization
plt.savefig("clustering_result.png", dpi=150)

# Display plots
plt.show()


# --------------------------------------------------
# Step 10: Final Result
# --------------------------------------------------

print("\nClustering Completed Successfully!")

print("Number of Clusters:", best_k)

print("K-Means Score:",
      round(silhouette_score(X, km), 3))

print("Hierarchical Score:",
      round(silhouette_score(X, hc), 3))
