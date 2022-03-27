"""
    CHAPTER NO. 14
    TUTORIAL NO. 165
    CHAPTER NO 14 INTRO

    -You have to have complete understanding of functions,
    -First class function / closures
    -Then finally we will learn about decorators
"""

def square(a):
    return a**2

s = square
# print(s(2))

# printing name of both s and square
print(s.__name__)
print(square.__name__)

# printing memory location of both s and square
print(s)
print(square)
