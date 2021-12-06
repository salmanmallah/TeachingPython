"""
    Programmer SalmanMallah
    Programme to check if the number is prime or not
"""

num = int(input('Enter your number to check prime number or not: '))
flag = True
if num > 1:
    for i in range(2, num+1):
        if (num % i) == 0:
            flag = False
            break
if flag:
    print(f'{num} is not prime number')
else:
    print(f'{num} is a prime number')
