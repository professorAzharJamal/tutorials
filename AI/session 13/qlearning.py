import random
from matplotlib import pyplot as plt

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

# Training loop (replace with actual environment interaction)
for episode in range(100):  # Number of training episodes
  # Find the starting point index dynamically
  if 'S' in world:
      current_row, current_col = world.index('S'), world[0].index('S')
  else:
      print("Error: Starting point character 'S' not found in the world")
      continue  # Skip episode if starting point is missing

  while world[current_row][current_col] != 'X':  # Loop until reaching the goal
    # Choose an action (epsilon-greedy policy for exploration vs. exploitation)
    if random.random() < 0.1:  # Explore randomly with 10% chance
      next_action = random.choice(actions)
    else:
      # Choose the action with the highest Q-value for the current state
      max_q_value = -float('inf')
      for action in actions:
        next_row, next_col = current_row + action[0], current_col + action[1]
        # Handle out-of-bounds movements (stay in the grid)
        if 0 <= next_row < rows and 0 <= next_col < cols:
          q_value = Q[next_row][next_col]
          if q_value > max_q_value:
            max_q_value = q_value
            next_action = action

    # Take the action, get reward, and move to the next state
    new_row, new_col = current_row + next_action[0], current_col + next_action[1]
    reward = -1  # Penalty for each move (encourages finding the goal faster)
    if world[new_row][new_col] == 'X':
      reward = 10  # Reward for reaching the goal

    # Update Q-value based on the Bellman equation (consider reward and future value)
    Q[current_row][current_col] = (1 - learning_rate) * Q[current_row][current_col] + learning_rate * (reward + discount_factor * max_q_value)

    # Update current state
    current_row, current_col = new_row, new_col

# Visualize the learned Q-table (optional)
fig, ax = plt.subplots()
ax.pcolor(Q, vmin=-1, vmax=1, cmap='coolwarm')

# Label states and actions
for i in range(rows):
  for j in range(cols):
    ax.text(j, i, f"{Q[i][j]:.2f}", ha='center', va='center', fontsize=8)
    ax.set_xticks(range(cols))
    ax.set_yticks(range(rows))
    ax.set_xlabel('Columns (Actions)')
    ax.set_ylabel('Rows (States)')
    ax.set_title('Learned Q-Values')

plt.show()
