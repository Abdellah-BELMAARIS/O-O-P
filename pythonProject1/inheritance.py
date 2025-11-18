class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting.")

    def stop(self):
        print("Vehicle is stopping.")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels=4):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

    def start(self):
        print(f"{self.brand} {self.model} car is starting with a key or button.")


class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels=2):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels

    def start(self):
        print(f"{self.brand} {self.model} bike is starting with a kick or button.")


# Create instances
car = Car("Ford", "Focus", 2008, 5, 4)
bike = Bike("Honda", "Scoopy", 2018, 2)

# Print information
print("Car details:", car.__dict__)
print("Bike details:", bike.__dict__)
print("\nFormatted output:")
print(f"Car: {car}")
print(f"Bike: {bike}")

# Demonstrate methods
print("\nStarting vehicles:")
car.start()
bike.start()

print("\nStopping vehicles:")
car.stop()
bike.stop()