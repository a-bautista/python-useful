class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount) -> None:
        # write code here
        self.balance = self.balance - amount

    def deposit(self, amount) -> None:
        # write code here
        self.balance = self.balance + amount

    def getBalance(self):
        # write code here
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        # write code here
        return (super().getBalance()*self.interestRate)/100


# code to test - do not edit this
demo1 = SavingsAccount("Mark", 2000, 5)  # initializing a SavingsAccount object