"""
    CHAPTER 5
    TEST FOUR
        - Filter Odd Even
"""
# [1,2,3,4,5,6,5,7,8,9,10]

def filter_numbers(l):
    odd = []
    even = []
    filtered_elements = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            even.append(l[i])
            filtered_elements.append
        else:
            odd.append(l[i])
            filtered_elements.append(odd)
        return filtered_elements

print(filter_numbers(list(range(1, 11))))