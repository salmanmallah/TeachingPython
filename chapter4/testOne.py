"""
    Chapter 4
    Test One

    test: * Define a function which takes two numbers as a input and return greater of two numbers.

"""


def greaterNumber(x, y):
    if x == y:
        return 'Both numbers are Equal'
    elif x > y:
        return f'{x} is greater'
    else:
        return f'{y} is greater'


print(greaterNumber(-5, -10))
