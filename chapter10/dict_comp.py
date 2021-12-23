"""
    CHAPTER 10
    DICTIONARY COMPREHENSION
"""
# square = {1:1, 2:4, 3:9}
# square = {num:num**2 for num in range(1,6)}
# print(square)

# d = {f'square of {num} is ':num**2 for num in range(1,11)}
# for key, value in d.items():
#     print(f'{key} : {value}')

# character counter with dict comprehension
string = 'salmanmallah'
word_count_dict = {char:string.count(char) for char in string}
print(word_count_dict)