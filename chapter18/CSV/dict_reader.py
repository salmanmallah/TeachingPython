"""
    CHAPTER NO 18
    TUTORIAL NO. 224
    Read CSV file with dict reader
"""
from csv import DictReader

with open('file.csv', 'r') as f:
    datacsv = DictReader(f, delimiter='|')
    for row in datacsv:
        print(row)