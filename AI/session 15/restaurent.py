# Define cuisines and preferences
cuisines = {
    "italian": ["pasta", "pizza", "seafood"],
    "mexican": ["tacos", "burritos", "enchiladas"],
    "indian": ["curry", "tandoori", "biryani"],
    "chinese": ["noodles", "fried rice", "stir-fry"]
}

preferences = {
    "pasta": "italian",
    "pizza": "italian",
    "tacos": "mexican",
    "burritos": "mexican",
    "curry": "indian",
    "tandoori": "indian",
    "noodles": "chinese",
    "fried_rice": "chinese"
}

# Function to recommend a restaurant
def recommend_restaurant(fav_dish):
  if fav_dish.lower() in preferences:
    return f"Based on your love for {fav_dish}, you might enjoy {preferences[fav_dish.lower()]} cuisine."
  else:
    return "Tell me about your favorite dish to get a recommendation!"

# Get user input
fav_dish = input("What's your favorite dish? ")

# Get recommendation
recommendation = recommend_restaurant(fav_dish)

# Print the recommendation
print(recommendation)
