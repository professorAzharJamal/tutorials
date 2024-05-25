import numpy as np
import matplotlib.pyplot as plt

def tanh(x):
  """
  This function implements the Hyperbolic Tangent activation function.

  Args:
      x: A numerical input value or a NumPy array of input values.

  Returns:
      The Hyperbolic Tangent activation of the input value(s).
  """
  return np.tanh(x)

# Generate input values
x = np.linspace(-5, 5, 100)  # Create a range of input values from -5 to 5

# Calculate tanh outputs
y = tanh(x)

# Plot the tanh function
plt.plot(x, y, label='Tanh Activation')

# Add labels and title
plt.xlabel('Input Value (x)')
plt.ylabel('Tanh Output (y)')
plt.title('Hyperbolic Tangent Activation Function')

# Add grid lines for better readability
plt.grid(True)

# Show the plot
plt.legend()
plt.show()

# Print explanation
print("Imagine a stronger dimmer switch with a wider range than the Sigmoid function.")
print("The Tanh function also maps input values to a range between -1 and 1.")
print("Here's how it works:")
print("- Large negative input values (far left on the graph) get squashed close to -1.")
print("- Large positive input values (far right on the graph) get squashed close to 1.")
print("- Values around 0 (center of the graph) are mapped to values between -1 and 1.")
print("This wider range can be beneficial for some neural network applications.")
