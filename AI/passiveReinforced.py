import random

# Define possible actions (agent's choices)
actions = ["up", "down", "left", "right"]

# Set the reward for reaching the goal (positive reinforcement)
goal_reward = 10

# Set the penalty for going out of bounds (negative reinforcement)
out_of_bounds_penalty = -5

# Define the environment (simplified maze) as a list of lists
environment = [
    ["X", "X", "X", "X"],  # Top row (wall)
    [" ", " ", " ", " "],  # Second row (empty space)
    [" ", "G", " ", " "],  # Third row (goal "G" in the middle)
    [" ", " ", " ", "X"],  # Bottom row (wall)
]

# Function to check if the agent is out of bounds
def is_out_of_bounds(x, y, environment):
  # Check if coordinates are within the environment dimensions
  return (x < 0 or x >= len(environment[0]) or y < 0 or y >= len(environment))

# Function to take an action and update the agent's position
def take_action(action, x, y):
  new_x = x
  new_y = y
  if action == "up":
    new_y -= 1
  elif action == "down":
    new_y += 1
  elif action == "left":
    new_x -= 1
  elif action == "right":
    new_x += 1
  
  # Check if the new position is out of bounds and apply penalty
  if is_out_of_bounds(new_x, new_y, environment):
    return x, y, out_of_bounds_penalty
  else:
    return new_x, new_y, 0

# Main loop (simulation)
x = 1  # Initial x-coordinate of the agent
y = 1  # Initial y-coordinate of the agent
total_reward = 0  # Cumulative reward over time

while True:
  # Print the environment with the agent's position
  for row in environment:
    print("".join(row))
  print("Agent is at:", (x, y))

  # Randomly choose an action
  action = random.choice(actions)

  # Take the action, update position, and get reward
  new_x, new_y, reward = take_action(action, x, y)

  # Check if the agent reached the goal and end the simulation
  if environment[new_y][new_x] == "G":
    reward += goal_reward
    print("Goal reached! Reward:", reward)
    break

  # Update the agent's position
  x = new_x
  y = new_y
  total_reward += reward

# Print the final results
print("Total reward:", total_reward)
