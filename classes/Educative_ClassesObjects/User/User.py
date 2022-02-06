class User:
    def __init__(self, username=None, password=None):
        self.__username = username
        self.__password = password

    def login(self, username, password):
        if (self.__username.lower() == username.lower()) and \
            (self.__password.lower() == password.lower()):
            print("access valid")
        else:
            print("access denied")
    
    def getUsername(self):
        return self.__username

    def setUsername(self, username):
        self.__username = username


