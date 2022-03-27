"""
    CHAPTER NO.14
    TUTORIAL NO. 155
    ITERATOR VS ITERABLE IN PYTHON
"""
numbers = [1, 2, 3, 4, 5] #strings, tubles, lists ---> iterables
squares = map(lambda a: a**2, numbers) # iterator

# for i in squares:
#     print(i)

iter_number = iter(numbers)
print(next(iter_number))
print(next(iter_number))
print(next(iter_number))
print(next(iter_number))
print(next(iter_number))