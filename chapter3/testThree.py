"""
    chapter three
    test three

    *Exercise ONE OF THREE.
    *sum of natural numbers
    *Ask a user for natural number (lines)
    *print() total from 1 to 10
"""
n = input('Enter natural number to find sum : ')
# i = 1
sum = 0
# while i <= lines:
#     sum += i
#     i += 1
# print(sum)


# same programme with for loop
for i in range(len(n)):
    sum += int(n[i])
print(sum)
