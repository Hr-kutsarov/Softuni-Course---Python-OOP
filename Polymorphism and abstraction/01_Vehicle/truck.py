from abc import ABC, abstractmethod


class Vehicle(ABC):
    AC_FUEL_CONSUMPTION = 0

    @abstractmethod
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.AC_FUEL_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Car(Vehicle):
    AC_FUEL_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)


class Truck(Vehicle):
    AC_FUEL_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    # override abstract method
    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)



