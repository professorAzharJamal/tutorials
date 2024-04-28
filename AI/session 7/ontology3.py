class Animal:
    def __init__(self, name):
        self.name = name
        self.characteristics = []

    def add_characteristic(self, characteristic):
        self.characteristics.append(characteristic)


class Ontology:
    def __init__(self):
        self.animals = {}

    def add_animal(self, animal):
        self.animals[animal.name] = animal

    def get_animal_characteristics(self, animal_name):
        if animal_name in self.animals:
            return self.animals[animal_name].characteristics
        else:
            return None


# Creating instances of animals and adding characteristics
lion = Animal("Lion")
lion.add_characteristic("Carnivore")
lion.add_characteristic("Feline")

elephant = Animal("Elephant")
elephant.add_characteristic("Herbivore")
elephant.add_characteristic("Pachyderm")

# Creating ontology and adding animals
animal_ontology = Ontology()
animal_ontology.add_animal(lion)
animal_ontology.add_animal(elephant)

# Retrieving characteristics of animals from ontology
print("Characteristics of Lion:", animal_ontology.get_animal_characteristics("Lion"))
print("Characteristics of Elephant:", animal_ontology.get_animal_characteristics("Elephant"))
print("Characteristics of Giraffe:", animal_ontology.get_animal_characteristics("Giraffe"))
