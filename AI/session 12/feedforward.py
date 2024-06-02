import numpy as np

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Input data (4 samples with 3 features each)
X = np.array([[0, 0, 1],
              [1, 1, 1],
              [1, 0, 1],
              [0, 1, 1]])

# Output data (4 samples with 1 output each)
y = np.array([[0],
              [1],
              [1],
              [0]])

# Seed random numbers to make calculation deterministic (just for this tutorial)
np.random.seed(1)

# Initialize weights randomly with mean 0
weights0 = 2 * np.random.random((3, 4)) - 1
weights1 = 2 * np.random.random((4, 1)) - 1

# Training
for iteration in range(10000):
    # Forward propagation
    layer0 = X
    layer1 = sigmoid(np.dot(layer0, weights0))
    layer2 = sigmoid(np.dot(layer1, weights1))

    # Error calculation
    layer2_error = y - layer2

    if (iteration % 1000) == 0:
        print(f"Error after {iteration} iterations: {np.mean(np.abs(layer2_error))}")

    # Backpropagation
    layer2_delta = layer2_error * sigmoid_derivative(layer2)
    layer1_error = layer2_delta.dot(weights1.T)
    layer1_delta = layer1_error * sigmoid_derivative(layer1)

    # Update weights
    weights1 += layer1.T.dot(layer2_delta)
    weights0 += layer0.T.dot(layer1_delta)

# Final output
print("Output after training:")
print(layer2)
