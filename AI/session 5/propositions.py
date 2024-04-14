def get_user_boolean(prompt):
  """Gets user input as True or False based on a prompt."""
  while True:
    response = input(prompt + " (y/n): ").lower()
    if response in ("y", "yes"):
      return True
    elif response in ("n", "no"):
      return False
    else:
      print("Invalid input. Please enter 'y' or 'n'.")

def weather_advice():
  """Provides weather advice based on user input."""
  raining = get_user_boolean("Is it raining?")
  windy = get_user_boolean("Is it windy?")

  if raining and windy:
    print("Bring an umbrella and a jacket! It's gonna be a rough day.")
  elif raining:
    print("Bring an umbrella! It's drizzling outside.")
  elif windy:
    print("It's a bit windy, dress warmly!")
  else:
    print("Looks like good weather today!")

weather_advice()
