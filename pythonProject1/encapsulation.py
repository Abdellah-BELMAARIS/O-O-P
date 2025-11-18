class BankAccount:
    def __init__(self):
        self.balance = 0.0
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

account = BankAccount()
print(account.balance)
account.deposit(1.99)
print(account.balance)
account.withdraw(1)
print(account.balance)

print("\n" + "=" * 50 + "\n")
class BankAccount2:
    def __init__(self):
        self._balance = 0.0
    @property
    def balance(self):
        return self._balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

account2 = BankAccount2()
print(account2.balance)
account2.deposit(1.99)
print(account2.balance)
account2.withdraw(1)
print(account2.balance)