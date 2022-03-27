"""
    CHAPTER NO. 16
    TUTORIAL NO. 202
    Magic/ dundar methods,
    Operator overloading,
    polymorphism

"""


class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f'{self.brand} {self.model} price is : {self.price}'

    # __str__  | __repr__
    def __str__(self):
        return f'{self.brand} {self.model}'

    def __repr__(self):
        return f'Phone(\'{self.brand}\', \'{self.model}\', {int(self.price)})'


phone = Phone('Nokia', '1100', 5000)
# print(str(phone))
# print(repr(phone))

l = [1, 2, 3]
print(len(l))