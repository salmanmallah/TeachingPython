"""
    CHAPTER 8
    PYTHON SET
        ACCESSING DATA FROM SET.
"""

# YOU CAN ACCESS DATA BY TWO WAYS.
# BY USEING FOR LOOP.
# BY USING in KEYWORD

thisset = {'apple', 'banana', 'cherry'}
# using for loop
# for i in thisset:
#     print(i)

# using in keyword
# print('banana' in thisset)

'''Remove items by using remove() method but this method will give error if item is not present.'''
# thisset.remove('cherry')
# print(thisset)

'''Remove item by using discard() method this method will not give any error if item is note present'''
thisset.discard('apple')
print(thisset)
