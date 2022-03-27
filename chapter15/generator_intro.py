"""
    CHAPTER NO. 15
    TUTORIAL NO. 176 | 177
    GENERATOR IN PYTHON

        What is generator?
        ans: Python provides a generator to create your own iterator function.
             A generator is a special type of function which does not return a single value,
             instead, it returns an iterator object with a sequence of values.
             In a generator function, a yield statement is used rather than a return statement.

        we use range() function in for loops.
        it is also a generator
"""

# create your first generator with generator function
# 1. generator function
# generator 1 to 10


def nums(n):
    for take in range(1, n + 1):
        yield take


# print(nums(10))
# for i in nums(5):
#     print(i)

numbers = nums(10)

for i in numbers:
    print(i)
    if i >= 5:
        break
