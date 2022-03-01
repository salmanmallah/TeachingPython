"""
    CHAPTER NO. 14
    TUTORIAL NO. 170

"""


def decorator_function(my_func):
    def inner_function(*args, **kwargs):
        print('this is awesome function')
        return my_func(*args, **kwargs)

    return inner_function


@decorator_function
def func(a):
    print(f'this is dummy function with argument {a}')


@decorator_function
def add(a, b):
    return a + b


print(add(1, 5))
