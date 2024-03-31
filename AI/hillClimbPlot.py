import matplotlib.pyplot as plt

# Define a function to evaluate a state (replace with your specific problem)
def evaluate(state):
  # Example: sum of squares of elements in a list
  return sum(element**2 for element in state)

# Hill climbing algorithm
def hill_climbing(initial_state, max_iterations):
  current_state = initial_state.copy()  # Copy to avoid modifying original
  current_score = evaluate(current_state)
  scores = [current_score]  # List to store scores for visualization

  for _ in range(max_iterations):
    # Explore neighbors (replace with valid neighbor generation for your problem)
    neighbors = [(i + 1, j) for i, j in enumerate(current_state) if i < len(current_state) - 1]
    neighbors.extend([(i - 1, j) for i, j in enumerate(current_state) if i > 0])

    # Find best neighbor with higher score
    best_neighbor = None
    best_neighbor_score = float('-inf')
    for neighbor in neighbors:
      new_state = current_state.copy()
      new_state[neighbor[0]] = new_state[neighbor[0]] + neighbor[1]  # Modify state (replace with valid modification logic)
      new_score = evaluate(new_state)
      if new_score > best_neighbor_score:
        best_neighbor = neighbor
        best_neighbor_score = new_score

    # Update current state and score if a better neighbor is found
    if best_neighbor:
      current_state[best_neighbor[0]] += best_neighbor[1]
      current_score = best_neighbor_score
    scores.append(current_score)  # Store score for each iteration

  return current_state, scores

# Example usage
initial_state = [1, 3, 2, 4]
max_iterations = 100

final_state, scores = hill_climbing(initial_state, max_iterations)
print("Final State:", final_state)
print("Final Score:", scores[-1])

# Plot the scores vs iterations
plt.plot(range(len(scores)), scores)
plt.xlabel("Iteration")
plt.ylabel("Score")
plt.title("Hill Climbing Results")
plt.show()
