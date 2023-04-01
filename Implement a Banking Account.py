# 4: Implement a Banking Account

# class Account:
#     def __init__(self, title, balance):
#         self.title = title
#         self.balance = balance

# class SavingsAccount(Account):
#     def __init__(self, title, balance, interestRate):
#         super().__init__(title, balance)
#         self.interestRate = interestRate

# account1 = SavingsAccount("Ashish", 5000, 5)
# print(account1.title)  
# print(account1.balance)  
# print(account1.interestRate)  

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

acc1 = SavingsAccount("Ashish", 2000, 5)
acc1.deposit(500)
print(acc1.getBalance()) 

acc1 = SavingsAccount("Ashish", 2000, 5)
acc1.withdrawal(500)
print(acc1.getBalance()) 

acc1 = SavingsAccount("Ashish", 2000, 5)
print(acc1.interestAmount()) 


