"""
    CHAPTER 9
    WHAT IS LIST COMPREHENSION?

"""
# create square from 1 to 10.

# creating a list of sqaure from 1 to 10
# s = []
# for i in range(1, 11):
#     s.append(i**2)
# print(s)
''' NOW BY USING LIST COMPREHENSION '''
# square_list = [i**2 for i in range(1, 11)]
# print(square_list)

# EXAMPLE NO. 2
# create list of negative number from 1 to 10
# empty_list = []
# for i in range(1, 11):
#     empty_list.append(-i)
# print(empty_list)

''' NOW BY USING LIST COMPREHENSION '''
# new_list = [-i for i in range(1, 11)]
# print(new_list)

'''Example 3 '''
names = ['Salman', 'Aslam', 'lucman']
# empty = []
# for i in names:
#     empty.append(i[0])
# print(empty)
''' NOW BY USING LIST COMPREHENSION '''
list_comp = [name[0] for name in names]
print(list_comp)
