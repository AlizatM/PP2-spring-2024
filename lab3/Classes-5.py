class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit of {} accepted".format(amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal of {} accepted".format(amount))
        else:
            print("Insufficient funds")

    def display_balance(self):
        print("Balance:", self.balance)

account = BankAccount("Ali", 1000)
account.display_balance()
account.deposit(500)
account.display_balance()
account.withdraw(200)
account.display_balance()
account.withdraw(2000)
