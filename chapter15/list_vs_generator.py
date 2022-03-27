"""
    CHAPTER NO. 15
    TUTORIAL NO. 182
    LIST VS GENERATOR

    TODAYS DISCUSSION.
        -LIST VS GENERATOR
        -MEMORY USAGE, TIME
        -WHEN TO USE LIST, WHEN TO USE GENERATOR
"""
import time

t1 = time.time()
# l = [i ** 2 for i in range(100000000)]
g = (i**2 for i in range(100000000))
t2 = time.time()
print(f'time taken is ({round(t2 - t1, 2)})')

