class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def sayHiToUser(self, user):
        print(
            f"Sending message to {user.username}: Hi {user.username}, it's {self.username} ;)"
        )


user1 = User("dantheman", "dan@gmail.com", "123")
user2 = User("batman", "bat@gmail.com", "abc")
user1.sayHiToUser(user2)

print(user1.email)

user1.email = "dan@outlook.com"  # Fixed: added missing @

print(user1.email)

from datetime import datetime


class User2:
    def __init__(self, username, email, isAdmin=False):
        self.username = username
        self._email = email  # Using protected attribute
        self.isAdmin = isAdmin

    def getEmail(self):
        if self.isAdmin:
            print(f"Email accessed at {datetime.now()}")
            return self._email
        return None

    def setEmail(self, newEmail):
        if "@" in newEmail:
            self._email = newEmail


user1 = User2("dantheman", "dan@gmail.com", True)
print(user1._email)
print(user1.getEmail())

user1.setEmail("dan@outlook.com")
print(user1.getEmail())


class User3:
    def __init__(self, username, email, isAdmin=False):
        self.username = username
        self.isAdmin = isAdmin
        # Use the property setter to validate initial email
        self.email = email  # This calls the @email.setter

    @property
    def email(self):
        if self.isAdmin:
            return self._email
        print("Not admin, so can't access email")
        return None

    @email.setter
    def email(self, newEmail):
        if "@" in newEmail:
            self._email = newEmail
        else:
            raise ValueError("Invalid email: no '@'")


user1 = User3("dantheman", "dan@gmail.com", True)
print(user1.email)
try:
    user1.email = "dayyn@gmail.com"  # Fixed typo in email
except ValueError as e:
    print(f"Error: {e}")

print(user1.email)


class User4:
    total_users_created = 0

    def __init__(self, username, email, isAdmin=False):
        self.username = username
        self.isAdmin = isAdmin
        # Use the property setter to validate initial email
        self.email = email

        User4.total_users_created += 1

    @property
    def email(self):
        if self.isAdmin:
            return self._email
        print("Not admin, so can't access email")
        return None

    @email.setter
    def email(self, newEmail):
        if "@" in newEmail:
            self._email = newEmail
        else:
            raise ValueError("Invalid email: no '@'")


print(User4.total_users_created)
user = User4("dantheman", "dan@gmail.com", True)
print(User4.total_users_created)
user2 = User4("joetheman", "joe@gmail.com", False)
print(User4.total_users_created)
user3 = User4("sally123", "sal@gmail.com", False)  # Fixed: changed user4 to user3
print(User4.total_users_created)