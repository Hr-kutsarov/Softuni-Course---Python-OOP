from meals.starter import Starter
from meals.dessert import Dessert
from meals.main_dish import MainDish
from client import Client


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.order_id = 0

    def find_client_in_clients_list_by_phone_number(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client

    def register_client(self, client_phone_number: str):
        found_client = self.find_client_in_clients_list_by_phone_number(client_phone_number)
        if found_client:
            raise Exception('The client has already been registered')
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {new_client.phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        validated_meals = []
        allowed_meals = ['Starter', 'MainDish', 'Dessert']
        for meal in meals:
            if meal.__class__.__name__ in allowed_meals:
                validated_meals.append(meal)
        self.menu.extend(validated_meals)

    def show_menu(self):
        result = ""
        if len(self.menu) < 5:
            raise Exception("The menu is not ready")
        for item in self.menu:
            result += f"{item.details()}\n"
        return result.strip()

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        try_to_find_client = self.find_client_in_clients_list_by_phone_number(client_phone_number)
        if not try_to_find_client:
            self.register_client(client_phone_number)

        client = self.find_client_in_clients_list_by_phone_number(client_phone_number)

        current_bill = 0
        for meal, quantity in meal_names_and_quantities.items():
            found_meal = self.find_meal_by_name(meal, self.menu)
            if not found_meal:
                raise Exception(f"{meal} is not on the menu!")
            if found_meal.quantity < quantity:
                raise Exception(f'Not enough quantity of {meal.__class__.__name__}: {found_meal.name}')

            found_meal.quantity -= quantity
            client.shopping_cart.append(found_meal)
            current_bill += quantity * found_meal.price

        cart = (x.name for x in client.shopping_cart)
        client.bill += current_bill
        return f"Client {client.phone_number} successfully ordered {', '.join(cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.find_client_in_clients_list_by_phone_number(client_phone_number)
        client.bill = 0.0
        if len(client.shopping_cart) == 0:
            raise Exception('There are no ordered meals!')
        client.shopping_cart = []
        return f"{client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        self.order_id += 1
        client = self.find_client_in_clients_list_by_phone_number(client_phone_number)
        current_bill = client.bill
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        client.shopping_cart = []
        client.bill = 0.0

        return f"Receipt #{self.order_id} with total amount of {current_bill:.2f} was successfully paid for {client.phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    @staticmethod
    def find_meal_by_name(meal, menu):
        for item in menu:
            if item.name == meal:
                return item






