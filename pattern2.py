numRows = int(input('Enter the numbers of rows: '))

for row in range(1, numRows+1):
    for column in range(1, row+1):
        print(row, end=' ')
    print()

# for row in range(numRows-1, 0, -1):
#     for column in range(1, row+1):
#         print(row, end=' ')
#     print()
