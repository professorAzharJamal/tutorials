import random

# Define the number of arms (options) in the bandit problem
num_arms = 5

# Set the average rewards for each arm (replace these with actual reward functions if possible)
average_rewards = [0.7, 0.6, 0.8, 0.5, 0.4]

# Epsilon value for exploration vs. exploitation trade-off (0 to 1)
epsilon = 0.2

# Initialize variables to track rewards for each arm
arm_rewards = [0] * num_arms

# Function to choose an arm based on epsilon-greedy policy
def choose_arm(epsilon, arm_rewards):
  # Explore randomly with epsilon probability
  if random.random() < epsilon:
    return random.randint(0, num_arms - 1)  # Random arm selection
  else:
    # Exploit the arm with the highest average reward based on current estimates
    return arm_rewards.index(max(arm_rewards))

# Main loop (simulation)
for i in range(1000):  # Number of rounds (iterations)
  # Choose an arm based on the epsilon-greedy policy
  chosen_arm = choose_arm(epsilon, arm_rewards)

  # Get the actual reward for the chosen arm (replace with your reward function if possible)
  actual_reward = random.random() + average_rewards[chosen_arm]  # Simulate reward with some randomness

  # Update the reward for the chosen arm
  arm_rewards[chosen_arm] = (arm_rewards[chosen_arm] + actual_reward) / (i + 1)  # Moving average

# Print the average rewards for each arm after the simulation
print("Average rewards for each arm:")
for i in range(num_arms):
  print("Arm", i+1, ":", arm_rewards[i])
