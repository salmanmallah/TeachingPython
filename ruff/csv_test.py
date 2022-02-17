# from csv import reader, writer
# with open('user.csv', 'r') as rf:
#     with open('salary.txt', 'w', newline="") as wf:
#         csv_reader = reader(rf)
#         csv_writer = writer(wf)
#         for user, salary in csv_reader:
#             if int(salary) > 14999:
#                 csv_writer.writerow([f'{user.title()}\'s salary is {salary}'])

from csv import DictReader, DictWriter
with open('user.csv', 'r') as rf:
    with open('salary.txt', 'w', newline="") as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf, fieldnames=['name', 'salary'])
        csv_writer.writeheader()
        for row in csv_reader:
            if int(row['salary']) > 14999:
                name, salary = row['name'], row['salary']
                csv_writer.writerow({
                    'name': name,
                    'salary': salary
                })
