"""
    CHAPTER 13
    tutorial no 152
    ENUMERATE() FUNCTION
        -we use enumerate() function with for loop to track position of our item in iterable
"""
name = ['abc', 'abcdef', 'salman', 'Rimsha']
# get output like this
# 0 ------> 'abc'
# 1 ------> 'abcdef'
# 2 ------> 'salman'

# without enumerate funciton
# for i in range(len(name)):
#     print(f"{i} --------> '{name[i]}'")

# with enumerate() function
# for pos, name in enumerate(name):
#     print(f'{pos} --> {name}')



# define a function that take 2 arguments
# 1. list containing strings
# 2. string that want to find in your list.
# and this function will return the index of string in your list and
# if string is not present then return -1

def find_me(l, find_name):
    for pos, name in enumerate(l):
        if name == find_name:
            return pos
    return -1


print(
    find_me(name, 'Rimsha')
)
