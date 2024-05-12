# Define probabilities
disease_prior = 0.01  # Prior probability of having the disease
test_positive_given_disease = 0.9  # Probability of a positive test if you have the disease
test_positive_given_no_disease = 0.05  # Probability of a positive test if you don't have the disease

# Calculate posterior probability (disease given positive test)
test_result = "positive"
if test_result == "positive":
  posterior_probability = (disease_prior * test_positive_given_disease) / (disease_prior * test_positive_given_disease + (1 - disease_prior) * test_positive_given_no_disease)

print(f"Posterior probability of disease given positive test: {posterior_probability:.4f}")
