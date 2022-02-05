"""
    CHAPTER NO. 18
    TUTORIAL NO. 214
    WITH BLOCK - READ FILE
"""

with open('life_rules.txt') as f:
    data = f.read()
    print(data)

