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
    
    def account_balance(self):
        return self.balance
    
    def yield_interest(self):
        interest = self.int_rate/100
        self.balance += self.balance * interest
        return self
    

account = BankAccount(150, 2)
newaccount = BankAccount(300)

# account.deposit(50).display_account_info().yield_interest().display_account_info().withdraw(90).display_account_info().withdraw(200).display_account_info()