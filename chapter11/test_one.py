"""
    CHAPTER 11
    TEST ONE.
"""
def power_three(user_input, *args):
    product_list = [i**user_input for i in args]
    return product_list

user_input = int(input('enter number: '))
num_list = [1, 2, 3]
print(power_three(user_input, *num_list))
#
# def power_three(num, *args):
#     if args:
#         return [i**num for i in args]
#     else:
#         return 'Sorry list is empty'
#
# print(power_three(3,*[1, 2, 3]))
