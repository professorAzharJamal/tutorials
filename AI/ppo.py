import random

# Define state and action spaces (very simple examples)
states = ["left", "right"]  # Possible states (e.g., agent's position)
actions = ["up", "down"]  # Possible actions (e.g., agent's movement)

# Set random reward values (replace with actual reward function later)
rewards = {
  ("left", "up"): 10,
  ("left", "down"): -5,
  ("right", "up"): 5,
  ("right", "down"): -2
}

# Simple actor (randomly chooses action based on a probability)
def actor(state):
  # Set probability for each action (could be learned in real PPO)
  action_probs = {"up": 0.7, "down": 0.3}
  return random.choices(actions, weights=action_probs.values())[0]

# Simple critic (estimates reward based on a fixed value)
def critic(state, action):
  return rewards[(state, action)]  # Replace with actual value function later

# Simulation loop (very basic representation)
episodes = 20  # Number of episodes (simulations)
for episode in range(episodes):
  # Start in a random state
  state = random.choice(states)

  # Perform actions and update policy (simplified representation)
  for step in range(5):  # Number of steps per episode (could be variable)
    action = actor(state)
    reward = critic(state, action)

    # Update policy here (simulated with random exploration vs exploitation)
    if random.random() < 0.2:  # Explore with 20% probability (replace with proper update rule)
      action = random.choice(actions)
    
    # Update state for next step (could be based on action and environment dynamics)
    state = "right" if state == "left" else "left"  # Simple state transition (replace with actual dynamics)

    print(f"Episode {episode+1}, Step {step+1}: State: {state}, Action: {action}, Reward: {reward}")

print("Simulation completed!")
