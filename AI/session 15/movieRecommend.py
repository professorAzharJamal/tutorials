# Define genres and user preferences
genres = {
    "action": ["fight scenes", "explosions", "adventures"],
    "comedy": ["funny characters", "hilarious situations", "slapstick humor"],
    "drama": ["emotional story", "character development", "thought-provoking themes"]
}

user_prefs = {
    "fight scenes": "action",
    "explosions": "action",
    "adventures": "action",
    "funny characters": "comedy",
    "hilarious situations": "comedy",
    "slapstick humor": "comedy",
    "emotional story": "drama",
    "character development": "drama",
    "thought-provoking themes": "drama"
}

# Function to recommend a movie
def recommend_movie(pref):
  if pref.lower() in user_prefs:
    return f"If you enjoy {pref}, you might like {user_prefs[pref.lower()]} movies."
  else:
    return "Tell me what you enjoy in movies to get a recommendation!"

# Get user input
movie_pref = input("What do you enjoy in movies (e.g., fight scenes, funny characters)? ")

# Get recommendation
recommendation = recommend_movie(movie_pref)

# Print the recommendation
print(recommendation)
