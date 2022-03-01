"""
    CHAPTER NO. 16
    TUTORIAL NO. 198
    PROPERTY, SETTER DECORATOR

"""


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.name = model_name
        self.price = max(price, 0)
        # if price > 0:
        #     self.price = price
        # else:
        #     self.price = 0
        # self.comptele_specification = f"{self.brand} {self.name} and price is {self.price}"

    @property
    def complete_specification(self):
        print(f"{self.brand} {self.name} and price is {max(self.price, 0)}")

    def make_a_call(self, phone_number):
        print(f'Calling {phone_number} ...')

    def full_name(self):
        print(f'{self.brand} {self.name}')


mobile_one = Phone('Samsung', 'J7 MAX', 32000)


mobile_one.price = -1111
print(mobile_one.price)
mobile_one.complete_specification