"""
    Chapter Three
    Test four

    *Ask user to input a number containing more than one digit
    *example 1256
    calculate 1 + 2 + 5 + 6 and print()

    algorithm ---> input 1234 con't convert it into string use indexing than fetch one by one from that string
                 convert into int than add into empty variable.
                 use while loop
"""
num = input('Enter more than one digit to add them ')
i = 0
sum = 0
while i < len(num):
    sum += int(num[i])
    i += 1
print(sum)