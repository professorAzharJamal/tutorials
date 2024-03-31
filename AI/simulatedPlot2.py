import math
import random
import numpy as np
import matplotlib.pyplot as plt

# Define the function to be optimized (we'll use a simple 2D function)
def function_to_optimize(x, y):
    return -(x ** 2 + y ** 2)  # Minus sign because we're maximizing

# Simulated Annealing algorithm
def simulated_annealing(initial_temperature, cooling_rate, max_iterations):
    current_x = random.uniform(-10, 10)
    current_y = random.uniform(-10, 10)
    current_solution = function_to_optimize(current_x, current_y)
    best_solution = current_solution

    for i in range(max_iterations):
        temperature = initial_temperature / (1 + i)  # Cooling schedule
        new_x = current_x + random.uniform(-1, 1)
        new_y = current_y + random.uniform(-1, 1)
        new_solution = function_to_optimize(new_x, new_y)

        # If the new solution is better, accept it
        if new_solution > current_solution:
            current_x = new_x
            current_y = new_y
            current_solution = new_solution
            if new_solution > best_solution:
                best_solution = new_solution
        else:
            # If the new solution is worse, accept it with a probability
            probability = math.exp((new_solution - current_solution) / temperature)
            if random.random() < probability:
                current_x = new_x
                current_y = new_y
                current_solution = new_solution

    return best_solution, current_x, current_y

# Perform simulated annealing and print the result
initial_temperature = 1000
cooling_rate = 0.01
max_iterations = 1000
best_solution, best_x, best_y = simulated_annealing(initial_temperature, cooling_rate, max_iterations)
print("Best solution:", best_solution)
print("Coordinates (x, y):", (best_x, best_y))

# Create a grid for plotting
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = -(X ** 2 + Y ** 2)  # Evaluate function on the grid

# Plot the function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Plot the best solution found by simulated annealing
ax.scatter(best_x, best_y, best_solution, color='red', s=100, label='Best Solution')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Optimization Function')
plt.legend()
plt.show()
