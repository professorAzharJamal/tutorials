# Define events
event_A = "It rains today"
event_B = "The ground is wet"

# Define probabilities
P_A = 0.4  # Probability of raining today (prior probability)
P_B = 0.5  # Probability of ground being wet (prior probability)
P_B_given_A = 0.8  # Probability of wet ground given it rains (likelihood)

# Calculate probability of rain given wet ground using Bayes' theorem
P_A_given_B = (P_B_given_A * P_A) / P_B

# Print the result
print(f"The probability of rain today given the ground is wet is: {P_A_given_B:.2f}")
