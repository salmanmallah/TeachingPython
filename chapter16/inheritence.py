"""
    CHAPTER NO. 16
    TUTORIAL NO. 199
    INHERITANCE INTRO

    Inherit one class to another
"""


# import time


class Phone:  # parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.name = model_name
        self.price = max(price, 0)

    @property
    def complete_specification(self):
        return f"{self.brand} {self.name} and price is {max(self.price, 0)}"

    @staticmethod
    def make_a_call(phone_number):
        return f'Calling {phone_number} ...'

    def full_name(self):
        return f'{self.brand} {self.name}'


class Smartphone(Phone):  # derived / child class
    def __init__(self, brand, model_name, price, ram, internal_memory, rare_camera):
        # two ways
        # Phone.__init__(self, brand, model_name, price) # first way
        super().__init__(brand, model_name, price)  # second way
        self.ram = ram
        self.memory = internal_memory
        self.camera = rare_camera

    @staticmethod
    def make_a_call(phone_number):
        return f'Calling {phone_number} ...'

    def full_name(self):
        return f'{self.brand} {self.name}'


# time.sleep(1)
# brand = input('Inter your Mobile Brand : ')
# time.sleep(1)
# modelname = input('Inter your Mobile\'s model name : ')
# time.sleep(1)
# price = int(input('Inter your Mobile\'s price : '))

# phone = Phone(brand, modelname, price)
# smartphone = Smartphone('Infinix', 'hot 10 play', 1000)
# time.sleep(1)
# print(phone.brand)
# time.sleep(1)
# print(phone.name)
# time.sleep(1)
# print(phone.price)
# time.sleep(1)
# print(phone.complete_specification)


phone = Phone('Nokia', '1100', 1500)
smartphone = Smartphone('Infinix', 'hot 10 play', 19600, '4GB', '64GB', '20 MP')
print(phone.full_name())
print(smartphone.full_name() + f'and price is {smartphone.price}')
