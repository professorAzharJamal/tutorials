# Define world states (propositions)
clear_path = True  # Is the path ahead clear?
destination_reached = False  # Has the agent reached its goal?

# Possible actions (change direction if path is blocked)
actions = ["move_forward", "turn_left", "turn_right"]
current_action = actions[0]  # Initial action is to move forward

# Knowledge base (rules)
can_move_forward = clear_path and not destination_reached
can_turn_left = not clear_path  # Simplified rule to turn if path is blocked

def update_world(obstacle_encountered=False, destination_found=False):
  """
  Simulates changes in the world (e.g., encountering an obstacle or reaching the destination).
  """
  global clear_path, destination_reached  # Access global variables

  if obstacle_encountered:
    clear_path = False
  if destination_found:
    destination_reached = True

def decide_and_act():
  """
  Uses propositional logic to decide on an action (move or turn) and updates the current action.
  """
  global clear_path, destination_reached, current_action, can_move_forward, can_turn_left

  can_move_forward = clear_path and not destination_reached

  if can_move_forward:
    current_action = actions[0]  # Move forward if possible
  elif can_turn_left:
    current_action = actions[1]  # Turn left if path is blocked (simplified strategy)
  else:
    # No valid action based on current rules (could be a dead end)
    current_action = "stop"
    print("Agent is stuck! Needs more complex logic to navigate dead ends.")

def main():
  """
  Simulates the agent's navigation loop with world updates, decision-making, and action selection.
  """
  while not destination_reached:
    # Decide and act based on current state
    decide_and_act()
    print(f"Agent action: {current_action}")

    # Simulate the action (could involve delays or errors)
    # (This part is simplified for demonstration purposes)
    if current_action == "move_forward":
      update_world(obstacle_encountered=random.random() < 0.2)  # 20% chance of obstacle
    elif current_action == "turn_left":
      pass  # No world update needed for turning (simplified)

    # Check if the goal is reached after the action (could involve sensors)
    update_world(destination_found=random.random() < 0.1)  # 10% chance of reaching destination

  print("Agent has reached the goal!")

if __name__ == "__main__":
  import random  # For simulating obstacles and reaching the destination
  main()
