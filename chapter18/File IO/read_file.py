"""
    CHAPTER NO. 18
    TUTORIAL NO. 213
    READING FILE
    Readfile
    open function
    read method
        to read the data in the file
    tell method
        to tell the position of cursor
    seek method
        to change the position of cursor
    readline method
        to read single line at a time
    readlines method
    close method
"""

# open_file = open('life_rules.txt')
# print(f'Cursor position {open_file.tell()}')
# print(open_file.read())
# print(f'Cursor position {open_file.tell()}')
# open_file.seek(0)
# print(open_file.read())
# open_file.close()


# readline method
# open_file = open('life_rules.txt')
# print(open_file.readline())
# open_file.close()


# readlines method
# f = open('life_rules.txt')
# lines = f.readlines()
# print(len(lines))
# f.close()


# name(), closed() method
f = open('life_rules.txt')
# print(f.name)
# print(f.closed)
# f.close()

# you can use indexing with readlines method
for line in f.readlines()[1:2]:
    print(line, end="")

f.close()
