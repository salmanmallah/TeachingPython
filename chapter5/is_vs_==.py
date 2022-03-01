"""
    CHAPTER 5
    is vs == COMPARISION
"""

list_one = [1, 2, 3, 4, 5]
list_two = [1, 2, 3, 4, 5]

print(list_one is list_one)  # this statement is true
print(list_one == list_two)  # this statement is true
print(list_one is list_two)  # this statement is false becuase we know that list_one is not list_two
