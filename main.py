class Bank_Account:
    def __init__(self, num, name, balance):
        self.num = num
        self.name = name
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, amt):
        if self.balance < amt:
            print("Error, you do not have enough money!")
        else:
            self.balance -= amt

    def transfer(self, receiver, amt):
        self.balance -= amt
        receiver.balance += amt
        print("Successfully transferred " + str(amt) + " to " + receiver.name)
        print("Your Balance is " + str(self.balance))


my_account = Bank_Account(194307, "Ayden", 500)
account_2 = Bank_Account(194308, "Jason", 500)

# my_account.deposit(1001)
# my_account.withdraw(1000)
my_account.transfer(account_2, 100)
