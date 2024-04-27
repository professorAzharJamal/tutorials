class Category:
    def __init__(self, name):
        self.name = name
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

class Object:
    def __init__(self, name):
        self.name = name

# Create categories
category1 = Category("Animals")
category2 = Category("Fruits")

# Create objects
cat = Object("Cat")
dog = Object("Dog")
apple = Object("Apple")
banana = Object("Banana")

# Add objects to categories
category1.add_object(cat)
category1.add_object(dog)
category2.add_object(apple)
category2.add_object(banana)

# Display categories and their objects
print("Category:", category1.name)
print("Objects:", [obj.name for obj in category1.objects])

print("Category:", category2.name)
print("Objects:", [obj.name for obj in category2.objects])
