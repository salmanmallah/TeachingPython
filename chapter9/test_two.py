"""
<<<<<<< HEAD
    CHAPTER NO 9
    EXERCISE 2
        NUM TO STRING
        DEFINE A FUNCTION
        EXAMPLE:
            INPUT === > [True, False, [1, 2, 3], 1, 1.0, 3]
            OUTPUT ===> ['1', '1.0', '3']
"""


def num_to_str(l):
    output = [str(i) for i in l if type(i) == int or type(i) == float]
    return output

print(num_to_str([True, False, [1, 2, 3], 1, 1.0, 3]))
