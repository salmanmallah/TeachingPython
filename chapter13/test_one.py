"""
    CHAPTER 13
    TUTORIAL 158
    TEST ONE.

    THIS IS CHALLENGE!
        -define a function that will take no of lists containing numbers
        -[1,2,3], [4,5,6], [7,8,9]
        -return average
        (1+4+7)➗3, (2+5+8)➗3, (3+6+9)➗3
"""

# def anonymous(*args):
#     # temp = 0
#     result = []
#     # tempList = []
#     for pair in zip(*args):
#         result.append(sum(pair)/len(pair))
#     return result
#

# NOW by using lambda method
anonymous = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(anonymous([1,2,3], [4,5,6], [7,8,9]))


