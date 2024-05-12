def temperature_membership(value):
  # Define fuzzy sets (triangular membership functions)
  cold = max(0, 1 - (value - 10) / 5)
  warm = min(1, max(0, (value - 15) / 5), max(0, 1 - (value - 25) / 5))
  hot = max(0, (value - 20) / 5)

  return cold, warm, hot

# Example usage
temperature = 8
cold_value, warm_value, hot_value = temperature_membership(temperature)

print(f"Temperature: {temperature} degrees")
print(f"Cold membership: {cold_value:.2f}")
print(f"Warm membership: {warm_value:.2f}")
print(f"Hot membership: {hot_value:.2f}")
