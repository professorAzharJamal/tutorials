import numpy as np

# Define the activation function (sigmoid function in this example)
def sigmoid(x):
  return 1 / (1 + np.exp(-x))

# Define the neural network class
class NeuralNetwork:
  def __init__(self, input_size, hidden_size, output_size):
    # Initialize weights with random values
    self.weights1 = np.random.rand(input_size, hidden_size)
    self.weights2 = np.random.rand(hidden_size, output_size)

  # Forward propagation (calculating output)
  def forward(self, X):
    # Calculate hidden layer activation
    hidden_layer = sigmoid(np.dot(X, self.weights1))
    # Calculate output layer activation
    output = sigmoid(np.dot(hidden_layer, self.weights2))
    return output

# Example usage
# Define network parameters
input_size = 2  # Number of input features
hidden_size = 3  # Number of neurons in the hidden layer
output_size = 1  # Number of output neurons (binary classification)

# Create a neural network instance
network = NeuralNetwork(input_size, hidden_size, output_size)

# Sample input data (replace with your actual data)
X = np.array([[0, 0], [1, 1], [0, 1], [1, 0]])

# Get the network's prediction
predicted_output = network.forward(X)

# Print the results (predicted output for each input)
for i, input_data in enumerate(X):
  print(f"Sample {i+1}: Input = {input_data}, Predicted Output = {predicted_output[i][0]:.2f}")
