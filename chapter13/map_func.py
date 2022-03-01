"""
    CHAPTER 13
    MAP() FUNCTION
    TUTORIAL 153.
"""

numbers = [1,2,3,4]
# def square(a):
#     return a**2
#
# squares = list(map(square, numbers))
# print(squares)

# # you can use lambda in map as a argument
# squares = list(map(lambda a : a**2, numbers))
# print(squares)
#
# # same output with list comprehension
# square = [i**2 for i in numbers]
# print(square)

# you can print a same result with forloop
# empty = []
# for i in numbers:
#     empty.append(square(i))
# print(empty)

string = ['david', 'alpha', 'salman mallah', 'rehman mallah', 'akram mallah']
# find length of every string in list

# with for loop
# for str in string:
#     print(f"{str} : {len(str)}")

# with map() function
# result = map(len, string)
# for i in result:
#     print(i)


# if you want to store result from map() func
# result = list(map(len, string))d
# print(result)
