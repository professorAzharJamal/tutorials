# Probability of event A
P_A = 0.4

# Probability of event B
P_B = 0.6

# Joint probability of A and B (assuming independence)
P_AB = P_A * P_B

# Calculate the probability of A or B using the addition rule
P_A_or_B = P_A + P_B - P_AB

# Calculate conditional probability P(A|B)
P_A_given_B = P_AB / P_B

# Calculate conditional probability P(B|A)
P_B_given_A = P_AB / P_A

# Print the results
print("Probability of event A:", P_A)
print("Probability of event B:", P_B)
print("Probability of A and B:", P_AB)
print("Probability of A or B:", P_A_or_B)
print("Conditional probability P(A|B):", P_A_given_B)
print("Conditional probability P(B|A):", P_B_given_A)
