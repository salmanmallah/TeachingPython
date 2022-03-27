"""
    CHAPTER NO. 16
    TUTORIAL NO. 185 | 186
    OOP - EXERCISE 1


    *Create a laptop class with attributes like brand_name,     model_name, price
    *Create two objects/instance of your laptop class

"""


class Laptop:
    def __init__(self, brand_name, model_name, price):
        # instance variable
        self.brand = brand_name
        self.model = model_name
        self.price = price
        self.brand_details = f'Brand : {brand_name}\nModel : {model_name}\nPrice : {price}\n\n\n'


laptop_one = Laptop('Dell', 'latitude E5540', 35000)
laptop_two = Laptop('Hp', 'Envy 13', 100000)

# object one
print(laptop_two.brand_details)
print(laptop_two.brand)
print(laptop_one.model)
print(laptop_one.price)

# object two
print('\n\n')
print(laptop_two.brand)
print(laptop_two.model)
print(laptop_two.price)
