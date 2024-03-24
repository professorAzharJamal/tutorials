# Define propositions (statements about the robot)
near_vase = False  # Is the robot near the vase?
arms_extended = True  # Are the robot's arms extended?

# Safety rule (formula) - We want to avoid arms being extended near the vase
safe_action = not (near_vase and arms_extended)

# Print the safety check
if safe_action:
  print("Robot is safe: Arms not extended near the vase!")
else:
  print("Warning! Robot arms might knock over the vase. Be careful!")