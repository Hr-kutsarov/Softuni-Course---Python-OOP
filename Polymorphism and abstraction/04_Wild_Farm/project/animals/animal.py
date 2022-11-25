from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, weight):
        self.weight = weight
        self.name = name
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @property
    @abstractmethod
    def weight_gain_per_item(self):
        pass

    @staticmethod
    @abstractmethod
    def allowed_foods():
        pass

    def feed(self, food):
        food_name = food.__class__.__name__
        if food_name in self.allowed_foods():
            weight_gain = food.quantity * self.weight_gain_per_item
            self.weight += weight_gain
            self.food_eaten += food.quantity
            return f"{self.__class__.__name__} just gained {weight_gain}"
        else:
            return f"{self.__class__.__name__} doesnt not eat {food_name}"


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
