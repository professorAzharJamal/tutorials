# Define lifestyle factors and pet types
lifestyle = {
    "active": ["dog", "cat"],
    "laid_back": ["cat", "guinea pig"],
    "apartment_dweller": ["cat", "fish"],
    "allergic": ["fish", "reptile"]
}

# Function to recommend a pet
def recommend_pet(factors):
  # Consider multiple factors (simplified here, choose one factor from user input)
  chosen_factor = factors[0]  # Assuming user selects one factor
  if chosen_factor in lifestyle:
    return f"Considering your {chosen_factor} lifestyle, {', '.join(lifestyle[chosen_factor])} could be good companions."
  else:
    return "Tell me more about your lifestyle to get a recommendation!"

# Get user input (example: prompt for preferred factor)
chosen_factor = input("Are you active, laid-back, or an apartment dweller? ")

# Get recommendation
recommendation = recommend_pet([chosen_factor])

# Print the recommendation
print(recommendation)
