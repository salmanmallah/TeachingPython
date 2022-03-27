"""
    CHAPTER NO. 16
    TUTORIAL NO. 184

        -OJCECTIVES
         *what is class
         *how to create a class
         *what is init method | constructor
         *what are attributes, instance, variables.
         *How to create our object
"""


class Person:
    def __init__(self, firstname, lastname, age):
        # instance variables
        self.person_firstname = firstname
        self.persone_lastnname = lastname
        self.persone_age = age


object1 = Person('salman', 'mallah', 22)
object2 = Person('Noman','Mallah', 19)


print(object1.person_firstname)
