"""
    CHAPTER NO 14
    TUTORIAL NO 168
    CLOSURE PRACTICE
        MEANS: Function returning function (closure) pracitice
"""

# make a function that do:
# square
# cube
# any power of given number


def power(p):
    def calc_power(n):
        return n**p
    return calc_power


square = power(3)  # now here you are calling power func and it is return a calc_power function and
# calc_power is saving in square so when we calc_power it is doing its job
print(square(2))
