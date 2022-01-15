"""
    CHAPTER NO. 16
    TUTORIAL NO. 192 | 193
    OOP - EXERCISE THREE
"""
# from itertools import count
#
#
# class Person:
#     count_object = count(0)
#
#     def __init__(self, person_name, persone_cast, person_age):
#         self.id = next(self.count_object)
#         self.name = person_name
#         self.cast = persone_cast
#         self.age = person_age


class Person:
    count_object = 0

    def __init__(self, person_name, persone_cast, person_age):
        Person.count_object += 1
        self.name = person_name
        self.cast = persone_cast
        self.age = person_age


personeOne = Person('salman', 'mallah', 22)
personeTwo = Person('noman', 'mallah', 19)
personeThree = Person('akram', 'mallah', 45)


print(Person.count_object)
