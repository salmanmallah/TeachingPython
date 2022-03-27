"""
    CHAPTER NO. 18
    TUTORIAL NO. 214
    WITH BLOCK - READ FILE
"""

# f = open('life_rules.txt', 'r')
# print(f.read())
# f.close()

with open('life_rules.txt') as f:
    data = f.read()
    print(data)

