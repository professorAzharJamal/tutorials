# Knowledge base (replace with real data)
movies = {
    "action": [
        {"title": "The Matrix", "year": 1999},
        {"title": "Mad Max: Fury Road", "year": 2015}
    ],
    "comedy": [
        {"title": "Monty Python and the Holy Grail", "year": 1975},
        {"title": "The Big Lebowski", "year": 1998}
    ],
    "drama": [
        {"title": "The Shawshank Redemption", "year": 1994},
        {"title": "Schindler's List", "year": 1993}
    ]
}

def recommend_movie(genre, year_preference):
  """Recommends a movie based on user's genre preference and year preference (newer/older)."""
  recommendations = []
  for movie in movies.get(genre, []):  # Get movies in the desired genre (or empty list if genre not found)
    if year_preference == "newer" and movie["year"] >= 2000:
      recommendations.append(movie["title"])
    elif year_preference == "older" and movie["year"] < 2000:
      recommendations.append(movie["title"])
  
  if recommendations:
    return f"Here's a {genre} movie recommendation for you: {recommendations[0]}"
  else:
    return f"Sorry, no movies found matching your criteria for {genre}."

# Example usage
user_genre = input("What genre are you interested in (action, comedy, drama)? ")
user_year_preference = input("Do you prefer newer (after 2000) or older movies? ")

recommendation = recommend_movie(user_genre, user_year_preference)
print(recommendation)
