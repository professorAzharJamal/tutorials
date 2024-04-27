# Define concepts and relationships as dictionaries
concepts = {
  "Apple": {
    "type": "Fruit",
    "color": "red",
  },
  "Banana": {
    "type": "Fruit",
    "color": "yellow",
  },
  "Fruit": {},  # Parent class without specific attributes
  "Person": {
    "has": ["name", "age"],  # List of attributes
  },
}

# Function to check if a concept is a subclass of another
def is_subclass(sub_concept, super_concept):
  # Check if the sub_concept directly inherits from the super_concept
  if concepts.get(sub_concept).get("type") == super_concept:
    return True
  # Recursively check parent classes if "type" exists
  parent_class = concepts.get(sub_concept).get("type")
  if parent_class and is_subclass(parent_class, super_concept):
    return True
  return False

# Example usage
apple = "Apple"
fruit = "Fruit"
person = "Person"

# Check subclass relationships
print(f"{apple} is a subclass of {fruit}: {is_subclass(apple, fruit)}")
print(f"{person} is a subclass of {fruit}: {is_subclass(person, fruit)}")

# Access concept attributes
print(f"Attributes of {person}: {concepts[person]['has']}")
