def choose_outfit(weather, temperature):
  if weather == "sunny":
    if temperature == "hot":
      return "shorts and t-shirt"
    else:
      return "jeans and long sleeve shirt"
  else:
    return "raincoat and boots"

# Example usage
outfit = choose_outfit("rainy", "cold")
print(f"Recommended outfit: {outfit}")
