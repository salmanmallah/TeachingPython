"""
    CHAPTER NO. 14
    TUTORIAL NO 173 | 174
    TEST ONE
"""
from functools import wraps
import time
#
# t1 = time.time()
# x = 1000000
# for i in range(x):
#     print(i)
# t2 = time.time()
#
# print(f'time taken is : {round(t2-t1, 2)}')


def calculate_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'Executing {function.__name__}')
        t1 = time.time()
        value = function(*args, **kwargs)
        t2 = time.time()
        print(f"total time taken : {t2-t1}")
        return value
    return wrapper


# @calculate_time
# def func():
#     for i in range(10000000):
#         print(f'{i} Sal{i}man')


@calculate_time
def square_finder(n):
    l = (i**2 for i in range(n))
    for i in l:
        print(i)


print(square_finder(1000000))
