class BankAccount:
    def __init__(self, balance = 0, int_rate = 1):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amt):
        self.balance += amt
        return self

    def withdraw(self, amt):
        if(self.balance>=amt):
            self.balance -= amt
        else:
            self.balance -= 5
            print("Insufficient funds: chargin a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        interest = self.int_rate/100
        self.balance += self.balance * interest
        return self
    

class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.account = BankAccount(int_rate=.02, balance=0)

    def make_deposit(self, amt):
        self.deposit(amt)
        return self

    def make_withdrawal(self, amt):
        self.withdraw(amt)
        return self
    
    def display_user_balance(self):
        print(f"{self.name}'s account balance is {self.display_account_info}")
        return self

    def transfer_money(self, other_user, amt):
        other_user.deposit(amt)
        self.deposit(amt)
        print(f"{self.name} transfers {amt} dollars to {other_user.name}")
        return self




chris = User("Chris Morton", "c@c.com")
chris.make_deposit(90).display_user_balance()
