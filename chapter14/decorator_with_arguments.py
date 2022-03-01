"""
    CHAPTER NO. 14
    TUTORIAL NO 176
    DECORATOR WITH ARGUMENTS
"""
from functools import wraps


def only_data_type_allow(data_type):
    def decorator(function):
        wraps(function)

        def wrapper(*args, **kwargs):
            if all([type(arg) == data_type for arg in args]):
                return function(*args, **kwargs)
            return "Invalid argument"
        return wrapper
    return decorator


@only_data_type_allow(str)
def string_join(*args, **kwargs):
    string = ''
    for i in args:
        string += i
    return string


print(string_join(1, 2, 3))
