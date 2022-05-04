class BankAccount:
    
    def __init__(self, name, int_rate=.01, balance = 0): 
        self.int_rate=int_rate
        self.balance = balance
        self.name = name
        
    
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= 5
            print(f"Insufficient funds: Charging a $5 fee")
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Account: {self.name} Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance * self.int_rate
            print(f"Interest Rate: {self.int_rate}")
        return self


account1 = BankAccount("Account 1",.20,20000)
account2 = BankAccount("Account 2",.20,500)

account1.deposit(500).deposit(700).deposit(1000).withdraw(300).deposit(1000).yield_interest().display_account_info()

account2.deposit(500).withdraw(70000).withdraw(7000).withdraw(50).withdraw(49).yield_interest().display_account_info()






# Create a BankAccount class with the attributes interest rate and balance


# Add a deposit method to the BankAccount class

# Add a withdraw method to the BankAccount class

# Add a display_account_info method to the BankAccount class

# Add a yield_interest method to the BankAccount class

# Create 2 accounts

# To the first account, make 3 deposits and 1 withdrawal, then yield 
# interest and display the account's info all in one line of code 
# (i.e. chaining)

# To the second account, make 2 deposits and 4 withdrawals, then yield 
# interest and display the account's info all in one line of code 
# (i.e. chaining)

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's 
# info