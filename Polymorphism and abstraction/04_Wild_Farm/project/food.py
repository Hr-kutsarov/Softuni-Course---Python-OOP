from abc import ABC, abstractmethod


class Food(ABC):

    @abstractmethod
    def __init__(self, quantity):
        self.quantity = quantity


class Meat(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Vegetable(Food):
    def __init__(self, quantity):
        super().__init__(quantity)
