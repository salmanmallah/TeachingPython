"""
    CHAPTER NO. 16
    TUTORIAL NO. 200
    More about inheritance, ✔
    multilevel inheritance, ✔
    MRO - Method Resolution Order, ✔
    method overriding, ✔
    isinstance(),
    issubclass()
"""


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


class Flagship(Smartphone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rare_camera, processor, screen):
        super().__init__(brand, model_name, price, ram, internal_memory, rare_camera)
        self.processor = processor
        self.screen = screen


flagship = Flagship('OPPO', 'RENO 6', 70000, '8GB', '240GB', '60MP', 'OCTA CORE PROCESSOR', '90HERTZ SECREEN')
# print(flagship.full_name())

# fulldict = flagship.__dict__
# for key, value in fulldict.items():
#     print(f'{key} : {value}')


'''MRO - Method Resolution Order'''

# print(help(Smartphone))

'''isinstance() issubclass()'''

oppo = Flagship('OPPO', 'RENO 6', 70000, '8GB', '240GB', '60MP', 'OCTA CORE PROCESSOR', '90HERTZ SECREEN')
# print(isinstance(oppo, Flagship))
# print(issubclass(Flagship, Smartphone))