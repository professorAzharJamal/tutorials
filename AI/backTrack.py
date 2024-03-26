# Define rules as dictionaries with conditions and conclusions
rules = {
    "rule4": {
        "conditions": ["viral_infection", "rash"],
        "conclusion": "measles"
    },
    "rule1": {
        "conditions": ["fever", "sore_throat"],
        "conclusion": "viral_infection"
    }
}

# Define facts as a dictionary
facts = {
    "fever": True,
    "sore_throat": True,
    "rash": True,
    "viral_infection" :True
}

# Function to check if a condition is met based on facts
def check_condition(condition):
  return facts.get(condition, False)  # Get value from facts or False

# Goal: Determine the cause of symptoms (backward chaining)
goal = "measles"

while goal:
  # Find a rule that has the goal as its conclusion
  for rule_name, rule in rules.items():
    if rule["conclusion"] == goal:
      # Check each condition of the rule
      conditions_met = all(check_condition(condition) for condition in rule["conditions"])
      if conditions_met:
        # All conditions met, conclude with this rule
        goal = rule["conclusion"]
        print(f"Based on the facts, the patient's symptoms may indicate {goal}.")
        break  # Stop if a rule applies and conditions are met
      else:
        # Conditions not met for this rule, keep searching
        continue
  else:
    # No rule found with the current goal, no conclusion reached
    print("Based on the available facts, a conclusion cannot be determined.")
    break
