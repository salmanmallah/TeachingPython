"""
    CHAPTER 5
        LIST METHODS

        clear()
            removes all items from the list

        copy()
            returns a shallow copy of the list

        count()
            returns count of the element in the list

        index()
            returns the index of the element in the list

        reverse()
            reverses the list

        sort()
            sorts elements of a list
"""

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# count() method
# print(fruits.count(fruits[1]))

# sort() method
# fruits.sort()

# sorted() method
empty_list = sorted(fruits)
# print(fruits)

# clear() method
# fruits.clear()
# print(fruits)

# reverse() method
print(empty_list)
empty_list.reverse()
print(empty_list)
