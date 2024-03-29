def euclidean_distance(p1, p2):
  """
  Calculates the Euclidean distance between two data points.

  Args:
      p1: A list representing the first data point (features).
      p2: A list representing the second data point (features).

  Returns:
      The Euclidean distance between the two data points.
  """

  # Calculate the squared difference for each dimension
  squared_differences = [(a - b) ** 2 for a, b in zip(p1, p2)]

  # Sum the squared differences
  sum_squared_differences = sum(squared_differences)

  # Return the square root of the sum (Euclidean distance)
  return sum_squared_differences ** 0.5

def knn_classify(data, target, new_data, k):
  """
  Classifies a new data point using KNN with manual distance calculation.

  Args:
      data: A list of lists representing the training data (features).
      target: A list representing the class labels (target variable) for the training data.
      new_data: A list representing the new data point to classify (features).
      k: The number of nearest neighbors to consider.

  Returns:
      The most frequent class label among the K nearest neighbors.
  """

  # Calculate distances between new data and all training data points
  distances = []
  for i in range(len(data)):
    distance = euclidean_distance(new_data, data[i])
    distances.append((distance, target[i]))  # Store distance and class label

  # Sort the distances based on distance (ascending order)
  distances.sort(key=lambda x: x[0])

  # Get the K nearest neighbors' class labels
  nearest_neighbors = [neighbor[1] for neighbor in distances[:k]]

  # Count the frequency of each class label among the neighbors
  class_counts = {}
  for label in nearest_neighbors:
    class_counts[label] = class_counts.get(label, 0) + 1

  # Find the class label with the highest count (majority vote)
  predicted_class = max(class_counts, key=class_counts.get)

  return predicted_class

# Sample data (modify as needed)
data = [[1, 2], [3, 4], [5, 1], [7, 2], [3, 5]]
target = ["red", "blue", "red", "blue", "red"]
new_data = [4, 3]
k = 4

# Predict the class label for the new data point
predicted_class = knn_classify(data, target, new_data, k)

print(f"Predicted class for the new data point: {predicted_class}")
