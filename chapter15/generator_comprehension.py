"""
    CHAPTER NO. 15
    TUTORIAL NO. 181
    Generator Comprehension
"""
square = (i**2 for i in range(1, 11)) # this is a generator comprehension just like list comprehension

print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))


# print(square)
# for i in square:
#     print(i)

