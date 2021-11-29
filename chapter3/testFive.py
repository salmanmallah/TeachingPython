"""
    chapter 5
    test  5

    * Ask from user for name
    * Example: salman
    * print count of each words
    output:
        S: 1
        A: 2
        l: 1
        M: 1
        A: 2
        N: 1
"""
name = input('Enter your name : ')
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        temp += name[i]
        print(f'{name[i]}:{name.lower().count(name[i].lower())}')