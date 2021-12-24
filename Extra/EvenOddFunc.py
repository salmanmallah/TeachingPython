def evenodd(l):
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return [even, odd]


unsorted_list = [3, 2, 1, 4, 7, 5, 6, 9, 8, 10, 12]
print(evenodd(unsorted_list))

