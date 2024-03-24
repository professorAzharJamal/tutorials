def is_cold(temperature):
  return temperature < 18

def heat_on(is_cold):
  if is_cold:
    return "Turn on heater"
  else:
    return "Turn off heater"

# Set the current temperature
current_temp = 15

# Let the thermostat decide what to do
action = heat_on(is_cold(current_temp))

# Print the thermostat action
print(action)