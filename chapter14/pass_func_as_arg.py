"""
    CHAPTER NO. 14
    TUTORIAL NO. 166
    PASS FUNCTION AS A ARGUMENT
"""

def square(a):
    return a**2

# revising map() function
l = [1, 2, 3, 4]

# print(tuple(map(square, l)))

def my_func(func, l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list


print(my_func(square, l))

