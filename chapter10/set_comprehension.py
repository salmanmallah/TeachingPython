"""
    CHAPTER 10.
    SET COMPREHENSION
"""
# creating set with set comprehension
# set_comp = {i for i in range(1,11)}
# print(set_comp)

list = ['salman', 'arsalan', 'ateeque']
reverse_set = {r[::-1] for r in list}
print(reverse_set)