"""
    CHAPTER NO. 16
    TUTORIAL NO. 196
    Encapsulation, Abstraction, Naming Conventions, Name Mangling

    -Encapsulation, Abstraction
        -A class is an example of encapsulation as it encapsulates all the data that is member functions,variables, etc.
        Consider a real-life example of encapsulation, in a company, there are different sections like the accounts section,
        finance section, sales section etc. The finance section handles all the financial transactions and keeps records of
        all the data related to finance. Similarly, the sales section handles all the sales-related activities and keep
        records of all the sales. Now there may arise a situation when for some reason an official from the finance section
        needs all the data about sales in a particular month. In this case, he is not allowed to directly access the data
        of the sales section. He will first have to contact some other officer in the sales section and then request him
        to give the particular data. This is what encapsulation is. Here the data of the sales section and the employees
        that can manipulate them are wrapped under a single name “sales section”. Using encapsulation also hides the data.
        In this example, the data of the sections like sales, finance, or accounts are hidden from any other section.

        Encapsulation means storing or placing data in a single place to make it easily readable and compact in one place.
        Whereas data abstraction in python programming means to hide internal functionalities that are performing on the
        application using codes and to show only essential information (class attributes)


    -NAMING CONVENTIONS
        #   _name #convention of private name
        # __name__ # dunder method / magic method



"""


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.name = model_name
        self.price = price

    def make_call(self, phone_number):
        print(f'Calling {phone_number} ...')

    def full_name(self):
        return f'{self.brand} {self.name}'


mobile_one = Phone('Samsung', 'J7 MAX', 32000)
