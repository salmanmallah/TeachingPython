"""
    CHAPTER NO. 14
    TUTORIAL NO. 175
    DECORATOR PRACTICE 2

    -Make a addition function that will take only  numbers not strings like addition(1,2,3,3,4, 'string')
    -So make a decoration which take only numbers as a argument in function~

"""
from functools import wraps


def only_int_allow(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if all([type(arg) == int for arg in args]):
            return function(*args, **kwargs)
        return 'Invalid argument'
    return wrapper

    args_data = []
    for i in args:
        args_data.append(type(i) == int)
    if all(args_data):
        return function(*args, **kwargs)
    else:
        return f'Invalid argument'
    return wrapper


@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add_all(1, 2, 3, 4, 5))
