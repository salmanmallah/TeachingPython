"""
    CHAPTER 4
    define fibonacci
"""


def fibonacci_seq(n):
    n = 10
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b)
    else:
        print(a, b, end=" ")
        for i in range(n - 1):
            c = a + b
            a = b
            b = c
            print(b, end=" ")
