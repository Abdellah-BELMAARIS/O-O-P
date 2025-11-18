class Dog:
    def bark(self):
        print("Woof woof")

dog = Dog()
dog.bark()

class Dog2:
    def __init__(self, first_name, last_name, breed):
        self.first_name = first_name
        self.last_name = last_name
        self.breed = breed

    def bark(self):
        print("Woof woof")

    def get_full_name(self):
        return self.first_name + " " + self.last_name

scottyDog = Dog2("Angus", "Biggsby", "Scottish Terrier")
scottyDog.bark()
print(scottyDog.get_full_name())
print(scottyDog.breed)

houndDog = Dog2("Elvis", "Presley", "Basset Hound")
houndDog.bark()
print(houndDog.get_full_name())
print(houndDog.breed)

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number

class Dog3:
    def __init__(self, first_name, last_name, breed, owner):
        self.first_name = first_name
        self.last_name = last_name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Woof woof")

    def get_full_name(self):
        return self.first_name + " " + self.last_name

owner = Owner("Danny", "122 Springfield Way, UK", "8888 888 888")
scottyDog = Dog3("Bruce", "Biggs", "Scottish Terrier", owner)
print(scottyDog.owner.name)