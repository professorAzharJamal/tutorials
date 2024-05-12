import random

# Define transition probabilities
sunny_to_sunny = 0.8
sunny_to_rainy = 0.2
rainy_to_sunny = 0.3
rainy_to_rainy = 0.7

# Define emission probabilities
sunny_day_given_sunny_state = 0.9
sunny_day_given_rainy_state = 0.1
rainy_day_given_sunny_state = 0.2
rainy_day_given_rainy_state = 0.8

# Function to simulate a weather sequence with a hidden state
def simulate_weather(num_days):
  # Initialize hidden state (randomly choose sunny or rainy)
  current_state = "sunny" if random.random() < 0.5 else "rainy"
  weather_sequence = [current_state]

  for _ in range(num_days - 1):
    # Transition to the next hidden state based on transition probabilities
    if current_state == "sunny":
      current_state = "sunny" if random.random() < sunny_to_sunny else "rainy"
    else:
      current_state = "sunny" if random.random() < rainy_to_sunny else "rainy"

    # Generate the observed weather based on the current hidden state and emission probabilities
    if current_state == "sunny":
      weather_sequence.append("sunny" if random.random() < sunny_day_given_sunny_state else "rainy")
    else:
      weather_sequence.append("sunny" if random.random() < rainy_day_given_sunny_state else "rainy")

  return weather_sequence

# Simulate a weather sequence for 30 days
weather_sequence = simulate_weather(30)

# Print the simulated weather sequence
print("Simulated Weather Sequence:")
for day, weather in enumerate(weather_sequence):
  print(f"Day {day+1}: {weather}")
