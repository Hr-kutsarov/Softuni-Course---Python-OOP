from abc import ABC, abstractmethod


class Movie(ABC):
    @abstractmethod
    def __init__(self, title, year, owner, age_restriction):
        self.owner = owner
        self.likes = 0
        self.age_restriction = age_restriction
        self.year = year
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value == "":
            raise ValueError("The title cannot be empty string!")
        self._title = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")
        self._year = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if value.__class__.__name__ != 'User':
            raise ValueError("The owner must be an object of type User!")
        self._owner = value

    @abstractmethod
    def details(self):
        # TODO returns a string with information about the movie by its type
        pass

