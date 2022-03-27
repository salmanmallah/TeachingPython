"""
    CHAPTER 4
    function Introduction
    what is a function

    syntax:
            def func_name(parameters):
                statements
"""


def add_three(a, b, c):
    return a + b + c


# calling of function
# print(add_three(3, 45, 5))


'''Check Odd or Even'''


def odd_even(num):
    if num % 2 == 0:
        return 'Even'
    return 'Odd'


def last_char(name):
    return name[-1]


print(last_char('salman'))

