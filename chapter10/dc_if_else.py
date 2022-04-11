"""
    CHAPTER 10
    DICTIONARY COMPREHENSION WITH IF ELSE STATEMENT
"""
# {1:odd, 2;even, 3:odd, 4:even, 5:odd, 6:even}

# odd_even_dict = {i:('even'if i % 2 == 0 else 'odd') for i in range(1,11)}
# print(odd_even_dict)


odd_even = {i: ('Even' if i % 2 == 0 else 'Odd') for i in range(1,11)}
print(odd_even)
for i in odd_even:
    print(odd_even[i])