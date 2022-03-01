"""
    CHAPTER NO. 18
    TUTORIAL NO. 227
    READ FROM ONE CSV FILE AND WRITE ONE'S DATA TO ANOTHER CSV FILE
"""
from csv import DictReader, DictWriter

with open('salary.csv', 'r') as rf:
    with open('top_paid.csv', 'w', newline="") as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf, fieldnames=['employee_name', 'salary'])
        csv_writer.writeheader()
        for row in csv_reader:
            if int(row[' salary']) > 19999:
                first_name, salary = row['employee_name'], row[' salary']
                csv_writer.writerow({
                    "employee_name": first_name.upper(),
                    "salary": salary
                })