"""
    CHAPTER NO. 17
    TUTORIAL NO. 211
    CUSTOM EXCEPTION
"""


class Nametooshort(ValueError):
    pass


def validate(name):
    if len(name) < 8:
        raise Nametooshort("name is too short")


username = input('enter your name : ')
validate(username)
print(f'Hello Mr.{username}')
