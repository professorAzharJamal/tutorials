# Knowledge base (facts represented as rules with empty conclusions)
knowledge_base = {
  "has_color(apple, red)": True,
  "has_color(banana, yellow)": True,
  "is_fruit(apple)": True,
  "is_fruit(banana)": True,
  "is_ripe(x)": None,  # Placeholder for rule (initially unknown)
}

# Function to check if a statement (fact) is true in the knowledge base
def is_true(statement):
  return knowledge_base.get(statement, False)  # Get value from knowledge base, default False

# Function for backward chaining (recursive)
def backward_chain(goal):
  # Base case: If goal is a fact in the knowledge base, return its truth value
  if is_true(goal):
    return True
  # Otherwise, find rules whose conclusion matches the goal
  for statement, _ in knowledge_base.items():
    if statement.split("(")[1].split(")")[0] == goal:  # Extract conclusion from statement
      # Split the rule's conditions (premises)
      conditions = statement.split("(")[0].split(" AND ")[1:]
      # Check if all conditions are true using recursive calls
      if all(backward_chain(condition) for condition in conditions):
        return True
  # If no rule matches the goal or all conditions are not met, return False
  return False

# Example usage
goal = "is_ripe(apple)"
if backward_chain(goal):
  print(f"{goal.capitalize()} is True")
else:
  print(f"{goal.capitalize()} cannot be determined from the knowledge base")

# Add a rule to determine ripeness based on color (example)
knowledge_base["is_ripe(x)"] = "(has_color(x, red) OR has_color(x, yellow))"

# Re-run with the updated knowledge base
goal = "is_ripe(apple)"
if backward_chain(goal):
  print(f"{goal.capitalize()} is True")
else:
  print(f"{goal.capitalize()} cannot be determined from the knowledge base")
