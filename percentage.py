# calculate percentage of given amount by user.
percent = float(input('percentage: '))
totalamount = float(input('total amount: '))


def Givepercentage(percentage, amount):
    # formula is : (p ➗ 100) * total amount = answer
    answer = (percentage / 100) * amount
    print(f'{percentage}% of {amount} is {answer}')


Givepercentage(percent, totalamount)

