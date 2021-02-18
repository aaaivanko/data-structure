class Parrot():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def description(self):
        return f"Hello, my name is {self.name}, I'm {self.age} years old"

parrot1 = Parrot('Ivan', 22, 80)
parrot2 = Parrot('Andriy', 23, 90)
parrot3 = Parrot('Varvara', 23, 56)

print(parrot3.name)