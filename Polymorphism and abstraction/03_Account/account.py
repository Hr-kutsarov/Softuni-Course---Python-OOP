class Account:
    def __init__(self, owner, starting_amount=0):
        self.owner = owner
        self.starting_amount = starting_amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        balance = self.starting_amount + transaction_amount
        if balance < 0:
            raise ValueError('sorry cannot go in debt!')
        self.starting_amount += transaction_amount
        self._transactions.append(transaction_amount)
        return f"New balance: {self.starting_amount}"

    def add_transaction(self, amount):
        balance = self.starting_amount + amount

        if type(amount) != int:
            raise ValueError("please use int for amount")
        if balance < 0:
            raise ValueError("sorry cannot go in debt!")

        self._transactions.append(amount)
        self.starting_amount += amount
        return f"New balance: {self.starting_amount}"

    def balance(self):
        return self.starting_amount

    def __str__(self):
        return f"Account of bob with starting amount: {self.starting_amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.starting_amount})"

    def __len__(self):
        return len(self._transactions)

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.starting_amount > other.starting_amount

    def __ge__(self, other):
        return self.starting_amount >= other.starting_amount

    def __eq__(self, other):
        return self.starting_amount == other.starting_amount

    def __add__(self, other):
        new_owner = self.owner + "&" + other.owner
        new_amount = self.starting_amount + other.starting_amount
        return Account(new_owner, new_amount)

    def __iter__(self):
        return iter(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]
