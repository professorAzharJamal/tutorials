def conditional_probability(A, B, joint_prob_ab, prob_b, prob_a=None):
  """
  Calculates the conditional probability of event A given event B.

  Args:
      A (str): The event for which we want the conditional probability.
      B (str): The conditioning event.
      joint_prob_ab (float): The joint probability of A and B.
      prob_b (float): The probability of event B.
      prob_a (float, optional): The probability of event A (needed for formula 2). Defaults to None.

  Returns:
      float: The conditional probability P(A | B).
  """

  # Check if both probabilities are provided for formula 2
  if prob_a is None:
    # Use formula 1 (P(A | B) = P(B) * P(A n B) / P(B))
    if prob_b == 0:
      raise ZeroDivisionError("Probability of B cannot be zero")
    conditional_prob = joint_prob_ab / prob_b
  else:
    # Use formula 2 (P(A | B) = P(B) * P(B | A) / P(A))
    if prob_b == 0 or prob_a == 0:
      raise ZeroDivisionError("Probability of B or A cannot be zero")
    conditional_prob = prob_b * (joint_prob_ab / prob_a) / prob_b

  return conditional_prob

# Example Usage:
# Scenario 1: Using formula 1 (joint probability and probability of B)
joint_prob_rain_umbrella = 0.1  # P(Rain n Umbrella)
prob_rain = 0.3  # P(Rain)

conditional_prob_umbrella_given_rain = conditional_probability(
    "Umbrella", "Rain", joint_prob_rain_umbrella, prob_rain
)
print(f"P(Umbrella | Rain) using formula 1: {conditional_prob_umbrella_given_rain:.4f}")

# Scenario 2: Using formula 2 (joint probability, probability of B, and probability of A)
prob_umbrella = 0.6  # P(Umbrella)

conditional_prob_rain_given_umbrella = conditional_probability(
    "Rain", "Umbrella", joint_prob_rain_umbrella, prob_umbrella, prob_a=prob_rain
)
print(f"P(Rain | Umbrella) using formula 2: {conditional_prob_rain_given_umbrella:.4f}")
