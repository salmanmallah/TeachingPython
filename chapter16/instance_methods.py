"""
    CHAPTER NO. 16
    TUTORIAL NO. 187
    OOP - Instance Methods
    -Instance or Objects both are something
    -Methods are those which we define inside a class

"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # creating our own method
    def full_name(self):
        return f'{self.first_name.title()} {self.last_name.title()}'

    # Creating another method
    def is_over_18(self):
        return self.age > 18


object1 = Person('salman', 'mallah', 22)
# print(object1.full_name())
# print(Person.full_name(object1))


l = [1, 2, 3]
# list methods => clear() , pop()
list.clear(l)
print(l)

# l.append(10) common way to append data in the list
list.append(l, 10)  # this is another way you can add data
print(l)

# calling our own object1 method
print(object1.is_over_18())