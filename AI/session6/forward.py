# Define facts as a dictionary
facts = {
    "grass_wet": True,
    "rained_yesterday": True,
    "light_on": False,
    "night_time": True
}

# Define rules as a list of dictionaries
rules = [
    {"if": {"grass_wet": True, "rained_yesterday": True}, "then": "ground_moist"},
    {"if": {"light_on": False, "night_time": True}, "then": "room_dark"}
]

# Function to infer new facts based on existing facts and rules
def forward_chaining(facts, rules):
  inferred_facts = {}
  for rule in rules:
    # Check if all conditions (facts) in the rule's "if" part are True in the current facts
    if all(facts[key] == value for key, value in rule["if"].items()):
      # If all conditions match, infer the new fact (rule's "then" part)
      new_fact = rule["then"]
      inferred_facts[new_fact] = True
      # Add the inferred fact to the main facts dictionary
      facts[new_fact] = True
  return inferred_facts

# Run the forward chaining logic
inferred_facts = forward_chaining(facts.copy(), rules.copy())  # Avoid modifying original data

# Print the initial facts and inferred facts
print("Initial Facts:")
for fact, value in facts.items():
  print(f"- {fact}: {value}")

print("\nInferred Facts:")
for fact, value in inferred_facts.items():
  print(f"- {fact}: {value}")
