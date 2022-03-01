"""
    CHAPTER NO. 14
    TUTORIAL NO. 169
    DECORATORS INTRO
        # Decorators - enahance  the functionality of other functions
        @ this symbol use for decorators
"""


def decorator_function(any_function):
    def wrapper_function():
        print('this is  awsome function')
        any_function()

    return wrapper_function()


@decorator_function
def func1():
    print('this is function 1')


func1


@decorator_function
def func2():
    print('this is function 2')


func2


# decorator_function(func1)
# decorator_function(func2)
