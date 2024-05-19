import random

# Define the reward range for each "bandit arm" (slot machine)
bandit_rewards = [0.2, 0.5, 0.7]  # Adjust these values for different reward probabilities

# Number of times to pull each arm (exploration)
exploration_steps = 10

# Function to pull a specific arm and get a reward
def pull_arm(arm_index):
  reward = random.random() * bandit_rewards[arm_index]
  return reward

# Initialize variables
total_rewards = [0 for _ in bandit_rewards]  # Track total reward for each arm
best_arm = None  # Track the arm with the highest average reward

# Exploration phase
for _ in range(exploration_steps):
  for arm_index in range(len(bandit_rewards)):
    reward = pull_arm(arm_index)
    total_rewards[arm_index] += reward

# Exploitation phase (choose the arm with the highest average reward)
average_rewards = [total / exploration_steps for total in total_rewards]
best_arm = average_rewards.index(max(average_rewards))

# Print results
print("Exploration Phase:")
for i, reward in enumerate(total_rewards):
  print(f"Arm {i+1} Average Reward: {reward / exploration_steps:.2f}")

print("Exploitation Phase:")
print(f"Best Arm: {best_arm+1} with Average Reward: {average_rewards[best_arm]:.2f}")
