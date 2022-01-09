"""
    CHAPTER NO. 13
    TUTORAL NO. 163
    ADVANCE SORTED() FUNCTION
"""
# list
fruits = ['grapes','apple','mango','banana']
# fruits.sort()
# print(fruits)

# tuple
fruits2 = ('grapes', 'apple', 'mango', 'banana')
# fruits2.sort() #AttributeError: 'tuple' object has no attribute 'sort'
# this will give you can not use sort() method with tuple bcz tuples are immutable
# SOLUTION: You can use sorted() functiond to sort tuple items but
# it will not change the tuple it will return a new list of sorted tuple items
# print(sorted(fruits2))

# set
fruits3 = {'grapes','mango','apple'}
# print(sorted(fruits3))

# sorted() with complex data structure
guitars = [
    {'model' : 'yamaha bike ', 'price' : 8400 },
    {'model' : '    fath neptune', 'price' :50000 },
    {'model' : 'fath apolo venus', 'price' :35000 },
    {'model' : 'taylor 814ce', 'price' :450000 }
]

# print(guitars[0]['price'])


top_expensive = sorted(guitars, key = lambda d:d['price'], reverse = True)
for i in top_expensive:
    print(i)


# unsorted = [8, 4, 6, 3, 10, 5, 7, 2]
# for srt in sorted(unsorted):
#     print(srt)