class BankAccount:
    
    def __init__(self, name, int_rate=.01, balance = 0): 
        self.int_rate=int_rate
        self.account_balance = balance
        self.name = name
        
    
    def deposit(self, amount):
        self.account_balance += amount
        return self
        
    def withdraw(self, amount):
        if self.account_balance > 0:
            self.account_balance -= 5
            print(f"Insufficient funds: Charging a $5 fee")
        else:
            self.account_balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Account: {self.name} Balance: {self.account_balance}")
        return self
    
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance * self.int_rate
            print(f"Interest Rate: {self.int_rate}")
        return self

class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.account = BankAccount(int_rate=0, balance=0)

    def make_deposit(self, amount):
        self.account += amount
        return self

    def make_withdrawal(self,amount):
        self.amount -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance:{self.amount}")
        return self
    
    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self