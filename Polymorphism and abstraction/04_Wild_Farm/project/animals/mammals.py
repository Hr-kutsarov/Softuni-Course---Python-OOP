from . animal import Mammal


class Mouse(Mammal):
    def make_sound(self):
        return 'Squeak'

    @property
    def weight_gain_per_item(self):
        return 0.1

    @staticmethod
    def allowed_foods():
        return ['Vegetable', 'Fruit']


class Cat(Mammal):
    def make_sound(self):
        return 'Meow'

    @property
    def weight_gain_per_item(self):
        return 0.3

    @staticmethod
    def allowed_foods():
        return ['Vegetable', 'Meat']


class Dog(Mammal):
    def make_sound(self):
        return 'Woof!'

    @property
    def weight_gain_per_item(self):
        return 0.4

    @staticmethod
    def allowed_foods():
        return ['Meat']


class Tiger(Mammal):
    def make_sound(self):
        return 'ROAR!!!'

    @property
    def weight_gain_per_item(self):
        return 1

    @staticmethod
    def allowed_foods():
        return ['Meat']
