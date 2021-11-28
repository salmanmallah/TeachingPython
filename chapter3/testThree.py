"""
    chapter three
    test three

    *Exercise ONE OF THREE.
    *sum of natural numbers
    *Ask a user for natural number (n)
    *print() total from 1 to 10
"""
n = int(input('Enter natural number to find sum : '))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print(sum)