# Facts about food and Ravi's likes 
facts = {
    "rule1": lambda x: x.startswith("likes_") and x.split("_")[1] in facts,  # Anything Ravi likes must be food
    "food_apple": True,
    "food_chicken": True,
    "rule2": lambda x, y: x == "alive" and "eats" in y,  # If someone eats and is alive, it's food
    "eats_ajay_peanuts": True,
    "alive_ajay": True,
    "rule3": lambda x: x == "not_killed",  # Alive implies not killed
}

# What we want to prove (negation)
to_prove = "not likes_ravi_peanuts"

# Function to check if a statement is true based on facts
def check_fact(statement):
  if isinstance(statement, str):  # Simple fact
    return facts.get(statement, False)  # Get value from facts or False
  else:  # Function-based fact
    return statement(facts)  # Call the function with facts as argument

# Function to resolve contradictions (simplified)
def resolve(statement1, statement2):
  # Try splitting statements, handle cases with no or one underscore
  concept1, rest1 = statement1.split("_", 1) if "_" in statement1 else (statement1, "")
  concept2, rest2 = statement2.split("_", 1) if "_" in statement2 else (statement2, "")
  
  # Check for contradiction (negation of the same concept)
  if concept1 != concept2 and ("not " + concept2 in statement1 or "not " + concept1 in statement2):
    # Combine remaining parts (ignoring negation for simplicity)
    return rest1 + " " + rest2
  else:
    return None  # No resolution possible

# Prove the statement using a loop (simulates resolution steps)
proven = False
while to_prove and not proven:
  # Try resolving with each fact
  for fact, value in facts.items():
    if value:  # Only consider true facts
      resolved = resolve(to_prove, fact)
      if resolved:
        to_prove = resolved
        break  # Stop if resolved
  # Check if we reached a known fact (contradiction)
  proven = check_fact(to_prove)

# Print the result
if proven:
  print("Based on the given facts, it can be concluded that Ravi likes peanuts.")
else:
  print("The given facts are not enough to prove that Ravi likes peanuts.")
