"""
    CHAPTER NO. 18
    TUTORIAL NO. 215
    Write to file.
    Python file operations
    modes: r, w, a, r+

    r mode : to reading in file
    w mode : to write in file
    a mode : to append in file at last.
    r+ mode: to read and write but it will not create file if file not exist.

"""
# if you pass a argument (w) in open() function. it wile rewrite that file
# with open('write_method.txt', 'a') as f:
#     f.write('\ni am writing this text with write method')

# if you pass argument (a) in open() function it will append data in file


with open("new_file.txt", 'r+') as f:
    f.seek(len(f.read()))
    f.write('\nplease write it')

