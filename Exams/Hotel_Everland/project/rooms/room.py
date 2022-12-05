class Room:
    def __init__(self, family_name, budget, members_count):
        self.members_count = members_count
        self.family_name = family_name
        self.budget = budget
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')
        self._expenses = value

    def calculate_expenses(self, *args):
        pass

    # Each element of args will be
    # a list (with children or appliances). Calculate the total
    # cost for a month (30 days) of all elements in the lists and set
    # the expenses attribute to the result.
