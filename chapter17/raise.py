"""
    CHAPTER NO. 17
    TUTORIAL NO 204
    RAISE ERROR
"""


def add(a, b):
    if (type(a) is int) and (type(b) is int):
        return a + b
    raise TypeError('sorry you can only pass integers to this function')
    # raise KeyError('sorry you can only pass integers to this function')


# print(add(8, 8))
# print(add('salman', 'mallahs'))
