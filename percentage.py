"""
    All about percentage with python.

    make a programme with find percentage from a given amount.

    Example: What is 10% of 150?
        * Convert the problem to an equation using the percentage formula: P% * X = Y
        * P is 10%, X is 150, so the equation is 10% * 150 = Y
        * Convert 10% to a decimal by removing the percent sign and dividing by 100: 10/100 = 0.10
        * Substitute 0.10 for 10% in the equation: 10% * 150 = Y becomes 0.10 * 150 = Y
        * Do the math: 0.10 * 150 = 15
        * Y = 15
        * So 10% of 150 is 15
        * Double check your answer with the original question: What is 10% of 150? Multiply 0.10 * 150 = 15

            :FORMULA IS : (p ➗ 100) * total amount = answer

"""


def Givepercentage(percentage, amount):
    answer = (percentage / 100) * amount
    print(f'{percentage}% of {amount} is {answer}')


amount = float(input('total amount: '))
percent = float(input('percentage: '))

Givepercentage(percent, amount)
