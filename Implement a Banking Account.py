# 4: Implement a Banking Account

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

account1 = SavingsAccount("Ashish", 5000, 5)
print(account1.title)  
print(account1.balance)  
print(account1.interestRate)  

# output  # Ashish is the title and 5000 is the balance and 5 is the interestRate.
Ashish
5000
5

# 5: Handling a Bank Account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    def withdrawal(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
    def getBalance(self):
        return self.balance
    
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    def interestAmount(self):
        return (self.balance * self.interestRate)/100

demo1 = SavingsAccount("Ashish", 2000, 5)
demo1.deposit(500)
print(demo1.getBalance()) 

demo1 = SavingsAccount("Ashish", 2000, 5)
demo1.withdrawal(500)
print(demo1.getBalance()) 

demo1 = SavingsAccount("Ashish", 2000, 5)
print(demo1.interestAmount()) 

# output 

2500
1500
100.0


