from unicodedata import name


class Player:
    # class variables: Dortmund value will be accessed by all the instances of the
    # class Player
    teamName = 'Dortmund'
    teamMembers = []

    @classmethod
    def getTeamName(cls):
        '''
            Class methods are accessed using the class names and can be 
            accessed without creating a class object.
        '''
        return cls.teamName

    @staticmethod
    def static_method():
        '''
             They are used as utility functions inside the class or when 
             we do not want the inherited classes to modify a method definition
        '''
        print("Static method activated")

    def __init__(self, name, salary) -> None:
        # instance variables: accessed only by the current instance
        self.name = name 
        self.formerTeams = []
        self.teamMembers.append(self.name)
        self.__salary = salary # this is a private property

    def demo(self, a, b, c, d= 5, e= None):
        '''
            There's no such thing as method overloading but you can overload
            a method but you can overload a method implicitly.
        '''
        print("a = ", a)
        print("b = ", b)
        print("c = ", c)
        print("d = ", d)
        print("e = ", e)
        
    def reveal_salary(self):
        print(self.__salary)

    def __reveal_id():
        '''
            Private method
        '''
        pass


    


