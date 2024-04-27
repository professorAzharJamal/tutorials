# Define categories and their properties
categories = {
  "mammal": {"properties": {"has_fur": True}, "subcategories": ["lion", "elephant"]},
  "bird": {"properties": {"has_feathers": True}, "subcategories": ["parrot", "penguin"]},
  "lion": {"properties": {"has_mane": True}, "parent": "mammal"},
  "elephant": {"properties": {"has_trunk": True}, "parent": "mammal"},
  "parrot": {"properties": {"can_talk": True}, "parent": "bird"},
  "penguin": {"properties": {"can_fly": False}, "parent": "bird"},
}

def has_property(category, property_name):
  # Check if the category has the property directly
  if property_name in categories[category]["properties"]:
    return categories[category]["properties"][property_name]
  # Check if a parent category has the property (inheritance)
  parent = categories.get(category, {}).get("parent")
  if parent:
    return has_property(parent, property_name)
  return False

def is_a(object_category, super_category):
  # Check if the object category is a direct subcategory
  if object_category in categories[super_category]["subcategories"]:
    return True
  # Recursively check parent categories for inheritance
  parent = categories.get(object_category, {}).get("parent")
  if parent:
    return is_a(parent, super_category)
  return False

# Example usage
animal = "lion"

print(f"{animal} has fur: {has_property(animal, 'has_fur')}")  # True (inherited from mammal)
print(f"{animal} can fly: {has_property(animal, 'can_fly')}")  # False

print(f"{animal} is a mammal: {is_a(animal, 'mammal')}")  # True
print(f"{animal} is a bird: {is_a(animal, 'bird')}")  # False (not a subcategory)
