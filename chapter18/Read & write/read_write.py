"""
    CHAPTER NO. 18
    TUTORIAL NO. 216
    READ AND WRITE
    read file and write its data to another file
"""

with open('file1.txt', 'r') as rf:
    with open('file2.txt', 'w') as wf:
        wf.write(rf.read())
