"""
    CHAPTER NO. 18
    TUTORIAL NO. 225
    CSV HEADER
"""
from csv import DictWriter
with open('final.csv', 'w', newline="") as f:
    csv_writer = DictWriter(f, fieldnames=['first_name', 'last_name', 'age'])
    csv_writer.writeheader()
    # write row, write rows
    csv_writer.writerow({
        'first_name': 'Salman',
        'last_name': 'Mallah',
        'age': 22
    })
    csv_writer.writerow({
        'first_name': 'Noman',
        'last_name': 'Mallah',
        'age': 18
    })
    # with writerows functiton
    # syntax --> csvObject.writerows([{key:value}])
    csv_writer.writerows([
        {'first_name': 'fayaz', 'last_name': 'umrani', 'age': 22},
        {'first_name': 'zulfiqar', 'last_name': 'jhagrani', 'age': 23},
        {'first_name': 'Abrar', 'last_name': 'unknown', 'age': 22}
    ])