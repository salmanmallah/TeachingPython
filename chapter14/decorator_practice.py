"""
    CHAPTER NO. 15
    TUTORIAL NO. 172
    DECORATOR PRACTICE
"""
from functools import wraps
from time import *


def print_function_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        sleep(2)
        print(f"You are calling {function.__name__}")
        sleep(2)
        print(function.__doc__)
        sleep(2)
        return function(*args, **kwargs)
    sleep(2)
    return wrapper


@print_function_data
def add(a, b):
    """ This function will take 2 numbers and return sum of numbers """
    return a + b


print(add(1, 3))
# output
# you are calling add function
# This function will take 2 numbers and return sum of numbers
# 4
