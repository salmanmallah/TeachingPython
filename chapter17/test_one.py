"""
    CHAPTER NO. 17
    TUTORIAL NO. 209 | 210
    TEST ONE
"""

# mylogic


def divide(divident, divisor):
    try:
        return divident / divisor
        # if (type(divident) == int) and (type(divisor) == int):
    except ValueError:
        return 'please enter numbers not strings'
    except ZeroDivisionError:
        return "Do not divide by zero"


print(divide(10, 0))