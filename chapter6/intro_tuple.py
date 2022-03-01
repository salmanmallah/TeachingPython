"""
    CHAPTER SIX
    INTRODUCTION TO TUPLES
"""
# tuple data structure
# tuple can store any data type
# most important tupes are immutable
# once tuple is created you can not update data inside tuple.

# example = ('one', 'two', 'three')
# print(type(example))
# print(example[0])

'''
    FOLLOWING METHODS USED WITH TUPLES    
'''
example = ('one', 'two', 'three', 'one', 'one', 'one')
print(
    f' {example[0]} is {example.count(example[0])} times\n',
    f'Index of {"three"} is {example.index("three")}\n',
    f'Tuple length is : {len(example)}'

)












