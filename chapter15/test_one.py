"""
    CHAPTER NO 15.
    TUTORIAL NO 179 | 180

    ASSINMENT
         -Define a generator function
         -Take  one number as argument
         -Generate a sequence of even numbers from 1 to that number:
"""


def generator(n):
    for n in range(1, n + 1):
        if n % 2 == 0:
            yield n


for i in generator(10):
    print(i)
