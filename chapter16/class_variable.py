"""
    CHAPTER NO. 16
    TUTORIAL NO. 190
    OOP - CLASS VARIABLE
"""


class Laptop:
    discount = 10 # this is class variable

    def __init__(self, brand_name, model, price):
        # instance variable
        self.brand = brand_name
        self.model = model
        self.price = price

    def apply_discount(self):
        price = self.price
        percentage = (Laptop.discount * price) / 100
        return f'Total Price : {price}\nDiscounted Price is {price - percentage}'


buy_laptop = Laptop('hp', 'Latitude e5540', 63000)
print(buy_laptop.apply_discount())
