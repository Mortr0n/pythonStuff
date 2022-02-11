from bank_account import BankAccount

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount()

    def make_deposit(self, amt):
        self.account.deposit(amt)
        return self

    # can either print using returned account_balance in the print statement or 
    # calling the display_account_info() by itself
    def display_user_balance(self):
        print(f"{self.name}'s")
        self.account.display_account_info()
        return self



chris = User("Chris Morton", "c@c.com")

chris.make_deposit(45).display_user_balance()
