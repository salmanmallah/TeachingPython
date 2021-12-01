"""
    CHAPTER 4
    test 2.5
    PROJECT: * Define a function that take one word in string as input.
             * and return Boleon value as True or false
"""


def is_palindrome(name):
    if name == name[::-1]:
        return True
    return False


print(is_palindrome('nalan'))
