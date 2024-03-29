import numpy as np

# Sample Data
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Initialize Parameters
theta0 = 0.5  # Initial guess for slope
theta1 = 0.5  # Initial guess for intercept

alpha = 0.01  # Learning rate

num_iterations = 2000  # Number of iterations for gradient descent

# Perform Gradient Descent for multiple iterations
for i in range(num_iterations):

  # Predictions
  y_pred = theta0 * X + theta1

  # Calculate gradients
  d_theta0 = (-2/len(X)) * np.sum(X * (y - y_pred))
  d_theta1 = (-2/len(X)) * np.sum(y - y_pred)

  # Update parameters
  theta0 = theta0 - alpha * d_theta0
  theta1 = theta1 - alpha * d_theta1

# Print the final parameters after training
print("Final theta0 (slope):", theta0)
print("Final theta1 (intercept):", theta1)
