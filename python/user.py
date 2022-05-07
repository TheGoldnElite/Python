class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
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


guido = User("Guido")
monty = User("Monty")
jeff = User("Jeff")

guido.make_deposit(100).make_deposit(500).make_deposit(1000).make_withdrawal(700).display_user_balance()

monty.make_deposit(500).make_deposit(500).make_withdrawal(300).make_withdrawal(100).display_user_balance()

jeff.make_deposit(1000000).make_withdrawal(1000).make_withdrawal(200000).make_withdrawal(80000).display_user_balance()

monty.transfer_money(400,jeff)


