import matplotlib.pyplot as plt

# Define neuron radius and spacing
neuron_radius = 0.8
neuron_spacing = 2

# Specify the number of neurons in each layer
input_size = 3  # Number of input neurons
hidden_size = 4  # Number of neurons in the hidden layer
output_size = 1  # Number of output neurons

# Create a list of layer positions (x, y coordinates)
layer_positions = []
# Input layer
for i in range(input_size):
  x = neuron_spacing * (i + 0.5)  # Center neurons within the layer
  y = 0.5
  layer_positions.append((x, y))
# Hidden layer
for i in range(hidden_size):
  x = neuron_spacing * (i + 0.5)
  y = 2.0  # Adjust y-coordinate for hidden layer
  layer_positions.append((x, y))
# Output layer
for i in range(output_size):
  x = neuron_spacing * (i + 0.5)
  y = 3.5  # Adjust y-coordinate for output layer
  layer_positions.append((x, y))

# Create the plot
plt.figure(figsize=(8, 4))  # Adjust figure size as needed

# Draw neurons
for x, y in layer_positions:
  circle = plt.Circle((x, y), neuron_radius, color='lightblue')
  plt.gca().add_artist(circle)

# Draw connections (lines) between layers (example: full connection)
for i in range(input_size):
  for j in range(hidden_size):
    start_pos = layer_positions[i]
    end_pos = layer_positions[j + input_size]
    plt.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], 'b--', alpha=0.7)  # Dashed blue lines

for i in range(hidden_size):
  for j in range(output_size):
    start_pos = layer_positions[i + input_size]
    end_pos = layer_positions[-1]  # Last element is the output neuron
    plt.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], 'b--', alpha=0.7)

# Add labels for layers
plt.text(-0.5, 0.2, 'Input Layer', ha='center', va='center', fontsize=12)
plt.text(-0.5, 1.7, 'Hidden Layer', ha='center', va='center', fontsize=12)
plt.text(-0.5, 3.2, 'Output Layer', ha='center', va='center', fontsize=12)

# Set axis limits and labels
plt.xlim(-neuron_spacing, neuron_spacing * (input_size + hidden_size + output_size) + neuron_spacing)
plt.ylim(-neuron_spacing, 4.2)  # Adjust y-limit for better visualization
plt.xlabel('X')
plt.ylabel('Y')

# Remove unnecessary elements (like ticks and title)
plt.tick_params(left=False, bottom=False)
plt.title('')

# Show the plot
plt.grid(False)  # Remove grid lines for a cleaner layout
plt.tight_layout()
plt.show()

# This program can be customized further to:
# - Represent different network architectures (e.g., convolutional layers)
# - Modify neuron colors or shapes
# - Add labels for individual neurons
