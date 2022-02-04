"""
    CHAPTER NO. 18
    TUTORIAL NO. 226
    READ FROM ONE CSV FILE AND WRITE ONE'S DATA TO ANOTHER CSV FILE
"""
from csv import DictReader, DictWriter
with open('salary.csv', 'r') as rf:
    with open('top_paid.csv', 'w') as wr:
        pass