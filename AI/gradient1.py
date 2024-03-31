import numpy as np
import matplotlib.pyplot as plt

# Define the function to be optimized (we'll use a simple 1D function)
def function_to_optimize(x):
    return x**2 + 2*x + 1

# Define the derivative of the function (gradient)
def derivative_of_function(x):
    return 2*x + 2

# Gradient Descent algorithm
def gradient_descent(initial_guess, learning_rate, max_iterations, epsilon):
    current_solution = initial_guess
    
    for i in range(max_iterations):
        gradient = derivative_of_function(current_solution)
        update = -learning_rate * gradient
        current_solution += update
        
        # Check convergence criteria
        if abs(gradient) < epsilon:
            break
    
    return current_solution, function_to_optimize(current_solution)

# Function to plot the optimization process
def plot_optimization_process(initial_guess, learning_rate, max_iterations, epsilon):
    # Initialize lists to store the trajectory
    trajectory_x = [initial_guess]
    trajectory_y = [function_to_optimize(initial_guess)]
    
    # Perform gradient descent
    current_solution = initial_guess
    for i in range(max_iterations):
        gradient = derivative_of_function(current_solution)
        update = -learning_rate * gradient
        current_solution += update
        trajectory_x.append(current_solution)
        trajectory_y.append(function_to_optimize(current_solution))
        
        # Check convergence criteria
        if abs(gradient) < epsilon:
            break
    
    # Plot the function and optimization process
    x = np.linspace(-5, 5, 100)
    y = function_to_optimize(x)
    plt.plot(x, y, label='Function')
    plt.scatter(trajectory_x, trajectory_y, color='red', label='Gradient Descent Trajectory')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gradient Descent Optimization')
    plt.legend()
    plt.grid(True)
    plt.show()

# Parameters
initial_guess = 3
learning_rate = 0.1
max_iterations = 1000
epsilon = 1e-6

# Perform gradient descent
best_solution, best_value = gradient_descent(initial_guess, learning_rate, max_iterations, epsilon)
print("Best solution:", best_solution)
print("Function value at best solution:", best_value)

# Plot the optimization process
plot_optimization_process(initial_guess, learning_rate, max_iterations, epsilon)
