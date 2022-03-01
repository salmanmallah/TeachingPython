"""
    CHAPTER 5
    min() function
    max() function
"""
list  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(min(list))
# print(max(list))

"""
    -Assignment    
        Make a function which give greatest difference.
"""


def greatest_diff(l):
    return max(l) - min(l)


list_two = [6, 60, 30]
print(greatest_diff(list_two))