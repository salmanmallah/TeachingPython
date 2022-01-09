"""
    CHAPTER NO. 13
    TUTORIAL NO. 160
    any() and all() function

    all() function will return True if all iterable are true.
    any() function will return True if anyone iterable is True.
"""

number1 = [2, 4, 6, 8, 10]
number2 = [1, 2, 3, 4, 5, 6]

check_even = [True if i%2==0 else False for i in number2]
print(check_even)