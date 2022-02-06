class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def Animal_details(self):
        print("Name: ", self.name)
        print("Sound: ", self.sound)

class Dog(Animal):
    # property = None

    def __init__(self, name, sound, property):
        super().__init__(name, sound)
        self.property = property

    def Animal_details(self):
        super().Animal_details()
        print("Family: ", self.property)

class Sheep(Animal):
    
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def Animal_details(self):
        super().Animal_details()
        print("Color: ", self.color)

d = Dog("Pongo", "Woof Woof", "Husky")
d.Animal_details()

s = Sheep("Billy", "Baaa Baaa", "White")
s.Animal_details()