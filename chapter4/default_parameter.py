"""
    CHAPTER 4
    Default Parameters
"""
# defining a function with default argument


def userInfo(fname="unknown", lname='unknown', age=None):
    print(f'name: {fname}')
    print(f'name: {lname}')
    print(f'name: {age}')


userInfo()