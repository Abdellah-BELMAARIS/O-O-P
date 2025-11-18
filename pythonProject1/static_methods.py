class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner}'s new balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account = BankAccount("Alice", 500)

account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))


class Person:
    def __init__(self, name, email, address) -> None:
        self.name = name
        self._email = email
        self.__home_address = address

    def print_details(self):
        print(
            f"Name: {self.name}; Email: {self._email}; Address: {self.__home_address}"
        )


person = Person("danny", "danny@gmail.com", "200 Springfield way, UK")
person.print_details()

print(person.name)
print(person._email)
print(person._Person__home_address)