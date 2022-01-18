"""
    CHAPTER NO. 16
    TUTORIAL NO. 199
    INHERITANCE INTRO
"""


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.name = model_name
        self.price = max(price, 0)

    @property
    def complete_specification(self):
        print(f"{self.brand} {self.name} and price is {max(self.price, 0)}")

    def make_a_call(self, phone_number):
        print(f'Calling {phone_number} ...')

    def full_name(self):
        print(f'{self.brand} {self.name}')

