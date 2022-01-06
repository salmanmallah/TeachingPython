"""
    CHAPTER 13
    TUTORIAL 156 | 157
    ZIP() FUNCTION

"""
user_id = [1, 2, 3, 4, 5, 6]
user_pass = ['pass1', 'pass2', 'pass3', 'pass4', 'pass5', 'pass6']
# print(list(zip(user_id, user_pass)))
# print(dict(zip(user_id, user_pass)))

# example     = [('a', 1), ('b', 2)]
# print(dict(example))


"""
    Zip() part too
    tutorial no. 157
"""

# l1 = [1, 3, 5, 7]
# l2 = [2 ,4, 6, 8]

l = [(1, 2), (3, 4), (5, 6), (7, 8)]  #how you can convert this list like above two lists.

# print(list(zip(l1, l2)))

# unpacking l to its original form
l1, l2 = list(zip(*l))
# print(l1)
# print(l2)
print(list(l1))
print(list(l2))