def get_cpt(variable, parents):
  """
  This function defines a Conditional Probability Table (CPT) for a variable
  given its parent variables.

  Args:
      variable: The variable for which the CPT is being created.
      parents: A list of parent variables for the given variable.

  Returns:
      A dictionary representing the CPT. The keys are the possible values
      of the variable, and the values are dictionaries containing the
      conditional probabilities for each combination of parent variable values.
  """

  # Replace this with your actual probability data
  # This is a placeholder for demonstration purposes
  if variable == "Grass":
    return {
        "wet": {
            ("Sprinkler", "on"): 0.8,
            ("Sprinkler", "off"): 0.2
        },
        "dry": {
            ("Sprinkler", "on"): 0.2,
            ("Sprinkler", "off"): 0.8
        }
    }
  elif variable == "Weather":
    # Example CPT for Weather (independent of other variables for simplicity)
    return {
        "sunny": 0.6,
        "rainy": 0.4
    }
  else:
    raise ValueError(f"Variable '{variable}' not found in the network")

# Example usage: CPT for Grass given Sprinkler state
grass_cpt = get_cpt("Grass", {"Sprinkler": "off"})
print(f"P(Grass | Sprinkler=off): {grass_cpt['wet']}")

# Example usage: Accessing specific probability
sprinkler_on_grass_wet = grass_cpt["wet"][("Sprinkler", "on")]
print(f"P(Grass=wet | Sprinkler=on): {sprinkler_on_grass_wet}")

# Example usage: Accessing specific probability
sprinkler_on_grass_dry = grass_cpt["dry"][("Sprinkler", "on")]
print(f"P(Grass=dry | Sprinkler=off): {sprinkler_on_grass_dry}")
