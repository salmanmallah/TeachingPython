"""
    CHAPTER 7
    TUTORIAL NO 118
        Fromkeys(), get(), clear(), copy() method.
"""

# fromkeys
d = dict.fromkeys(['name', 'name', 'email', 'age'], 'Unkown')
# print(d)


d = dict.fromkeys(range(1, 11), 'google is default')
# print(d)

d = {
    'name': 'salman',
    'surname': 'mallah',
    'email': 'pythonsalman06@gmail.com'
}

print(d.get('email'))
