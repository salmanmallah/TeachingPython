"""
    CHAPTER 5
    TEST
        -Define a function which take a list containing numbers as
         input and return list containing square of every number
"""

def square_list(l):
    null = []
    for i in l:
        null.append(i**2)
    return null

list = list(range(1,11))
print(
    square_list(list)
)