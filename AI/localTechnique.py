import random

# Define a simple problem: finding the maximum value in a list
class LocalSearchProblem:
    def __init__(self, data):
        self.data = data

    def random_neighbor(self, current_state):
        # Generate a random neighbor by randomly changing one element of the list
        neighbor = list(current_state)
        index = random.randint(0, len(neighbor) - 1)
        neighbor[index] = random.randint(0, 100)  # Assume values are between 0 and 100
        return tuple(neighbor)

    def value(self, state):
        # The value of a state is the sum of its elements
        return sum(state)

# Hill climbing algorithm for local search
def hill_climbing(problem, iterations):
    current_state = problem.data
    for _ in range(iterations):
        neighbor = problem.random_neighbor(current_state)
        if problem.value(neighbor) > problem.value(current_state):
            current_state = neighbor
    return current_state

# Example usage:
data = (10, 20, 30, 40, 50)  # Example list of numbers
problem = LocalSearchProblem(data)
solution = hill_climbing(problem, iterations=100)
print("Maximum value found:", max(solution))
