class Student:

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    # Setter methods
    def set_name(self, name):
        self.name = name

    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_age(self, age):
        self.age = age

    # Getter methods
    def get_name(self):
        return self.name

    def get_lastname(self):
        return self.lastname

    def get_age(self):
        return self.age
