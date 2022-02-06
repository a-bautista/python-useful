class AnimalSound:
    def Sound(self, animal):
        animal.Speak()

class Dog:
    def Speak(self):
        print("Woof woof!")

class Cat:
    def Speak(self):
        print("Meow meow!")


sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.Sound(dog)
sound.Sound(cat)


'''
    Duck typing refers to using Polymorphism without inheritance.
    
    Similarly, in the above example, the animal object does not
    matter in the definition of the Sound method as long as it has 
    the associated behavior, Speak(), defined in the object’s class 
    definition. In layman terms, since both the animals, dog and cats,
    can speak like animals, they both are animals. This is how we have 
    achieved polymorphism without inheritance.
'''