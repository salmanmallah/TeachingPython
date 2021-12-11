"""
    CHAPTER 6
    MORE ABOUT TUPLES
        - looping in tuples
        - tuple with one element
        - tuple without paranthesis
        - tuple unpacking
        - list inside tuple
        - some function that you can use with tuples
"""

mixed = (1, 2, 3, 4.5)

# loop with tuple
for i in mixed:
    print(i)

# while loop with tuple
i = 0
while i < len(mixed):
    print(mixed[i])
    i += 1


oneElementTuple = (1,)
word_tuple = ('salman',)

print(type(word_tuple))
print(type(oneElementTuple))