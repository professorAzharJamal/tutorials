import numpy as np

def sigmoid(x):
    """
    Compute the sigmoid activation function
    """
    return 1 / (1 + np.exp(-x))

def main():
    # Example input data (3 input neurons)
    inputs = np.array([0.5, -0.2, 0.1])

    # Weights for the connections (input to hidden layer)
    weights_input_hidden = np.array([
        [0.4, 0.6, -0.5],
        [-0.3, 0.1, 0.2],
        [0.2, -0.4, 0.5],
        [0.1, 0.2, 0.6]
    ])

    # Weights for the connections (hidden to output layer)
    weights_hidden_output = np.array([0.3, -0.7, 0.2, 0.1])

    # Bias for hidden and output layers
    bias_hidden = np.array([0.1, -0.2, 0.3, 0.4])
    bias_output = 0.1

    # Compute the hidden layer activations
    hidden_layer_input = np.dot(weights_input_hidden, inputs) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)

    # Compute the output layer activations
    output_layer_input = np.dot(weights_hidden_output, hidden_layer_output) + bias_output
    output = sigmoid(output_layer_input)

    print("Inputs: ", inputs)
    print("Hidden Layer Input: ", hidden_layer_input)
    print("Hidden Layer Output: ", hidden_layer_output)
    print("Output Layer Input: ", output_layer_input)
    print("Output: ", output)

if __name__ == "__main__":
    main()
