"""
    CHAPTER NO. 16
    TUTORIAL NO. 190 | 191
    OOP - CLASS VARIABLE

    Instance variable or object variable are two names of same thing

"""


class Laptop:
    discount_percent = 50  # this is class variable

    def __init__(self, brand_name, model, price):
        # instance variable
        self.brand = brand_name
        self.model = model
        self.price = price

    def apply_discount(self):
        price = self.price
        percentage = (self.discount_percent * price) / 100
        return f'Total Price : {price}\nDiscounted Price is {price - percentage}'


buy_laptop1 = Laptop('hp', 'Latitude e5540', 100)
buy_laptop2 = Laptop('dell', 'atutx', 100)

buy_laptop2.discount_percent = 25
print(buy_laptop2.__dict__)
print(buy_laptop2.apply_discount())

buy_laptop1.discount_percent = 100
print(buy_laptop1.apply_discount())
print(buy_laptop1.__dict__)


