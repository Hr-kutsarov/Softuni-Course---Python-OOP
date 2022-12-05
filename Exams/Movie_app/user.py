class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.movies_liked = []  # will contain objects
        self.movies_owned = []  # will contain objects

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError('Invalid username!')
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError('Users under the age of 6 are not allowed!')
        self._age = value

    def __str__(self):
        # todo "Liked movies:"
        # "{details() of each movie liked by the user, on separate lines}"
        # •	If no liked movies: "No movies liked."
        # "Owned movies:"
        # "{details() of every movie owned by the user}"
        # •	If no owned movies: "No movies owned."
        return f"Username: {self.name}, Age: {self.age}"
