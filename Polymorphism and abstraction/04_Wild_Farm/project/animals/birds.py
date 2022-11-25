from . animal import Bird


class Owl(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    @staticmethod
    def allowed_foods():
        return ['Meat']

    @property
    def weight_gain_per_item(self):
        return 0.25


class Hen(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    @staticmethod
    def allowed_foods():
        return ['Meat', 'Vegetable', 'Seed', 'Fruit']

    @property
    def weight_gain_per_item(self):
        return 0.35
