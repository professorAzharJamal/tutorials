from scipy.stats import norm

# Define mean and standard deviation for men and women
mean_men = 178  # cm
std_men = 8  # cm
mean_women = 165  # cm
std_women = 6  # cm

# Function to calculate conditional probability (e.g., P(height > 180 | male))
def conditional_prob_continuous(variable, value, condition, mean_cond, std_cond):
  # Assuming condition is "male" or "female" based on mean and std provided
  if condition == "male":
    dist = norm(mean_men, std_men)
  else:
    dist = norm(mean_women, std_women)

  # Calculate probability (P(x > value)) using cumulative distribution function (cdf)
  return 1 - dist.cdf(value)

# Example: P(height > 180 cm | male)
condition = "male"
value = 180  # cm
prob = conditional_prob_continuous(variable="height", value=value, condition=condition, mean_cond=mean_men, std_cond=std_men)
print(f"P(height > 180 cm | male): {prob:.4f}")
