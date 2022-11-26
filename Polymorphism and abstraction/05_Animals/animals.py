from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.gender = gender
        self.age = age
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {class_name}"


class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return 'Woof!'


class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return 'Meow meow!'


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, 'Female')

    def make_sound(self):
        return 'Meow'


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, 'Male')

    def make_sound(self):
        return 'Hiss'