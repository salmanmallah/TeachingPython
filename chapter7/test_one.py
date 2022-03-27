"""
    Chapter 7
    Test One
        -Define a function that takes a number(lines)
        -Return a dictionary containing cube of numbers from 1 to 3.

        example
            cube_finder(3)
            {1:1, 2:8, 3:27}

        for i in range(3)
"""


def cube_finder(n):
    cube_dict = {}
    for i in range(1, n+1):
        cube_dict[i] = i * i * i
    return cube_dict


print(cube_finder(4))
