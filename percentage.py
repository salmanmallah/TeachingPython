# calculate percentage of given amount by user.
totalAmount = int(input('Enter you total amount : '))
getPercentage = int(input('percentage you want to know: '))
def Givepercentage(amount,percentage):
    quotients = percentage / amount
    answer = quotients * 100
    print(f'{percentage}% of {amount} is {answer}')

Givepercentage(totalAmount,getPercentage)