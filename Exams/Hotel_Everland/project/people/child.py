class Child:
    def __init__(self, cost, *args):
        self.cost = cost + sum([int(x) for x in args])
