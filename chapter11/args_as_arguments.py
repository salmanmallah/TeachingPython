"""
    CHAPTER 11
    ARGS AS ARGUMENTS
"""
def multiplay_num(*args):
    multiple = 1
    print(args)
    for i in args:
        multiple *= i
    return multiple

num_list = [1, 2, 3, 4, 5, 6]
print(
    multiplay_num(*num_list)
)