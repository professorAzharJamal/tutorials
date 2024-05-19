from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace with your actual data)
data = np.array([[1, 1], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])  # Each row represents a data point (features)

# Define the number of clusters (k)
num_clusters = 2

# Create a KMeans object
kmeans = KMeans(n_clusters=num_clusters, random_state=0)

# Fit the model to the data
kmeans.fit(data)

# Get cluster labels for each data point
cluster_labels = kmeans.labels_

# Print cluster labels
print("Cluster Labels:", cluster_labels)

# Visualize clusters (optional)
plt.scatter(data[:, 0], data[:, 1], c=cluster_labels)  # Plot data points with colors based on cluster labels
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
