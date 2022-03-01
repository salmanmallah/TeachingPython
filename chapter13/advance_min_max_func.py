"""
    CHAPTER NO. 13
    TUTORIAL NO. 162
    Advance min() and max() function
"""
# import time
# names = ['z', 'sb', 'Salman', 'Suleman', 'Sultan Suleman', 'sultan abdul hameed majeed saani']
#
# print(
#     len(max(names, key = lambda item:len(item)))
# )


# numbers = [1, 2, 3, 4, 5, 6]

# print(max(numbers))


# students2 = [
#     {'name':'salman','score': 90, 'age': 24},
#     {'name':'Noman','score': 95, 'age': 22},
#     {'name':'Akram','score': 100, 'age': 45}
# ]
#
# print(
#     max(
#         students2, key = lambda item:item.get('score')
#     )['name']
# )


students = {
    'salman' : {'score': 90, 'age': 24},
    'Noman' : {'score': 95, 'age': 22},
    'Akram' : {'score': 100, 'age': 45}
}

# for key, value in students.items():
#     for subkey in value.items():
#         time.sleep(1)
#         print(f'{key}:\lines{subkey}\lines')

# for key, value in students.items():

print(
    max(students, key = lambda item:students[item]['score'])
)