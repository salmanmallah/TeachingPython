"""
    CHAPTER 11
    *ARGS WITH NORMAL PARAMETERS
"""
def multiple(*args):
    product = 1
    for i in args:
        product *= i
    return product

print(multiple(1,2,3))
