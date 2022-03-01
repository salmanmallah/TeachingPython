"""
    CHAPTER 8
    INTRODUCTION TO SET

        Defination: unordered collection of unique items.
"""
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10}
list_one = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]

# print(list(set(list_one)))
# print(len(s))

'''
    # Access Data from SET.
    # 2 ways to access data from set.
    #    1. using for loop to access data.
    #    2. in keyword
'''
fruits_set = {'Orange', 'Banana', 'Apple', 'Grapes'}
for i in fruits_set:
    print(i)

if 'Grapes' in fruits_set:
    print('Grapes is present')
else:
    print('Gapes is not present')


'''
    # ADD DATA TO SET
    # Add an item to a set use the add() method.    
'''
# fruits_set.add('Watermelon')
# print(fruits_set)

more_fruites = {'Green Orange', 'Blue Orange', 'Red Orange'}
# update() method
fruits_set.update(more_fruites)
print(
    fruits_set
)
