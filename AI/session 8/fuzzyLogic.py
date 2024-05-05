# Define membership functions (simplified)
def is_cold(temperature):
  if temperature <= 15:
    return 1.0  # Fully cold
  elif temperature <= 20:
    return (20 - temperature) / 5  # Gradually decreasing coldness
  else:
    return 0.0  # Not cold

def is_comfortable(temperature):
  if temperature >= 20 and temperature <= 25:
    return 1.0  # Perfectly comfortable
  elif temperature >= 18 and temperature <= 28:
    return min((temperature - 18) / 5, (28 - temperature) / 5)  # Gradually decreasing/increasing comfort
  else:
    return 0.0  # Not comfortable

# Example temperature
temperature = 13

# Get degree of coldness and comfort
cold_degree = is_cold(temperature)
comfort_degree = is_comfortable(temperature)

# Print results (simplified)
print(f"Temperature: {temperature} degrees Celsius")
print(f"Degree of coldness: {cold_degree}")
print(f"Degree of comfort: {comfort_degree}")

# Simple rule (assuming higher comfort is preferred)
if comfort_degree > 0.1:
  print("It's comfortable. No need for adjustments.")
else:
  print("It's a bit cold. Consider wearing warmer clothes.")
