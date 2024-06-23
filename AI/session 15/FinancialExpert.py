# Define investment goals and risk tolerance options
investment_goals = {
    "retirement": "Long-term growth",
    "short_term_savings": "Income generation and capital preservation",
    "major_purchase": "Balanced growth and income"
}

risk_tolerance = {
    "low": "Conservative investments with lower potential returns",
    "medium": "Balanced investments with moderate risk and reward",
    "high": "Growth-oriented investments with higher risk and potentially higher returns"
}

# Function to recommend investments
def recommend_investments(goal, tolerance):
  # Define recommendations based on goals and risk tolerance (simplified)
  if goal == "retirement":
    if tolerance == "low":
      return "Fixed-income investments like bonds and CDs"
    elif tolerance == "medium":
      return "Mix of stocks, bonds, and index funds"
    else:
      return "Growth stocks and ETFs with a long-term focus"
  elif goal == "short_term_savings":
    if tolerance == "low" or tolerance == "medium":
      return "High-yield savings accounts and short-term bonds"
    else:
      return "Balanced mix of stocks and bonds with some income-generating options"
  else:
    if tolerance == "low":
      return "Income-producing investments like dividend stocks and REITs"
    elif tolerance == "medium":
      return "Growth stocks and index funds with some income-generating options"
    else:
      return "Aggressive growth stocks and sector-specific ETFs"

# Get user input
goal = input("What is your primary investment goal (retirement, short-term savings, major purchase)? ")
tolerance = input("What is your risk tolerance (low, medium, high)? ")

# Validate user input
valid_goals = investment_goals.keys()
valid_tolerance = risk_tolerance.keys()
if goal.lower() not in valid_goals or tolerance.lower() not in valid_tolerance:
  print("Invalid input. Please choose from the provided options.")
  exit()

# Get recommendations
recommendation = recommend_investments(goal.lower(), tolerance.lower())

# Print the recommendation
print("Based on your goals and risk tolerance, we recommend:", recommendation)
print("**Disclaimer:** This is a simplified example. Please consult a financial advisor for personalized advice.")

