"""
    CHAPTER NO. 14
    TUTORIAL NO 171
    DECORATOR PART 3
"""
from functools import wraps


def decorator_function(my_func):
    @wraps(my_func)
    def inner_function(*args, **kwargs):
        """ This is inner_function and takes *args & **kwargs """
        print('this is awesome function')
        return my_func(*args, **kwargs)

    return inner_function


@decorator_function
def add(a, b):
    """Add function will take two arguments as numbers and return sum of those arguments"""
    return a + b


print(add.__doc__)
print(add.__name__)
