"""
    CHAPTER NO. 18
    TUTORIAL. 217 | 218
    TEST ONE
"""

# with open('user_data.txt', 'r') as rf:
#     for lines in rf.readlines():
#         name, salary = lines.split(',')
#         print(f"{name}'s salary is{salary}", end=" ")


with open('salary.txt', 'r') as rf:
    with open('output.txt', 'w') as wf:
        for lines in rf.readlines():
            name, salary = lines.split(',')
            wf.write(f"{name}'s salary is{salary}")
