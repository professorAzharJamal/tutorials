import random

# Define the grid world (replace with your desired environment)
world = [
    ['.', '.', 'X'],  # X represents the goal
    ['.', '.', '.'],
    ['.', 'S', '.']   # S represents the starting point
]

# Learning parameters
learning_rate = 0.8  # How much to update Q-values based on new information
discount_factor = 0.9  # Importance of future rewards

# Initialize Q-value table (all zeros initially)
rows, cols = len(world), len(world[0])
Q = [[0 for _ in range(cols)] for _ in range(rows)]

# Possible actions (up, down, left, right)
actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Function to choose an action based on epsilon-greedy policy
def choose_action(state, epsilon):
  if random.random() < epsilon:  # Explore randomly with probability epsilon
    return random.choice(actions)
  else:
    # Choose the action with the highest Q-value for the current state
    max_q_value = -float('inf')
    best_action = None
    for action in actions:
      next_row, next_col = state[0] + action[0], state[1] + action[1]
      # Handle out-of-bounds movements (stay in the grid)
      if 0 <= next_row < rows and 0 <= next_col < cols:
        q_value = Q[next_row][next_col]
        if q_value > max_q_value:
          max_q_value = q_value
          best_action = action
    return best_action

# Training loop (replace with actual environment interaction)
for episode in range(100):  # Number of training episodes
  # Find the starting point index dynamically
  if 'S' in world:
      current_state = (world.index('S'), world.index('S'))  # State as a tuple (row, col)
  else:
      print("Error: Starting point character 'S' not found in the world")
      continue  # Skip episode if starting point is missing

  while world[current_state[0]][current_state[1]] != 'X':  # Loop until reaching the goal
    # Choose an action based on the current state and epsilon-greedy policy
    action = choose_action(current_state, 0.1)  # Epsilon set to 0.1 for this example

    # Take the action, get reward, and move to the next state
    new_row, new_col = current_state[0] + action[0], current_state[1] + action[1]
    reward = -1  # Penalty for each move (encourages finding the goal faster)
    if world[new_row][new_col] == 'X':
      reward = 10  # Reward for reaching the goal
    next_state = (new_row, new_col)

    # Update Q-value based on SARSA (consider current state-action, next state, and next action)
    next_action = choose_action(next_state, 0.1)  # Choose the next action based on the next state
    Q[current_state[0]][current_state[1]] = (1 - learning_rate) * Q[current_state[0]][current_state[1]] + learning_rate * (reward + discount_factor * Q[next_state[0]][next_action[0]][next_action[1]])

    # Update current state
    current_state = next_state

# Print the learned Q-table (optional)
for row in Q:
  print(row)
