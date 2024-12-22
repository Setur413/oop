class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print("I'm moving!")

class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying!")

class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming!")

class Dog(Animal):
    def move(self):
        print(f"{self.name} is running!")

# Create some animals
eagle = Bird("Eagle")
nemo = Fish("Nemo")
rex = Dog("Rex")

# Make them move
animals = [eagle, nemo, rex]
for animal in animals:
    animal.move()