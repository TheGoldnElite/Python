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


````````````````````````


"""

make_withdrawal(self, amount) - have this method decrease the user's balance by the amount 
specified
display_user_balance(self) - have this method print the user's name and account balance 
to the terminal
eg. "User: Guido van Rossum, Balance: $150
BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's
 balance by the amount and add that amount to other other_user's balance



Create a file with the User class, including the __init__ and 
make_deposit methods

Add a make_withdrawal method to the User class

Add a display_user_balance method to the User class

Create 3 instances of the User class

Have the first user make 3 deposits and 1 withdrawal and then display their balance

Have the second user make 2 deposits and 2 withdrawals and then display their balance

Have the third user make 1 deposits and 3 withdrawals and then display their balance

BONUS: Add a transfer_money method; have the first user transfer money to the third user 
and then print both users' balances

"""