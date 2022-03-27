"""
    CHAPTER NO. 17
    TUTORIAL NO. 212
    DEBUGGING
"""
# import pdb
# Modul - python file contains usefull classes and fucntions wrote by developer.

# According to wikipedia - Debugging is the process of finding and resolving defects or poblems within a computer
# program that prevent correct operation of computer software or a system


# Why dubugging?
# 1. our program is not running and causing unexpected errors.
# 2. our program is working fine but  not working the same way we want.


# Steps for debugging.
# 1. set trace
# 2. execute code line by line.
import pdb
pdb.set_trace()
name = input('Please type your name: ')
age = int(input('Please type your age: '))
print(f'Hello {name} your age is {age}')
age2 = age + 5
print(f'{name} your age will be {age2} in next 5 years ')
