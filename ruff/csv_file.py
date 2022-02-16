# from csv import reader
# with open('names.csv', 'r') as data:
#     csv_data = reader(data)
#     next(csv_data)
#     for name, salary in csv_data:
#         if int(salary) > 14999:
#             print(f'{name}, {salary}')

from csv import DictReader
with open('names.csv', 'r') as rf:
    csv_reader = DictReader(rf, delimiter=',')
    for row in csv_reader:
        print(row)
