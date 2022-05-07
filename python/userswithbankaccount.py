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
    def __init__(self, int_rate=0,balance=0):
        self.int_rate=int_rate
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(self.balance)
        else:
            print("Insufficient funds: Charging $5 fee")
            self.balance -= 5
            print(self.balance)
        return self
    
    def yield_int(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            print(self.balance)
        return self
    
    def display_user_balance(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def transfer_money(self,amount,user):
        self.balance -= amount
        user.balance += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


user1 = User('Jeff')
user2 = User('Bob')
user3 = User('Bri')
user4 = User('Anakin')

user = [user1,user2,user3,user4]

user1.make_deposit(1000).display_user_balance().display_user_balance
user1.make_deposit(250).display_user_balance().display_user_balance

