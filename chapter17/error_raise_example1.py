"""
    CHAPTER NO. 17
    TUTORIAL NO. 205
    ERROR RAISE EXAMPLE 1
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError('you have not define this method in your subclass')


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'bhow bhow'


class Cat(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age = age

    def sound(self):
        return 'meow meow'


dog1 = Dog('moti', 'German shephard')
print(dog1.sound())
