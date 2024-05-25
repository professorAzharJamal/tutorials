import matplotlib.pyplot as plt

# Define neuron radius and spacing
neuron_radius = 0.8
neuron_spacing = 2

def draw_neural_network(layers, figsize=(10, 6)):
  """
  This function draws the structure of a neural network with specified layers.

  Args:
      layers: A list containing the number of neurons in each layer (including input and output layers).
      figsize: A tuple specifying the figure size for the plot (optional, default (10, 6)).
  """
  # Create a plot
  plt.figure(figsize=figsize)

  # Calculate total number of layers
  num_layers = len(layers)

  # Calculate layer positions (x, y coordinates)
  layer_positions = []
  max_neurons = max(layers)  # Find the layer with the most neurons
  for i in range(num_layers):
    x = neuron_spacing * (i + 0.5)  # Center layers horizontally
    y_pos = (1 - (i / (num_layers - 1))) * 0.7  # Distribute layers vertically
    layer_positions.append([])
    for j in range(layers[i]):
      # Distribute neurons within a layer
      x_offset = (j / (max_neurons - 1)) * (neuron_spacing * 1.2 - neuron_radius * 2)
      layer_positions[i].append((x + x_offset, y_pos))

  # Draw neurons
  for layer_i, layer_positions_i in enumerate(layer_positions):
    for neuron_x, neuron_y in layer_positions_i:
      circle = plt.Circle((neuron_x, neuron_y), neuron_radius, color='lightblue')
      plt.gca().add_artist(circle)
      # Add neuron labels (optional)
      # plt.text(neuron_x, neuron_y + 0.1, f"L{layer_i+1}N{neuron_i+1}", ha='center', va='center', fontsize=10)

  # Draw connections (lines) between layers
  for layer_i in range(num_layers - 1):
    for j, start_pos in enumerate(layer_positions[layer_i]):
      for end_pos in layer_positions[layer_i + 1]:
        plt.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], 'b--', alpha=0.7)  # Dashed blue lines

  # Add labels for layers (optional)
  for i, layer_size in enumerate(layers):
    x = -neuron_spacing + 0.2
    y = (1 - (i / (num_layers - 1))) * 0.7
    plt.text(x, y, f"Layer {i+1} ({layer_size} Neurons)", ha='left', va='center', fontsize=12)

  # Set axis limits and labels
  plt.xlim(-neuron_spacing, neuron_spacing * (num_layers + 0.5))
  plt.ylim(0, 1)
  plt.xlabel('X')
  plt.ylabel('Y')

  # Remove unnecessary elements (like ticks and title)
  plt.tick_params(left=False, bottom=False)
  plt.title('')

  # Show the plot
  plt.grid(False)  # Remove grid lines for a cleaner layout
  plt.tight_layout()
  plt.show()

# Example usage: Define the network architecture (layers)
network_architecture = [3, 4, 2]  # Example: 3 input neurons, 4 hidden neurons, 2 output neurons

# Draw the neural network
draw_neural_network(network_architecture)
