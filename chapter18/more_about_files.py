"""
    CHAPTER NO. 18
    TUTORIAL NO. 222
    PRINT EMOJIS
"""
with open('dummy_text.txt', 'r', encoding='utf-8') as rf:
    print(rf.encoding)
    print(rf.read(100))


# with open('dummy_text.txt', 'r', encoding='utf-8') as rf:
#     data = rf.read(100)
#     while len(data) > 0:
#         print(data)
#         data = rf.read(100)
