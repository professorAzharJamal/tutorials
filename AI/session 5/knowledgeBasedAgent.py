import csv

def load_restaurants(filename):
  """Loads restaurant data from a CSV file."""
  restaurants = {}
  with open(filename, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      cuisine = row["cuisine"]
      restaurants.setdefault(cuisine, []).append(row)
  return restaurants

def recommend_restaurant(restaurants, cuisine, price_range):
  """Recommends a restaurant based on user preferences."""
  for c, restaurants_list in restaurants.items():
    if c.lower() == cuisine.lower():  # Case-insensitive match
      for restaurant in restaurants_list:
        if restaurant["price_range"] == price_range:
          return restaurant["name"]
  return "No restaurant found matching your criteria."

# Load restaurants from the file (replace "restaurants.csv" with your actual filename)
restaurants = load_restaurants("restaurants.csv")

# User input for preferences
user_cuisine = input("Enter your desired cuisine (e.g., Italian, Indian): ")
user_price_range = input("Enter your preferred price range ($, $$): ")

# Recommend a restaurant based on user input
recommended_restaurant = recommend_restaurant(restaurants, user_cuisine, user_price_range)

print(f"Recommended restaurant: {recommended_restaurant}")
