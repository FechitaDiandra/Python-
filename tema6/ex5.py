class Animal:
    def __init__(self, species, habitat):
        self.species = species
        self.habitat = habitat


class Mammal(Animal):
    def __init__(self, species, habitat, leg_count):
        super().__init__(species, habitat)
        self.leg_count = leg_count

    def get_leg_count(self):
        return self.leg_count

    def use_legs(self):
        print("mammal doing something: I am using my legs,", self.leg_count, "in total")

    def print(self):
        print("Printing for Mammal")
        print("leg count:", self.get_leg_count())
        self.use_legs()

class Bird(Animal):
    def __init__(self, species, habitat, wingspan):
        super().__init__(species, habitat)
        self.wingspan = wingspan

    def get_wingspan(self):
        return self.wingspan

    def fly(self):
        print("bird doing something: I am using my wings, having a wingspan", self.wingspan)

    def print(self):
        print("Printing Bird")
        print("wingspan: ",self.get_wingspan())
        self.fly()

class Fish(Animal):
    def __init__(self, species, habitat, length):
        super().__init__(species, habitat)
        self.length = length

    def get_length(self):
        return self.length

    def swim(self):
        print("fish doing something: Swimming with length", self.length)

    def print(self):
        print("Printing Fish")
        print("fish length:", self.get_length())
        self.swim()


animals = [Mammal("koala", "savanna", "4"), Bird("falcon", "forest", 1.4), Fish("sardine", "water", 0.3)]

for animal in animals:
    animal.print()
    print()