# with open('file1.txt', 'r', encoding='utf-8') as rf:
#     with open('file2.txt', 'w', encoding='utf-8') as wf:
#         file1 = rf.read()
#         wf.write(file1)
"""
    Reading CSV files with reader and DictReader method
"""

# from csv import reader
#
# with open('names.csv', 'r') as data:
#     csv_data = reader(data)
#     next(csv_data)
#     for name, salary in csv_data:
#         if int(salary) > 14999:
#             print(f'{name}, {salary}')
#
# from csv import DictReader
# with open('names.csv', 'r') as rf:
#     csv_reader = DictReader(rf, delimiter=',')  # delimiter means seperator
#     for row in csv_reader:
#         if int(row['salary']) > 14999:
#             print(row)

'''Writing data to CSV file with writer'''

# from csv import writer
# with open('user.csv', 'w', newline='') as wf:
#     csv_ = writer(wf)
#     csv_.writerow(['first_name', 'last_name', 'age'])
#     csv_.writerow(['Akram', 'Mallah', '40'])
#     csv_.writerow(['Salman', 'Mallah', '22'])
#     csv_.writerow(['Noman', 'Mallah', '20'])
#
#     csv_.writerows([['first_name', 'last_name', 'age'],
#                     ['Ateeque', 'solangi', 20],
#                     ['Arsalan', 'solangi', 20],
#                     ['Khalil', 'solangi', 20],
#                     ['Noor', 'solangi', 20],
#                     ['Iqra', 'solangi', 20],
#                     ['Isra', 'solangi', 20],
#     ])


'''Writing data to CSV file with DictWriter'''

# from csv import DictWriter
#
# with open('final.csv', 'w', newline="") as wf:
#     csv_writer = DictWriter(wf, fieldnames=['name', 'age', 'country', 'phone'])
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         'name': 'Salman',
#         'age': 20,
#         'country': 'Pakistan',
#     })
#     csv_writer.writerow({
#         'name': 'Noman',
#         'age': 18,
#         'country': 'Saudi Arebia'
#     })

from csv import DictReader, DictWriter
with open('final.csv', 'r') as rf:
    with open('new_fine.csv', 'w', newline="") as wf:
        read_csv = DictReader(rf)
        write_csv = DictWriter(wf, fieldnames=['name', 'age', 'country', 'phone'])
        write_csv.writeheader()
        for row in read_csv:
            name = row['name']
            age = row['age']
            country = row['country']
            phone = row['phone']
            write_csv.writerow({
                'name': name,
                'age': age,
                'country': country,
                'phone': phone,
            })

