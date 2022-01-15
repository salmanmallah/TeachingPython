"""
    CHAPTER NO. 16
    TUTORIAL NO. 188
    EXERCISE NO 2


"""


class Laptop:
    def __init__(self, brand_name, model, price):
        # instance variable
        self.brand = brand_name
        self.model = model
        self.price = price

    def apply_discount(self, discount):
        total = self.price
         = (discount * )



total_price = 35000
discount = 25
result = (discount * total_price) / 100
# print(f'{discount}% of {total_price} is {result}')

buy_laptop = Laptop('hp', 'Latitude e5540', 100)
