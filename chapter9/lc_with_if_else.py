"""
    CHAPTER 9
    TUTORIAL NO. 134.
    LIST COMPREHENSION WITH if-else STATEMENT
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# make new list = [-1, 4, -3, 8]

empty_list = []
for i in numbers:
    if i%2==0:
        empty_list.append(i*2)
    else:
        empty_list.append(-i)
print(empty_list)

# now with list comprehension
even_odd_neg = [i*2 if (i % 2 == 0) else -i for i in numbers]
print(even_odd_neg)