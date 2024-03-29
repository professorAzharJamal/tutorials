def friends_rule(friendships, weight, person1, person2):
  """
  This function simulates a simple MLN rule for friendship prediction.

  Args:
      friendships: A dictionary representing friendships (key: person, value: list of friends).
      weight: The weight of the rule (probability strength).
      person1: The first person.
      person2: The second person.

  Returns:
      The probability of person2 being a friend of person1 based on the rule.
  """

  # Check if person1 is a friend of person2 based on existing data
  is_friend = person1 in friendships.get(person2, [])

  # Apply the rule weight to the friendship existence
  probability = weight * is_friend

  return probability

def similar_interests_rule(interests, weight, person1, person2):
  """
  This function simulates a simple MLN rule for friendship based on similar interests.

  Args:
      interests: A dictionary representing interests (key: person, value: list of interests).
      weight: The weight of the rule (probability strength).
      person1: The first person.
      person2: The second person.

  Returns:
      The probability of person2 being a friend of person1 based on the rule.
  """

  # Calculate the number of shared interests
  shared_interests = len(set(interests.get(person1, [])) & set(interests.get(person2, [])))

  # Apply the rule weight based on the number of shared interests (more shared interests, higher probability)
  probability = weight * shared_interests

  return probability

def predict_friendship(friendships, interests, weight_friends, weight_interests, person1, person2):
  """
  This function predicts the probability of friendship using two MLN rules.

  Args:
      friendships: A dictionary representing friendships (key: person, value: list of friends).
      interests: A dictionary representing interests (key: person, value: list of interests).
      weight_friends: The weight of the friendship rule.
      weight_interests: The weight of the similar interests rule.
      person1: The first person.
      person2: The second person.

  Returns:
      The combined probability of friendship based on both rules.
  """

  # Calculate probabilities from each rule
  probability_friends = friends_rule(friendships, weight_friends, person1, person2)
  probability_interests = similar_interests_rule(interests, weight_interests, person1, person2)

  # Simple combination of rule probabilities (assuming independence for simplicity)
  combined_probability = probability_friends + probability_interests

  return combined_probability

# Example usage
friendships = {
  "John": ["Alice", "Bob"],
  "Alice": ["John", "Mary"],
  "Bob": ["John"]
}

interests = {
  "John": ["Sports", "Music"],
  "Alice": ["Music", "Movies"],
  "Bob": ["Sports"],
  "Mary": ["Movies", "Art"]
}

weight_friends = 0.7  # Weight of the friendship rule
weight_interests = 0.5  # Weight of the similar interests rule

# Predict if Mary is a friend of John based on both rules
probability_mary_friend = predict_friendship(friendships, interests, weight_friends, weight_interests, "John", "Mary")

print(f"Probability of Mary being John's friend based on combined rules: {probability_mary_friend}")
