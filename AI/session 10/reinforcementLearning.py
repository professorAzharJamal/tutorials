import numpy as np
import random

# Define the environment
grid_size = 4
actions = ['up', 'down', 'left', 'right']
action_to_index = {action: i for i, action in enumerate(actions)}

# Initialize Q-table with zeros
Q = np.zeros((grid_size, grid_size, len(actions)))

# Parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
episodes = 1000

# Define rewards
def get_reward(state):
    if state == (3, 3):
        return 100  # Reward for reaching the goal
    else:
        return -1  # Penalty for each step taken

# Define next state
def get_next_state(state, action):
    row, col = state
    if action == 'up':
        row = max(0, row - 1)
    elif action == 'down':
        row = min(grid_size - 1, row + 1)
    elif action == 'left':
        col = max(0, col - 1)
    elif action == 'right':
        col = min(grid_size - 1, col + 1)
    return (row, col)

# Q-learning algorithm
for episode in range(episodes):
    state = (0, 0)  # Start state
    while state != (3, 3):
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)  # Explore
        else:
            action = actions[np.argmax(Q[state])]  # Exploit

        next_state = get_next_state(state, action)
        reward = get_reward(next_state)
        
        # Update Q-value
        best_next_action = np.argmax(Q[next_state])
        td_target = reward + gamma * Q[next_state][best_next_action]
        Q[state][action_to_index[action]] += alpha * (td_target - Q[state][action_to_index[action]])
        
        state = next_state

# Display the learned Q-values
for row in range(grid_size):
    for col in range(grid_size):
        print(f"Q[{row},{col}] = {Q[row, col]}")

# Display the optimal policy
policy = np.full((grid_size, grid_size), '', dtype=object)
for row in range(grid_size):
    for col in range(grid_size):
        policy[row, col] = actions[np.argmax(Q[row, col])]
print("\nOptimal Policy:")
print(policy)
