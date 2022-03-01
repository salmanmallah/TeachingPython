"""
    CHAPTER NO. 14
    TUTORIAL NO. 167
    FUNCTION RETURNING FUNCTION
"""

def outer_func():
    def inner_func():
        return ('salman is inside the inner func')
    return inner_func()

# var = outer_func()
# print(var)


def outer_func2(mesg):
    def inner_func2():
        print(f'Message is : {mesg}')
    return inner_func2

var = outer_func2('i am salman')
var()
