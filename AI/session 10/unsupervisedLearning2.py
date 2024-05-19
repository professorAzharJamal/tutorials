from sklearn.cluster import KMeans

# Sample data (replace with your actual data)
data = [[1, 1.5], [2, 1.2], [5, 8], [8, 8.5], [1, 0.8], [7, 9],[6,7]]

# Define the number of clusters (k)
num_clusters = 2

# Create a KMeans model
kmeans = KMeans(n_clusters=num_clusters)

# Fit the model to the data (performs clustering)
kmeans.fit(data)

# Get the cluster labels for each data point
cluster_labels = kmeans.labels_

# Print results
for i, data_point in enumerate(data):
  print(f"Sample {i+1}: Data Point = {data_point}, Cluster = {cluster_labels[i]}")
