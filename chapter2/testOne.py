'''
    chapter two
    test one
'''

'''
    *Ask user to input 3 number and you have to print average of three numbers using string formatting
    
    logic:
        1. input -> 20 40 50 split()
        2. Calculating -> sum of 20 40 50 / numbers of inputs 3
        3. print
'''


def add_three_numbers(x, y, z):
    return int(x) + int(y) + int(y)


numOne, numTwo, numThree = input('Enter numbers separated by coma.').split(",")
cl = add_three_numbers(numOne, numTwo, numThree)
print(f'Sum of {numOne} ➕ {numTwo} ➕ {numThree} = {cl}')
average = cl/3
print(f'Average of {numOne} ➕ {numTwo} ➕ {numThree} = {average}')


