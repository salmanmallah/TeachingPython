"""
    CHAPTER 5
    TEST FIVE
        - COMMON ELEMENTS FINDER FUNCTION
            * Define a function which take 2 lists as input and return a list which contains
            common elements of both lists.

        -Example taking [1,2,3,4,5,], [10,11,12,13,5,1]
            return commonMembers[5,1]
"""

def commonTaker(listOne, listTwo):
    common_members = []
    for i in range(len(listOne)):
        if listOne[i] in listTwo:
            common_members.append(listOne[i])
    if common_members:
        common_members.sort()
        return common_members
    else:
        return f'Sorry!, No common elements found!'

print(
    commonTaker([12, 1, 2, 3, 4, 10], [10, 11, 12, 13, 5, 3])
)
