"""
    CHAPTER NO. 17
    TUTORIAL NO. 207 | 208
    EXCEPTION HANDLING
    try, except, else, finally

"""

import random

# while True:
#     try:
#         age = int(input('Enter your age: '))
#         break
#     except ValueError:
#         print(ValueError.__name__, '\nMayBe you enter string instead of integer')
#     except:
#         print('Unknown Error!')
#
# if age >= 18:
#     print('You can play this game')
# else:
#     print('You are under 18 and can not play game')
#

"""
    TUTORIAL NO. 2O8
    ELSE, FINALLY CLAUSE IN EXCEPTION HANDLIN
"""


ran_num = random.randint(1, 5)
while True:
    try:
        usr_num = int(input('Guess a number'))
    except ValueError:
        print("Sorry input integer value not string")
    else:
        if usr_num == ran_num:
            print(f'Congrates you win!!, winning number is {ran_num}')
            break
        else:
            print('Please Try again')


