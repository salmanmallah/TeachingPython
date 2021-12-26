"""
    CHAPTER 11
    INTRODUCTOIN TO *args
"""
# make flexible functions
# * operator
# *args

def total(a, b):
    return a + b
# print(total(10, 10)) # but we cannot pass more than two parameters

''' NOW BY USING *ARGS TECHNIQUE WE CAN SOLVE ABOVE PROBLEM '''
def arg_total(*args):
    total = 0
    for i in args:
        total += i
    return total

print(arg_total(10, 10, 10, 10, 10, 10, 10))
