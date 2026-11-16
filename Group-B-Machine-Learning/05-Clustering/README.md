# Practical 5: K-Means & Agglomerative Hierarchical Clustering

## Objective
Apply unsupervised machine learning algorithms (K-Means Clustering and Agglomerative Hierarchical Clustering) on sales transaction data (`sales_data_sample.csv`) to segment customers and transactions based on purchasing behavior.

---

## Theory & Algorithms

### 1. K-Means Clustering (Partitioning Approach)
- Partitions $N$ observations into $K$ distinct non-overlapping clusters.
- Iteratively computes cluster centroids and minimizes Within-Cluster Sum of Squares (WCSS / Inertia).
- Uses the **Elbow Method** and **Silhouette Score** to determine optimal $K$.

### 2. Agglomerative Hierarchical Clustering (Hierarchical Approach)
- Bottom-up clustering where each data point starts in its own single-element cluster.
- Pairs of clusters are successively merged based on linkage criteria (Ward's linkage minimizing variance).

---

## Files in this Directory
- `clustering.py` / `05_kmeans_hierach.py`: Complete Python script for K-Means and Hierarchical Clustering.
- `clustering.ipynb` / `05_kmeans_hierarchical_clustering.ipynb`: Jupyter notebook with matplotlib/seaborn cluster scatter plots.
- `sales_data_sample.csv`: Retail and sales transactional dataset containing order quantities, sales values, price each, and product codes.

---

## How to Run

### Command Line
```bash
cd Group-B-Machine-Learning/05-Clustering
python clustering.py
```

### Jupyter Notebook
```bash
jupyter notebook clustering.ipynb
```
