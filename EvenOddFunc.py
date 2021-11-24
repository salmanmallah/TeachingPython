def evenodd(l):
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return [even, odd]


unsorted_list = [9,1,3,2,6,5,8,7]
print(evenodd(unsorted_list))
