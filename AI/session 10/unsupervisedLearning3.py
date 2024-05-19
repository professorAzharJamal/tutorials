import numpy as np #pip install numpy
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris #pip install sklearn
from sklearn.cluster import KMeans

# Load the Iris dataset
iris = load_iris()
X = iris.data

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Plot the clustering results
plt.figure(figsize=(8, 6))
colors = ['r', 'g', 'b']
for i in range(3):
    points = X[labels == i]
    plt.scatter(points[:, 0], points[:, 1], s=50, c=colors[i], label=f'Cluster {i}')
plt.scatter(centers[:, 0], centers[:, 1], s=200, c='yellow', marker='X', label='Centroids')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('K-means Clustering of Iris Dataset')
plt.legend()
plt.show()
