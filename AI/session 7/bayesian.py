# Probabilities (assuming pre-calculated or estimated values)
# P(A) - Prior probability of event A
# P(B|A) - Likelihood of event B given event A is true

# Example: Is it likely to rain today?
rain_prior = 0.3  # Prior probability of rain (30%)
cloudy_given_rain = 0.71  # Likelihood of it being cloudy given it's raining (90%)
cloudy_today = False  # Observed fact: It's cloudy today

# Calculate posterior probability (probability of rain given it's cloudy) using Bayes' rule
def posterior_probability(rain_prior, cloudy_given_rain, cloudy_today):
  # Assuming no event is completely impossible (avoid division by zero)
  sunny_given_not_rain = 0.01  # Likelihood of it being sunny given it's not raining (small value)
  total_likelihood = cloudy_given_rain * rain_prior + (1 - cloudy_given_rain) * (1 - rain_prior)
  return (cloudy_given_rain * rain_prior) / total_likelihood

# Calculate posterior probability
rain_posterior = posterior_probability(rain_prior, cloudy_given_rain, cloudy_today)

# Print results
print(f"Prior probability of rain: {rain_prior:.2f}")
print(f"Likelihood of cloudy given rain: {cloudy_given_rain:.2f}")
print(f"Observed fact: It's {'cloudy' if cloudy_today else 'sunny'} today")
print(f"Posterior probability of rain given it's cloudy: {rain_posterior:.2f}")

# Simple interpretation (adjust based on your specific scenario)
if rain_posterior > 0.5:
  print("It's more likely to rain today based on the observed cloudiness.")
else:
  print("It's less likely to rain today based on the observed cloudiness.")
