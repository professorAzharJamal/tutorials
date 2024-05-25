import matplotlib.pyplot as plt
import numpy as np

def draw_neural_network(ax, layer_sizes, weights):
    """
    Draw a neural network cartoon using matplotlib.

    Args:
    ax : matplotlib.axes.Axes
        The axes on which to plot the cartoon (get e.g. by plt.gca())
    layer_sizes : list of int
        List containing the number of nodes in each layer
    weights : list of 2D np.array
        List containing weight matrices for connections between layers
    """
    v_spacing = (1.0 / (max(layer_sizes))) 
    h_spacing = (1.0 / (len(layer_sizes) - 1))

    # Nodes
    for i, layer_size in enumerate(layer_sizes):
        layer_top = v_spacing * (layer_size - 1) / 2
        for j in range(layer_size):
            circle = plt.Circle((i * h_spacing, layer_top - j * v_spacing), v_spacing / 4, 
                                color='w', ec='k', zorder=4)
            ax.add_artist(circle)
            if i == 0:
                ax.text(-0.05, layer_top - j * v_spacing, f'Input {j+1}', ha='right', va='center', fontsize=12)
            elif i == len(layer_sizes) - 1:
                ax.text(i * h_spacing + 0.05, layer_top - j * v_spacing, f'Output {j+1}', ha='left', va='center', fontsize=12)

    # Edges
    for i, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        layer_top_a = v_spacing * (layer_size_a - 1) / 2
        layer_top_b = v_spacing * (layer_size_b - 1) / 2
        for j in range(layer_size_a):
            for k in range(layer_size_b):
                line = plt.Line2D([i * h_spacing, (i + 1) * h_spacing], 
                                  [layer_top_a - j * v_spacing, layer_top_b - k * v_spacing], 
                                  c='k')
                ax.add_artist(line)
                # Annotate weights
                mid_x = (i * h_spacing + (i + 1) * h_spacing) / 2
                mid_y = (layer_top_a - j * v_spacing + layer_top_b - k * v_spacing) / 2
                weight_text = f'{weights[i][j, k]:.2f}'
                ax.text(mid_x, mid_y, weight_text, fontsize=10, ha='center', va='center', color='red')

def main():
    fig = plt.figure(figsize=(12, 8))
    ax = fig.gca()
    ax.axis('off')

    # Example architecture and weights
    layer_sizes = [3, 5, 4, 2]
    weights = [
        np.random.randn(layer_sizes[0], layer_sizes[1]),
        np.random.randn(layer_sizes[1], layer_sizes[2]),
        np.random.randn(layer_sizes[2], layer_sizes[3])
    ]

    draw_neural_network(ax, layer_sizes, weights)
    plt.title('Artificial Neural Network with Weights')
    plt.show()

if __name__ == "__main__":
    main()
