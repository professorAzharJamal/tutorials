import numpy as np
import random

# Define the environment
class GridWorld:
    def __init__(self, size):
        self.size = size
        self.state = (0, 0)  # Start state
        self.goal = (size - 1, size - 1)  # Goal state
    
    def reset(self):
        self.state = (0, 0)
        return self.state
    
    def step(self, action):
        x, y = self.state
        if action == 0:  # Up
            x = max(0, x - 1)
        elif action == 1:  # Down
            x = min(self.size - 1, x + 1)
        elif action == 2:  # Left
            y = max(0, y - 1)
        elif action == 3:  # Right
            y = min(self.size - 1, y + 1)
        
        self.state = (x, y)
        reward = -1
        if self.state == self.goal:
            reward = 10
            done = True
        else:
            done = False
        
        return self.state, reward, done
    
    def get_state(self):
        return self.state
    
# Q-learning parameters
alpha = 0.1  # Learning rate
gamma = 0.99  # Discount factor
epsilon = 0.1  # Exploration rate

# Environment and Q-table
env = GridWorld(size=4)
q_table = np.zeros((4, 4, 4))  # Q-table initialized to zero

# Training
episodes = 1000
for episode in range(episodes):
    state = env.reset()
    done = False
    
    while not done:
        x, y = state
        
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 3)
        else:
            action = np.argmax(q_table[x, y])
        
        next_state, reward, done = env.step(action)
        next_x, next_y = next_state
        
        # Q-learning update
        q_value = q_table[x, y, action]
        max_next_q = np.max(q_table[next_x, next_y])
        q_table[x, y, action] = q_value + alpha * (reward + gamma * max_next_q - q_value)
        
        state = next_state

# Display the learned Q-values
print("Learned Q-values:")
print(q_table)

# Test the learned policy
state = env.reset()
done = False
total_reward = 0
print("\nTesting the learned policy:")

while not done:
    x, y = state
    action = np.argmax(q_table[x, y])
    state, reward, done = env.step(action)
    total_reward += reward
    print(f"State: {state}, Action: {action}, Reward: {reward}")

print(f"Total reward: {total_reward}")
