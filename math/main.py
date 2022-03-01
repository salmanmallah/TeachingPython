"""
    Programmer SalmanMallah
    Programme to check if the number is prime or not
"""

num = int(input('Enter your number to check prime number or not: '))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if num == 1:
    print(f'{num} is not prime number')
elif flag:
    print(f'{num} is not prime number')
else:
    print(f'{num} is a prime number')



