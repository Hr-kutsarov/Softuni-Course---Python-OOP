class Client:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0

    @staticmethod
    def validate_phone_number(value):
        if len(value) == 10 and int(value[0]) == 0 and value.isnumeric():
            return value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        validated = self.validate_phone_number(value)
        if validated:
            self.__phone_number = value
        else:
            raise ValueError('Invalid phone number')
