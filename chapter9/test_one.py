"""
    CHAPTER 9
    TEST ONE
        -Define a function that take list of strings
        list containing reverse of string
     NOTE - USE list comprehension because we already did this exercise using normal moethods.

     EXAMPLE: l = ['abc', 'tub', 'xyz']
     reverse => ['cba', tub', 'zyx']
"""
forward = ['abc','tub', 'xyz']
# reverse_list = [e[::-1] for e in forward]
# print(reverse_list)

def reverse_elements(l):
    return [e[::-1] for e    in l]


