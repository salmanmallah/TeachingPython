"""
    CHAPTER 5
    TEST FIVE
        -Define a function that take list of words as argument and returns list with reverse of every
        element in that ist.

        EXAMPLE:
            ['abc', 'tuv', xyz] ==> ['cba', 'vut', 'zyx']

"""

def reverse_elements(l):
    rev_element = []
    for e in l:
        rev_element.append(e[::-1])
    return rev_element
print(reverse_elements(['abc', 'tuv', 'xyz']))
