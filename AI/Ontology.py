class Category:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

        if parent:
            parent.children.append(self)

    def is_descendant_of(self, category):
        if self.parent is None:
            return False
        elif self.parent == category:
            return True
        else:
            return self.parent.is_descendant_of(category)

# Creating categories
animal = Category("Animal")
mammal = Category("Mammal", animal)
bird = Category("Bird", animal)
dog = Category("Dog", mammal)
cat = Category("Cat", mammal)
parrot = Category("Parrot", bird)

# Example reasoning
print("Is a dog an animal?", dog.is_descendant_of(animal))  # True
print("Is a cat a bird?", cat.is_descendant_of(bird))  # False
print("Is a parrot a mammal?", parrot.is_descendant_of(mammal))  # False
