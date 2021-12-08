"""
    CHAPTER 5
    TEST TWO
        -Define a function which will take list as a argument and this
         function will return a reveresed list
"""

def reversed_list(l):
    return l[::-1]

num_list = list(range(1,11))
salmaninfo = 'salman is the best in the world'.split()
print(
    reversed_list(salmaninfo)
)