class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

account = BankAccount("123456789", "John Doe", 1000)
print("Account Holder:", account.account_holder)
print("Account Balance:", account.get_balance())

account.deposit(500)
print("Account Balance:", account.get_balance())

account.withdraw(200)
print("Account Balance:", account.get_balance())

account.withdraw(2000)
print("Account Balance:", account.get_balance())
