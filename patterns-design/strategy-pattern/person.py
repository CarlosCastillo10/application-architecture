class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return str({"name": self.name, "age": self.age})

    
    def get_name():
        return self.name

    def get_age():
        return self.age
