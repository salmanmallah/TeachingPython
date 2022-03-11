import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as box
from csv import DictWriter
import os

# starterCode
win = tk.Tk()
win.title('Desktop Application')
win.geometry('800x600')

# frame
frame = ttk.LabelFrame(win, text='Admission Form')

# labels
label_name = ttk.Label(frame, text='Name: ')
label_fathername = ttk.Label(frame, text='Father\'s Name: ')
label_birthdate = ttk.Label(frame, text='Date Of Birth: ')
label_cnic = ttk.Label(frame, text='CNIC: ')
label_gender = ttk.Label(frame, text='Gender: ')
label_religion = ttk.Label(frame, text='Religion: ')
label_domicile = ttk.Label(frame, text='Domicile: ')
label_mobnumber = ttk.Label(frame, text='Contact Number: ')
label_email = ttk.Label(frame, text='Email: ')
label_qualification = ttk.Label(frame, text='Qualification: ')

# EntryBox variables
var_name = tk.StringVar()
var_fathername = tk.StringVar()
var_birthdate = tk.StringVar()
var_cnic = tk.StringVar()
var_gender = tk.StringVar()
var_religion = tk.StringVar()
var_domicile = tk.StringVar()
var_mobnumber = tk.StringVar()
var_email = tk.StringVar()
var_qualification = tk.StringVar()

# EnterBoxes
entry_name = ttk.Entry(frame, textvariable=var_name)
entry_fathername = ttk.Entry(frame, textvariable=var_fathername)
entery_birthdate = ttk.Entry(frame, textvariable=var_birthdate)
entery_cnic = ttk.Entry(frame, textvariable=var_cnic)
entery_gender = ttk.Entry(frame, textvariable=var_gender)
entery_religion = ttk.Entry(frame, textvariable=var_religion)
entery_domicile = ttk.Entry(frame, textvariable=var_domicile)
entery_mobnumber = ttk.Entry(frame, textvariable=var_mobnumber)
entery_email = ttk.Entry(frame, textvariable=var_email)
entery_qualification = ttk.Entry(frame, textvariable=var_qualification)

# Submit Button
# submitbutton function


def submit_action():
    name = var_name.get()
    fathername = var_fathername.get()
    birthdate = var_birthdate.get()
    cnic = var_cnic.get()
    gender = var_gender.get()
    religion = var_religion.get()
    domicile = var_domicile.get()
    contactnumber = var_mobnumber.get()
    email = var_email.get()
    qualification = var_qualification.get()
    print(name, fathername, birthdate, cnic, gender, religion, domicile, contactnumber, email, qualification)
    with open('FormData.csv', 'a', newline='') as wf:
        csv_writer = DictWriter(wf, fieldnames=(['Name', 'FatherName', 'BirthDate', 'Cnic', 'Gender', 'Religion',
                                                 'Domicile', 'ContactNumber', 'Email', 'Qaulification']))

        if os.path.getsize('FormData.csv') == 0:
            csv_writer.writeheader()
        csv_writer.writerow({
            'Name': name,
            'FatherName': fathername,
            'BirthDate': birthdate,
            'Cnic': cnic,
            'Gender': gender,
            'Religion': religion,
            'Domicile': domicile,
            'ContactNumber': contactnumber,
            'Email': email,
            'Qaulification': qualification,

        })


submit_btn = ttk.Button(frame, text='SUBMIT', command=submit_action)

# »»»»»»»»»» Grid start here »»»»»»»»»»»»
# frame grid
frame.pack(pady=50, padx=50)

# label grid
label_name.grid()
label_fathername.grid()
label_birthdate.grid()
label_cnic.grid()
label_gender.grid()
label_religion.grid()
label_domicile.grid()
label_mobnumber.grid()
label_email.grid()
label_qualification.grid()


# entrybox grid
entry_name.grid(row=0, column=1, pady=5)
entry_fathername.grid(row=1, column=1, pady=5)
entery_birthdate.grid(row=2, column=1, pady=5)
entery_cnic.grid(row=3, column=1, pady=5)
entery_gender.grid(row=4, column=1, pady=5)
entery_religion.grid(row=5, column=1, pady=5)
entery_domicile.grid(row=6, column=1, pady=5)
entery_mobnumber.grid(row=7, column=1, pady=5)
entery_email.grid(row=8, column=1, pady=5)
entery_qualification.grid(row=9, column=1, pady=5)


# submit button grid
submit_btn.grid(row=10, columnspan=2)

win.mainloop()
