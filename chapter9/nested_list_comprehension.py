"""
    CHAPTER 9
    TUTORIAL NO. 135.
    NESTED LIST COMPREHENSION
"""

nested_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(nested_list)

nested_comp = [[i for i in range(1, 4)] for j in range(len(nested_list))]
print(nested_comp)