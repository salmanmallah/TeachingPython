"""
    CHAPTER NO. 16
    TUTORIAL NO. 194
    OOP - CLASS METHODS

        -Class methods
        -Different between class methods and instance methods
"""


class Person:
    count_instance = 0

    def __init__(self, person_name, person_cast, person_age):
        Person.count_instance += 1
        self.name = person_name
        self.cast = person_cast
        self.age = person_age

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

# print(personOne.full_name())
# print(personOne.is_over_18())

print(Person.count_class_object())
# print(personOne.count_class_object())
