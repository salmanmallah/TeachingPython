"""
    CHAPTER NO. 16
    TUTORIAL NO. 196
    OOP - STATIC METHOD
    this method is not belongs to object or class but this method has logical relationship with class and object
"""


class Person:
    count_instance = 0

    def __init__(self, person_name, person_cast, person_age):
        Person.count_instance += 1
        self.name = person_name
        self.cast = person_cast
        self.age = person_age

    @classmethod
    def from_string(cls, string):
        fname, lname, age = string.split(',')
        return cls(fname, lname, age)

    @classmethod
    def count_class_object(cls):
        return f"you have created {cls.count_instance} objects of {cls.__name__} Class"

    @staticmethod
    def hello():
        print('Hello static method called!!!')

    def full_name(self):
        return f"{self.name} {self.cast}"

    def is_over_18(self):
        return self.age > 18


personOne = Person('salman', 'mallah', 22)
personTwo = Person('noman', 'mallah', 16)
personThree = Person('akram', 'mallah', 40)
personFour = Person.from_string('jack, ob, 50')

# print(Person.count_class_object())
# Person.hello()

print(personFour.age)