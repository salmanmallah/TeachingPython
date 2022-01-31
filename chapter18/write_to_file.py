"""
    CHAPTER NO. 18
    TUTORIAL NO. 215
    Write to file.
    Python file operations
    modes: r, w, a, r+
"""
# if you pass a argument (w) in open() function. it wile rewrite that file
# with open('new_file.txt', 'w') as f:
#     f.write('Salman is here')

# if you pass argument (a) in open() function it will append data in file
with open("life_rules.txt", 'r+') as f:
    f.write('\nSalman is writted this file')
    print(f.read())