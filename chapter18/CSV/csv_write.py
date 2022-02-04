"""
    CHAPTER NO. 18
    TUTORIAL NO. 225
"""

from csv import writer

with open('user_data.csv', 'w', newline="") as rf:
    csv_writer = writer(rf)
    csv_writer.writerow(['name', 'country'])
    csv_writer.writerow(['Salman', 'Pak'])
    csv_writer.writerow(['David', 'Niger'])


