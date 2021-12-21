"""
    CHAPTER 9
    TEST TWO
        NUM TO STRING
        DEFINE A FUNCTION
        EXAMPLE:
            INPUT === > [True, False, [1, 2, 3], 1, 1.0, 3]
            OUTPUT ===> ['1', '1.0', '3']
"""
mix = [True, False, [1, 2, 3], 1, 1.0, 3]
output = [str(i) for i in mix if type(i) == int or type(i) == float]
print(output)


