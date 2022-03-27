"""
    CHAPTER 5
    TEST TWO
        -Define a function which will take list as a argument and this
         function will return a reveresed list
"""

# def reversed_list(l):
#     return l[::-1]

def reversed_list(l):
    null = []
    for i in range(len(l)):
        null.append(l.pop())
    return null


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# salmaninfo = 'salman is the best in the world'.split()
print(
    reversed_list(num_list)
)

