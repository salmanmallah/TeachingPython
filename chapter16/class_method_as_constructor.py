"""
    CHAPTER NO. 16
    TUTORIAL NO. 195
    OOP - CLASS METHODS AS CONSTRUCTOR
"""


class Person:
    count_instance = 0

    def __init__(self, person_name, person_cast, person_age):
        Person.count_instance += 1
        self.name = person_name
        self.cast = person_cast
        self.age = person_age

    # this class method we learn in this tutorial how to just pass one single string in person class'name,cast,age'
    @classmethod
    def from_string(cls, string):
        fname, lname, age = string.split(',')
        return cls(fname, lname, age)

    @classmethod
    def count_class_object(cls):
        return f"you have created {cls.count_instance} objects of {cls.__name__} Class"

    def full_name(self):
        return f"{self.name} {self.cast}"

    def is_over_18(self):
        return self.age > 18


personOne = Person('salman', 'mallah', 22)
personTwo = Person('noman', 'mallah', 16)
personThree = Person('akram', 'mallah', 40)
personFour = Person.from_string('jack, ob, 50')

print(Person.count_class_object())
print(personOne.name)
print(personTwo.name)
print(personThree.name)
print(personFour.name)
print(personFour.age)