"""
    Chapter Three
    if elif else statements
"""
"""
    *SHOW TICKET PRICING
    0 to 3 years of age (free)
    4 to 10 years of age (140)
    10 to 30 years of age (200)
    31 to 60 year of age (250)
    people above age of 60 is free
    
"""
age = int(input('Enter you age to check ticket price : '))
if age == 0 or age < 0:
    print('invalid ages')
elif 0 < age <= 3:
    print('Your ticket price is free')
elif 3 < age <= 10:
    print('Your ticket price is (140)')
elif 10 < age <= 30:
    print('Your ticket price is 200')
elif 30 < age <= 60:
    print('Your ticket price is 250')
else:
    print('Your ticket price is free')