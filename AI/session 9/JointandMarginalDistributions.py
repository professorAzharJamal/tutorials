# Joint probability distribution (weather, temperature)
joint_prob = {
    ("sunny", "hot"): 0.3,
    ("sunny", "cold"): 0.2,
    ("rainy", "hot"): 0.1,
    ("rainy", "cold"): 0.4
}

# Function to calculate marginal probability (e.g., P(weather=sunny))
def marginal_prob(variable, joint_dist):
  marginal_prob = 0
  for assignment in joint_dist:
    if assignment[0] == variable:  # Check if it's the variable of interest
      marginal_prob += joint_dist[assignment]
  return marginal_prob

# Example: P(weather=sunny)
variable = "weather"
prob = marginal_prob(variable, joint_prob)
print(f"P(weather=sunny): {prob:.4f}")
