def bayesian_network(P_A, P_B_given_A, P_C_given_A):
  """
  This function calculates the probability of a specific scenario in a Bayesian network
  using factorization representation.

  Args:
      P_A: A list representing the probability of event A (True/False).
      P_B_given_A: A 2D list representing the probability of event B given A (True/False).
      P_C_given_A: A 2D list representing the probability of event C given A (True/False).

  Returns:
      The probability of the specific scenario (A, B, C).
  """

  # Event states (True or False)
  A = True  # Crime scene happened
  B = True  # Witness B testimony
  C = False  # Witness C testimony

  # Probability lookups using conditional independence
  probability_A = P_A[int(A)]
  probability_B_given_A = P_B_given_A[int(A)][int(B)]
  probability_C_given_A = P_C_given_A[int(A)][int(C)]

  # Probability of the scenario using factorization
  scenario_probability = probability_A * probability_B_given_A * probability_C_given_A

  return scenario_probability

# Example probabilities
P_A = [0.6, 0.4]  # P(A=True), P(A=False)
P_B_given_A = [[0.8, 0.2], [0.3, 0.7]]  # P(B=True | A=True), P(B=True | A=False)
P_C_given_A = [[0.9, 0.1], [0.4, 0.6]]  # P(C=True | A=True), P(C=False | A=True)

# Calculate the probability of the scenario (A=True, B=True, C=False)
scenario_probability = bayesian_network(P_A, P_B_given_A, P_C_given_A)

print("Probability of scenario (Crime scene=True, Witness B=True, Witness C=False):", scenario_probability)
