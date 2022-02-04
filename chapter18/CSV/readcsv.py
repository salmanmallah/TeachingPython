"""
    CHAPTER NO. 18
    TURORIAL NO. 223c
"""

from csv import reader

with open('file.csv', 'r') as f:
    csv_reader = reader(f)
    next(csv_reader) # to hide header
    # iterator
    for row in csv_reader:
        print(row)