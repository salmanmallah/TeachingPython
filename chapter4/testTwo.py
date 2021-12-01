"""
    CHAPTER 4
    define greatest

    PROJECT: * Create a function with 3 parameters
"""
import random as r


def greatest(x, y, z):
    if x > y and x > z:
        return f'{x} is greatest'
    elif y > x and y > z:
        return f'{y} is greatest'
    else:
        return f'{z} is greatest'


x = r.randint(1, 60)
y = r.randint(1, 60)
z = r.randint(1, 60)

print(f'x is = {x}')
print(f'y is = {y}')
print(f'z is = {z}')

print(greatest(x, y, z))
