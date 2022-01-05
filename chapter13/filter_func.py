"""
    CHAPTER NO. 13
    TUTORIAL NO. 154
    filter() function

"""
def is_even(n):
    return n%2==0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# even_tuple = tuple(filter(is_even, numbers))
# print(even_tuple)

# with lambda expression as a filter argument
even_tuple2 = tuple(filter(lambda n: n%2==0, numbers))
print(even_tuple2)

# now with list comprehension
l = [i for i in numbers if i % 2 == 0]
print(l)