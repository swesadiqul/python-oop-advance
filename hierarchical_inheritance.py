class Vehicle:
    def __init__(self, wheels, engine_type):
        self.wheels = wheels
        self.engine_type = engine_type

class Car(Vehicle):
    def __init__(self):
        super().__init__(4, "Gasoline")

class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__(2, "Gasoline")

class Truck(Vehicle):
    def __init__(self):
        super().__init__(18, "Diesel")

car = Car()
motorcycle = Motorcycle()
truck = Truck()

print(car.wheels, car.engine_type)             # Output: 4 Gasoline
print(motorcycle.wheels, motorcycle.engine_type) # Output: 2 Gasoline
print(truck.wheels, truck.engine_type)           # Output: 18 Diesel
