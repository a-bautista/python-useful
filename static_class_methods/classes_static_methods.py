class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Rolf")
player_one.numbers =  (1,2,3,4)
player_two = LotteryPlayer("Adam")

print(player_one.numbers, player_two.numbers)

class Student:
    def __init__ (self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    # self is necessary because whenever you call the object.method, the self is passed implicitly in the parenthesis
    #def go_to_school(self):
    #    print("I am going to school.")

    # The class method calls directly to the class attributes, so you don't have to put any argument inside the parenthesis
    #@classmethod
    #def go_to_school(cls):
    #    print("I'm going to school.")
    #    print("I'm a {}".format(cls))

    # Static methods can be called without the self argument, you
    @staticmethod
    def go_to_school():
        print("I'm going to school.")


anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(71)
print(anna.average())
print(anna.go_to_school())
print(Student.go_to_school())