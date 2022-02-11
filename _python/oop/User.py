class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amt):
        self.account_balance += amt
        return self

    def make_withdrawal(self, amt):
        self.account_balance -= amt
        return self
    
    def display_user_balance(self):
        print(f"{self.name}'s account balance is {self.account_balance}")
        return self

    def transfer_money(self, other_user, amt):
        other_user.account_balance += amt
        self.account_balance -= amt
        print(f"{self.name} transfers {amt} dollars to {other_user.name}")
        return self
        





chris = User("Chris Morton", "c@c.com")
misty = User("Misty Morton", "m@m.com")
jiraiya = User("Jiraiya Morton", "j@j.com")

print(chris.name)
print(misty.name)
print(jiraiya.name)

chris.make_deposit(1000).make_withdrawal(20).make_withdrawal(45).display_user_balance().transfer_money(misty, 345).display_user_balance()
misty.make_deposit(1000).make_deposit(344).make_withdrawal(900).transfer_money(jiraiya, 23).display_user_balance()
jiraiya.make_deposit(1000).make_withdrawal(500).make_withdrawal(344).make_deposit(456).transfer_money(chris, 89).display_user_balance()




        
