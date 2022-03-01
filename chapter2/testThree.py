"""
    chapter two
    test three

    * Take two comma separated inputs from user
        * user's name , example 'salman'
        * A single character , "a"

    output:
        * Print 2 lines
            *user's name length
            *count the character that user inputted.
"""

name, char = input('Enter you name & character you want to find: ').split(",")
print(f'{name.strip()} length of your name is: {len(name.strip())}')
print(f'{char.strip()} is {name.lower().count(char.strip().lower())} times in your name {name.strip()}) ')
