"""
    CHAPTER NO. 16
    TUTORIAL NO. 188 | 189
    EXERCISE NO 2 | SOLUTION


"""


class Laptop:
    def __init__(self, brand_name, model, price):
        # instance variable
        self.brand = brand_name
        self.model = model
        self.price = price

    def apply_discount(self, discount):
        price = self.price
        percentage = (discount * price) / 100
        return f'Total Price : {price}\nDiscounted Price is {price - percentage}'


buy_laptop = Laptop('hp', 'Latitude e5540', 63000)
print(buy_laptop.apply_discount(5))
