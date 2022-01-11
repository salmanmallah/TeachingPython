def decorator(function):
    def wrapper(*args):
        print("Inner Function: before enhancing")
        print(function(*args))
        print("Inner Function: after enhancing")
    return wrapper


@decorator
def name(*args):
    """ This function takes args """
    return f'{args} is here !!!\nthis is to learn decorator'


# result = decorator(name)
# result()

# by syntactic sugare
name()
