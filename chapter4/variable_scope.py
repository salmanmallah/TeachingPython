"""
    CHAPTER 4
    Scope of variable inside and outside functions
"""

x = 5  # global variable


def func():
    x = 7  # local variable
    return x


print(func())
print(x)
