"""
     CHAPTER 5
     LIST INSIDE LIST
"""
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
# for sublist in matrix:
#     for element in sublist:
#         print(element)

""""
    ----------- MORE ABOUT LIST
"""

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
# how you retrieve data from list inside list
# print(matrix[2][0])


# you can generate a list with range function
numbers = list(range(1,11))
# print(numbers)

"""
    USER-DEFINE FUNCTIONS
"""


def reversed_list(l):
    return l[::-1]


def negative_elements(l):
    mix = []
    negative = []
    positive = []
    for i in l:
        negative.append(-i)
    mix.extend(reversed_list(negative))
    for pos in range(len(l)+1):
        positive.append(pos)
    mix.extend(positive)
    return mix
print(negative_elements(numbers))