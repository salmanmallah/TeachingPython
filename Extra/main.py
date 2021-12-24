# Code by Salman Mallah
lsOne = [6, 2, 3, 4, 5, 1]
lsTwo = [1, 2, 3, 4, 5, 6]


def addlist(one, two):
    empty_list = []
    for i in range(len(one)):
        empty_list.append(one[i] + two[i])
    print(empty_list)


addlist(lsOne, lsTwo)

