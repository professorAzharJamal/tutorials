# Probability distribution for a die roll
die_roll_prob = {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}

# Function to calculate conditional probability (e.g., P(even | roll > 3))
def conditional_prob_discrete(event, value, condition, prob_dist):
  # Filter probabilities based on the condition
  filtered_prob = {k: v for k, v in prob_dist.items() if (condition == "gt3" and k > 3) or (condition == "even" and k % 2 == 0)}

  # Calculate conditional probability (normalize filtered probabilities)
  total_prob_condition = sum(filtered_prob.values())
  if total_prob_condition == 0:
    raise ValueError("Condition probability is zero")
  return filtered_prob[value] / total_prob_condition

# Example: P(even | roll > 3)
condition = "even"  # even or gt3 (greater than 3)
value = 4  # specific value for event
prob = conditional_prob_discrete(event="roll", value=value, condition=condition, prob_dist=die_roll_prob)
print(f"P(even | roll > 3): {prob:.4f}")
