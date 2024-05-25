import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    """
    Compute the sigmoid of x
    """
    return 1 / (1 + np.exp(-x))

def main():
    # Example input
    inputs = np.array([-10, -5, 0, 5, 10])
    
    # Apply sigmoid function
    outputs = sigmoid(inputs)
    
    print("Inputs: ", inputs)
    print("Sigmoid Outputs: ", outputs)
    
    # Visualize the Sigmoid function
    x_values = np.linspace(-10, 10, 400)
    y_values = sigmoid(x_values)
    
    plt.plot(x_values, y_values)
    plt.title('Sigmoid Activation Function')
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
