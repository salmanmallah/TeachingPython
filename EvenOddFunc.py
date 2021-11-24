def evenodd(l):
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return [even, odd]


unsorted_list = []
numbers = int(input('Enter Numbers: '))

