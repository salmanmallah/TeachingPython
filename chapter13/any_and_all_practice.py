"""
    CHAPTER NO 13
    TUTORIAL NO 161
    any() and all() practice
"""

# def my_sum(*args): # this function only add numbers but first it filter the integers
#     empty = []
#     for i in args:
#         if type(i) == int or type(i) == float:
#             empty.append(i)
#     return sum(empty)

def my_sum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for i in args:
            total += i
        return total
    else:
        return "\n  Sorry! Operation unsuccessfull bcz parameters not only integers"
print(
    my_sum(1,2,3,4,5,5,5)
)