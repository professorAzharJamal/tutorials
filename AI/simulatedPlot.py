import random
import matplotlib.pyplot as plt

# Define a function to evaluate a state (replace with your specific problem)
def evaluate(state):
  # Example: sum of squares of elements in a list
  return sum(element**2 for element in state)

# Simulated annealing algorithm
def simulated_annealing(initial_state, max_iterations, start_temp, cooling_rate):
  current_state = initial_state.copy()  # Copy to avoid modifying original
  current_score = evaluate(current_state)
  scores = [current_score]  # List to store scores for visualization
  temp = start_temp

  for _ in range(max_iterations):
    # Explore neighbors (replace with valid neighbor generation for your problem)
    neighbors = [(i + 1, j) for i, j in enumerate(current_state) if i < len(current_state) - 1]
    neighbors.extend([(i - 1, j) for i, j in enumerate(current_state) if i > 0])

    # Find best neighbor
    best_neighbor = None
    best_neighbor_score = float('-inf')
    for neighbor in neighbors:
      new_state = current_state.copy()
      new_state[neighbor[0]] = new_state[neighbor[0]] + neighbor[1]  # Modify state (replace with valid modification logic)
      new_score = evaluate(new_state)
      if new_score > best_neighbor_score:
        best_neighbor = neighbor
        best_neighbor_score = new_score

    # Accept neighbor based on probability (Metropolis criterion)
    delta_e = new_score - current_score
    if delta_e > 0 or random.random() < np.exp(delta_e / temp):
      current_state = new_state
      current_score = new_score

    scores.append(current_score)  # Store score for each iteration
    temp *= cooling_rate  # Decrease temperature

  return current_state, scores

# Example usage
initial_state = [1, 3, 2, 4]
max_iterations = 50
start_temp = 10.0
cooling_rate = 0.95

final_state, scores = simulated_annealing(initial_state, max_iterations, start_temp, cooling_rate)
print("Final State:", final_state)
print("Final Score:", scores[-1])

# Plot the scores vs iterations
plt.plot(range(len(scores)), scores)
plt.xlabel("Iteration")
plt.ylabel("Score")
plt.title("Simulated Annealing Results")
plt.show()

import numpy as np  # Import NumPy for the exponential function
