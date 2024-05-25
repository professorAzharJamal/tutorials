import numpy as np
import matplotlib.pyplot as plt

def relu(x):
  return np.maximum(0, x)  # Maximum of 0 or the input value

# Generate input values
x = np.linspace(-5, 5, 100)  # Create a range of input values from -5 to 5

# Calculate ReLU outputs
y = relu(x)

# Plot the ReLU function
plt.plot(x, y, label='ReLU Activation')

# Add labels and title
plt.xlabel('Input Value (x)')
plt.ylabel('ReLU Output (y)')
plt.title('Rectified Linear Unit (ReLU) Activation Function')

# Add grid lines for better readability
plt.grid(True)

# Show the plot
plt.legend()
plt.show()

# Print explanation
print("The ReLU function is a simpler activation function compared to sigmoid and tanh.")
print("It works as follows:")
print("- If the input value (x) is greater than 0, the output is the same as the input.")
print("- If the input value (x) is less than or equal to 0, the output is set to 0.")
print("This function is often preferred for its simplicity and efficiency in training neural networks.")
