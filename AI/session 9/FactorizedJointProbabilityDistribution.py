# Define variables and their possible values
variables = {"Coin": ["heads", "tails"]}

# Placeholder CPT (Conditional Probability Table) for simplicity
def get_cpt(variable, parents):
  # Replace this with your actual probability data
  return {"heads": 0.5, "tails": 0.5}  # Assuming a fair coin

# Example: Calculate JPD for Coin="heads"
evidence = {"Coin": "tails"}
joint_prob = 1.0

# Since there are no parent variables, iterate directly
for variable, value in evidence.items():
  joint_prob *= get_cpt(variable, {})[value]

#print(f"P(Coin=heads): {joint_prob}")

print(f"P(Coin=tails): {joint_prob}")


