# num = int(input('Enter the number of rows: '))
num = 5
for row in range(num):
    val = row+1
    for col in range(row+1):
        print(val, end=" ")
    print()