"""
    Chapter three
    if statement
"""


rungame = True

while rungame:
    age = int(input("Enter your age : "))
    if age == 14:
        print(f'Your age {age} years old, You can play our game.')
        rungame = False
    elif age > 14:
        print(f'your are older than 14 years, You can play our game.')
        rungame = False
    else:
        print(f'you are not older enough to play our game.')
