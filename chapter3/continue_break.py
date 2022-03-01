"""
    chapter 3
    break and continue
    break keyword
    continue keyword
"""
import random

# 1 to 10 print
for i in range(1, 100):
    ranNumber = random.randint(50, 100)
    if ranNumber == 5:  # when it reach the number 5 it will skip the number 5
        continue
    print(ranNumber)

# 1 to 10 print
print(
    'break keyword'.center(30, '*')
)
for i in range(1, 20):
    ranNumber = random.randint(1, 10)
    if ranNumber == 5:  # when it reach the number 5 it will break the for loop
        break
    print(ranNumber)
